---
layout: lecture
---
{% raw %}

# The Maxwell Boltzmann Distribution

The next question we want to ask is, given a gas at a certain temperature, what is the distribution of particle velocities within that gas?

First, we will ignore all rotational or vibrational energies associated with any particles (that is, we will assume a monatomic gas where the energy only arises due to translational motion of the particles, see Lecture 9). As such, the energy of a single particle can be written as

$$
    \epsilon = \frac{p^2}{2m}
$$

The probability that a particle is in a particular state $s$ with translational energy $\epsilon$ is then given by

$$
    P_s = \frac{1}{Z_1}e^{-\beta \epsilon}
$$

If the gas consists of $N$ particles, the mean number $\bar{n}_s$ of particles which are in the translational state $s$ is given by

$$
    \bar{n}_s = NP_s
$$

Now, substituting for $Z_1$ and $\epsilon$ then gives

$$
    \bar{n}_s(p) = \frac{\hbar^3 N}{V} \left(\frac{2\pi}{mk_{\rm B}T}\right)^{3/2} \exp \left( \frac{- p^2}{2mk_{\rm B}T} \right)
$$

We now need to figure out what the appropriate expression is for particles which have momenta between ${\bf p}$ and ${\bf p}+{\rm d}{\bf p}$. Fortunately, we can get this from the density of states equation

$$
    g(k){\rm d}k = \frac{V k^2 {\rm d} k}{2\pi^2}
$$

and using the relation that $p=\hbar k$. This gives 

$$
    f(p){\rm d}p = \frac{V p^2 }{2\pi^2 \hbar^3} {\rm d} p
$$

This means that the probability that a particle will possess a momentum with magnitude between ${\bf p}$ and ${\bf p}+{\rm d}{\bf p}$ is given by

$$
    P(p)dp = \frac{1}{N} f(p) \; dp \;\bar{n}(p)
$$

Plugging in our above expressions thus gives

$$
    P(p)dp = \frac{4\pi p^2}{(2 \pi m k_{\rm B} T)^{3/2}} \exp \left(\frac{- p^2}{2mk_{\rm B}T}\right) dp
$$

The normalisation for this equation is the condition that

$$
    \int_{0}^{\infty} P(p)dp = 1
$$

So, what does this equation tell us? If we let $p=mv$, then the expression above becomes

$$
    P(v)dv = 4\pi v^2\left( \frac{m}{2 \pi k_{\rm B} T}\right)^{3/2} \exp \left(\frac{- mv ^2}{2k_{\rm B}T}\right) dv
$$

which, if we then let $u=v / \left(\frac{2 k_{\rm B} T}{m}\right)^{1/2}$, becomes 

$$
    P(u)du = \frac{4}{\sqrt{\pi}} u^2 \exp (-u^2) du = F_1(u) du
$$

This equation describes a Maxwell speed distribution, and is plotted below.

![Max_Boltzmann](Figures/Maxwell_Distribution.png)

First, the maximum of the distribution occurs at

$$
    v_{\rm max}=\left(\frac{2 k_{\rm B} T}{m}\right)^{1/2}
$$

Now, the mean value for the velocity, $\langle v \rangle$, can be found using

$$
    \langle u \rangle = \int_0^\infty u P(u) du = \frac{4}{\sqrt{\pi}} \int_0^\infty u^3 e^{-u^2} du
$$

That last term is a known intergral, and is $\int_0^\infty u^3 e^{-u^2} du = \frac{1}{2}$. This gives

$$
    \langle u \rangle = \frac{2}{\sqrt{\pi}}
$$

which, substituting in for $\langle v \rangle$, gives

$$
    \langle v \rangle = \left(\frac{8 k_{\rm B} T}{\pi m}\right)^{1/2} = \frac{2}{\sqrt{\pi}} v_{\rm max}
$$

The mean value for the squared-velocity can be found using a similar procedure, and gives

$$
    \langle v^2 \rangle = \frac{3 k_{\rm B} T}{m}
$$

which means the root-mean-square (RMS) of the velocity is

$$
    v_{\rm RMS} = \sqrt{\langle v^2 \rangle} = \sqrt{\frac{3 k_{\rm B} T}{ m}} = \sqrt{\frac{3}{2}} v_{\rm max}
$$

This means that $v_{\rm max} \lt \langle v \rangle \lt v_{\rm RMS}$ - so the velocity which has the highest probability of occuring is lower than the mean velocity, which is lower than the RMS velocity. This is because the long tail to our distribution. Remembering this is important when discussing the kinematics of gases (to come next year).

This means that the average kinetic energy of a particle in this gas is

$$
    \langle E \rangle= \frac{1}{2} m \langle v^2 \rangle= \frac{3}{2} k_{\rm B} T
$$

in agreement with our previous result for the an ideal gas (if we multiple this by N particles).

The distribution we have derived above is the speed distribution - the velocity distribution is subtlety different in its derivation, but I recommend looking it up to become familiar with it.
{% endraw %}
