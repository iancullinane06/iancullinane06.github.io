---
layout: lecture
---
{% raw %}
# Topics
* Stirling's Law for large numbers
* Macroscopic quantities
* The Ideal Gas Law
* Heat
* Heat Capacity
# Introduction
We want to study the physics of a macroscopic object which is comprised of many particles. Say, for example, that we had one mole of a substance. This would mean we have $N_{\rm A} \sim6\times10^{23}$ particles (where this is Avagadro's number) to study. Clearly this is not feasible, as to have a proper description we would need the momenta and positions for each particle.

---
**Working with large numbers**
Fortunately, there are some tips and tricks we can use when dealing with large numbers, which will help throughout our studies. As an example, imagine I have 10 containers, each of which can only hold 1 marble, and I have some marbles. How many distinct ways can we arrange our 10 cups (empty, not empty) if (i) I have 10 marbles or (ii) only 4 marbles? First, let's consider a general example where I have $n$ cups and $r$ marbles.

The first marble can go in any of the $n$ cups, the second can go in any of $n-1$, etc, until the $r^{th}$ marble can go into any of the remaining $n-r+1$ cups. Thus, the number of possible arrangements is
$$
    \Omega = n\times (n-1) \times (n-2) \times ... \times (n-r+1)
$$
which, simplified, is
$$
    \Omega = \frac{n\times (n-1) \times (n-2) \times ... \times 1}{(n-r)\times (n-r-1) \times (n-r-2) \times ... \times 1} = \frac{n!}{(n-r)!}.
$$
Now, in the above, I said first marble, and second marble, as if each marble is special or identifiable. In general, I don't actually care which marble goes in which cup - to account for this, we take the above expression and divide by $r!$ to get
$$
    \Omega = \frac{n!}{(n-r)!r!}.
$$
This expression can be used to work out the questions discussed above. However, this expression can get unwieldy. To see how, let's turn the above problem into a physics problem - simple replace cups with atoms, and marbles with units (or quanta) of energy. So imagine I have $n=6 \times 10^{23}$ atoms. At this stage, it's a bit easier to look at the natural log of $\Omega$, which is 
$$
    \ln(\Omega) = \ln(n!) - \ln((n-r)!) - \ln(r!)
$$
This would mean our expression for $\ln(\Omega)$ would involve $\ln(6 \times 10^{23}!)$ - try running this on a calculator. To overcome this issue, it's useful to use **Stirling's formula**
$$
    \ln n! = n\ln(n) - n.
$$
---
Instead of doing this, we are going to study **macroscopic** laws and properties which are ultimately governed by **microscopic** properties, but which emerge from averaging over these microscopic properties.

Thus, there are two approaches to studying macroscopic physics. The first is the study of classical thermodynamics (Carnot, Clausius, Kelvin, Joule). This approach requires experiments on macroscopic systems, and avoids any description of atomic physics. The laws are thus phenomenological. The second approach is that of statistical physics, which starts out from an atomic description of matter and tries to derive the laws of macroscopic bodies from these atomic properties (Maxwell, Boltzmann, Gibbs). There is also the kinetic theory of gases which attempts to understand thermodynamics by considering velocity distributions of particles. We will touch on this in places, but a more rigorous treatment will come in PY3104.
# Macroscopic quantities & the Thermodynamic limit
So what exactly are macroscopic quantities, and how do they arise? Consider the diagram below, in which we have a gas in a sealed container and a movable piston.
![Sealed_Cotainer](Sealed_Container.svg)

When that piston at rest, the force exerted on the piston balances the pressure exerted on the piston by the gas, and are related through
$$
	P=F/A
$$
where $A$ is the surface area of the piston exposed to the gas. The pressure arises due to the elastic collisions of the particles within the gas with the walls of the container. Thus, the pressure is not really time independent - at any given time, there may be more or less particles hitting the wall then at other times due to the random movements of the particles in the gas - this is Brownian motion. As such, the piston is not perfectly in place - it is constantly shifting around by small amounts as the number of particles hitting it varies. 

If we were studying a small number of particles, or the system we were studying was very small, we would be sensitive to these variations. However, when dealing with a large number of particles, or with macroscopic objects then the variation in the number of particles hitting the piston is so small, we cannot observe the changes, meaning the pressure appears to be constant to us. This is what we'll refer to as the thermodynamic limit.

This is not always the case - for very small macroscopic bodies or using very sensitive instruments, the effects of Brownian motion can be witnessed, which thus limit the accuracy of any measurements.

Our goal is then to describe macroscopic systems using well defined, measurable quantities such as the mass, pressure, volume, or temperature of an object. These quantities can be split into two different categories:
- **Extensive variables** (such as volume, total energy), which scale with the size of the system.
- **Intensive variables** (such as temperature, pressure), which do not scale with the size of the system.
As an example, consider a volume $V$ of a gas at temperature $T$ and pressure $P$. If you now only study one half of the container, the volume of gas you are studying has halved, but the temperature and pressure of the gas are the same.
# The Ideal Gas
For the ideal gas, we will follow the developments of classical thermodynamics. That is, we will rely on phenomenological laws observed in experiments, and combine them together. The three relevant observed laws are 
**Boyle's Law**:
$$
    P \propto \frac{1}{V}.
$$
**Charles' Law:**
$$
    V \propto T.
$$
**Gay-Lussac Law**:
$$
    P \propto T.
$$
Combining these together, we get
$$
    P V \propto T.
$$
The constants of proportionality turn out to be $N k_{\rm B}$, where $N$ is the number of particles in the gas and $k_{\rm B}=1.3807\times10^{-23}$ J K$^{-1}$ is Boltzmann's constant. This gives the ideal gas equation of
$$
    P V = N k_{\rm B} T
$$
Alternatively, this can be written as 
$$
    P V = n R T
$$
where $n$ is the number of moles and $R=8.31$ J /(mol K), and is related to $N$ by $N=n \times N_{\rm A}$ where is $N_{\rm A}$ is Avagadro's number.

So why is it ideal? First, we have assumed that there are no inter-particle forces occurring, and we also assume that all particles are point like and have zero-size. As we'll see later, this also means that the total internal energy of an ideal gas is simply given by
$$
	U = \frac{3}{2} N k_{\rm B} T
$$
# Heat
As we begin our studies, the next concept we need to deal with is heat. So, what does it mean to say something is hot? If I'm standing beside a radiator, I can feel the heat coming from it. If I'm standing in a fridge, I can feel heat being drawn away from me. So, let's use that as our starting definition: *Heat is energy in transit.*

So is there a natural direction for this flow of energy? If we put a hot object in contact with a cold object, there is a natural flow of energy from the hot object to the cold object which increases the temperature of the cold object. 

There are instances when the direction can be reversed (e.g. fridges/freezers) where the hot object decreases to match the temperature of the cold object, but the key difference here is that we need to put additional energy into the system to cause this.

It's also important to note the "in transit" part of the definition, but we'll return to this later on in the course.
# Heat Capacity
Next, let's ask the question "how much heat needs to be supplied to an object to raise its temperature by a small amount $dT$?" The answer is
$$
    dQ=CdT
$$
where $C$ is the heat capacity of an object. $C$ can come in a few flavours (see Section 2.2 of Blundell), but the most common one is the specific heat capacity, which is the heat capacity per unit mass ($c=M/C$) (given a mass $M$ of an object which has some measured heat capacity $C$).

The equation above is only somewhat useful to us. It simply asks the question "how much heat should be added to raise the temperature of a gas?". In practice there are two ways to do this:

1. Place the gas in a sealed box and add heat. Since this is at fixed volume, the pressure increases.
2. Place our gas in a chamber with a piston (like in the diagram above). As we add heat in now, the piston will rise (work is being done against the atmosphere) - hence this process is being done at constant pressure, but the volume will increase.

Both ways apply different constraints to the system, so the equation above must be modified to be either:
$$
\begin{align}
    C_{V} & = \left( \frac {\partial Q}{\partial T} \right)_V,\\
    C_{P} & = \left( \frac {\partial Q}{\partial T} \right)_P.\\
\end{align}
$$
We'll come back to which one we think should be larger later.
{% endraw %}
