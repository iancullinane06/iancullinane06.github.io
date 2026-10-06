---
layout: lecture
---
At the end of the last lecture, we derive Curie's, which states that magnetic susceptability of a paramagnet is inversely proportional to its temperature, or
$$
    \chi \propto \frac{1}{T}
$$
then this means that 
$$
    \left( \frac{\partial \chi}{\partial T} \right)_B < 0
$$
We'll need this in a second.

So, what does this let us accomplish? Well, let's consider the Helmholtz Free Energy again. It leads to the equivalent Maxwell relation of
$$
    \left(\frac{\partial S}{\partial B}\right)_T = \left(\frac{\partial m}{\partial T}\right)_B \approx \frac{V B}{\mu_0} \left( \frac{\partial \chi}{\partial T} \right)_B
$$
where that last simplification comes from taking 
$$
\chi \approx \frac{\mu_0 M}{B}
$$
and replacing $M$ with $m/V$, and carrying out the derivative (that is, it only works for paramagnets).

Thus, the change in heat during an isothermal change in the B field is
$$
\begin{align}
\Delta Q &= T \left( \frac{\partial S}{\partial B} \right)_T\\
\Delta Q &= \frac{T V B}{\mu_0} \left( \frac{\partial \chi}{\partial T} \right)_B\\ 
\Delta Q&<0\\
\end{align}
$$
This means that heat is emitted from the material during this process.

We can use our usual trick of dealing with differentials
$$
    \left(\frac{\partial T}{\partial B}\right)_S \left(\frac{\partial B}{\partial S}\right)_T \left(\frac{\partial S}{\partial T}\right)_B = -1
$$
to obtain an expression for change in temperature due to an adiabatic change in the B field
$$
    \left(\frac{\partial T}{\partial B}\right)_S = - \left(\frac{\partial S}{\partial B}\right)_T \left(\frac{\partial T}{\partial S}\right)_B.
$$
If we define the heat capacity at constant magnetic field to be $C_{B} = T \left(\frac{\partial S}{\partial T}\right)_B$ then we get
$$
    \left(\frac{\partial T}{\partial B}\right)_S = - \frac{T V B}{\mu_0 C_B} \left(\frac{\partial \chi}{\partial T}\right)_B
$$ 
where has to be $>0$. This means that we can cool down the paramagnet by adiabatically reducing the magnetic field on the sample. This is an incredibly useful result, as experimentally it allows for cooling of systems to millikelin (for electronic systems) and microkelvin (nuclear systems).

Such a cooling proceeds in the following manner.

1. A paramagnetic system is coupled to a heat bath, which is typically liquid helium at 4.2 K.
2. Isothermal magnetisation of the sample proceeds. Since in this process $\Delta Q < 0$ for positive increases in the B field, the paramagnet transfers heat into the liquid helium heat bath.
3. The system is decouple from the heat bath.
4. The system is adiabatically demagntised. Since $\left(\frac{\partial T}{\partial B}\right)_S$ is positive, this means reducing the B field reduces the temperature. This leads to a significant cooling of the system.
---
Now we come to another section of the course. Our goal is to use our understanding of statistical physics to derive the ideal gas equation. We need some background tools first.
# Density of States
In order to derive the equation of state of an ideal gas from statistical mechanics, we require a few results from quantum mechanics, and a more general discussion on the partition function. The first thing we need to do is to figure out what the allowed states are for an ideal gas, as we need this for the partition function.

Imagine a cube with dimensions $L\times L \times L$ and a volume of $V$, filled with a gas. Each molecule in the gas will have a mass $m$ and momentum ${\bf p}$. For convenience, we are going to use the parameter ${\bf k}=\frac{{\bf p}}{\hbar}$, which is also known as the wave vector.

The result we require from quantum mechanics is that the solution to the Schrodinger equation for a particle which is trapped in a box is
$$
    \psi (x,y,z) = \left(\frac{2}{L}\right)^{3/2} \sin (k_x x)\sin (k_y y)\sin (k_z z)
$$

The leading factor here is a normalising factor such that $\int |\psi|^2 = 1$. Now we are going to impose that the particles must be inside of the box. This means that the wave equation must go to 0 at the boundaries of our cube ($x=0$,$x=L$,$y=0$,$y=L$,$z=0$,$z=L$). This occurs when
$$
    k_x = \frac{n_x \pi}{L}, \: \: \: k_y = \frac{n_y \pi}{L}, \: \: \: k_z = \frac{n_z \pi}{L}
$$
where $n_x,n_y, n_z$ are all positive integers. This means that every state that a particle can exist in within the box can be specified by a triplet of integers. As such, we can represent these states in three-dimensional k-space. The distance between a given point and a point in any other direction is thus $\pi / L$. To really see this, imagine we were doing this in two dimensions instead of three.

Back in 3 dimensions, this means that a single point in k-space occupies a volume of
$$
    \frac{\pi}{L}\times\frac{\pi}{L}\times\frac{\pi}{L} = \left(\frac{\pi}{L}\right)^3
$$

Now, let's say we have a wave vector of magnitude $k=|{\bf k}|$. The number of allowed states with a wave vector whose magnitude lies between $k$ and $k+{\rm d}k$ lie within one octant of a spherical shell shell of radius $k$ and thickness $k+{\rm d}k$ (where we are only concerned with 1 octant as we are only allowing $k_x,k_y,k_z$ to be positive).  The volume occupied by this shell is
$$
    \frac{1}{8} 4\pi k^2 {\rm d} k
$$

![DoS|300](Figures/Density_of_States.svg)

As such, the number of allowed states with a wave vector whose magnitude lies between $k$ and $k+{\rm d} k$ is given by $g(k){\rm d}k$ where $g(k)$ is the density of states. An example of this is given below in 2-D (assuming a $k_z=\pi/L$).
![DoS|450](Figures/k_space_2D.png)
This number of states is given by
$$
    g(k){\rm d}k = \frac{{\rm volume\;in\;k-space\;of\;one\;octant\;of\;the\;spherical\;shell}}{{\rm volume\;in\;k-space\;occupied\;per\;allowed\;state}}
$$
This implies that
$$
    g(k){\rm d}k = \frac{1}{8}\frac{4\pi k^2 {\rm d} k}{(\pi/L)^3} = \frac{V k^2 {\rm d} k}{2\pi^2}
$$