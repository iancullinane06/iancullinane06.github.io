"""Fit spring-force measurements and inspect the residuals."""

from labplotlib import Measurement, apply_theme, finish_plot, polynomial_fit, scatter_with_residuals


def main() -> None:
    extension = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06]
    force = Measurement([0.24, 0.48, 0.73, 0.97, 1.22, 1.44], 0.04)

    fit = polynomial_fit(extension, force)
    print(f"Spring constant: {fit.coefficients[0]:.2f} N/m")
    print(f"Intercept: {fit.coefficients[1]:.3f} N")
    print(f"Reduced chi-squared: {fit.reduced_chi_squared:.2f}")

    apply_theme()
    fig = scatter_with_residuals(
        extension, force, title="Hooke's law", xlabel="Extension (m)", ylabel="Force (N)"
    )
    finish_plot(fig, filename="hookes_law.png", show=True)


if __name__ == "__main__":
    main()
