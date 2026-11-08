---
title: Hooke's law
nav_order: 3
---

# Hooke's law: measuring a spring constant

Fit force against extension to estimate the spring constant from the slope.
The lower panel shows residuals, helping you spot patterns that a single
best-fit line can hide. The fit assumes independent force uncertainties and
does not account for uncertainty in extension.

![Force versus extension with a fitted line and residuals]({{ '/examples/hookes_law.png' | relative_url }})

[Download the Python source]({{ '/examples/hookes_law.py' | relative_url }}).

{% capture example_source %}{% include_relative hookes_law.py %}{% endcapture %}
<pre><code class="language-python">{{ example_source | escape }}</code></pre>

The sample data give a spring constant of about **24.17 N/m**.
