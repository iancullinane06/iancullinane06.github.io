# The Clausius-Clapeyron Equation

We next will focus on deriving a differential equation for the slope of a phase equilibrium curve. This specifies the slope ${\rm d} P/{\rm d} T$ at every point of the curve. First, let's consider two points separated by some small ${\rm d} T$ and ${\rm d} P$ on the phase equilibrium curve such that
$$
\begin{align}
g_1(T,P) &= g_2(T,P)\\
g_1(T+{\rm d}T,P+{\rm d}P) &= g_2(T+{\rm d}T,P+{\rm d}P)\\
\end{align}
$$
The difference between these points is given by
$$
{\rm d}g_1(T,P)={\rm d}g_2(T,P)
$$
Using our usual trick of
$$
    {\rm d} g_1(T,P) = \left(\frac{\partial g_1}{\partial T}\right)_P {\rm d}{T} + \left(\frac{\partial g_1}{\partial P}\right)_T {\rm d}{P}
$$
we get that
$$
    \left(\frac{\partial g_1}{\partial T}\right)_P {\rm d}{T} + \left(\frac{\partial g_1}{\partial P}\right)_T {\rm d}{P} = \left(\frac{\partial g_2}{\partial T}\right)_P {\rm d}{T} + \left(\frac{\partial g_2}{\partial P}\right)_T {\rm d}{P}
$$
Thus
$$
\frac{{\rm d} P}{{\rm d} T} = \frac{\left(\frac{\partial g_1}{\partial T}\right)_P - \left(\frac{\partial g_2}{\partial T}\right)_P}{\left(\frac{\partial g_2}{\partial P}\right)_T - \left(\frac{\partial g_1}{\partial P}\right)_T} = - \frac{\left(\frac{\partial g_2}{\partial T}\right)_P - \left(\frac{\partial g_1}{\partial T}\right)_P}{\left(\frac{\partial g_2}{\partial P}\right)_T - \left(\frac{\partial g_1}{\partial P}\right)_T}
$$
Using the notation $\Delta f \equiv f_2-f_1$, we can write this as
$$
    \frac{{\rm d} P}{{\rm d} T} = - \frac{\Delta \left(\frac{\partial g}{\partial T}\right)_P}{\Delta \left(\frac{\partial g}{\partial P}\right)_T}
$$
In order to simplify this equation further, recall that the Gibbs free energy for a system in phase i is given
$$
    {\rm d} G_i = V_i {\rm d} P - S_i {\rm d} T + \mu_i {\rm d} N_i.
$$
For a single component system we have that $\mu_i = g_i$ and $G_i = N_i g_i$, which means we can write this as
$$
    N_i {\rm d}g_i = V_i {\rm d} P - S_i {\rm d} T
$$
which gives
$$
    \left(\frac{\partial g_i}{\partial T}\right)_P = -\frac{S_i}{N_i} \:\:\:\: \left(\frac{\partial g_i}{\partial P}\right)_T = \frac{V_i}{N_i}.
$$
These let us simplify the above expression for ${\rm d}P/{\rm d}T$ to
$$
    \frac{{\rm d} P}{{\rm d} T} = \frac{\Delta S}{\Delta V}
$$
This equation relates the change in entropy and change in volume of a system at different pressures and temperatures which lie along the phase equilibrium curve. In order to better understand this expression, consider two phases of a 1 component system which are in thermodynamic equilibrium with each other at a temperature of $T$. To convert any of the component from phase 1 to phase 2, a **latent heat** must be added. This represents the difference in entropy between the 2 phases, and is given by
$$
    L_{1,2} = T \left(S_2-S_1\right) = T \Delta S.
$$
This allows us to write the Clauius-Clapeyron equation as
$$
    \frac{{\rm d} P}{{\rm d} T} = \frac{L_{1,2}}{T \Delta V}
$$
It's useful to point out at this stage that, because we cancelled a $N_i$ (particle number in phase i) in the last lecture to arrive at this expression, then $L_{1,2}$ and $\Delta V$ must refer to the same amount of substance - that is, if $L_{1,2}$ is given for 1 mole of a substance, then $\Delta V$ should be the volume change of 1 mole.

Immediately, some useful information can be drawn from this equation. First, for melting, evaporation, or sublimation, the entropy changes are positive (during these processes, we are going from more-ordered to less ordered states). 

Second, when going from a solid or a liquid to a gas, the density decreases, which means the volume increases. As such, $\frac{{\rm d} P}{{\rm d} T}$ is positive for the vapour-pressure and sublimation curves. 

For melting, things get a bit more complicated. **Most** substances expand when they melt, and for such substances $\frac{{\rm d} P}{{\rm d} T}$ is also positive for melting. However, some substances (such as water) contract when they melt (which is of course why ice floats and is due to the unusual shape of water molecules). For these substances, $\frac{{\rm d} P}{{\rm d} T}$ is negative for melting.

## Examples
### Pressure dependence of melting point of water

First, let us consider the phase equilibrium curve for ice and liquid water at 0$^{\rm o}$ C. In order to work with the Clausius-Clapyeron equation, we need

* The latent heat of fusion for water at 0$^{\rm o}$ C: $L_{1,2}=3.35 \times 10^5$ J/kg
* The volumes per gram in the solid and liquid phases at 0$^{\rm o}$ C, which are: $V_1=1.09070$ cm$^{3}$/g and $V_2=1.00013$ cm$^{3}$/g respectively.

From this, we have that $\Delta V=-0.0906 \times 10^{-3}$ m$^{3}$/kg. This gives that
$$
    \frac{{\rm d} P}{{\rm d} T} = \frac{3.35 \times 10^5}{(273.15)(-0.0906 \times 10^{-3})} = -1.35 \times 10^7 \: {\rm N} \: {\rm m^{-2}} \: {\rm K^{-1}}.
$$
Knowing that $1.01325\times 10^5\: {\rm N} \: {\rm m^{-2}} = 1.01325\times 10^5\: {\rm Pa}= 1 \: {\rm atm}$, we can write this as 
$$
    \frac{{\rm d} P}{{\rm d} T} = -134 \: {\rm atm} \: {\rm K^{-1}}
$$
This means that the melting point decreases by 1$^{\rm o}$ when the pressure is increased by $134$ atmospheres. This decrease is also what allows for glaciers to move. At their base, the high pressure due to the weight of the ice above the base lowers the melting point, meaning the base of the glacier becomes a liquid on which the glacier can move.

### Pressure dependence of boiling point of water

Ok, let us now consider liquid water and water vapour. For this, we need 

* The latent heat of vaporisation for water at 100$^{\rm o}$ C: $L_{1,2}=2.257 \times 10^6$ J/kg
* The volumes per gram in the liquid and gas phases at 100$^{\rm o}$ C, which are: $V_1=1.043$ cm$^{3}$/g and $V_2=1,673$ cm$^{3}$/g respectively.

Thus we get
$$
    \frac{{\rm d} P}{{\rm d} T} = \frac{2.257 \times 10^6}{(373.15)(1.672)} = 3.62 \times 10^3 \: {\rm N} \: {\rm m^{-2}} \: {\rm K^{-1}}.
$$

So, if we were at the peak of Mt. Everest, which is at a pressure of $3.6 \times 10 ^ 4\: {\rm N} \: {\rm m^{-2}}$, then the change in pressure relative to 1 atmosphere is
$$
    \Delta P = -6.5\times10^4 \: {\rm N} \: {\rm m^{-2}}
$$
The change in the temperature at which water boils is thus
$$
    \Delta T = - \frac{6.5\times10^4}{3.62\times10^3} = -18^{\rm o}
$$
Meaning water boils at $82^{\rm o}$C at this altitude.