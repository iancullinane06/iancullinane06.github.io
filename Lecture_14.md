# Quantum Concentration
Now, the partition function for a single particle in an ideal gas is given by
$$
    Z_1 = \int_0 ^\infty {\rm e}^{-\beta E(k)} g(k) {\rm d}{k}
$$
where the energy of a single particle with wave vector $k$ is given by
$$
    E(k) = \frac{\hbar^2 k^2}{2m}
$$
Substituting for $E$ and $g$ now gives
$$
    Z_1 = \int_0 ^\infty {\rm e}^{-\beta \frac{\hbar^2 k^2}{2m}} \frac{V k^2 }{2\pi^2} {\rm d}{k} = \frac{V}{\hbar^3} \left(\frac{mk_{\rm B}T}{2\pi}\right)^{3/2}
$$
which is more easily written as
$$
    Z_1 = V n_{\rm Q}
$$
where $n_{\rm Q}$ is known as the quantum concentration, and is given by 
$$
    n_{\rm Q} = \frac{1}{\hbar^3} \left(\frac{mk_{\rm B}T}{2\pi}\right)^{3/2}
$$
We can now define what is known as the **thermal wavelength** as 
$$
    \lambda_{\rm th} = 1/n_{\rm Q}^{1/3} = \frac{h}{\sqrt{2\pi m k_{\rm B} T}}
$$
which also means that the partition function is given by
$$
    Z_1 = \frac{V}{\lambda_{\rm th}^3}
$$
# Distinguishability
So now that we know what the partition function is for a single particle, we need to derive what it is for the entire system. First, let's say that each particle can have energies
$$
    \epsilon_1 \leq \epsilon_2 \leq \epsilon_3...\leq\epsilon_r \leq ...
$$
with each energy level being discrete (which again is a results from quantum mechanics). Now if the gas has N particles at temperature T and within volume V, then we will say that 

* $n_1$ are in state $\epsilon_1$
* $n_2$ are in state $\epsilon_2$

etc. As such, $n_r$ is our occupation number. The energy must then be
$$
    U = \sum_r n_r \epsilon_r
$$
and
$$
    N = \sum_r n_r
$$
For one particle in this system, the partition function is
$$
    Z_1 = \sum_r {\rm e}^{-\beta \epsilon_r}
$$
When we considered paramagntism, we simply said that
$$
    Z = Z_1^N
$$
However, this is only true because the particles were distinguishable. In this case, we have no way of telling one particle from another, which means this is not true for indistinguishable particles. Let's look at this in detail.

Imagine there are 3 particles:
$$
    Z_3 \propto \sum_q {\rm e}^{-\beta \epsilon_q} \sum_r {\rm e}^{-\beta \epsilon_r} \sum_s {\rm e}^{-\beta \epsilon_s}
$$
(which is just a product of the individual partition functions for each of the particles). Rewriting gives 
$$
    Z_3 \propto \sum_q \sum_r \sum_s {\rm e}^{-\beta (\epsilon_q+\epsilon_r+\epsilon_s)}
$$
Regrouping terms for clarity this becomes
$$
    Z_3 \propto \sum_r {\rm e}^{-3 \beta (\epsilon_r)} + (\sum_r\sum_s)_{r \neq s} {\rm e}^{- \beta (2 \epsilon_r + \epsilon_s)} + (\sum_r\sum_s\sum_q)_{r \neq s \neq q} {\rm e}^{- \beta (\epsilon_r + \epsilon_s+ \epsilon_q)}
$$
where the first term accounts for all 3 particles being in the same state, the second accounts for 2 particles in same state, and the last accounts for all particles in different states. Now we must find the appropriate normalisation coefficients, so that we don't want to count the same state more than once.

* The first term has a coefficient of 1: there is only 1 way to put all three particles in the same state.

![Term_1](Figures/Energy_levels_all_in_one.svg)

* The second term has a coefficient of 1/3: There are three possibilities to have one particle in one state and the other two particles in the same, different state. Note that we always have to have 2 particles in level $\epsilon_r$ because of how we have grouped the terms in the previous equation.

![Term_2](Figures/Energy_levels_two_in_one_one_in_other.svg)

* The third term has a coefficient of 1/3!: particle 1 is in 1 state of any 3 states, particle 2 is then in 1 state of the remaining 2 states, and particle 3 then has to be in the last available state = (3x2x1 = 3!).

![Term_3](Figures/Energy_levels_all_diff.svg)

Thus,
$$
    Z_3 = \sum_r {\rm e}^{-3 \beta (\epsilon_r)} + \frac{1}{3}(\sum_r\sum_s)_{r \neq s} {\rm e}^{- \beta (2 \epsilon_r + \epsilon_s)} + \frac{1}{3!}(\sum_r\sum_s\sum_q)_{r \neq s \neq q} {\rm e}^{- \beta (\epsilon_r + \epsilon_s+ \epsilon_q)}
$$
So to generalise this to $N$ particles:
$$
Z = \sum_r {\rm e}^{-N \beta (\epsilon_r)} + ... + \frac{1}{N!} (\sum_{r_1} ...\sum_{r_n})_{{r_1} \neq ... \neq {r_n}} {\rm e}^{- \beta (\epsilon_{r_1}+...+ \epsilon_{r_n})}
$$
where the $...$ represent terms where we have multiple particles in different states. Now, we make an important assumption: the number of states in a given energy interval is much larger than the number of particles with an energy in that interval. In the classical regime, the probability that any state r is occupied by more than one particle is very low. This means only the last term is significantly different from 0.

The partition function then becomes
$$
\begin{align}
Z &= \frac{1}{N!} \sum_{r_1} ...\sum_{r_n} {\rm e}^{- \beta (\epsilon_{r1}+...+ \epsilon_{rn})}\\
Z &= \frac{1}{N!} \sum_{r_1} {\rm e}^{- \beta \epsilon_{r1}}...\sum_{r_N} {\rm e}^{- \beta \epsilon_{rn}}\\
Z &= \frac{1}{N!} \left(\sum_{r_1} {\rm e}^{- \beta \epsilon_{r1}}\right)^N\\
Z &= \frac{1}{N!} Z_1^N
\end{align}
$$

This is true for the perfect, classical gas. Here, perfect means the particles are weakly/non-interacting (which let's us to write down the energies as $\epsilon_1 \leq \epsilon_2 \leq \epsilon_3...\leq\epsilon_r \leq ...$), and classical means there is a very low probability that there are multiple particles in any state. When is this last condition valid?

There will only be one particle occupying each state if the system is in a regime where the number of states is much larger than the number of particles. For an ideal gas, this means we require that the number of thermally accessible states is larger than the number of particles. As such, we require that the number density of molecules be much less than the quantum concentration:
$$
    n<<n_{\rm Q}
$$
# Functions of state for an Ideal Gas
So now that we know how to calculate the partition function for N indistinguishable particles, let's apply the techniques we have developed to understand an ideal gas. The partition function for N particles in a gas is
$$
    Z_N = \frac{1}{N!} \left( \frac{V}{\lambda_{\rm th}^3}\right)^N
$$
Using the expression for $\lambda_{\rm th}$, we then get that
$$
    Z_N = \frac{1}{N!} V^N \left( \frac{ 2\pi m k_{\rm B} T}{h^2}\right)^{3N/2}
$$
This means that
$$
    \ln{Z_N} = N \ln{V} + \frac{3}{2} N \ln{T} + C
$$
The internal energy is then given by
$$
    U = -\frac{\partial \ln Z_N}{\partial \beta} = k_{\rm B} T^2 \frac{\partial \ln Z_N}{\partial T} = \frac{3}{2}N k_{\rm B}T
$$
The Helmholtz free energy is
$$
    F = -k_{\rm B} T \ln Z_N = -k_{\rm B} T N \ln{V} -k_{\rm B} T \frac{3}{2} N \ln{T} -k_{\rm B} T C
$$
such that if we use (from Lecture 7)
$$
    P = -\left( \frac{\partial F}{\partial V} \right)_T = \frac{N k_{\rm B} T}{V}
$$
which is the equation of state for an ideal gas!

In order to work out the other thermodynamic quantities, we need to be a bit more careful with those constants in earlier equations. Returning to the partition function, we can write it instead as.
$$
    \ln{Z_N} = N \ln{V} - 3 N \ln {\lambda_{\rm th}} - N \ln N + N
$$
after using Stirlings approximation of $\ln{N!} \sim N\ln {N} - N$. This further simplifies to
$$
    \ln{Z_N} = N \ln \left(\frac{V {\rm e} }{N \lambda_{\rm th}^3}\right)
$$
and so the Helmholtz free energy is given by
$$
\begin{align}
    F &= -N k_{\rm B} T \ln \left(\frac{V {\rm e} }{N \lambda_{\rm th}^3}\right)\\
      &= N k_{\rm B} T[ \ln (n \lambda_{\rm th}^3)-1]
\end{align}
$$
from which all other thermodynamic quantities of an ideal gas can be derived.