---
title: Pendulum gravity
nav_order: 4
---

# Estimate gravity with a pendulum

For small oscillations, the period satisfies `T² = (4π²/g)L`. Square each
measured period, including its propagated uncertainty, then fit period squared
against length. The slope gives an estimate of gravitational acceleration.
The model assumes a simple pendulum and ignores uncertainty in length.

![Pendulum period squared against length with a fitted line]({{ '/examples/pendulum_gravity.png' | relative_url }})

[Download the Python source]({{ '/examples/pendulum_gravity.py' | relative_url }}).

{% capture example_source %}{% include_relative pendulum_gravity.py %}{% endcapture %}
<pre><code class="language-python">{{ example_source | escape }}</code></pre>

For these illustrative measurements, the estimate is **9.83 m/s²**.
