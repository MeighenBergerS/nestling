"""
Monte Carlo Pi estimation: Python loop vs Numba JIT.

Run this script directly:

    python examples/coding/performance/pi_estimation.py

This example highlights two things:

  1.  The JIT compilation overhead on the FIRST call.
      The second Numba call reuses the compiled machine code — this is why the
      warm-up pattern matters in performance-critical code.

  2.  The speedup Numba gives on a tight loop that would otherwise pay Python
      interpreter overhead on every iteration.
"""

import random
import time

from numba import njit

# ── Python implementation ──────────────────────────────────────────────────────


def estimate_pi_python(n: int) -> float:
    """Estimate Pi by counting random points that fall inside the unit circle."""
    count = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            count += 1
    return 4.0 * count / n


# ── Numba implementation — identical logic, single decorator ───────────────────


@njit(cache=True)
def estimate_pi_numba(n: int) -> float:
    """
    Same algorithm as estimate_pi_python, compiled by Numba.

    Note: Numba reimplements random.random() with its own internal RNG.
    The state is independent of Python's random module, so results will
    differ numerically but converge to Pi at the same statistical rate.
    """
    count = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1.0:
            count += 1
    return 4.0 * count / n


# ── Benchmark ─────────────────────────────────────────────────────────────────

N = 10_000_000  # number of Monte Carlo samples

print(f"\nMonte Carlo Pi estimation — N = {N:,} samples")
print("─" * 52)

# Python
t0 = time.perf_counter()
pi_py = estimate_pi_python(N)
t_py = time.perf_counter() - t0
print(f"  Pure Python         : {t_py:.3f} s   π ≈ {pi_py:.6f}")

# Numba — first call (includes JIT compilation)
t0 = time.perf_counter()
pi_nb1 = estimate_pi_numba(N)
t_nb1 = time.perf_counter() - t0
print(f"  Numba (1st call)    : {t_nb1:.3f} s   π ≈ {pi_nb1:.6f}  ← includes compilation")

# Numba — second call (uses compiled machine code)
t0 = time.perf_counter()
pi_nb2 = estimate_pi_numba(N)
t_nb2 = time.perf_counter() - t0
print(f"  Numba (2nd call)    : {t_nb2:.3f} s   π ≈ {pi_nb2:.6f}  ← compiled code only")

print("─" * 52)
print(f"  Speedup (2nd call vs Python): {t_py / t_nb2:.0f}×")
print(f"  Compilation overhead        : {t_nb1 - t_nb2:.2f} s  (paid once; @njit(cache=True))")
