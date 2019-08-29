---
title: Satellite State
---

The classical Keplarian set of parameters that describe the state of the satellite is given by:

1. $a$ : Semimajor Axis
2. $e$ : eccentricity
3. $i$ : inclination
4. $\Omega$ : longitude of acending node
5. $\omega$ : argument of perigee
6. $\nu$ : True anomaly

# Elliptical and Circular Orbits

For elliptical and circular orbits we don't have to worry about some of the parameters going out of bound.

$a$ can be determined from the following relations can be established:

$$
a = \frac{r_a + r_p}{2}\\
r_p = a(1-e)\\
r_a = a(1+e)\\
p = \frac{b^2}{a} = a(1-e^2)
$$

$e$ from the following:

$$
e = \sqrt{1 - \frac{p}{a}}\\
e = \sqrt{1 + \frac{2 \xi L^2}{\mu^2}}
$$