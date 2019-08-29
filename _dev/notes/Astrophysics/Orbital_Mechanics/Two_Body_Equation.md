---
title: Two Body Equation
---

Consider the two body problem where the Moon orbits the Earth. To be general, let's take the coordinate system $S$ where $\vec r_1$ is the distance boldsymboltor to the Earth and $\vec r_2$ is the distance boldsymboltor to the Moon. The boldsymboltor between the Earth and Moon is $\Delta \vec r$

Let's consider the geocentric coordinate system $S'$ (centered at the Earth) where the gravitational force acting on the Moon by the Earth is given by

$$
F_g = -\frac{G m_1 m_2}{r^2}~ \hat r
$$

* $\vec r$ :The boldsymboltor between the Earth and Moon. Naturally, it is equivalen to $\vec r = \Delta \vec r$
* $r$ : The distance betwen the Earth and Moon, $r = \lvert{\Delta r}\rvert$

The force of gravity felt by each body is then,

$$
F_{g1} = -\frac{Gm_1m_2}{r^2} \hat r  = m_1 \ddot{\vec{r}}_1
$$

$$
F_{g2} = \frac{Gm_1m_2}{r^2} \hat r = m_2 \ddot{\vec r}_2
$$

The relative acceleration seen in $S'$ is $\ddot{\vec r}$ given by,

$$
\ddot{\vec{r}} = - \frac{G(m_1 + m_2)}{r^2} \hat r
$$

Defining the gravitational parameter $\mu = G(m_1 + m_2)$, we end up with the **Two Body Equation**.

$$
\ddot{\vec{r}} = -\frac{\mu}{r^2} \hat r
$$