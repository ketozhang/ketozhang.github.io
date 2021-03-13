---
title: Kepler's Third Law
---

Kepler's third law states the orbital period as a simple relationship to its semi-major axis and mass of the system. Most commonly, this relationship is stated as a proportion to the semi-major axis,

$$
P \propto a^{3/2}
$$

More useful is the full expression,

$$
P = 2 \pi \sqrt{\frac{a^3}{G(m_1 + m_2)}}
$$

Alternatively expressed with $\mu = G(m_1 + m_2)$

## Proof - Using Specific Angular Momentum

Following the proof of [Kepler's 2nd law](Keplers_Second_Law),

$$
\mathrm dA = \frac{h}{2} \mathrm dt
$$

To get the period we need to solve for $\mathrm dt$ and recall that the area of an ellipse is $A = \pi a b$.

$$
P = \int_A \mathrm dt = \int_A \frac{2}{h}\mathrm dA\\
P = \frac{2\pi a b}{h}
$$

Recall that $b = \sqrt{ap}$ and $h = \sqrt{\mu p}$ gives,

$$
P = 2 \pi \sqrt{\frac{a^3}{\mu}}
$$