# The Chemical Potential and Phase transitions
The next part of this course will focus on what happens if the particle number within a system is no longer kept constant, and what happens when systems of two or more phases are in equilibrium. Here, a phase is a homogeneous part of a system bounded by surfaces, across which the properties of the system change discontinuously (say for example a container which has both water which is boiling at 100 degrees, above which we have water vapour also at 100 degrees). We will restrict ourselves to a single component (that is, we won't consider a mixture of water and acid) as this would be a complex task.

In this setup, we will be able to transfer matter between the different phases. For different phases to be in equilibrium, certain conditions must hold such that no matter transfer occurs.

### Equilibrium conditions
Imagine we have a one component system, and we want to determine the conditions for which 2 phases can exist in equilibrium. First, let's assume the system is totally isolated, such that
$$
\begin{align}
    U_1+U_2 &= U\\
    V_1+V_2 &= V\\
    N_1+N_2 &= N\\
\end{align}
$$
The entropy of the system is given by
$$
    S(U,V,N,U_1,V_1,N_1) = S_1(U_1,V_1,N_1)+S_2(U_2,V_2,N_2).
$$
To be in equilibrium, the entropy must be maximised, giving
$$
    {\rm d} S = {\rm d} S_1 + {\rm d} S_2
$$
Now,
$$
    {\rm d} S_1 = \left( \frac{\partial S_1}{\partial U_1}\right)_{V_1,N_1} {\rm d} U_1 +\left( \frac{\partial S_1}{\partial V_1}\right)_{U_1,N_1} {\rm d} V_1 +\left( \frac{\partial S_1}{\partial N_1}\right)_{V_1,U_1} {\rm d} N_1 
$$
and
$$
    {\rm d} S_2 = \left( \frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2} {\rm d} U_2 +\left( \frac{\partial S_2}{\partial V_2}\right)_{U_2,N_2} {\rm d} V_2 +\left( \frac{\partial S_2}{\partial N_2}\right)_{V_2,U_2} {\rm d} N_2
$$
Using
$$
    U_2 = U - U_1 \to {\rm d} U_2 = - {\rm d} U_1
$$
gives
$$
    {\rm d} S_2 = -\left( \frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2} {\rm d} U_1 -\left( \frac{\partial S_2}{\partial V_2}\right)_{U_2,N_2} {\rm d} V_1 -\left( \frac{\partial S_2}{\partial N_2}\right)_{V_2,U_2} {\rm d} N_1
$$
which finally gives
$$
\begin{align}
    {\rm d} S &= \left[\left( \frac{\partial S_1}{\partial U_1}\right)_{V_1,N_1} - \left( \frac{\partial S_2}{\partial U_2}\right)_{V_2,N_2}\right]{\rm d} U_1 \\
    &+ \left[\left( \frac{\partial S_1}{\partial V_1}\right)_{U_1,N_1} - \left( \frac{\partial S_2}{\partial V_2}\right)_{U_2,N_2}\right]{\rm d} V_1\\ 
    &+\left[\left( \frac{\partial S_1}{\partial N_1}\right)_{V_1,U_1} - \left( \frac{\partial S_2}{\partial N_2}\right)_{V_2,U_2}\right]{\rm d} N_1 =0
\end{align}
$$
Since $U_1$, $V_1$, and $N_1$ are all independent, each of these terms must go to 0 for equilibrium to be achieved. The first two terms equate to saying that both phases must be at the same temperature and pressure (refer to the definition of entropy in Lecture 5 if this isn't clear). The last term implies that
$$
    \left( \frac{\partial S_1}{\partial N_1}\right)_{V_1,U_1} = \left( \frac{\partial S_2}{\partial N_2}\right)_{V_2,U_2}
$$
is the condition for particle equilibrium. If we now define the chemical potential as
$$
    \mu_i = -T_i \left( \frac{\partial S_i}{\partial N_i}\right)_{V_i,U_i}
$$
then the condition becomes
$$
    \mu_1 = \mu_2.
$$
So how are we to interpret the chemical potential? Consider a system that is not in equilibrium. The phase with a larger $\left( \frac{\partial S_i}{\partial N_i}\right)$ will tend to gain particles (as this maximises entropy) - but because $\mu$ is proportional to the negative of this quantity, this means that this phase has a smaller chemical potential - so particles flow from a phase of higher $\mu$ to one with a lower $\mu$.

## Fundamental Thermodynamic Relation
So what does this do to the fundamental thermodynamic relation? Consider again
$$
    {\rm d} S = \left( \frac{\partial S}{\partial U}\right)_{V,N} {\rm d} U +\left( \frac{\partial S}{\partial V}\right)_{U,N} {\rm d} V +\left( \frac{\partial S}{\partial N}\right)_{V,U} {\rm d} N.
$$
Using our known substitutions, we get 
$$
    {\rm d} S = \frac{1}{T} {\rm d} U +\frac{1}{T} P {\rm d} V - \frac{1}{T} \mu {\rm d} N.
$$
Tidying up gives
$$
    {\rm d} U = T {\rm d} S - P {\rm d} V + \mu {\rm d} N.
$$
What this is telling us is that if we keep the entropy and volume of a system constant, then adding a single particle increases the internal energy by $\mu$.
From this, we can express $\mu$ in terms of $U$ as 
$$
    \mu = \left( \frac{ \partial U }{ \partial N} \right)_{S,V} 
$$
which is not altogether useful, as both $S$ and $V$ are hard to keep constant. Modifying either the Helmholtz free energy or the Gibbs free energy to account for this change to the fundamental thermodynamic relation thus gives
$$
\begin{align}
    {\rm d} F &= - P {\rm d} V - S {\rm d} T + \mu {\rm d} N. \\
    {\rm d} G &= V {\rm d} P - S {\rm d} T + \mu {\rm d} N. \\
\end{align}
$$
which leads to
$$
\begin{align}
    \mu &= \left( \frac{ \partial F }{ \partial N} \right)_{V,T}\\ 
    \mu &= \left( \frac{ \partial G }{ \partial N} \right)_{P,T} 
\end{align}
$$
In the case we are considering of single component system (remember, this is us saying that we only have one type of particle in the system, like a system containing just water molecules), then the Gibbs free energy depends on N, the particle number, such that
$$
    G(T,P,N) = N\; G(T,P,1) = N g(T,P)
$$
where
$$
    g(T,P) = \frac{G(T,P,N)}{N}
$$
is the Gibbs free energy per particle. From above, this then means that we can write the chemical potential for a single component, homogeneous system as
$$
    \mu = g(T,P).
$$
Finally, this means that for a two phase, single component system, where each phase is homogeneous, we require that
$$
    g_1(T,P) = g_2(T,P)
$$
This condition defines a curve in the $(P,T)$ plane. For any combination of temperature and pressure which lie on the curve, the phases are in equilibrium, while for any points that lie off of the curve, they are not.

A simple example of this is shown below. In this, 1 and 2 define the regions in which $g_1 < g_2$ and $g_2 < g_1$ respectively.

![TPCurve](Figures/Gibbs_Free_Energy.svg)

If $N_1$ and $N_2$ are the number of molecules in phases 1 and 2 respectively, then the Gibbs free energy of the system is
$$
    G = N_1 g_1(T,P)+N_2 g_2(T,P)
$$
For a system at a pressure and temperature given by point A in the figure above, $g_1<g_2$, and so the Gibbs free energy is minimised if all of the substance is in phase 1. Similar logic applies to point B, where $G$ is a minimum if all of the substance is in phase 2. Thus, the curve divides the $(P, T)$ plane into regions where one or other phase represents the stable equilibrium state.

It is only along the curve that the phases can coexist in equilibrium - as such, this curve is called a **phase equilibrium curve**. This curve has a different name depending on which 2 phases are being discussed:

* If the two phases are liquid and vapour, it's a vapour pressure curve.
* If the two phases are liquid and solid, it's a melting curve.
* If the two phases are vapour and solid, it's a sublimation curve.

Let's now briefly consider what happens for a 3 phase system. The equilibrium condition for such a system is given by
$$
    g_1(T,P) = g_2(T,P) = g_3(T,P)
$$
Rather than just describing a curve, this condition describes the intersection of two curves, with the intersection point known as the triple point. A simple curve is plotted below as an example, but I recommend looking up the curve for water to get an idea of the full complexity of such a graph. The triple point of water occurs at a temperature and pressure of (611.567 Pa, 273.16 K).

![TPCurve](Figures/Triple_Phase.svg)