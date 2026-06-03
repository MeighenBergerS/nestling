# Lesson 07: ML Basics with PyTorch

Machine learning has become a standard tool in high-energy physics, neutrino astronomy,
and gravitational-wave analysis.
This lesson covers the concepts and PyTorch mechanics you need to start using it,
and to understand what it is actually doing.

---

## Where ML fits in physics research

ML is not a replacement for physics understanding. It is a function approximator that is
useful when:

- The relationship between inputs and outputs is too complex to write by hand (e.g.
  classifying signal from background in a high-dimensional feature space).
- You need a **surrogate model**: a neural network trained to emulate an expensive simulation
  so you can call it millions of times during inference.
- You want to reconstruct a physical quantity (energy, direction, vertex) from raw detector
  data.
- You are doing parameter estimation and need a differentiable likelihood.

[Prometheus](https://github.com/Harvard-Neutrino/prometheus) uses ML-based photon
propagation (the `olympus` module) as a surrogate for the full optical simulation,
exactly the surrogate model use case. Instead of running the slow photon transport code
for every event, it calls a trained neural network that gives the same answer in
microseconds.

---

## Tensors

A PyTorch `Tensor` is conceptually the same as a NumPy array, but it can live on a GPU
and tracks gradient information for automatic differentiation.

```sh
pip install torch
```

```python
import torch

x = torch.tensor([1.0, 2.0, 3.0])          # from a list
y = torch.zeros(100)                         # zeros
z = torch.randn(32, 10)                      # random normal, shape (32, 10)

# Operations look identical to NumPy
x ** 2                                       # element-wise square
z.shape                                      # torch.Size([32, 10])
z.mean(), z.std()
```

Converting between NumPy and PyTorch:

```python
a = z.numpy()                                # tensor → numpy (CPU only)
b = torch.from_numpy(a)                      # numpy → tensor
```

Moving to GPU when available:

```python
device = "cuda" if torch.cuda.is_available() else "cpu"
z = z.to(device)
```

---

## A simple neural network

PyTorch models are classes that inherit from `torch.nn.Module`.
Define the layers in `__init__`, and the forward computation in `forward`.

```python
import torch
import torch.nn as nn

class FluxRegressor(nn.Module):
    """Predicts log-flux from log-energy using a small fully-connected network."""

    def __init__(self, n_hidden: int = 64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, n_hidden),
            nn.ReLU(),
            nn.Linear(n_hidden, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)

model = FluxRegressor(n_hidden=128)
```

---

## The training loop

Training a neural network follows the same four steps every iteration:

1. **Forward pass**: run the model on a batch of inputs to get predictions.
2. **Compute loss**: measure how wrong the predictions are.
3. **Backward pass**: compute gradients via backpropagation.
4. **Update weights**: move parameters in the direction that reduces the loss.

```python
import torch
import torch.nn as nn
from torch.optim import Adam

# Toy training data: power-law spectrum
E_train = torch.logspace(2, 6, 2000).unsqueeze(1)   # shape (2000, 1)
phi_true = E_train ** -2.37

log_E = torch.log10(E_train)
log_phi = torch.log10(phi_true)

model = FluxRegressor(n_hidden=128)
optimizer = Adam(model.parameters(), lr=1e-3)
loss_fn = nn.MSELoss()

for epoch in range(1000):
    optimizer.zero_grad()                       # 1. clear old gradients
    log_phi_pred = model(log_E)                 # 2. forward pass
    loss = loss_fn(log_phi_pred, log_phi)       # 3. compute loss
    loss.backward()                             # 4. compute gradients
    optimizer.step()                            # 5. update weights

    if epoch % 200 == 0:
        print(f"Epoch {epoch:5d}  Loss {loss.item():.4e}")
```

After training, the model evaluates new energies in microseconds, even if the
training data took hours to generate.

---

## Evaluation and saving

Switch the model to evaluation mode before making predictions
(this disables dropout and batch normalisation layers if present):

```python
model.eval()

with torch.no_grad():                           # disable gradient tracking
    log_phi_pred = model(log_E_test)
    phi_pred = 10 ** log_phi_pred.squeeze()

# Save
torch.save(model.state_dict(), "flux_model.pt")

# Load
loaded = FluxRegressor(n_hidden=128)
loaded.load_state_dict(torch.load("flux_model.pt", weights_only=True))
loaded.eval()
```

---

## Physics use-cases

| Task | ML approach |
|------|------------|
| Signal/background classification | Binary classifier (sigmoid output + BCELoss) |
| Energy / direction reconstruction | Regression (MSELoss) |
| Fast surrogate for slow simulation | Regression or normalising flow |
| Posterior estimation | Neural posterior estimation (see [sbi](https://sbi-dev.github.io/sbi/)) |
| Anomaly detection | Autoencoder or flow-based density model |

### Libraries worth knowing

| Library | Purpose |
|---------|---------|
| [pytorch-lightning](https://lightning.ai/) | Reduces training loop boilerplate |
| [sbi](https://sbi-dev.github.io/sbi/) | Simulation-based inference |
| [zuko](https://github.com/probabilists/zuko) | Normalising flows in PyTorch |
| [torch-geometric](https://pytorch-geometric.readthedocs.io/) | Graph neural networks (event reconstruction) |

---

## What to read next

[Lesson 08](lesson-08.md) starts the best-practices block: how to structure a Python
project so the code you have been writing can be shared, tested, and maintained.
