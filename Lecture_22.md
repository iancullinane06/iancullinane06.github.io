---
layout: lecture
---
{% raw %}
# The Joule Thomson Expansion
The Joule-Thompson builds on this initial picture. Instead of a container with a stationary gas, and where we let the gas change volume at constant energy, it instead assumes we have a steady flow of gas from a high pressure region at $P_1$ to a low pressure region at $P_2$ via a throttle (or a porous plug, something that can maintain the pressure difference).

![Joule_Expansion](Figures/Joule_Thompson_Expansion.svg)

This is an irreversible process. However, since the initial and final states are both equilibrium states, we can pretend that it does happen reversibly. This leads to the following treatment.

Any gas that is entering into throttle must have work equal to $P_1 V_1$ done on it. After the gas has passed through the throttle, it will expand to pressure $P_2$, thus doing work $P_2 V_2$ on whatever gas was there before. As such, the total work done on the gas as it is compressed and then expands is $W= P_1V_1 - P_2V_2$. Assuming the system is thermally isolated, this means that the change in internal energy of the gas must be $U_2 - U_1 = P_2V_2 - P_1V_1$ which gives
$$
    U_1+ P_1V_1=U_2+ P_2V_2
$$
Since we know that the enthalpy is $H=U+PV$, this means that
$$
    H_1 = H_2.
$$
That is, the enthalpy is conserved in such a process! So for this process, we want to ask the question: "What is the change in temperature with respect to pressure, when performed at constant enthalpy?" or, more formally, we will define the Joule-Thomson coefficient to be
$$
    \mu_{\rm JT} = \left( \frac{\partial T}{\partial P} \right) _H.
$$
As done above, we can subsitute the partial derivative term with
$$
    \left( \frac{\partial T}{\partial P} \right) _H = - \left( \frac{\partial T}{\partial H} \right) _P \left( \frac{\partial H}{\partial P} \right)_T
$$
which means we can write $\mu_{\rm JT}$ to be
$$
    \mu_{\rm JT} = - \frac{1}{C_{\rm P}} \left( \frac{\partial H}{\partial P} \right)_T
$$
We also know that ${\rm d} H = T {\rm d} S +V {\rm d} P$ (see Lecture 7), giving
$$
    \left( \frac{\partial H}{\partial P} \right)_T = T \left( \frac{\partial S}{\partial P} \right)_T + V
$$
leading to
$$
    \mu_{\rm JT} = \frac{1}{C_{\rm P}} \left[ T \left( \frac{\partial V}{\partial T} \right)_P - V \right]
$$
where we've used a Maxwell relation to replace the partial derivative that was there.

It's worth comparing this to the Joule coefficient for a moment. For $\mu_{\rm J}$, we had to evaluate $\left(\frac{\partial P}{\partial T} \right)_V$ for both an ideal gas and a Van der Waals gas to determine the sign of the coefficient, and we found that it's always negative for any gas. However, for $\mu_{\rm J}$, we instead need to evaluate $\left( \frac{\partial V}{\partial T} \right)_P$. This is fine for an ideal gas, but even just for a Van der Waals gas, it is very difficult (give it a try if you don't believe me).

The key point to take away is that $\mu_{\rm J}$ can take either a positive or a negative sign. The point at which the coefficient vanishes is given by
$$
    T \left( \frac{\partial V}{\partial T} \right)_P - V = 0
$$
or when
$$
    \left( \frac{\partial V}{\partial T} \right)_P = \frac{V}{T}
$$
This equation defines a curve in the T-P plane, and is known as the inversion curve. In the lecture, and in Blundell & Blundell, they give a nice discussion as to what the inversion curve is - I highly recommend reading this in order to get a better understanding of what this equation means.
{% endraw %}
