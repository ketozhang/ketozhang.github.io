---
title: Specific Mechanical Energy
---

The energy of an orbit is given by the kinetic energy of the reduced mass $m$ and the gravitational potential energy,

$$
E = \frac{1}{2}mv^2 - \frac{Gm_1m_2}{r} = \frac{1}{2}mv^2 - \frac{Gm(m_1 + m_2)}{r}
$$

A more useful vector for orbital mechanics is the **specific mechanical energy** (SME) $\epsilon \equiv E / m$,

$$
\epsilon = \frac{v^2}{2} - \frac{\mu}{r}
$$

This SME for the two-body problem is called the **energy integral**

In terms of the semimajor axis $a$,

$$
\epsilon = -\frac{\mu}{2a}
$$

Constant SME for the Two Body Problem
: $\epsilon$ is constant which can be shown by first taking the dot product of the two body equation with the velocity vector of the satellite $\vec v$ (note that $\vec v \neq \dot{\vec r}$)

    $$
    \ddot{\vec r} \cdot \vec v = -\frac{\mu}{r^2} (\hat r \cdot \vec v)
    $$

    Note that the dot product is the radial component of the velocity vector $v_r = \hat r \cdot \vec v$. Equivalently its the magnitude of the velocity of $r$

    $$
    \dot{r} = v_r = \vec v \cdot \hat r
    $$

    $$
    \ddot{\vec r} \cdot \vec v = -\frac{\mu}{r^2} \dot{r}
    $$

    Notice that the acceleration vector of the tangential and radial velocity vector is the same $\ddot{\vec r} = \dot{\vec v}$

    $$
    \dot{\vec v} \cdot \vec v = -\frac{\mu}{r^2} \dot{r}
    $$

    The two sides are derivatives of the kinetic energy and potential energy respectively thus we get the energy equivalence,

    $$
    \frac{\rm d}{\rm d t} \left(\frac{v^2}{2}\right) = \frac{\rm d}{\rm d t} \left(\frac{\mu}{r}\right)\\
    \frac{\rm d}{\rm d t} \left(\frac{v^2}{2}\right) - \frac{\rm d}{\rm d t} \left(\frac{\mu}{r}\right) = 0\\
    \epsilon = \frac{v^2}{2} - \frac{\mu}{r} = \text{constant}
    $$