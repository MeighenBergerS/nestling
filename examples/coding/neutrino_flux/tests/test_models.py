"""Tests for spectral flux models."""

import numpy as np
import pytest
from pytest import approx

from neutrino_flux import BrokenPowerLaw, PowerLaw
from neutrino_flux.exceptions import InvalidEnergyError, InvalidSpectralIndexError


class TestPowerLaw:
    def test_unity_at_reference_energy(self):
        """Flux at E_ref must equal norm regardless of gamma."""
        model = PowerLaw(gamma=2.37, norm=3.5e-18, E_ref=1e5)
        assert model(1e5) == approx(3.5e-18)

    def test_scales_with_spectral_index(self, unit_model):
        """10x energy increase should reduce flux by 10^gamma (gamma=2 → factor 100)."""
        assert unit_model(10.0) == approx(unit_model(1.0) / 100.0)

    def test_vectorised_input(self, unit_model):
        """Model must accept and return a numpy array of the same shape."""
        E = np.array([1.0, 10.0, 100.0])
        result = unit_model(E)
        assert result.shape == (3,)
        assert result[0] == approx(1.0)
        assert result[1] == approx(0.01)
        assert result[2] == approx(1e-4)

    def test_negative_gamma_raises(self):
        with pytest.raises(InvalidSpectralIndexError, match="gamma must be positive"):
            PowerLaw(gamma=-1.0, norm=1.0)

    def test_zero_gamma_raises(self):
        with pytest.raises(InvalidSpectralIndexError):
            PowerLaw(gamma=0.0, norm=1.0)

    def test_zero_E_ref_raises(self):
        with pytest.raises(InvalidEnergyError):
            PowerLaw(gamma=2.0, norm=1.0, E_ref=0.0)

    def test_negative_E_ref_raises(self):
        with pytest.raises(InvalidEnergyError):
            PowerLaw(gamma=2.0, norm=1.0, E_ref=-1.0)


class TestBrokenPowerLaw:
    def test_flux_equals_norm_at_break(self, broken_model):
        """At E_break both branches evaluate to (E_break/E_break)^-gamma = 1."""
        assert broken_model(1e5) == approx(1e-18)

    def test_continuous_at_break(self, broken_model):
        """Flux evaluated 1 GeV either side of the break should be nearly equal."""
        just_below = broken_model(1e5 - 1)
        just_above = broken_model(1e5 + 1)
        assert just_below == approx(just_above, rel=1e-3)

    def test_steeper_above_break(self, broken_model):
        """
        With gamma2 > gamma1, flux drops faster per energy decade above the break.
        ratio_per_decade_below = model(1e4) / model(1e5) = 10^gamma1 = 100
        ratio_per_decade_above = model(1e5) / model(1e6) = 10^gamma2 = 1000
        """
        ratio_below = broken_model(1e4) / broken_model(1e5)
        ratio_above = broken_model(1e5) / broken_model(1e6)
        assert ratio_above > ratio_below

    def test_vectorised_input(self, broken_model):
        E = np.logspace(3, 7, 20)
        result = broken_model(E)
        assert result.shape == (20,)
        assert np.all(result > 0)

    def test_invalid_gamma1_raises(self):
        with pytest.raises(InvalidSpectralIndexError, match="gamma1"):
            BrokenPowerLaw(gamma1=-1.0, gamma2=3.0, norm=1.0, E_break=1e5)

    def test_invalid_gamma2_raises(self):
        with pytest.raises(InvalidSpectralIndexError, match="gamma2"):
            BrokenPowerLaw(gamma1=2.0, gamma2=0.0, norm=1.0, E_break=1e5)

    def test_invalid_E_break_raises(self):
        with pytest.raises(InvalidEnergyError):
            BrokenPowerLaw(gamma1=2.0, gamma2=3.0, norm=1.0, E_break=-1.0)
