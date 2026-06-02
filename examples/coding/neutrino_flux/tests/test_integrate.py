"""Tests for flux integration utilities."""

import numpy as np
import pytest
from pytest import approx

from neutrino_flux import flux_above, threshold_energy
from neutrino_flux.exceptions import ConvergenceError, InvalidEnergyError


class TestFluxAbove:
    def test_analytical_result(self, unit_model):
        """
        int_1^10 x^-2 dx = [-x^-1]_1^10 = -(1/10) + 1 = 0.9.
        Verifies that the numerical integration matches the analytical answer.
        """
        result = flux_above(unit_model, E_min=1.0, E_max=10.0)
        assert result == approx(0.9, rel=1e-5)

    def test_wider_range_gives_more_flux(self, unit_model):
        """Integrating over a wider range must give a larger result."""
        narrow = flux_above(unit_model, E_min=1.0, E_max=10.0)
        wide = flux_above(unit_model, E_min=1.0, E_max=100.0)
        assert wide > narrow

    def test_infinite_upper_bound(self, unit_model):
        """
        int_1^inf x^-2 dx = 1.0.
        Verifies that scipy.integrate.quad handles np.inf correctly.
        """
        result = flux_above(unit_model, E_min=1.0, E_max=np.inf)
        assert result == approx(1.0, rel=1e-5)

    def test_icecube_model_positive(self, icecube_model):
        """Sanity check: integrated IceCube flux must be positive."""
        result = flux_above(icecube_model, E_min=1e4, E_max=1e7)
        assert result > 0

    def test_zero_E_min_raises(self, unit_model):
        with pytest.raises(InvalidEnergyError):
            flux_above(unit_model, E_min=0.0)

    def test_negative_E_min_raises(self, unit_model):
        with pytest.raises(InvalidEnergyError):
            flux_above(unit_model, E_min=-1.0)


class TestThresholdEnergy:
    def test_roundtrip(self, unit_model):
        """
        Integrating above the returned threshold should recover the target value.
        For unit_model: flux_above(E) = 1/E, so threshold=0.5 => E=2.
        """
        target = 0.5
        E_thresh = threshold_energy(unit_model, threshold=target, E_lo=1.0, E_hi=1e6)
        recovered = flux_above(unit_model, E_min=E_thresh)
        assert recovered == approx(target, rel=1e-3)

    def test_known_value(self, unit_model):
        """
        flux_above(unit_model, E) = 1/E, so threshold_energy(..., threshold=0.25) = 4.
        """
        E = threshold_energy(unit_model, threshold=0.25, E_lo=1.0, E_hi=1e6)
        assert E == approx(4.0, rel=1e-3)

    def test_threshold_outside_bracket_raises(self, unit_model):
        """
        flux_above(unit_model) ranges from 1.0 at E=1 to 0.1 at E=10.
        A threshold of 1e6 is not achievable in this bracket.
        """
        with pytest.raises(ConvergenceError, match="not bracketed"):
            threshold_energy(unit_model, threshold=1e6, E_lo=1.0, E_hi=10.0)
