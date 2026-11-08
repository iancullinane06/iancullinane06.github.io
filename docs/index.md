---
title: Overview
nav_order: 0
---

# LabPlotLib reference

This reference describes the LabPlotLib 0.6.0 API. Each page covers one
module, with examples, parameters, and return values.

| Module | What it covers |
| --- | --- |
| [measurement](measurement.html) | Values, uncertainties, arithmetic, and formatting |
| [plotting](plotting.html) | Line plots, fits, error bars, and residuals |
| [methods](methods.html) | Polynomial fits, fit statistics, and clustering |
| [styling](styling.html) | Theme, axes, figure layout, saving, and showing |
| [symbols](symbols.html) | Mathematical symbol lookup and printing |

Most frequently used names are available directly from `labplotlib`. Other
functions shown with module imports are available from their respective modules.
See the [examples]({{ '/examples/' | relative_url }}) for complete runnable
programs, including measurement formatting, a speed-of-sound calculation, and
plotting experiments.

## Conventions

- Parameters after `*` in a signature must be supplied by keyword.
- Plotting helpers return a Matplotlib `Figure`; they do not call `show()` by
  default. When neither saving nor showing, they leave figure layout to the
  caller.
- A `Measurement` stores a value and an optional **absolute standard
  uncertainty**. Its units are display metadata, not dimensional analysis or
  unit conversion.
- Examples assume LabPlotLib is installed. DataFrame examples additionally
  require pandas.
