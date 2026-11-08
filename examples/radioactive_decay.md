---
title: Radioactive decay
nav_order: 5
---

# Radioactive decay with error bars

Compare illustrative count data with an exponential decay curve. The
uncertainties use the Poisson approximation `√N` for each count. The curve
is a chosen model, not a fit to these observations.

![Counts with error bars and an exponential decay curve]({{ '/examples/radioactive_decay.png' | relative_url }})

[Download the Python source]({{ '/examples/radioactive_decay.py' | relative_url }}).

{% capture example_source %}{% include_relative radioactive_decay.py %}{% endcapture %}
<pre><code class="language-python">{{ example_source | escape }}</code></pre>

This example draws both datasets on the same Matplotlib axes and adds a legend
before saving the figure.
