---
title: Joint Density
---

Consider two random variables $X$ and $Y$. The probability of some event $A$ that lies in the domain of both $X$ and $Y$ can be expressed as,

$$
P((X,Y) \in A) = \iint_A f(x,y)~ dxdy
$$

Where $f(x,y)$ is the joint probability density function

## Independence

If $X$ and $Y$ are independent then their joint PDF is separable,

$$
f(x,y) = f_X(x)f_Y(y)
$$

## Marginal Density
The PDF of $X$ can be solved using the marginal density.

$$
f_X(x) = \int_y f(x,y)~ dy
$$

## Conditional Density
The conditoinal density can be determined using the divison rule,

$$
f(y \mid x) = \frac{f(x,y)}{f_X(x)}
$$