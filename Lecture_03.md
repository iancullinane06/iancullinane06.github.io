---
layout: lecture
---
{% raw %}
# Topics
* The Boltzmann Distribution
* Partition Function and Energy
* The First Law of Thermodynamics
# The Boltzmann Distribution
Ok, now let's consider the example of two systems put into thermal contact as discussed in lecture 2. However, we're going to change one of the systems such that it acts as a reservoir (or heat bath). We then place the other system into thermal contact with the reservoir. The reservoir has such an enormous amount of energy compared to the system that any change in its temperature as it heats the smaller system is completely negligible. This is the canonical ensemble discussed previously.

![Reservoir](Figures/Reservoir.svg)

Now, we're going to assume that for each energy of the system, there is only a single allowed microstate. As such, $\Omega(\epsilon)=1$.

So, the probability that the system has energy $\epsilon$ is proportional to the number of microstates of the reservoir times the number of microstates of the system:
$$
    P(\epsilon) \propto \Omega(E-\epsilon)\Omega(\epsilon)=\Omega(E-\epsilon)
$$
Now using
$$
    \frac{1}{k_{\rm B}T} = \frac{{\rm d ln} \Omega}{{\rm d} E}
$$
and given that $\epsilon \ll E$, we can Taylor expand ${\rm ln} \Omega$ around 0 to give
$$
    {\rm ln} \Omega(E-\epsilon) = {\rm ln} \Omega(E) - \frac{{\rm d ln} \Omega(E)}{{\rm d} E}\epsilon + ...
$$
which gives
$$
    {\rm ln} \Omega(E-\epsilon) = {\rm ln} \Omega(E) - \frac{\epsilon}{k_{\rm B} T} + ...
$$
This then gives
$$
    \Omega(E-\epsilon) = \Omega(E){\rm e}^{-\frac{\epsilon}{k_{\rm B} T}}
$$
Finally, this gives
$$
    P(\epsilon) \propto {\rm e}^{-\frac{\epsilon}{k_{\rm B} T}}
$$
This probability tells us how the system reacts to being placed in the bath. There is a high probability that the system will achieve an energy $\epsilon$ which is less than ${k_{\rm B} T}$, but it quickly decays above this energy, meaning we are unlikely to observe the system to have an energy much higher than the reservoir. Now, to normalise the probability, we must divide by all possible microstates:
$$
    P(E_r) = \frac{{\rm e}^{-E_r/k_{\rm B} T}}{\sum_i {\rm e}^{-E_i/k_{\rm B} T}}
$$
This is known as the **Boltzmann distribution**. It is also written as 
$$
    P(E_r) = \frac{1}{Z}{\rm e}^{-\beta E_r}
$$
where
$$
    Z = \sum_i {\rm e}^{-\beta E_i}
$$
is  called the **partition function**.
In deriving this, we have assumed that every energy has a single microstate which describes it.

Finally, it's useful to note that $1/k_{\rm B} T$ comes up a lot in statistical mechanics. As such, it's often simply written as
$$
    \beta \equiv \frac{1}{k_{\rm B} T}
$$
to save time.

## The partition function and Energy
So now assume we have some system with internal energy $U$. What is the average energy of the system? To calculate this, we need to take the energy of each state and multiply it by the probability that each state will occur. This gives
$$
    \bar{U} = \sum_{i} P(E_i) E_i = \frac{1}{Z} \sum_{i} E_i {\rm e}^{(-\beta E_i)}.
$$
However,
$$
    \sum_{i} E_i {\rm e}^{(-\beta E_i)} = -\frac{{\rm d} Z}{{\rm d} \beta}
$$
so we get
$$
    \bar{U} = - \frac{1}{Z} \frac{{\rm d} Z}{{\rm d} \beta} = -\frac{{\rm d} \ln Z}{{\rm d} \beta}
$$
## Some final definitions
Right, we need a few final terms before we can move on.

**Thermal equilibrium** : A system is in thermal equilibrium when its macroscopic properties have ceased to change with time.

**Functions of state** : Any physical quantity that has a well defined value for each equilibrium state of a system. For example: Pressure, temperature, volume. In mathematical terms, these are exact differentials.

Work put into a system and total heat put into or out of a system are thus **not** functions of state. They are inexact differentials.

As a nice example, consider warming up your hands. If you change the temperature of your hands, they achieve an equilibrium state with a given temperature, independent of how you managed to get them to this temperature. That is, you could rub them together (performing work on them) or sinking them into a tub of hot water (adding heat to them).

In this course, we will endeavour to write exact differentials as ${\rm d} T$, and inexact differentials as đQ. However, some times latex doesn't work with this symbol, so always check one of the course books to be sure whether an equation involves an exact or an inexact differential.

**Equation of state**: An equation of state links together functions of state. For example, $P V = N k_{\rm B} T$ is the equation of state of an Ideal Gas.
{% endraw %}
