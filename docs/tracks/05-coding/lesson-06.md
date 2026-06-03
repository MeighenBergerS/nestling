# Lesson 06: Performance & Parallelism

Python is slow for explicit loops but can be as fast as C when you use the right tools.
This lesson explains why, how to find bottlenecks, and which technique to reach for first.

---

## Why Python loops are slow

Python executes one bytecode instruction at a time, with type checking and memory
management overhead on every operation.
A loop over a million elements that runs in milliseconds in C can take seconds in Python.

The **Global Interpreter Lock (GIL)** adds a second constraint: the CPython interpreter
allows only one thread to execute Python bytecode at a time.
Pure-Python threading does not give you CPU parallelism.

The solution is not to rewrite in C. It is to push loops into libraries that run in
compiled code.

---

## Vectorisation first

Replacing Python `for` loops with NumPy operations is called **vectorisation**.
It should be your first instinct whenever you find yourself looping over array elements.

```python
import numpy as np

# Slow: explicit Python loop
def slow_flux(energies, gamma):
    result = []
    for E in energies:
        result.append(E ** (-gamma))
    return result

# Fast: vectorised
def fast_flux(energies: np.ndarray, gamma: float) -> np.ndarray:
    return energies ** (-gamma)
```

The vectorised version runs the same arithmetic in compiled C code inside NumPy.
For arrays with a million elements the difference is typically 100–1000×.

SciPy, Pandas, and most of the scientific Python stack are already vectorised internally.
The rule: **if you are writing a `for` loop over a NumPy array, ask whether a NumPy or
SciPy function already does what you need.**

---

## Profiling: find the bottleneck first

Optimising the wrong function wastes time and makes code harder to read.
Always profile before optimising.

### cProfile

```sh
python -m cProfile -s cumtime myscript.py | head -20
```

This prints the 20 functions where your program spends the most cumulative time.

### line_profiler

For line-by-line timing within a specific function:

```sh
pip install line-profiler
```

Decorate the function you want to examine:

```python
@profile
def compute_spectrum(energies, gamma):
    ...
```

Run with:

```sh
kernprof -l -v myscript.py
```

---

## Multiprocessing

When you have many **independent** tasks, such as running the same simulation with different seeds
or processing different files, `multiprocessing` gives you true CPU parallelism by spawning
separate processes, each on its own core, bypassing the GIL entirely.

```python
from multiprocessing import Pool
import numpy as np

def run_simulation(seed: int) -> float:
    rng = np.random.default_rng(seed)
    events = rng.exponential(scale=1e5, size=10000)
    return float(events.mean())

seeds = list(range(500))

with Pool(processes=8) as pool:
    results = pool.map(run_simulation, seeds)
```

`concurrent.futures.ProcessPoolExecutor` is a cleaner modern API for the same thing:

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(run_simulation, seeds))
```

!!! note "Threading vs multiprocessing"
    Use **threading** for I/O-bound work (downloading files, reading from disk)
    where the bottleneck is waiting, not computing. Threads release the GIL while waiting.
    Use **multiprocessing** for CPU-bound work where you want to use multiple cores.
    For most physics computation, multiprocessing is the right choice.

---

## Numba

[Numba](https://numba.readthedocs.io/) compiles Python functions to native machine code
using LLVM. It is most useful when your computation is genuinely loop-heavy and cannot
be vectorised, for example when each step depends on the result of the previous one.

```sh
pip install numba
```

```python
from numba import njit
import numpy as np

@njit
def track_particle(positions: np.ndarray, momenta: np.ndarray,
                   dt: float, n_steps: int) -> np.ndarray:
    for step in range(n_steps):
        for i in range(len(positions)):
            positions[i] += momenta[i] * dt
    return positions
```

The `@njit` decorator compiles the function the **first time it is called**.
Subsequent calls run at near-C speed.
The compilation happens once per session; after that you pay only the cost of the computation.

**When to use Numba**: loops that cannot be vectorised, recurrence relations, particle
tracking with branching logic.

---

## JAX

[JAX](https://jax.readthedocs.io/) is a NumPy replacement that runs on CPUs, GPUs, and
TPUs, and supports **automatic differentiation** (autodiff).
It is used in machine learning (including physics applications with PyTorch-adjacent
workflows) and increasingly in physics simulation.

```sh
pip install jax
```

```python
import jax.numpy as jnp
from jax import jit, grad

@jit
def chi_squared(params: jnp.ndarray, E: jnp.ndarray, observed: jnp.ndarray) -> float:
    gamma, norm = params
    predicted = norm * E ** (-gamma)
    return jnp.sum((predicted - observed) ** 2)

# Compute the gradient exactly — no finite differences
gradient = grad(chi_squared)(params, E, observed)
```

`@jit` compiles the function to XLA code. `grad` computes its exact gradient via backpropagation.
This is very powerful for fitting problems where you optimise over many parameters at once.

JAX enforces **functional programming**: no in-place mutation of arrays.
This is the main learning curve; once you are comfortable with it, the performance and
autodiff capabilities are hard to give up.

---

## GPU computing

### Why GPUs are fast

A modern CPU has 8–64 powerful cores designed to execute complex, branchy code as fast as
possible. A modern GPU has thousands of simpler cores designed to execute the *same*
instruction on thousands of data elements simultaneously. This is called
**SIMT** (Single Instruction, Multiple Threads).

For physics work this matters when:

- You are training or running a neural network (matrix multiplications on millions of weights)
- You are running many independent simulations (particle showers, MC sampling)
- You are computing large FFTs or solving dense linear systems

It does **not** help when:

- The computation is sequential (each step depends on the previous)
- The array fits comfortably in CPU cache and the operation is simple (vectorised NumPy is
  already close to optimal)
- The time to transfer data to GPU memory (VRAM) exceeds the time saved by faster compute

### The memory bottleneck

Data lives in CPU RAM by default. Before the GPU can operate on it, it must be copied to
GPU VRAM. For small problems this transfer cost can dominate entirely. The GPU is faster per
FLOP but you spend more time moving data than computing. Rule of thumb: only use GPU if the
computation takes at least 10× longer than the transfer would on its own.

### PyTorch on GPU

PyTorch makes GPU programming straightforward. The core pattern is selecting a device and
moving tensors to it; all subsequent operations run on that device automatically.

```python
import torch

# Select the best available device
if torch.cuda.is_available():
    device = "cuda"          # NVIDIA GPU
elif hasattr(torch, "xpu") and torch.xpu.is_available():
    device = "xpu"           # Intel Arc GPU (requires intel-extension-for-pytorch)
elif torch.backends.mps.is_available():
    device = "mps"           # Apple Silicon
else:
    device = "cpu"

print(f"Using: {device}")

# Create tensors directly on the device
a = torch.randn(10_000, 10_000, device=device)
b = torch.randn(10_000, 10_000, device=device)

# This matrix multiplication runs on the GPU — no code change needed
c = a @ b
```

For accurate GPU timing you must call `torch.cuda.synchronize()` before stopping the clock,
because GPU kernels are dispatched asynchronously. The Python line returns immediately while
the GPU is still computing.

```python
import time

# CPU timing — straightforward
t0 = time.perf_counter()
c_cpu = a_cpu @ b_cpu
t_cpu = time.perf_counter() - t0

# GPU timing — must synchronise first
t0 = time.perf_counter()
c_gpu = a_gpu @ b_gpu
torch.cuda.synchronize()   # wait for GPU to finish
t_gpu = time.perf_counter() - t0
```

Forgetting `synchronize()` produces meaningless GPU timings that appear impossibly fast.

### Moving data between CPU and GPU

```python
# CPU → GPU
tensor_gpu = tensor_cpu.to(device)          # or .cuda()

# GPU → CPU (needed before converting to NumPy)
tensor_cpu = tensor_gpu.cpu()
arr = tensor_cpu.numpy()
```

Keep transfers to a minimum. Load your data once onto the GPU at the start of a loop, do
all the compute there, and transfer back only the final result.

### JAX on GPU

JAX selects the GPU automatically, no device management needed.
The same `@jit`-decorated function runs on CPU or GPU depending on what is installed.

```python
import jax
import jax.numpy as jnp
from jax import jit

print(jax.devices())   # shows [CudaDevice(id=0)] on a GPU machine

@jit
def matmul(a, b):
    return a @ b

a = jnp.ones((10_000, 10_000))
b = jnp.ones((10_000, 10_000))
c = matmul(a, b)   # runs on GPU if available, CPU otherwise
```

### Hardware options

| Hardware | Framework | Device string |
| -------- | --------- | ------------- |
| NVIDIA GPU | PyTorch (standard) | `"cuda"` |
| NVIDIA GPU | JAX | automatic |
| Intel Arc GPU | [intel-extension-for-pytorch](https://intel.github.io/intel-extension-for-pytorch/) | `"xpu"` |
| AMD GPU | PyTorch (ROCm build) | `"cuda"` (ROCm maps to the CUDA API) |
| Apple Silicon | PyTorch (standard) | `"mps"` |

!!! note "WSL2 and Intel Arc"
    Intel Arc GPU compute (OpenCL / Level Zero / IPEX XPU) requires the `/dev/dri` render
    node provided by Intel's DRM kernel driver. The Microsoft WSL2 kernel does not include
    this driver, so Intel GPU compute is not accessible from WSL2 without a custom kernel.
    Run Linux natively for full Intel Arc support.

!!! note "HPC clusters"
    Research computing clusters almost universally provide NVIDIA GPUs.
    Check with `nvidia-smi` on the login node or in the job script to confirm availability
    and see which CUDA version is loaded.

---

## Decision guide

| Situation | Recommended tool |
|-----------|-----------------|
| Loop over array elements | NumPy vectorisation (always try this first) |
| Many independent tasks in parallel | `multiprocessing` / `ProcessPoolExecutor` |
| Loop-heavy code that cannot be vectorised | Numba `@njit` |
| Large matrix ops, neural networks, many-particle simulation | GPU via PyTorch or JAX |
| Autodiff / differentiable programming | JAX or PyTorch autograd |
| I/O-bound parallel work | `threading` |

---

## What to read next

[Lesson 07](lesson-07.md) introduces machine learning with PyTorch, where the performance
ideas from this lesson (GPU arrays, differentiable computation) become central.
