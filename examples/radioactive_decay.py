"""Compare simulated radioactive counts with an exponential decay curve."""

import numpy as np

from labplotlib import Measurement, apply_theme, errorbar_plot, finish_plot, line_plot


def main() -> None:
    time = np.arange(0, 11)
    counts = np.array([202, 174, 151, 129, 110, 96, 80, 68, 61, 50, 43])
    observations = Measurement(counts, np.sqrt(counts))
    model_time = np.linspace(0, 10, 200)
    model_counts = 200 * np.exp(-0.15 * model_time)

    apply_theme()
    fig = errorbar_plot(
        time, observations, title="Radioactive decay",
        xlabel="Time (minutes)", ylabel="Counts per minute",
        label="Observed counts", color="C0"
    )
    line_plot(model_time, model_counts, ax=fig.axes[0], label="Decay model", color="C1")
    fig.axes[0].legend()
    finish_plot(fig, filename="radioactive_decay.png", show=True)


if __name__ == "__main__":
    main()
