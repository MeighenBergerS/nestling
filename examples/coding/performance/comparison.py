"""
Performance comparison: Python loop vs NumPy vs Numba.

Run this script directly to see timings on your machine:

    python examples/coding/performance/comparison.py

Two tasks are timed:

  Task A  (1-D vectorisation) — evaluate E^2 * Phi(E) at 1 000 000 energies for
           a single spectral index.  Shows the classic loop-vs-vectorise speedup.

  Task B  (sequential simulation) — simulate 500 muon tracks losing energy step
           by step according to:
               E_new = E_old * (1 - alpha) - beta * sqrt(E_old)
           Each step depends on the previous energy, so NumPy cannot vectorise
           the step dimension.  This is the canonical use case for Numba.

           Three approaches are compared:
             1. Python nested loop  — slow (Python overhead at every step of every track)
             2. NumPy per-step loop — medium (Python loop over steps; vectorised over tracks)
             3. Numba @njit         — fast (both loops compiled to machine code)

           The Numba kernel is defined at module level so that JIT compilation is
           excluded from the timing.  The warm-up call is reported separately so you
           can see how long compilation takes on the first run (subsequent runs load
           from the on-disk cache thanks to cache=True).
"""

import time

import numpy as np

# ── Physical constants ─────────────────────────────────────────────────────────
NORM = 1.66e-18  # GeV^-1 cm^-2 s^-1 sr^-1
E_REF = 1e5  # GeV

# ── Energy-loss simulation parameters ─────────────────────────────────────────
# Step: E_new = E_old * (1 - ALPHA) - BETA * sqrt(E_old)
# Parameters chosen so all particles retain >10 % of initial energy after
# N_STEPS steps (no early exit via the E <= 0 break).
N_TRACKS = 500
N_STEPS = 5_000
ALPHA = 3e-4  # fractional ionisation loss per step
BETA = 1e-4  # sqrt-dependent radiative-like term
E_INIT = np.full(N_TRACKS, 1e6, dtype=np.float64)  # all start at 1 PeV


# ── Numba kernel (module level so JIT compilation happens once) ────────────────
try:
    from numba import njit

    @njit(cache=True)
    def _numba_energy_loss(E0: np.ndarray, alpha: float, beta: float, n_steps: int) -> np.ndarray:
        """Compiled nested loop: tracks × steps.  Both loops run at machine-code speed."""
        results = np.empty(len(E0))
        for i in range(len(E0)):
            E = E0[i]
            for _ in range(n_steps):
                E = E * (1.0 - alpha) - beta * E**0.5
                if E <= 0.0:
                    E = 0.0
                    break
            results[i] = E
        return results

    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False


# ── Helpers ────────────────────────────────────────────────────────────────────


def time_it(label: str, fn, *args) -> tuple[float, object]:
    t0 = time.perf_counter()
    result = fn(*args)
    elapsed = time.perf_counter() - t0
    print(f"  {label:<34s} {elapsed * 1000:8.2f} ms")
    return elapsed, result


# ── Task A implementations ─────────────────────────────────────────────────────

E_1D = np.logspace(3, 7, 1_000_000)
GAMMA_FIXED = 2.37


def task_a_loop(E: np.ndarray, gamma: float) -> list:
    """Python list comprehension — one Python call per element."""
    return [NORM * (e / E_REF) ** (-gamma) * e**2 for e in E]


def task_a_vectorised(E: np.ndarray, gamma: float) -> np.ndarray:
    """NumPy — the arithmetic loop runs in compiled C."""
    return NORM * (E / E_REF) ** (-gamma) * E**2


# ── Task B implementations ─────────────────────────────────────────────────────


def task_b_python(E0: np.ndarray, alpha: float, beta: float, n_steps: int) -> np.ndarray:
    """
    Python nested loop: outer over tracks, inner over steps.

    The inner loop CANNOT be vectorised: step n uses the energy from step n-1.
    Python pays interpreter overhead at every single step of every track.
    """
    results = np.empty(len(E0))
    for i, E in enumerate(E0):
        for _ in range(n_steps):
            E = E * (1.0 - alpha) - beta * E**0.5
            if E <= 0.0:
                E = 0.0
                break
        results[i] = E
    return results


def task_b_numpy_per_step(E0: np.ndarray, alpha: float, beta: float, n_steps: int) -> np.ndarray:
    """
    NumPy vectorised over tracks; Python loop over steps.

    Each step applies one vectorised NumPy operation to all N_TRACKS at once,
    so Python overhead is paid once per step, not once per (track × step).
    Faster than pure Python, but the step loop is still in Python.
    """
    E = E0.copy()
    for _ in range(n_steps):
        E = E * (1.0 - alpha) - beta * np.sqrt(E)
        np.maximum(E, 0.0, out=E)
    return E


def task_b_numba_timed(
    E0: np.ndarray, alpha: float, beta: float, n_steps: int
) -> np.ndarray | None:
    """Thin wrapper around the pre-compiled Numba kernel."""
    if not HAS_NUMBA:
        return None
    return _numba_energy_loss(E0, alpha, beta, n_steps)


# ── Main ───────────────────────────────────────────────────────────────────────


def main() -> None:
    # ── Task A ──
    print(f"\nTask A — vectorisation: E²·Φ(E) for {len(E_1D):,} energies")
    print("─" * 62)
    t_loop, r_loop = time_it("Python loop", task_a_loop, E_1D, GAMMA_FIXED)
    t_vec, r_vec = time_it("NumPy (vectorised)", task_a_vectorised, E_1D, GAMMA_FIXED)
    assert np.allclose(r_loop, r_vec, rtol=1e-10)
    print(f"  → NumPy speedup: {t_loop / t_vec:.0f}×")
    print("  Key: NumPy eliminates per-element Python overhead.")

    # ── Task B ──
    print(f"\nTask B — sequential energy loss: {N_TRACKS} tracks × {N_STEPS:,} steps")
    print("  Step:  E_new = E_old*(1-α) - β*√E_old  (non-linear, step-dependent)")
    print("─" * 62)

    # Warm up Numba outside the timed region.
    # First run: JIT-compiles and writes to disk cache (~400 ms).
    # Later runs: loads cache from disk (~5 ms).
    if HAS_NUMBA:
        t0 = time.perf_counter()
        _numba_energy_loss(E_INIT[:2], ALPHA, BETA, 10)
        t_warmup = time.perf_counter() - t0
        print(
            f"  Numba warm-up: {t_warmup * 1000:.0f} ms "
            f"({'JIT compile — saved to cache' if t_warmup > 0.05 else 'loaded from cache'})"
        )

    t_py, r_py = time_it("Python nested loop", task_b_python, E_INIT, ALPHA, BETA, N_STEPS)
    t_np, r_np = time_it(
        "NumPy (per-step loop)", task_b_numpy_per_step, E_INIT, ALPHA, BETA, N_STEPS
    )

    if HAS_NUMBA:
        t_nb, r_nb = time_it("Numba @njit", task_b_numba_timed, E_INIT, ALPHA, BETA, N_STEPS)
    else:
        print("  Numba @njit" + " " * 22 + "[not installed — pip install numba]")
        t_nb, r_nb = None, None

    assert np.allclose(r_py, r_np, rtol=1e-8), "Python vs NumPy mismatch"
    if r_nb is not None:
        assert np.allclose(r_py, r_nb, rtol=1e-8), "Python vs Numba mismatch"

    print(f"  → NumPy speedup over Python: {t_py / t_np:.0f}×")
    if t_nb is not None:
        print(f"  → Numba speedup over Python: {t_py / t_nb:.0f}×")
        print(f"  → Numba speedup over NumPy : {t_np / t_nb:.0f}×")

    print("\n  Key: NumPy vectorises the OUTER loop (across tracks) but still pays")
    print("       Python overhead for each of the N_STEPS inner iterations.")
    print("       Numba compiles BOTH loops — eliminating Python at every level.")


if __name__ == "__main__":
    main()
