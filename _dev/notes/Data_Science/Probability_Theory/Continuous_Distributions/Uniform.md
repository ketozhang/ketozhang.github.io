---
title: Uniform (Continuous)
---

$$
f_X(x) = \frac{1}{a}; \qquad a \le x \le 1
$$

Linear Transformation of Uniform(0,1)
:	A time-saving property of the uniform random variable is all uniform random variable can be expressed as a linear transformation of the $U \sim \text{Uniform}(0,1)$ with PDF,

$$
f_U(u) = 1; \qquad 0 \le u \le 1
$$

Variance
:	Since the second moment is,

	$$
	E(U^2) = \int_0^1 x^2 ~du = \frac{1}{3}
	$$

	$$
	\text{Var}(U) = \frac{1}{12}
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