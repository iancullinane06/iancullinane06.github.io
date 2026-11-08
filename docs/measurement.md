---
title: Measurement
nav_order: 1
---

# Measurements and uncertainty

```python
from labplotlib import Measurement
```

`Measurement` stores a numeric value or array and, optionally, its absolute
standard uncertainty. Values and uncertainties are read-only NumPy arrays,
including zero-dimensional arrays for scalar inputs. Arithmetic assumes
independent quantities and propagates uncertainties in quadrature; repeated
use of the same quantity or correlated errors requires a covariance-aware
analysis.

## `Measurement(value, uncertainty=None, unit=None, prefix=None)`

Create a scalar or array-valued measurement.

| Parameter | Meaning |
| --- | --- |
| `value` | Finite number or array-like of finite numbers. |
| `uncertainty` | Non-negative finite absolute standard uncertainty, broadcastable to the shape of `value`; `None` means unknown. |
| `unit` | Optional non-empty, unprefixed unit label, such as `"Pa"`. Used for display only. |
| `prefix` | Optional SI prefix name or symbol, such as `"mega"` or `"M"`; requires `unit`. Used to scale the display only. |

**Returns:** a `Measurement`. Invalid values, uncertainties, units, or prefixes
raise `ValueError`.

```python
from labplotlib import Measurement

pressure = Measurement(2_000_000, 100_000, unit="Pa", prefix="mega")
print(pressure)  # 2.000 ± 0.100 MPa
```

## `Measurement.from_pm(value, uncertainty=None, *, relative=None, granularity=None)`

Combine independent uncertainty components in quadrature.

| Parameter | Meaning |
| --- | --- |
| `value` | Finite number or array-like. |
| `uncertainty` | Optional absolute standard uncertainty. |
| `relative` | Optional fractional uncertainty: `0.02` means 2%, not 0.02%. |
| `granularity` | Optional absolute standard uncertainty due to instrument granularity. Convert a raw resolution to an appropriate standard uncertainty first. |

All uncertainty components must be finite, non-negative, and broadcastable to
the value shape. **Returns:** a `Measurement`; its uncertainty is `None` if no
components were provided.

```python
from labplotlib import Measurement

length = Measurement.from_pm(2.0, 0.1, relative=0.02, granularity=0.01)
print(length)
```

## `Measurement.from_stdev(samples, *, axis=None, mean_error=False, granularity=None)`

Construct a measurement from repeated observations.

| Parameter | Meaning |
| --- | --- |
| `samples` | Finite observations, as a scalar sequence or array. |
| `axis` | Axis over which to calculate the mean and spread; `None` uses all elements. |
| `mean_error` | If `False` (default), use sample standard deviation (`ddof=1`); if `True`, use the standard error of the mean. |
| `granularity` | Optional absolute standard uncertainty combined in quadrature after calculating the spread. |

**Returns:** a `Measurement` of the mean. At least two observations along the
selected axis are required; otherwise `ValueError` is raised.

```python
from labplotlib import Measurement

time = Measurement.from_stdev([1.2, 1.3, 1.4], mean_error=True)
print(time)
```

## `Measurement.from_dataframe(frame, value, *, uncertainty=None, relative=None, granularity=None)`

Read values and uncertainty components from named DataFrame columns. Pandas
is optional and must be installed separately.

| Parameter | Meaning |
| --- | --- |
| `frame` | A DataFrame-like object supporting column lookup with `frame[name]`. |
| `value` | Name of the values column. |
| `uncertainty` | Optional name of an absolute uncertainty column. |
| `relative` | Optional name of a fractional relative uncertainty column. |
| `granularity` | Optional absolute standard uncertainty value or array; not a column name. |

**Returns:** a `Measurement` as produced by `from_pm`. Normal column lookup
and validation errors are propagated.

```python
import pandas as pd
from labplotlib import Measurement

frame = pd.DataFrame({"distance": [1.0, 2.0], "error": [0.1, 0.2]})
distance = Measurement.from_dataframe(frame, "distance", uncertainty="error")
print(distance)
```

## `relative_uncertainty()`

**Parameters:** none. **Returns:** an array containing
`uncertainty / abs(value)`, or `None` when uncertainty is absent. Raises
`ValueError` if an uncertainty is present and any value is zero.

```python
from labplotlib import Measurement

reading = Measurement(10, 0.5)
print(reading.relative_uncertainty())  # 0.05
```

## `set_unit(unit, prefix=None)`

Set or clear display-only unit metadata on an existing measurement.

| Parameter | Meaning |
| --- | --- |
| `unit` | Unprefixed unit string, or `None` to clear the unit. |
| `prefix` | Optional SI prefix name or case-sensitive symbol; requires a unit. Omit it to clear a previously set prefix. |

**Returns:** `None`. Raises `ValueError` for an invalid unit or prefix.
Stored values must be expressed in the base unit: a value of `2_000_000` with
`unit="Pa", prefix="mega"` displays as `2.000 MPa`. No values are converted
in storage and no dimensional compatibility is checked.

```python
from labplotlib import Measurement

pressure = Measurement(2_000_000, 100_000)
pressure.set_unit("Pa", "mega")
print(pressure)  # 2.000 ± 0.100 MPa
pressure.set_unit(None)
```

## `to_string(format="auto", *, decimals=3, unit=None, prefix=None)`

Format a measurement without changing its stored values or display metadata.
`str(measurement)` and `print(measurement)` use the defaults and stored unit.

| Parameter | Meaning |
| --- | --- |
| `format` | `"auto"` uses scientific notation for nonzero magnitudes below `0.001` or at least `1000`; `"raw"` uses decimal notation; `"scientific"` always uses scientific notation. |
| `decimals` | Number of decimal places, including in the scientific mantissa; defaults to `3`. `None` disables rounding. |
| `unit` | Optional unprefixed display unit overriding the stored unit. Supplying it without `prefix` omits any stored prefix. |
| `prefix` | Optional SI prefix name or symbol. With no `unit` argument, a stored unit is used. If neither argument is supplied, the stored prefix is used. |

**Returns:** a string containing the value, optional `±` uncertainty, and
optional prefixed unit. Scientific exponents use Unicode superscripts.
Invalid options and non-finite results from display scaling raise `ValueError`.
Value and uncertainty are formatted independently, including for arrays.

```python
from labplotlib import Measurement

pressure = Measurement(2_000_000, 100_000)
print(pressure.to_string(format="raw", decimals=1))  # 2000000.0 ± 100000.0
print(pressure.to_string(unit="Pa", prefix="mega"))  # 2.000 ± 0.100 MPa
```

## Arithmetic

The operators `+`, `-`, `*`, `/`, and `**` return new measurements and
propagate supplied standard uncertainties. Scalars and broadcastable arrays
can also be operands. Results do not inherit display units; set one explicitly
if needed. If no input has an uncertainty, the result's uncertainty is `None`.
Division by a zero-valued measurement raises `ZeroDivisionError`.

```python
from labplotlib import Measurement

length = Measurement(4, 0.2)
time = Measurement(2, 0.1)
speed = length / time
speed.set_unit("m/s")
print(speed)
```

## `unpack_measurements(data)`

```python
from labplotlib.measurement import unpack_measurements
```

Extract numerical values and uncertainties for downstream code.

| Parameter | Meaning |
| --- | --- |
| `data` | A `Measurement`, an iterable of scalar measurements, or other data. |

**Returns:** `(values, uncertainties)`. For other data the result is
`(data, None)`. An iterable mixing measurements and non-measurements, or
mixing known and absent uncertainties, raises `ValueError`.

```python
from labplotlib import Measurement
from labplotlib.measurement import unpack_measurements

values, errors = unpack_measurements([Measurement(1, 0.1), Measurement(2, 0.2)])
print(values, errors)
```
