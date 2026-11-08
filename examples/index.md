---
title: Examples
nav_order: 0
---

# LabPlotLib examples

These complete programs combine measurements, uncertainty, fitting, and
plotting. The datasets are illustrative; replace them with your own readings.
Every page includes copyable code and a downloadable Python file.

| Example | What you'll explore |
| --- | --- |
| [Measurement formatting](measurement_formatting.html) | Display uncertainty and SI prefixes |
| [Speed of sound](speed_of_sound.html) | Read a DataFrame and propagate measurement errors |
| [Hooke's law](hookes_law.html) | Fit a spring constant and inspect residuals |
| [Pendulum gravity](pendulum_gravity.html) | Estimate gravitational acceleration from a linearized fit |
| [Radioactive decay](radioactive_decay.html) | Overlay a decay model on observations with error bars |

## Running the examples

The examples were tested with LabPlotLib 0.6.0. Install it with:

```shell
pip install labplotlib
```

The speed-of-sound example additionally requires `pip install pandas`. Save an
example's Python file and run it using `python filename.py`. The plotting
examples save a PNG in the working directory and display the plot when run
with an interactive Matplotlib backend.

Measurement formatting uses Unicode symbols; on Windows, use a UTF-8 terminal
or run Python with `-X utf8` if your terminal cannot display them.
