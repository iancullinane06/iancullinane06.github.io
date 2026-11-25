---
layout: lecture
nav_order: 23
---
{% raw %}

# Lecture 23: Photons

One of the keystones of quantum mechanics is that light behaves like both a particle and a
wave. Using one of these results, we can write down the energy of a single photon as

$$
    E = \hbar\omega = h\nu
$$

A single photon has a momentum $p = \hbar k$, where $k$ is the wave vector introduced when
discussing k-space, and is related to the wavelength of the photon by

$$
    k = \frac{2\pi}{\lambda}
$$

Now, any object which has a temperature $T$ emits thermal radiation. The focus of this lecture
is to understand this radiation.
Up until this section of the course, we've considered gases of traditional particles. Now,
given that photons behave both like waves and particles, we'll next consider a container
which is filled with radiation, and where the radiation is in thermal equilibrium with the walls
of the container.
There's one key difference between a gas of traditional particles and a gas of photons. For
traditional particles, when the particles encounter the walls of the vessel, they simply bounce
off. However, for photons, there's a non-0 chance that the photon will be absorbed by the
vessel, meaning the number of particles in the container is not necessarily the same
moment-to-moment. However, if the vessel is in thermal equilibrium with the photon gas,
then the vessel must be producing the same number of photons as it is absorbing -
otherwise we'd have a flow of energy, and we would not be in thermal equilibrium!
Given this, let's now calculate the internal energy of the photon gas. Recalling that the
density of states for particles with wave vectors between $k$ and ${\rm d}k$ is given by

$$
    g(k)\,{\rm d}k = \frac{4\pi k^2\,{\rm d}k}{(2\pi/L)^3}\times 2
$$

The first part of this expression comes from the end of lecture 13. The factor of 2 comes
from the fact that light has 2 different types of polarisation - linear and circular. This means
that there are 2 unique states for each point in k-space (one for each polarisation). Letting our
container be a cube of side $L$ changes this to

$$
    g(k)\,{\rm d}k = \frac{V k^2\,{\rm d}k}{\pi^2}
$$

Now, let's convert away from k-space to frequency space (as when we observe the
Universe, we tend to observe at specific frequencies or wavelengths, not specific $k$ values).
Since $\omega = ck$, we get

$$
    g(\omega) = g(k)\frac{{\rm d}k}{{\rm d}\omega}
    = \frac{g(k)}{c}
    = \frac{V\omega^2\,{\rm d}\omega}{\pi^2c^3}
$$

The internal energy of the gas is then given by

$$
    U = \int_0^\infty g(\omega)\,{\rm d}\omega\,\hbar\omega
    \left(\frac{1}{2}+\frac{1}{e^{\beta\hbar\omega}-1}\right)
$$

where $\hbar\omega$ is the energy of a photon in the state, and the expression in brackets
comes from assuming that each photon behaves like a simple harmonic oscillator (which we've
done for particles in a box before).
Splitting this out, we get

$$
    U = \int_0^\infty g(\omega)\,{\rm d}\omega\frac{\hbar\omega}{2}
    + \int_0^\infty \frac{g(\omega)\hbar\omega}
    {e^{\beta\hbar\omega}-1}\,{\rm d}\omega
$$

Unfortunately, the first term here diverges. For the moment, let's just ignore it (I've read this
as being assigned to the vacuum energy of space, or just readjusting our energy levels so
that the ground state lies at 0 rather than $\hbar\omega/2$). A better explanation comes from
considering how gases of Bosons and Fermions behave, but that's for next year.

So what we're left with is

$$
\begin{aligned}
    U &= \int_0^\infty
    \frac{g(\omega)\hbar\omega}{e^{\beta\hbar\omega}-1}\,{\rm d}\omega \\
    U &= \frac{V\hbar}{\pi^2c^3}
    \int_0^\infty \frac{\omega^3}{e^{\beta\hbar\omega}-1}\,{\rm d}\omega
\end{aligned}
$$

Using the substitution $x = \hbar\beta\omega$ and the known integral
$\int_0^\infty \frac{x^3}{e^x-1}\,{\rm d}x = \frac{\pi^4}{15}$ gives

$$
    U = \frac{V\pi^2 k_{\rm B}^4}{15c^3\hbar^3}T^4
$$

This means the energy density of the gas is

$$
    u = \frac{U}{V} = aT^4
$$

where $a$ is a constant, and is more normally given as $a = \frac{4\sigma}{c}$ and $\sigma$ is the
Stefan-Boltzmann constant.

Now, remember that the vessel is in thermal equilibrium with the gas of photons - which
means the vessel produces radiation that has the same energy density. This means that any
object which is at a temperature $T$ emits radiation with an energy density solely related to
the object's temperature!
The above expression only tells us what the total energy density is - it doesn't tell us
anything about how this energy is distributed among the frequencies of the individual
photons. Hence, we now define the spectral energy density, $u_\omega$, to be

$$
    u = \frac{U}{V} = \int_0^\infty u_\omega\,{\rm d}\omega
$$

Giving

$$
    u_\omega = \frac{\hbar}{\pi^2c^3}
    \frac{\omega^3}{e^{\beta\hbar\omega}-1}
$$

This distribution is called the blackbody distribution. In terms of frequency, $\nu$, and
wavelength, $\lambda$, it is given by

$$
    u_\nu = \frac{8\pi h}{c^3}
    \frac{\nu^3}{e^{\beta h\nu}-1}
$$

$$
    u_\lambda = \frac{8\pi hc}{\lambda^5}
    \frac{1}{e^{\beta hc/\lambda}-1}
$$

These distributions are plotted below for different temperatures. You don't need to know
much about them yet, but you'll be seeing them again in PY2106 (and in all astro courses!).

![Plancks curve graphs](../Figure/Blackbody.png)

{% endraw %}
