---
title: Kepler's First Law
---

Kepler's first law states the equation of motion of two bodies influenced by each other's gravity travels an ellipse.

Most commonly, the first law describe two objects a planet and a satellite (e.g., the Earth and Moon) where the planet has a mass much greater than the satellite. This allows the convenience to place an inertial reference centered on the planet. Given this frame, the most common form of the first law is the distance of the satellite given by the equation of an ellipse centered at the primary foci given by either the semi-major axis $a$ or the semiparameter $p$.

$$
r = \frac{a(1-e^2)}{1 + e \cos \nu}
$$

$$
r = \frac{p}{1 + e \cos \nu}
$$

* $\nu$ : True anomaly, a fancy word for the angle between the periapsis and the satellite.

## Proof - Analytical Geometry

This proof is not the most straightforward way of proving Kepler's first law but natural as it relies on the geometry of the orbit.

Begin by the cross product of the Two Body Equation and specific angular momentum vector.

$$
\ddot{\vec r} \times \vec h = - \frac{\mu}{r^2}(\hat r \times h)
$$

```
TODO: Full Proof
```

We get the time differential equations,

$$
\frac{\mathrm d}{\mathrm dt}(\dot{\vec r} \times \vec h) = \mu \frac{\mathrm d}{\mathrm dt}\hat r
$$

The integral of this gives,

$$
\dot{\vec r} \times \vec h = \mu \hat r + \vec c
$$

To get some form of the distance vector we need to dot product with $\vec r$ itself.

$$
h^2 = \mu r + rc\cos(\nu)
$$

Solving for $r$

$$
r = \frac{h^2}{\mu + rc\cos(\nu)}
$$

Dividing $\mu$ and noting $h^2/\mu = p$ and $c/\mu = e$,

$$
r = \frac{p}{1 + e \cos \nu}
$$