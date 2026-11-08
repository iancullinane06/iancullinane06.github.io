---
title: Measurement formatting
nav_order: 1
---

# Measurement formatting

Display a pressure measurement in different formats and SI prefixes, then
propagate its uncertainty through a calculation. Prefixes affect display only:
the stored value remains in pascals.

[Download the Python source]({{ '/examples/measurement_formatting.py' | relative_url }}).

{% capture example_source %}{% include_relative measurement_formatting.py %}{% endcapture %}
<pre><code class="language-python">{{ example_source | escape }}</code></pre>

The final result is `4.0 ± 0.2 MPa`. The published 0.6.0 package accepts units
and prefixes in `to_string`; it does not support `set_unit` or `decimals`,
which are currently described in the
[measurement reference]({{ '/docs/measurement.html' | relative_url }}).
