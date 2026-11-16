# Dimensional analysis

`Unit` stores a tuple of seven exponents in this order: metre (m), second (s),
kilogram (kg), ampere (A), kelvin (K), mole (mol), and candela (cd). For
example, metres per second have the vector `(1, -1, 0, 0, 0, 0, 0)`.
Multiplication adds exponents, division subtracts them, and raising a unit to a
power multiplies each exponent by that power.

```python
from labplotlib import Unit

metre = Unit("metre", "m", (1, 0, 0, 0, 0, 0, 0))
second = Unit("second", "s", (0, 1, 0, 0, 0, 0, 0))
speed = metre / second

print(speed.vector)  # (1.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0)
print(speed)         # metre second^-1
Unit.set_display_style("symbol")
print(speed)         # ms^-1
print(speed.is_compatible(metre / second))  # True
```

Unit names are displayed by default; `Unit.set_display_style("symbol")` switches
formatting to compact SI symbols with exponents. A `Unit` checks dimensional
compatibility but does not store scale factors or convert between units.
`Measurement` accepts a `Unit` in its `unit` field and propagates it through
multiplication, division, and powers. Addition and subtraction reject two
incompatible specified units. Unspecified units remain allowed and do not
prevent calculations.
