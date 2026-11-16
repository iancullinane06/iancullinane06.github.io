"""Generate the plotting examples embedded in docs/plotting.md."""

from pathlib import Path

import numpy as np
from matplotlib.figure import Figure

from labplotlib import (
    Measurement,
    apply_theme,
    bode_plot,
    errorbar_plot,
    finish_plot,
    line_plot,
    scatter_plot,
    scatter_with_bands,
    scatter_with_fit,
    scatter_with_residuals,
)


OUTPUT_DIR = Path(__file__).parent


def save_example(fig: Figure, filename: str) -> None:
    finish_plot(fig, filename=OUTPUT_DIR / filename, dpi=180)


def main() -> None:
    apply_theme()

    time = np.arange(0, 12, 2)
    temperature = [72, 56, 45, 38, 33, 30]
    fig = line_plot(
        time,
        temperature,
        title="Cooling after a warm-water bath",
        xlabel="Time (min)",
        ylabel="Temperature (°C)",
        label="Water temperature",
        color="C0",
        marker="o",
        figsize=(9, 5.5),
    )
    fig.axes[0].legend()
    save_example(fig, "line_plot.png")

    horizontal = np.linspace(0, 10, 11)
    height = -0.32 * (horizontal - 5) ** 2 + 8
    elapsed = np.linspace(0, 2, horizontal.size)
    fig = scatter_plot(
        horizontal,
        height,
        c=elapsed,
        title="Ball flight | colour shows elapsed time",
        xlabel="Horizontal distance (m)",
        ylabel="Height (m)",
        cmap="flare",
        colorbar=True,
        colorbar_label="Time (s)",
        marker="o",
        figsize=(9, 5.5),
    )
    save_example(fig, "scatter_plot.png")

    time = np.arange(9)
    distance = Measurement(
        [0.4, 1.5, 2.7, 3.8, 5.1, 6.2, 7.5, 8.7, 9.8],
        [0.25, 0.20, 0.30, 0.25, 0.35, 0.25, 0.30, 0.25, 0.35],
    )
    fig = scatter_with_fit(
        time,
        distance,
        title="Position from a constant-speed run",
        xlabel="Time (s)",
        ylabel="Distance (m)",
        label="Measured position",
        color="C0",
        fit_color="C1",
        show_stats=True,
        figsize=(9, 5.5),
    )
    save_example(fig, "scatter_with_fit.png")

    concentration = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30])
    response = Measurement(
        [1.9, 2.8, 3.8, 4.0, 5.1, 5.8],
        [0.20, 0.22, 0.18, 0.25, 0.21, 0.24],
    )
    fig = scatter_with_bands(
        concentration,
        response,
        title="Calibration curve with uncertainty bands",
        xlabel="Concentration (mol/L)",
        ylabel="Sensor response (V)",
        fit_range=(0, 0.35),
        prediction_uncertainty=0.25,
        show_stats=True,
        label="Calibration samples",
        color="C0",
        fit_color="C1",
        figsize=(9, 5.5),
    )
    ax = fig.axes[0]
    ax.axvline(0.35, color="C3", linestyle=":", label="Extrapolation edge")
    ax.set_xlim(0, 0.38)
    ax.legend(loc="lower right")
    save_example(fig, "scatter_with_bands.png")

    current = np.arange(1, 8)
    voltage = [0.48, 0.91, 1.36, 1.69, 2.17, 2.55, 2.88]
    fig = errorbar_plot(
        current,
        voltage,
        xerr=[0.12, 0.10, 0.12, 0.15, 0.12, 0.16, 0.14],
        yerr=[0.10, 0.12, 0.09, 0.13, 0.10, 0.15, 0.12],
        title="Voltage-current measurements",
        xlabel="Current (mA)",
        ylabel="Voltage (V)",
        label="Measured voltage",
        color="C2",
        marker="o",
        figsize=(9, 5.5),
    )
    fig.axes[0].legend()
    save_example(fig, "errorbar_plot.png")

    time = np.arange(9)
    residual_data = 0.5 + 1.1 * time + 0.10 * (time - 4) ** 2
    residual_data += np.array([0.00, -0.12, 0.10, -0.08, 0.05, 0.13, -0.09, 0.08, 0.02])
    position = Measurement(residual_data, 0.20)
    fig = scatter_with_residuals(
        time,
        position,
        title="Residuals reveal a curved trend",
        xlabel="Time (s)",
        ylabel="Position (m)",
        label="Measurements",
        color="C0",
        fit_color="C1",
        show_stats=True,
        figsize=(9, 7),
    )
    save_example(fig, "scatter_with_residuals.png")

    frequency = np.logspace(1, 4, 24)
    gain = Measurement(1 / np.sqrt(1 + (frequency / 650) ** 2), 0.015)
    phase = Measurement(-np.degrees(np.arctan(frequency / 650)), 1.0)
    fig = bode_plot(
        frequency,
        gain,
        phase,
        title="RC low-pass filter | gain and phase",
        label="Measured response",
        figsize=(9, 5.5),
    )
    save_example(fig, "bode_plot.png")


if __name__ == "__main__":
    main()
