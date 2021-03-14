---
title: Vector Equation
---

The **vector equation** (aka the **vis-viva equation**) is given by:

$$
v = \sqrt{2\left(\frac{\mu}{r} + \epsilon \right)}
$$

In terms of the semi-major axis $a$ by replacing $\epsilon = -\mu/2a$,

$$
v = \sqrt{\mu\left(\frac{2}{r} - \frac{1}{a} \right)}
$$

Using the relationship of $a$ in ellipse equation of motion gives us a form that is computationally more useful when dealing with  parabolic orbits,

$$
v = \sqrt{\frac{\mu}{r} \bigg( 2 - \frac{1-e^2}{1 + e \cos\nu} \bigg)}
$$

For a circle, $r=a$ so

$$
v_\text{circ} = \sqrt{\frac{\mu}{r}}
$$

## Proof - Energy Integral

Recall the [energy integral equation](#Specific_Mechanical_Energy),

$$
\epsilon = \frac{v^2}{2} - \frac{\mu}{r}
$$

Solving for velocity gives,

$$
v = \sqrt{2\left(\frac{\mu}{r} + \epsilon \right)}
$$