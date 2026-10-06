---
layout: lecture
---
# The absolute scale of entropy?
The second law of thermodynamics introduced the concept of entropy, and that it either always stays constant or else increases for an isolated system. However, we don't know yet how to measure entropy, or what a typical value for it might be.

Consider again our definitions of heat capacities. We have that
$$
    C_{\rm V} = \left(\frac{\partial Q}{\partial T}\right)_V = T \left(\frac{\partial S}{\partial T}\right)_V
$$
and 
$$
    C_{\rm P} = \left(\frac{\partial Q}{\partial T}\right)_P = T \left(\frac{\partial S}{\partial T}\right)_P
$$
From this, we have that
$$
    S = \int \frac{{\rm d}Q}{T} = \int \frac{C_P}{T} {\rm d} T
$$
If we integrate this function, we end up with an undefined constant
$$
    S(T) = S(T_0) + \int _{T_0} ^T \frac{C_P}{T} {\rm d} T
$$
We've seen that measuring changes of S is possible, but figuring out an absolute measurement of entropy is not easy. This is what the third law of thermodynamics addresses.

# The Third Law of Thermodynamics
There are two ways of arriving at a definition of the third law: statistically and experimentally. Let's start with the statistical definition.
## Statistical
Consider a system which has distinct energy levels. If we enumerate over the energy levels without repetition, we have
$$
    E_1<E_2<E_3<...<E_r<...
$$
such that the degeneracy of level $E_r$ is $g(E_r)$. The probability of the system being in a state with energy $E_r$ is thus
$$
    P(E_r) = \frac{1}{Z} g(E_r) {\rm e}^{-\beta E_r}
$$
If the temperature of the system is low enough such that
$$
    E_2 - E_1 >> k_{\rm B}T
$$
Then we'll have that
$$
    P(E_1) \approx 1, P(E_r) \approx 0
$$
for all r > 1. Basically, we're saying that at low temperatures, we should only ever find the system to be in its ground state. The entropy of the system at these low temperatures must then satisfy
$$
   \lim_{T\to 0} S = k_{\rm B} \ln g(E_1)
$$
Although it has not be proven that $g(E_1)=1$ for all systems (that is, the ground state for every system is non-degenerate), it holds for all cases that have been checked. This then means that
$$
   \lim_{T\to 0} S = 0
$$
This leads quite nicely to Planck's statement of the third law, which is that

**The entropy of all systems in internal equilibrium is the same as absolute 0, and may be taken to be zero**

In the last lecture, we looked at a statistical definition of the third law of thermodynamics. Let's continue that discussion today, and look at a classical definition
## Classical
Let's consider the enthalpy and the Gibb's free energy again:
$$
\begin{align}
    {\rm d} H &= T{\rm d} S + V {\rm d} P\\
    {\rm d} G &= {\rm d} H - T {\rm d} S - S {\rm d} T
\end{align}
$$
If we perform a reaction in the lab (meaning it will be under constant temperature and pressure) we got the following information. First, change in enthalpy just becomes
$$
    \Delta{H} = \Delta{Q}
$$
If $\Delta{H}<0$, then heat is emitted from the system (exothermic reactions). If $\Delta{H}>0$, then heat is absorbed into the system (endothermic reactions). For the Gibb's free energy, we found that under such conditions (constant T and P), ${\rm d} G \leq 0$ - that is, the system will always try to minimise the Gibbs energy in order to reach equilibrium. As such, if for the reaction $\Delta G < 0$, it can occur spontaneously!

So, for such a reaction we have that
$$
    {\rm \Delta} G = {\rm \Delta} H - T {\rm \Delta} S
$$
This means that as the temperature approaches 0, the Gibbs Free energy and the enthalpy approach each other. This was experimentally proven by Walter Nernst, who then postulated that the entropy should go as $\Delta S \to 0$ as $T \rightarrow 0$. This lead to the statement that

**Near absolute zero, all reactions in a system in internal equilibrium take place with no change in entropy.**

## Consequences

### Heat Capacity
So how does the 3rd Law affect all of the things we've talked about so far? First, let's consider heat capacity. Given that
$$
    C = T \left( \frac{\partial S}{\partial T}\right) = \left( \frac{\partial S}{\partial \ln T}\right) \rightarrow 0
$$
as, when $T\rightarrow 0$, $\ln T\rightarrow \infty$ - so heat capacities go to 0 at 0 temperature!
### Ideal gases
Ideal gases cannot exist at 0 temperature. One of the early results we concluded for ideal gases was that the different in heat capacities should be $C_P-C_V = Nk_{\rm B}$. However, as $T\rightarrow0$ , both of these must go to 0. Even worse, we found that $C_V=3Nk_{\rm B}/2$. So when working at low temperatures, in order to satisfy the 3rd law, we must abandon the ideal gas.
### Thermal Expansion
From Maxwell's equations, we have that
$$
    \left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P
$$
Since $S=S(T,P)\rightarrow 0$ as $T\rightarrow 0$ for all P, this implies that the left hand side of this equation also goes to 0. As such,
$$
    \lim _{T\to 0} \left(\frac{\partial V}{\partial T}\right)_P = 0
$$
which also means that $\beta_P \to 0$. This means that thermal expansion stops.

With that, our discussion of the laws of classical thermodynamics comes to a close. Next, we're going to discuss statistical mechanics, and start looking at how we apply both classical and statistical thermodynamics to particular problems.

## Unattainability of absolute zero
Another consequence is that no system can be cooled to absolute 0 K. To see this, consider two different tracks through the $S-T$ plane, where each track represents a different parameter (like pressure or volume). If there existed a track where the entropy did not go to 0 at 0 K, then you could imagine cooling a system by first reducing the systems entropy isothermally (to get you to the lower track), then cooling the system isentropically (bringing you back to the upper track) and you could do this repeatedly until the system was below 0 K.

![Third_Law](Figures/ThirdLaw.jpg)
However, if instead all processes lead to an entropy of 0 at a temperature of 0 K, then such a combination of isentropic and isothermal processes will only ever let you approach a temperature of 0 K, it will never actually get you there.