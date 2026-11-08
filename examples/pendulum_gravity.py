"""Estimate gravitational acceleration using a linearized pendulum model."""

import numpy as np

from labplotlib import Measurement, apply_theme, finish_plot, polynomial_fit, scatter_with_fit


def main() -> None:
    length = [0.25, 0.40, 0.55, 0.70, 0.85, 1.00]
    period = Measurement([1.01, 1.27, 1.48, 1.68, 1.85, 2.01], 0.02)
    period_squared = period**2

    fit = polynomial_fit(length, period_squared)
    gravity = 4 * np.pi**2 / fit.coefficients[0]
    print(f"Estimated g: {gravity:.2f} m/s^2")
    print(f"Reduced chi-squared: {fit.reduced_chi_squared:.2f}")

    apply_theme()
    fig = scatter_with_fit(
        length, period_squared, title="A simple pendulum",
        xlabel="Length (m)", ylabel="Period squared (s²)"
    )
    finish_plot(fig, filename="pendulum_gravity.png", show=True)


if __name__ == "__main__":
    main()
