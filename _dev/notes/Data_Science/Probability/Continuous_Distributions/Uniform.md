---
title: Uniform (Continuous)
---

## Uniform(0,1)

The uniform(0,1) PDF is,

$$
f_U(x) = 1; \qquad a < x < 1
$$

, and otherwise zero.

CDF
:	$$
	F_U(x) = x
	$$

Expectation
: The expectation not surprisingly is at the midpoint

	$$
	E(U) = \frac{1}{2}
	$$

Variance
:	Since the second moment is,

	$$
	E(U^2) = \int_0^1 x^2 ~du = \frac{1}{3}
	$$

	$$
	\text{Var}(U) = \frac{1}{12}
	$$

## Uniform(a,b)

All other uniform PDF are either translation or scaling of this uniform PDF.

$$
f_X(x) = x; \qquad a < x < 1
$$

CDF
:	$$
	F_U(x) = \frac{x-a}{b-a}
	$$

Expectation
:	$$
	E(X) = a + (b-a)E(U) = \frac{a+b}{2}
	$$

Variance
:	$$
	\text{Var}(X) = (b-a)^2\text{Var}(U) = \frac{(b-a)^2}{12}
	$$