---
layout: lecture
title: Summary: Lectures 1–9
---
{% raw %}

# Thermodynamics Study Summary: Lectures 1–9

This summary collects the central definitions, equations, and derivation outlines from [Lecture 1](./Lecture_01.md) through [Lecture 9](./Lecture_09.md). Unless stated otherwise, use the sign convention from these notes: heat $Q$ is positive when supplied to the system, and work $W$ is positive when done on the system.

## 1. Counting states and macroscopic descriptions

### Microstates, macrostates, and multiplicity

- A **microstate** is a particular microscopic arrangement of a system.
- A **macrostate** is specified by observable macroscopic quantities, such as energy, pressure, or magnetisation; many microstates can correspond to the same macrostate.
- The **multiplicity** or statistical weight $\Omega$ is the number of microstates compatible with a macrostate. For equally likely microstates, the macrostate with the largest $\Omega$ is the most probable.
- For $N$ two-state dipoles, with $n$ aligned one way and $N-n$ the other:

$$
E(n)=(N-2n)\mu B,\qquad
\Omega(n)=\binom{N}{n}=\frac{N!}{n!(N-n)!}.
$$

### Combinations and Stirling's approximation

Choosing $r$ indistinguishable objects from $n$ available positions gives

$$
\Omega=\binom{n}{r}=\frac{n!}{r!(n-r)!}.
$$

For large $n$, factorials are simplified using Stirling's approximation:

$$
\ln(n!)\simeq n\ln n-n.
$$

### Macroscopic variables and the ideal gas

- **Extensive variables** scale with system size (for example, volume and total energy).
- **Intensive variables** do not scale with system size (for example, pressure and temperature).
- The thermodynamic limit is the large-system regime in which microscopic fluctuations are negligible at ordinary measurement scales.
- An ideal gas is modelled as point particles with negligible interparticle forces. Its equation of state is

$$
PV=Nk_{\rm B}T=nRT,\qquad R=N_{\rm A}k_{\rm B}.
$$

For the monatomic ideal gas considered in these notes,

$$
U=\frac{3}{2}Nk_{\rm B}T.
$$

### Heat and heat capacity

**Heat** is energy in transit due to a temperature difference; it is not energy stored as a state property. Heat capacity describes the heat required for a temperature change, subject to the process constraint:

$$
C_V=\left(\frac{\partial Q}{\partial T}\right)_V,\qquad
C_P=\left(\frac{\partial Q}{\partial T}\right)_P.
$$

## 2. Equilibrium, temperature, and ensembles

### Zeroth law and thermal equilibrium

Two systems are in **thermal equilibrium** when there is no net heat flow between them. The **zeroth law** says that if each of two systems is separately in thermal equilibrium with a third, then they are in thermal equilibrium with each other. This makes temperature a usable property for comparing systems and underpins thermometers.

### Statistical definition of temperature

For two systems exchanging energy in an isolated whole, $E=E_1+E_2$ is fixed. The number of combined microstates at a given energy split is

$$
\Omega_{\rm total}(E_1)=\Omega_1(E_1)\Omega_2(E_2).
$$

Equilibrium is the most probable energy split, so it maximises this product. Differentiating its logarithm and using ${\rm d}E_2=-{\rm d}E_1$ gives

$$
\left(\frac{\partial\ln\Omega_1}{\partial E_1}\right)
=
\left(\frac{\partial\ln\Omega_2}{\partial E_2}\right).
$$

Since systems in thermal equilibrium have the same temperature, define

$$
\frac{1}{T}=k_{\rm B}\left(\frac{\partial\ln\Omega}{\partial E}\right),
\qquad\text{or}\qquad
\frac{1}{k_{\rm B}T}=\frac{\partial\ln\Omega}{\partial E}.
$$

### Ensembles

- **Microcanonical:** fixed energy; isolated system.
- **Canonical:** energy can be exchanged with a large heat reservoir; temperature is fixed.
- **Grand canonical:** both energy and particles can be exchanged with a reservoir.

## 3. Boltzmann distribution and partition function

For a small system in thermal contact with a much larger reservoir, a system microstate of energy $\epsilon$ has probability proportional to the reservoir multiplicity:

$$
P(\epsilon)\propto\Omega_R(E-\epsilon).
$$

For $\epsilon\ll E$, expand the reservoir's log multiplicity to first order:

$$
\ln\Omega_R(E-\epsilon)
\simeq\ln\Omega_R(E)
-\epsilon\left(\frac{\partial\ln\Omega_R}{\partial E}\right)
=\ln\Omega_R(E)-\frac{\epsilon}{k_{\rm B}T}.
$$

Exponentiating and normalising over system microstates gives the **Boltzmann distribution**:

$$
\beta\equiv\frac{1}{k_{\rm B}T},\qquad
Z\equiv\sum_i e^{-\beta E_i},\qquad
P_i=\frac{e^{-\beta E_i}}{Z}.
$$

$Z$ is the **partition function**. The expression above gives the probability of a microstate; if an energy level has degeneracy, its total probability includes the number of microstates at that energy.

The mean internal energy follows by averaging over states:

$$
\bar U=\sum_i P_iE_i
=\frac{1}{Z}\sum_i E_i e^{-\beta E_i}.
$$

Since $\partial Z/\partial\beta=-\sum_i E_i e^{-\beta E_i}$,

$$
\boxed{\bar U=-\frac{\partial\ln Z}{\partial\beta}}.
$$

## 4. State functions, first law, heat capacities, and ideal-gas processes

### State functions and differentials

A **state function** has a value determined by the equilibrium state, independent of the path used to reach it. Its differential is exact (for example, ${\rm d}U$). Heat and work depend on the process and are inexact differentials ($\delta Q$, $\delta W$). An **equation of state** relates state variables, such as $PV=Nk_{\rm B}T$.

### First law and pressure-volume work

With heat supplied to the system positive and work done on it positive, the first law is

$$
\Delta U=Q+W,\qquad {\rm d}U=\delta Q+\delta W.
$$

For reversible quasistatic pressure-volume work, compression changes the system's volume by ${\rm d}V<0$ and work is

$$
\delta W=-P\,{\rm d}V.
$$

Therefore, for a reversible process with only pressure-volume work,

$$
{\rm d}U=\delta Q-P\,{\rm d}V.
$$

### Heat-capacity relations

Writing $U=U(T,V)$ and taking its total differential,

$$
{\rm d}U=
\left(\frac{\partial U}{\partial T}\right)_V{\rm d}T+
\left(\frac{\partial U}{\partial V}\right)_T{\rm d}V.
$$

Combining this with $\delta Q={\rm d}U+P\,{\rm d}V$ gives

$$
C_V=\left(\frac{\partial U}{\partial T}\right)_V,
$$

and

$$
C_P-C_V=
\left[\left(\frac{\partial U}{\partial V}\right)_T+P\right]
\left(\frac{\partial V}{\partial T}\right)_P.
$$

The **adiabatic index** is $\gamma=C_P/C_V$. For a monatomic ideal gas:

$$
C_V=\frac{3}{2}Nk_{\rm B},\qquad
C_P=\frac{5}{2}Nk_{\rm B},\qquad
\gamma=\frac{5}{3}.
$$

### Reversible isothermal ideal-gas expansion

At constant temperature, the ideal gas has ${\rm d}U=C_V{\rm d}T=0$. Thus $\delta Q=-\delta W=P\,{\rm d}V$. Using $P=Nk_{\rm B}T/V$:

$$
Q_{\rm rev}
=\int_{V_1}^{V_2}P\,{\rm d}V
=Nk_{\rm B}T\ln\frac{V_2}{V_1}
=nRT\ln\frac{V_2}{V_1}.
$$

During expansion, $V_2>V_1$, so the gas absorbs heat and does an equal amount of work on its surroundings.

### Reversible adiabatic ideal-gas expansion

Adiabatic means no heat transfer, $\delta Q=0$. The first law and ideal-gas relation give

$$
C_V\,{\rm d}T=-P\,{\rm d}V
=-\frac{Nk_{\rm B}T}{V}\,{\rm d}V.
$$

Integrating and using $\gamma=C_P/C_V$ yields

$$
TV^{\gamma-1}=\text{constant},\qquad
PV^\gamma=\text{constant},\qquad
P^{1-\gamma}T^\gamma=\text{constant}.
$$

## 5. Second law, heat engines, and entropy

### Second-law statements

- **Clausius:** heat cannot, as its sole effect, flow from a colder body to a hotter body.
- **Kelvin–Planck:** no cyclic engine can convert heat taken from a single reservoir entirely into work.

The notes show their equivalence by coupling a hypothetical violation of either statement to a Carnot engine: either violation would produce a violation of the other.

### Carnot engine and refrigerator

A reversible Carnot engine runs between hot and cold reservoirs at $T_H>T_L$. Over a cycle $\Delta U=0$, so the work output is $W=Q_H-Q_L$. The reversible isothermal and adiabatic legs give

$$
\frac{Q_H}{Q_L}=\frac{T_H}{T_L}.
$$

For an ideal gas, the magnitudes of the heat transfers on the isothermal legs are

$$
Q_H=RT_H\ln\frac{V_B}{V_A},\qquad
Q_L=RT_L\ln\frac{V_C}{V_D}.
$$

The two adiabatic legs imply $V_B/V_A=V_C/V_D$. Substituting that shared volume ratio into the isothermal heat expressions gives $Q_H/Q_L=T_H/T_L$.

Thus the engine efficiency is

$$
\eta=\frac{W}{Q_H}
=1-\frac{Q_L}{Q_H}
=1-\frac{T_L}{T_H}.
$$

No engine operating between the same reservoir temperatures can exceed this reversible efficiency. Reversing the cycle gives the refrigerator coefficient of performance (heat removed from the cold reservoir per work input):

$$
\mathrm{COP}_{R}=\frac{Q_L}{W}
=\frac{T_L}{T_H-T_L}.
$$

This is a coefficient of performance, not an engine efficiency.

### Clausius theorem and entropy

For a reversible cycle,

$$
\oint\frac{\delta Q_{\rm rev}}{T}=0.
$$

The integral between equilibrium states is therefore path-independent. Define **entropy** by

$$
{\rm d}S=\frac{\delta Q_{\rm rev}}{T},\qquad
\Delta S=\int_A^B\frac{\delta Q_{\rm rev}}{T}.
$$

For an irreversible cycle, Clausius' inequality is

$$
\oint\frac{\delta Q}{T}\leq 0.
$$

Consequently, for a change between equilibrium states,

$$
\Delta S\geq\int_A^B\frac{\delta Q}{T}.
$$

For an isolated system, $\delta Q=0$, so $\Delta S\geq0$: entropy stays constant for a reversible process and increases for an irreversible one.

## 6. Entropy changes and the fundamental relation

### System in contact with a thermal reservoir

For a constant-heat-capacity system changing from $T_S$ to reservoir temperature $T_R$, the system's entropy change is

$$
\Delta S_S=\int_{T_S}^{T_R}\frac{C\,{\rm d}T}{T}
=C\ln\frac{T_R}{T_S}.
$$

The reservoir changes entropy by heat transferred divided by its fixed temperature. Although either part can gain or lose entropy, the combined entropy change of system plus reservoir is non-negative; this illustrates the second law for the universe (system and surroundings together).

With the system's heat capacity $C$ constant and initial temperature $T_S$, the reservoir entropy change is $C(T_S-T_R)/T_R$. Therefore

$$
\Delta S_{\rm total}
=C\left[\frac{T_S}{T_R}-1+\ln\frac{T_R}{T_S}\right]\geq0.
$$

The inequality follows by setting $x=T_S/T_R>0$ and using $x-1-\ln x\geq0$.

### Fundamental thermodynamic relation

For a reversible change with pressure-volume work, the first law and entropy definition give

$$
{\rm d}U=T\,{\rm d}S-P\,{\rm d}V.
$$

Because $U$, $S$, and $V$ are state functions, this is the fundamental relation between equilibrium states, not a claim that every real process is reversible. If $U=U(S,V)$, comparing total differentials identifies

$$
T=\left(\frac{\partial U}{\partial S}\right)_V,\qquad
P=-\left(\frac{\partial U}{\partial V}\right)_S.
$$

### Joule free expansion

An isolated ideal gas expanding into a vacuum does no work and receives no heat, so $\Delta U=0$. Since ideal-gas internal energy depends only on temperature, $\Delta T=0$. Doubling the volume therefore halves the pressure. Entropy is a state function, so calculate its change along a hypothetical reversible isothermal path:

$$
\Delta S
=\int_{V_i}^{V_f}\frac{P}{T}\,{\rm d}V
=Nk_{\rm B}\ln\frac{V_f}{V_i}.
$$

For $V_f=2V_i$, $\Delta S=Nk_{\rm B}\ln 2$. For a microcanonical state of fixed energy, comparing the statistical temperature definition with the thermodynamic one gives Boltzmann's formula:

$$
S=k_{\rm B}\ln\Omega.
$$

## 7. Entropy of mixing and probability

### Mixing two distinguishable ideal gases

Suppose the gases initially occupy fractions $x$ and $1-x$ of a container, at the same pressure and temperature. Their particle numbers are $N_1=xN$ and $N_2=(1-x)N$. Treat each gas as expanding isothermally into the full volume:

$$
\begin{aligned}
\Delta S
&=N_1k_{\rm B}\ln\frac{V}{xV}
+N_2k_{\rm B}\ln\frac{V}{(1-x)V}\\
&=-Nk_{\rm B}\left[x\ln x+(1-x)\ln(1-x)\right].
\end{aligned}
$$

The increase is greatest at $x=1/2$, where $\Delta S=Nk_{\rm B}\ln2$. This mixing entropy applies to distinguishable gases; mixing identical gases does not create this increase.

### Gibbs entropy

If macrostate $i$ has probability $P_i=n_i/N$, where $n_i$ is its count of equally likely microstates, then the total number of microstates is $N=\sum_i n_i$. Separating the entropy associated with the macrostate probabilities from the microstate contribution yields

$$
S=-k_{\rm B}\sum_i P_i\ln P_i.
$$

This is **Gibbs entropy**. For a single macrostate with equal probability over $\Omega$ microstates, it reduces to $S=k_{\rm B}\ln\Omega$.

## 8. Thermodynamic potentials and availability

Starting from ${\rm d}U=T\,{\rm d}S-P\,{\rm d}V$, define potentials by adding or subtracting products of state variables. Their differentials show their natural independent variables:

| Potential | Definition | Differential | Natural variables | Useful derivatives |
|---|---|---|---|---|
| Internal energy | $U$ | ${\rm d}U=T\,{\rm d}S-P\,{\rm d}V$ | $S,V$ | $T=(\partial U/\partial S)_V$; $P=-(\partial U/\partial V)_S$ |
| Enthalpy | $H=U+PV$ | ${\rm d}H=T\,{\rm d}S+V\,{\rm d}P$ | $S,P$ | $T=(\partial H/\partial S)_P$; $V=(\partial H/\partial P)_S$ |
| Helmholtz free energy | $F=U-TS$ | ${\rm d}F=-S\,{\rm d}T-P\,{\rm d}V$ | $T,V$ | $S=-(\partial F/\partial T)_V$; $P=-(\partial F/\partial V)_T$ |
| Gibbs free energy | $G=H-TS=U+PV-TS$ | ${\rm d}G=-S\,{\rm d}T+V\,{\rm d}P$ | $T,P$ | $S=-(\partial G/\partial T)_P$; $V=(\partial G/\partial P)_T$ |

At constant volume, ${\rm d}U=T\,{\rm d}S$; at constant pressure, ${\rm d}H=T\,{\rm d}S$. For reversible changes these give, respectively,

$$
\Delta U=\int C_V\,{\rm d}T,\qquad
\Delta H=\int C_P\,{\rm d}T.
$$

At constant temperature, ${\rm d}F=-P\,{\rm d}V$, so the Helmholtz free-energy change is the negative of the reversible expansion work done by the system. At fixed temperature and pressure, $G$ is especially useful for analysing equilibrium and phase changes.

### Availability criteria

If a system is in thermal contact with surroundings at fixed temperature $T_0$, with the system at that temperature, and total energy is conserved, then

$$
{\rm d}S_{\rm total}=-\frac{{\rm d}F}{T_0}.
$$

The second law therefore implies ${\rm d}F\leq0$: at fixed temperature and volume, Helmholtz free energy cannot increase spontaneously. When the system can also change volume against surroundings at fixed pressure $P_0$,

$$
{\rm d}S_{\rm total}=-\frac{{\rm d}G}{T_0},
$$

so at fixed temperature and pressure, Gibbs free energy cannot increase spontaneously: ${\rm d}G\leq0$.

## 9. Maxwell's relations and heat-capacity difference

### Maxwell's relations

For a state function $f(x,y)$ with exact differential

$$
{\rm d}f=
\left(\frac{\partial f}{\partial x}\right)_y{\rm d}x+
\left(\frac{\partial f}{\partial y}\right)_x{\rm d}y,
$$

the mixed second derivatives are equal. Applying this fact to the thermodynamic potentials gives Maxwell's relations:

$$
\begin{aligned}
\left(\frac{\partial T}{\partial V}\right)_S
&=-\left(\frac{\partial P}{\partial S}\right)_V,\\
\left(\frac{\partial T}{\partial P}\right)_S
&=\left(\frac{\partial V}{\partial S}\right)_P,\\
\left(\frac{\partial S}{\partial V}\right)_T
&=\left(\frac{\partial P}{\partial T}\right)_V,\\
\left(\frac{\partial S}{\partial P}\right)_T
&=-\left(\frac{\partial V}{\partial T}\right)_P.
\end{aligned}
$$

These relations connect derivatives that may be difficult to measure directly to more accessible quantities. For example, the last relation equates the entropy change with pressure at fixed temperature to minus the volume change with temperature at fixed pressure.

### Measurable expression for $C_P-C_V$

Writing entropy as $S(T,V)$ and using the fundamental relation gives

$$
{\rm d}S
=\frac{1}{T}\left(\frac{\partial U}{\partial T}\right)_V{\rm d}T
+\frac{1}{T}\left[P+\left(\frac{\partial U}{\partial V}\right)_T\right]{\rm d}V.
$$

Equality of the mixed derivatives of $S$ then yields

$$
T\left(\frac{\partial P}{\partial T}\right)_V
=P+\left(\frac{\partial U}{\partial V}\right)_T.
$$

Combining this with the heat-capacity difference identity and the cyclic derivative relation leads to

$$
C_P-C_V
=T\left(\frac{\partial P}{\partial T}\right)_V
\left(\frac{\partial V}{\partial T}\right)_P
=\frac{TV\beta_P^2}{\kappa_T},
$$

where the isobaric expansivity and isothermal compressibility are

$$
\beta_P=\frac{1}{V}\left(\frac{\partial V}{\partial T}\right)_P,
\qquad
\kappa_T=-\frac{1}{V}\left(\frac{\partial V}{\partial P}\right)_T.
$$

Thus, the difference between the heat capacities can be determined from measurable expansion and compressibility data.

## Quick reference: core equations

$$
\begin{gathered}
PV=Nk_{\rm B}T,\qquad
\beta=(k_{\rm B}T)^{-1},\qquad
P_i=\frac{e^{-\beta E_i}}{Z},\qquad
Z=\sum_i e^{-\beta E_i},\\
\bar U=-\frac{\partial\ln Z}{\partial\beta},\qquad
{\rm d}U=\delta Q+\delta W,\qquad
\delta W_{\rm rev}=-P\,{\rm d}V,\\
{\rm d}U=T\,{\rm d}S-P\,{\rm d}V,\qquad
{\rm d}S=\frac{\delta Q_{\rm rev}}{T},\qquad
\Delta S_{\rm isolated}\geq0,\\
TV^{\gamma-1}=\mathrm{constant},\qquad
PV^\gamma=\mathrm{constant},\qquad
\eta_{\rm Carnot}=1-\frac{T_L}{T_H},\\
S=k_{\rm B}\ln\Omega,\qquad
S_{\rm Gibbs}=-k_{\rm B}\sum_iP_i\ln P_i,\\
\left(\frac{\partial T}{\partial V}\right)_S=-\left(\frac{\partial P}{\partial S}\right)_V,\qquad
\left(\frac{\partial T}{\partial P}\right)_S=\left(\frac{\partial V}{\partial S}\right)_P,\\
\left(\frac{\partial S}{\partial V}\right)_T=\left(\frac{\partial P}{\partial T}\right)_V,\qquad
\left(\frac{\partial S}{\partial P}\right)_T=-\left(\frac{\partial V}{\partial T}\right)_P,\\
C_P-C_V=\frac{TV\beta_P^2}{\kappa_T}.
\end{gathered}
$$

{% endraw %}
