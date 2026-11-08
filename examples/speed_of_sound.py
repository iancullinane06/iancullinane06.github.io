"""Compute sound speed from open-open tube resonances in a DataFrame."""

import numpy as np
import pandas as pd

from labplotlib import Measurement


def main() -> None:
    data = pd.DataFrame(
        {
            "length_m": [0.85, 0.86, 0.84],
            "length_error_m": [0.01, 0.01, 0.01],
            "frequency_hz": [200, 200, 200],
            "frequency_error_hz": [1, 1, 1],
            "harmonic": [1, 1, 1],
        }
    )
    length = Measurement.from_dataframe(data, "length_m", uncertainty="length_error_m")
    frequency = Measurement.from_dataframe(
        data, "frequency_hz", uncertainty="frequency_error_hz"
    )
    harmonic = Measurement.from_dataframe(data, "harmonic")

    # Open-open tube, neglecting end corrections: f = n * c / (2 * L).
    speeds = 2 * length * frequency / harmonic
    mean_speed = Measurement(
        np.mean(speeds.value), np.sqrt(np.sum(speeds.uncertainty**2)) / len(speeds.value)
    )
    print("Individual speeds:", speeds.to_string(unit="m/s"))
    print("Mean speed:", mean_speed.to_string(unit="m/s"))


if __name__ == "__main__":
    main()
