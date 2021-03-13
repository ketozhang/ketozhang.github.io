---
title: Matrix Calculus Cheatsheet
---

## WRT Vector

Let $x$ be a vector.

| $f$ | $\nabla_x f$ | Common Usage |
|-----|--------------|---------|
| $Ax$  | $A$  |
| $\lvert Ax-y \rvert^2$ | $2A^\top(Ax-y)$ | Ordinary Least Squares |
| $x^\top A x$ | $(A + A^\top)x$ | Squared length of $Bx;~A:=B^TB$ |

### Gradient Chain Rule

The **gradient chain rule** or the **reverse chain rule** follows from the original chain rule:

$$
f = g \circ x
$$

$$
\nabla_x f = \left[ \frac{\partial f }{\partial x} \right]^\top = \left[ \frac{\partial f }{\partial g}\frac{\partial g }{\partial x} \right]^\top = \left(\frac{\partial g }{\partial x}\right)^\top \left(\frac{\partial f }{\partial g}\right)^\top
$$

### Motivating Derivations

* Squared length of $Bx$

    $$
    f(x) = |Bx|^2 = xB^\top B x
    $$

    $$
    A := B^\top B
    $$

    $$
    \begin{align}
    \nabla_x f &= \left[ \frac{\partial}{\partial x} x^\top Ax + x^\top \frac{\partial}{\partial x} (Ax) \right]^\top\\
    &= \bigg[\underbrace{\hat T (Ax)}_{x^\top A^\top} + x^\top A \bigg]^\top\\
    &= (A + A^\top)x
    \end{align}
    $$