---
title: Coplanar Maneuvers
---

Coplanar maneuvers are maneuvers that do not change the oribtal plane instead changes the orbit's size, shape, and location of the apsides.

For burns tangential to the orbit with the additional constraint that the burn only occur at the apoapsis and periapsis (flight-path angle is zero) we can perform the following maneuvers:

* Hohmann Transfers (two tangential burns)
* One-Tangent Burn (one tangential burn)
* General Transfers (two nontangential burns)

## One-Tangent Burn

The one-tangent burn changes the velocity of the object by simply:

$$
\Delta v = v_f - v_i
$$

We assume this burn is instantaneous at the position equal to the periapsis $\vec r = \vec r_\text{per}$. Note that this means $\vec r$ is constant throughout the burn

Using the velocity equation as a function of the semi-major axis to replace the velocities we get

$$
\Delta v = \sqrt{\frac{2\mu}{r} - \frac{\mu}{a_f}} - \sqrt{\frac{2\mu}{r} - \frac{\mu}{a_i}}
$$

Solving for $a_f$ and setting the constants $\eta = \frac{2\mu}{r}$

$$
a_f = \frac{\mu a_i}{-2a_i \Delta v \sqrt{\frac{\eta a_i-\mu}{a_i}}}
$$

## Hohmann Transfer

The hohmann transfer