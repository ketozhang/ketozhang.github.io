---
title: Einstein's Summation Convention
---

## Contravariant "Upstairs" Vector

Let the spacetime four-vector be $a$. The transformation of the interial reference frame can be represented for each component indexed as $\mu$. We can represent this as the linear combination of the bases of $x^\nu \in \vec x$

$$
\set{x^\mu} \rightarrow \set{\bar x^\mu}\\
\bar a^\mu = \sum_\nu \left(\frac{\partial \bar x^\mu}{\partial x^\nu} \right)a^\nu
$$

In Enstein's summation convention, the twice repeated indices are summed across so we can simply that to,

$$
\bar a^\mu = \left(\frac{\partial \bar x^\mu}{\partial x^\nu} \right)a^\nu
$$

## Covariant "Downstairs" Vector

Let a constant be $\alpha$, the gradient vector is represented by a the four-derivative operator,

$$
\partial_\mu \equiv \frac{\partial}{\partial x^\mu} = \left[\frac{\partial}{t}, \nabla \right]
$$

The gradient of $\alpha$ is then,

$$
\partial_\mu \alpha \equiv \frac{\partial\alpha}{\partial\bar x^\mu} = \left(\frac{\partial x^\nu}{\partial \bar x^\mu}\right) \frac{\partial \phi}{\partial x^\nu}
$$