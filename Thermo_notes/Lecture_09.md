---
layout: lecture
---
{% raw %}

# Maxwell's Relations

Next, we're going to use our new thermodynamic potentials to arrive at some very useful relations.
First, we need to do a bit of setup. For a general function of two variables which has an exact differential, $f(x,y)$, we have that

$$
    {\rm d}f = \left(\frac{\partial f}{\partial x}\right)_y {\rm d}x + \left(\frac{\partial f}{\partial y}\right)_x {\rm d}y
$$

as we've used many times before. Because ${\rm d}f$ is an exact differential we can say that

$$
    \left(\frac{\partial ^2 f}{\partial x \partial y}\right) = \left(\frac{\partial ^2 f}{\partial y \partial x}\right)
$$

If we then write

$$
    F_x = \left(\frac{\partial f}{\partial x}\right)_y ; \:\:\: F_y = \left(\frac{\partial f}{\partial y}\right)_x
$$

we have

$$
    \frac{\partial F_y}{\partial x} = \frac{\partial F_x}{\partial y}.
$$

We can now use these relations on $U$, $H$, $F$, and $G$.

## Example using the Gibbs Free Energy

The Gibbs Free Energy is $G = H - TS$. As we saw earlier, this gives us that

$$
    {\rm d} G= - S {\rm d} T + V {\rm d} P.
$$

We can also write ${\rm d} G$ as

$$
    {\rm d} G= \left(\frac{\partial G}{\partial T}\right)_P {\rm d}T + \left(\frac{\partial G}{\partial P}\right)_T {\rm d}P
$$

which gives

$$
   S = -\left(\frac{\partial G}{\partial T}\right)_P; \:\:\: V = \left(\frac{\partial G}{\partial P}\right)_T
$$

Let's consider the first of these statements. We can perform the following operation

$$
    -\left(\frac{\partial S}{\partial P}\right)_T = \left(\frac{\partial^2 G}{\partial P \partial T}\right)
$$

We can do the following to the second statement

$$
    \left(\frac{\partial V}{\partial T}\right)_P = \left(\frac{\partial^2 G}{\partial T \partial P}\right)
$$

Now

$$
    \left(\frac{\partial^2 G}{\partial T \partial P}\right) = \left(\frac{\partial^2 G}{\partial P \partial T}\right)
$$

because $G$ is a function of state (${\rm d}G$ is an exact differential). So, we get that

$$
    -\left(\frac{\partial S}{\partial P}\right)_T = \left(\frac{\partial V}{\partial T}\right)_P
$$

This is one of Maxwell's relations. We can do the same analysis for the other 3 thermodyanmic potentials, and we end up with the following relations

$$
\begin{align}
\left(\frac{\partial T}{\partial V}\right)_S &= - \left(\frac{\partial P}{\partial S}\right)_V\\
\left(\frac{\partial T}{\partial P}\right)_S &= \left(\frac{\partial V}{\partial S}\right)_P\\
\left(\frac{\partial S}{\partial V}\right)_T &= \left(\frac{\partial P}{\partial T}\right)_V\\
\left(\frac{\partial S}{\partial P}\right)_T &= -\left(\frac{\partial V}{\partial T}\right)_P
\end{align}
$$

So why do we care about these? Well, Maxwell's relations allow us to relate quantities that are difficult to measure with those that are easier to measure. For example, consider the last expression. The change in volume with respect to temperature of a system at constant pressure is a trivial thing to measure - but we now know that this gives us the change in entropy with respect to pressure at constant temperature, which is a very difficult quantity to measure.

## Revisiting Heat Capacity (again)

Ok let's use one of the tricks from the last lecture to derive some more helpful quantities. First, let's start with the fundamental thermodynamic relation, which we can write as :

$$
     {\rm d} S = \frac{1}{T} {\rm d} U+\frac{P}{T}{\rm d} V
$$

We would like to have the entropy as a function of just temperature and volume,$S=S(T,V)$ such that

$$
    {\rm d}S = \left(\frac{\partial S}{\partial T} \right)_V {\rm d}T + \left(\frac{\partial S}{\partial V} \right)_T {\rm d}V
$$

We combining these we get

$$
     {\rm d} S = \frac{1}{T} \left(\frac{\partial U}{\partial T}\right)_V {\rm d} T + \frac{1}{T}\left[ P + \left(\frac{\partial U}{\partial V}\right)_T \right] {\rm d} V
$$

Which immediately gives

$$
    \left(\frac{\partial S}{\partial T} \right)_V = \frac{1}{T} \left(\frac{\partial U}{\partial T}\right)_V; \: \: \: \left(\frac{\partial S}{\partial V} \right)_T = \frac{1}{T}\left[ P + \left(\frac{\partial U}{\partial V}\right)_T \right]
$$

Using the fact that

$$
    \frac{\partial^2 S}{\partial V \partial T} = \frac{\partial^2 S}{\partial T \partial V}
$$

leads us to

$$
    T \left(\frac{\partial P}{\partial T} \right)_V = P + \left(\frac{\partial U}{\partial V} \right)_T
$$

Recalling that

$$
    C_P-C_V = \left[ \left(\frac{\partial U}{\partial V}\right)_T +P \right] \left( \frac{\partial V}{\partial T}\right)_P.
$$

(from Lecture 4), we then get

$$
    C_P-C_V = T \left(\frac{\partial P}{\partial T} \right)_V \left(\frac{\partial V}{\partial T}\right)_P.
$$

If we now define

$$
    \beta_P = \frac{1}{V} \left(\frac{\partial V}{\partial T} \right)_P; \: \: \: -\kappa_T = \frac{1}{V} \left(\frac{\partial V}{\partial P} \right)_T;
$$

where $\beta_P$ is the isobaric expansivity and $\kappa_T$ is the isothermal compressibility, and use the following identity

$$
    \left(\frac{\partial x}{\partial y}\right)_z \left(\frac{\partial y}{\partial z}\right)_x \left(\frac{\partial z}{\partial x}\right)_y = -1
$$

which gives

$$
    \left(\frac{\partial P}{\partial T} \right)_V = - \left(\frac{\partial V}{\partial T} \right)_P \left(\frac{\partial P}{\partial V} \right)_T
$$

Tidying up gives that

$$
    C_P-C_V = \frac{T V \beta_P^2}{\kappa_T}
$$

These are all quantities which are easily measurable in the lab, meaning the difference in the heat capacities can be easily obtained.
{% endraw %}
