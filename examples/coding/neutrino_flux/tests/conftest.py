"""Shared fixtures for neutrino_flux tests."""

import pytest

from neutrino_flux import BrokenPowerLaw, PowerLaw


@pytest.fixture
def unit_model() -> PowerLaw:
    """Power law with norm=1, gamma=2, E_ref=1 — easy to verify analytically."""
    return PowerLaw(gamma=2.0, norm=1.0, E_ref=1.0)


@pytest.fixture
def icecube_model() -> PowerLaw:
    """IceCube best-fit single power-law (arXiv:2111.10973, Table 2)."""
    return PowerLaw(gamma=2.37, norm=1.66e-18, E_ref=1e5)


@pytest.fixture
def broken_model() -> BrokenPowerLaw:
    """Broken power-law with a break at 100 TeV."""
    return BrokenPowerLaw(gamma1=2.0, gamma2=3.0, norm=1e-18, E_break=1e5)
