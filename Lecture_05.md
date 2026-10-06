---
layout: lecture
---
{% raw %}
# Topics
* The second law of thermoydnamics.
* Heat Engines.
* Clausius' Theorem.
* Entropy.
* Irreversibility.
## Isotherms & Adiabats
So now we have two scenarios for working an ideal gas. It can undergo an adiabatic process, in which case $P V^\gamma = const$, or it can undergo an isothermal expansion, in which case $PV=const$. We'll cover what these processes can be used for later, but the below can be treated as a prelude, as it plots pressure versus volume for both processes for two different initial conditions. In the last lecture, we defined 
$$
\gamma=\frac{C_{\rm P}}{C_{\rm V}}=\frac{5}{3}
$$
where that last value is true for an ideal gas.

![Adiabats_isotherms](Figures/Adiabats_vs_isotherms.jpg)
## Applications
The idea of an isothermal process can be used as a rough model for the atmosphere close to the Earth's surface. By treating the air as an ideal gas and assuming the temperature is constant, an expression relating the number density of particles and the altitude above the Earth's surface can be arrived it. This is shown below alongside a more complex model, and as can be seen, the isothermal model breaks down pretty quickly.

We can also use an adiabatic model by assuming that as pockets of air rise, they do not exchange energy with neighbouring colder pockets, but instead expand and cool down in order to reach thermodynamic equilibrium. This leads to better agreement with the more complex model close to the Earth's surface, but also diverges when this approximation breaks down.

![Model_atmo](Figures/Model_Atmosphere.png)
## Heat engines & and the second law
At the end of the last lecture, we stated the second law of thermodynamics in 2 different ways:
****
1. No process is possible whose sole result is the transfer of heat from a colder to a hotter body. (Clausius)
2. No process is possible whose sole result is the complete conversion of heat into work. (Kelvin)
****
So, assuming that these statements are true, let's consider the second statement. This says that no process can completely convert heat into work, meaning there must be a limit to the efficiency of converting heat into work. As such, we want to figure what this efficiency is. First, we are going to define efficiency as:
$$
    \eta = \frac{W}{Q_{\rm H}}
$$
That is, we will supply a system with heat $Q_{\rm H}$, and the system will then do some work $W$. To figure out what this efficiency is and how the various terms in that equation work, we will consider the Carnot engine.
## The Carnot Engine
Consider the following engine.

![Carnot_Engine](Figures/Carnot_Engine.svg)

It is able to draw heat $Q_{\rm H}$ from a reservoir which is at a temperature $T_H$. It then dumps heat $Q_{\rm L}$ to reservoir which is at a temperature $T_L$ while doing some work.

We are going to let the engine perform the following steps: an isothermal expansion, followed by an adiabatic expansion, followed by an isothermal compression, and then another adiabatic compression. These 4 processes will trace out a path shown below in the P-V diagram, where the process follows a series of isotherms and adiabats.
![Carnot_cycle](Figures/Carnot_Cycle.jpg)
Because the processes B-C and D-A are adiabatic, and A-B and C-D are isothermal, we can make the following statement. Heat $Q_{\rm H}$ enters the engine during process A-B, and heat $Q_{\rm L}$ leaves during C-D, and no heat is lost duing B-C and D-A. Finally, the process is cyclic, meaning there is no change in the internal energy of our engine. As such, the work done by the engine is given by
$$
W = Q_{\rm H}-Q_{\rm L}
$$
In order to understand this expression, we need to figure out what $Q_{\rm H}$ and $Q_{\rm L}$ might be. As such, let's consider an ideal gas and follow it during each of the 4 stages.

1. A-B, Isothermal expansion. $Q_{\rm H} = R T_{\rm H} \ln \frac{V_B}{V_A}$.
2. B-C, Adiabatic expansion. $\frac{T_{\rm H}}{T_{\rm L}} = \left(\frac{V_{\rm C}}{V_{\rm B}}\right)^{\gamma - 1}$.
3. C-D, Isothermal compression. $Q_{\rm L} = -R T_{\rm L} \ln \frac{V_D}{V_C}$.
4. B-C, Adiabatic compression. $\frac{T_{\rm L}}{T_{\rm H}} = \left(\frac{V_{\rm A}}{V_{\rm D}}\right)^{\gamma - 1}$.

Combining all of these together thus gives:
$$
    \frac{Q_H}{Q_L} = \frac{T_H}{T_L}
$$
It's also important to note that all of these processes are being done reversibly, so we are free to change the directions of the arrows in our schematic (we'll come across this later in this lecture).

We now consider the efficiency of our engine. By efficiency, we mean the ratio of "what we want to achieve" versus "what we have to do to achieve it". For an engine, this means we want to get work out, and we we need to supply heat in order to this, giving:
$$
\eta = \frac{W}{Q_{\rm H}}
$$
For the Carnot engine with an ideal gas, we can thus express the efficiency in terms of the temperatures of the isotherms by:
$$
\begin{align}
\eta &= \frac{Q_{\rm H}-Q_{\rm L}}{Q_{\rm H}}=1-\frac{Q_{\rm L}}{Q_{\rm H}}\\
\eta &= 1-\frac{T_{\rm L}}{T_{\rm H}}
\end{align}
$$
It turns out that this expression for efficiency is the highest efficiency any engine can achieve for a given $T_{\rm H}$ and $T_{\rm L}$, assuming Clausius's statement of the second law.
## The equivalence of Clausius's and Kelvin's statement of the 2nd law
We now want to solve 2 statements.
1. If a system violates Kelvin's statement, it also violates Clausius' statement.
2. If a system violates Clausius' statement, it also violates Kelvin's statement.

To answer these questions, we're going to take the Carnot engine and hook up some special equipment, and see what happens.

### 1. If a system violates Kelvin's statement, it also violates Clausius' statement.
Let's assume we have the following system. This system violates Kelvin's statement, as the Kelvin violator is converting heat solely into work.

![Kelvin Violator](Figures/Kelvin_Violator.svg)

In this case, we would have $Q_{\rm  H}' = W$ from the Kelvin violator, and $Q_{\rm H} = Q_{\rm L} + W$ from the Carnot engine. The heat dumped into the reservoir at $T_{rm H}$ is then $Q_{H}-Q_{H}'=Q_{L}$. Thus, the net process of the entire system is a flow of energy of $Q_{\rm L}$ from the cold reservoir to the hot reservoir, which violates Clausius' statement.

### 2. If a system violates Clausius' statement, it also violates Kelvin's statement.
Let's assume we have the following system. This system violates Clausius' statement, as the Clausius violator is transferring heat from a colder body to a hotter body.

![Clausius Violator](Figures/Clausius_Violator.svg)

The first law implies that for the Carnot engine, $Q_{\rm H}-Q_{\rm L} = W$. The sole effect of the whole system is thus to convert the heat $Q_{\rm H}-Q_{\rm L}$ into work. This violates Kelvin's law!
## Refrigerators
Let's now consider a engine running in the reverse direction to that discussed above.
![Clausius Violator](Figures/Reverse_Carnot_Engine.svg)

In this case, work is put into the engine, and heat flows from the cold temperature reservoir to hot reservoir. The relevant efficiency in this case is
$$
    \eta = \frac{Q_{\rm L}}{W}
$$
as we want to know what flow of heat we can achieve for a given amount of work. Using the above arguments that we used for the Carnot engine, it's then easy to show that
$$
    \eta = \frac{T_{\rm L}}{T_{\rm H}-T_{\rm L}}
$$
which can be greater than 100%. So, when we design an engine to do work, the efficiency will be less than 1. However, when we design an engine to exchange heat between bodies, the efficiency will be greater than 1.
## Clausius' Theorem
Consider one cycle of a Carnot engine. Over this cycle, $Q_{\rm H}$ enters the engine and $Q_{\rm L}$ leaves the engine. We know from earlier discussions that
$$
    \frac{Q_{\rm H}}{Q_{\rm L}} = \frac{T_{\rm H}}{T_{\rm L}}
$$
We will now define $\Delta Q_{\rm rev}$ as the heat entering the system at each point of the process, such that
$$
    \sum \frac{\Delta Q_{\rm rev}}{T} = \frac{Q_{\rm H}}{T_{\rm H}} + \left(-\frac{Q_{\rm L}}{T_{\rm L}}\right) = 0
$$

Rather than just summing up all the contributions, we could instead integrate, in which case we get
$$
    \oint \frac{{\rm d} Q_{\rm rev}}{T} = 0
$$

While this is a useful result, we must now remember that the Carnot engine does everything reversibly. So now we want to consider what this inequality looks like for real world systems.

Consider now the following setup. We have two engines which are connected to two reservoirs, one at temperature $T_{\rm H}$ and one at $T_{\rm L}$. One engine is a Carnot engine, and so everything is performed reversibly, while the other one is not.

![Clausius_Inequality](Figures/Clausius_Inequality.svg)

Now let's consider the efficiencies of both engines. For the Carnot engine, I'll use subscript R for reversible, and for the other engine I'll use I for irreversible.
$$
\begin{align}
\eta_R &= 1-\frac{Q_{L,R}}{Q_{H,R}}\\
\eta_I &= 1-\frac{Q_{L,I}}{Q_{H,I}}
\end{align}
$$
So we stated earlier that a Carnot engine is the most efficient type of engine we can have. As such
$$
    \eta_{R} \geq \eta_{I}
$$
These leads to
$$
\begin{align}
1-\frac{Q_{L,R}}{Q_{H,R}} &\geq 1-\frac{Q_{L,I}}{Q_{H,I}}\\
\frac{Q_{L,R}}{Q_{H,R}} &\leq \frac{Q_{L,I}}{Q_{H,I}}\\
\end{align}
$$
Now recalling that for a Carnot engine we have
$$
    \frac{Q_H}{Q_L} = \frac{T_H}{T_L}
$$
we then get
$$
\begin{align}
\frac{T_{L}}{T_{H}} &\leq \frac{Q_{L,I}}{Q_{H,I}}\\
\frac{Q_{H,I}}{T_{H}} - \frac{Q_{L,I}}{T_{L}} &\leq 0\\
\end{align}
$$
which is the same as 
$$
    \oint \frac{{\rm d} Q}{T} \leq 0
$$
There are many other ways of arriving at this inequality, which I recommend you look up. The identity will become important in the next lecture.

Clausius' theorem states that
$$
    \oint \frac{{\rm d} Q_{\rm rev}}{T} = 0
$$
This means that the quantity
$$
    \int ^A_B \frac{{\rm d} Q_{\rm rev}}{T}
$$
is a function of state (that is, it has an exact value for a given equilibrium state of the system). Another way of saying this is that this quantity is an exact differential, and is path independant. We are going to now define this function of state as the **entropy** S of the system such that
$$
    {\rm d} S = \frac{{\rm d} Q_{\rm rev}}{T}
$$
and 
$$
    S(B)-S(A) = \int ^A_B \frac{{\rm d} Q_{\rm rev}}{T}
$$
Recalling that for an adiabatic process, ${\rm d} Q_{\rm rev} = 0$, this would also mean that there is no change in entropy during this process. As such, an adiabatic process can also be called an **isentropic** process.

## Irreversibility
S is defined in relation to a reversible change of heat. Taking Clausius' theorem for reversible processes again, we have that
$$
    \oint \frac{{\rm d} Q_{\rm rev}}{T} = 0
$$
We are now going to consider a cycle which starts with some irreversible process, followed by a reversible process. Such a process is given in the P-V diagram below.

![Irreversible](Figures/Entropy_Irreversible_Process.svg)

The Clausius' inequality tell us that 
$$
    \oint \frac{{\rm d} Q}{T} \leq 0
$$
We can then split this integral into two segments
$$
    \int ^B_A \frac{{\rm d} Q}{T} + \int ^A_B \frac{{\rm d} Q_{\rm rev}}{T} \leq 0
$$
which simplifies to 
$$
    \int ^B_A \frac{{\rm d} Q}{T} \leq \int ^B_A \frac{{\rm d} Q_{\rm rev}}{T}
$$
This is true no matter how close the curves joining A to B and B to A get. As such, we can also write the change in entropy of a system to be
$$
    {\rm d} S = \frac{{\rm d} Q_{\rm rev}}{T} \geq \frac{{\rm d} Q}{T} 
$$
Now consider a thermally isolated system. This means that ${\rm d} Q$ is always 0 for this system. Then, for any process within the system, the inequality becomes
$$
    {\rm d} S \geq 0.
$$
It's worth considering exactly what this condition is now saying. For any system that is thermally isolated, the entropy will stay the same for reversible processes, or will increase for irreversible processes. This is another way of stating the second law of thermodynamics: **"The entropy of an isolated system tends to a maximum"**. 

This has some very fundamental consequences. For example, if the Universe is a isolated system, then it means that entropy of the Universe can only increase.
{% endraw %}
