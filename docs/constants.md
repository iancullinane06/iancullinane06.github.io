# Scientific constants

Import constants for use in calculations:

```python
from labplotlib import Measurement, consts

temperature = Measurement(300, 3)
energy = consts.kb * temperature
```

Constants carry `Unit` objects, which propagate through measurement
multiplication and division. To check a result against a known dimension, use
`energy.unit.is_compatible(...)`. A measurement without a unit is still
accepted; it simply contributes no dimensions.

To list the constants, run the source file directly from the project root:

```powershell
python .\src\labplotlib\consts.py
```