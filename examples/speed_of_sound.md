---
title: Speed of sound
nav_order: 2
---

# Speed of sound from resonances

Read tube lengths and frequencies from a pandas DataFrame, then calculate the
speed of sound using `c = 2Lf / n` for an open-open tube. This simplified
model ignores end corrections. Each reading's uncertainty is propagated from
the length and frequency.

This example requires pandas as well as LabPlotLib.
[Download the Python source]({{ '/examples/speed_of_sound.py' | relative_url }}).

{% capture example_source %}{% include_relative speed_of_sound.py %}{% endcapture %}
<pre><code class="language-python">{{ example_source | escape }}</code></pre>

The mean is approximately **340.0 ± 2.5 m/s**. Its uncertainty combines the
individual propagated uncertainties assuming independent readings; it does
not include shared systematic effects or estimate the spread of repeated
readings.
