---
title: Specific Angular Momentum
---

The angular momentum $\vec L = I\vec\omega$ in this system is purely the oribtal angular momentum of two point masses with $I=r^2m$. Thus,

$$
\vec L = (r^2 m)\left(\frac{\vec r \times \dot{\vec r}}{r^2}\right) = \vec r \times \vec p = \vec r \times m \vec v
$$

* Note that $m$ here is the reduced mass given by the relation $m^{-1} = m_1^{-1} + m_2^{-1}$

A more useful vector in orbital mechanics is the **specific angular momentum** vector , $\vec h$, which is the angular momentum vector divided by the reduced mass.

$$
\vec h = \vec r \times \vec v
$$

Constant Specific Angular Momentum for the Two Body Problem
: $\vec h$ is constant in the two body problem. This is simple fact from its derivative and plugging in the acceleration with the two body equation.

    $$
    \dot{\vec h} = \underbrace{\dot{\vec r} \times \dot{\vec r}}_0 + \dot{\vec r} \times \ddot{\vec r}
    $$

    $$
    \dot{\vec r} \times \ddot{\vec r} = -\frac{\mu}{r^2} (\vec r \times \hat r) = 0
    $$

    $$
    \dot{\vec h} = \vec 0 \implies \vec h = \text{constant}
    $$

To determine the magnitude of $\vec h$ we rely on the flight path angle $\phi_\text{fpa}$

1. Definition of cross product magnitude

    $$
    h = rv \sin(\theta_{rv}) = rv \cos(\phi_\text{fpa})
    $$

2. Extremities of flight path angle are at its periapsis and apoapsis

    $$
    h = r_a v_a\\
    h = r_p v_p
    $$

3. Trigonometry of the true anomaly $\nu$
    $$
    \cos(\phi_\text{fpa}) = \frac{r \dot \nu}{v}\\
    h = r^2 \dot \nu
    $$

4. Using the trajectory equation in terms of the semiparameter $p$

    $$
    h = \sqrt{\mu p}
    $$