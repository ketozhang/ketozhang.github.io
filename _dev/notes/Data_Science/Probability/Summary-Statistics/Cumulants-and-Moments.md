---
title: Cumulants and Moments
---

## Moment Generating Function

The **moment generating function (MGF)** is some function that defines for some random variable $X$,

$$
M_X(t) = E(e^{tX})
$$

The Taylor expansion of $e^{tX}$ gives us each expected value of the powers of $X$,

$$
M_X(t) = 1 + t\frac{E(X)}{1!} + t^2\frac{E(X^2)}{2!} + t^3\frac{E(X^3)}{3!} + \ldots
$$

$E(X^k)$ is called the $k$th **moment** of $X$. Given a MGF, it is not easy to use the above to extract out a moment. Instead, notice, the $k$th derivative evaluted at zero gives

$$
M_X^{(k)}(0) = E(X^k)
$$

Uniqueness
: Two distributions with the same MGF have the same distribution.

Independent Sums
: The sum of two independent random variables has the MGF that is separable,

	$$
	\begin{align*}
	M_{X + Y}(t) &= E(e^{tX}e^{tY})\\
	&= E(e^{tX})E(e^{tY}) \tag{independence}
	\end{align*}
	$$

	$$
	M_{X + Y}(t) = M_X(t)M_Y(t)
	$$

### Central Limit Theorem

If two distribution are the same if they have the same MGF, it is natural to think if one MGF tends towards another at some asymptotic limit, the the distribution tends towards the other. This is the basis for using MGF with CLT.

Consider a sum $S$ of iid random variables $X_1, X_2, \ldots, X_n$. The standardized form is,

$$
S^* = \frac{S - n\mu}{\sqrt{n}\sigma} = \sum_{i=1}^n \frac{1}{\sqrt{n}}\left(\frac{X_i - \mu}{\sigma}\right) = \sum_{i=1}^n \frac{X_i^*}{\sqrt{n}}
$$

Solving for the MGF

$$
\begin{align*}
M_{S^*}(t) &= \left[ M_{X^*}(t/\sqrt{n}) \right]^n\\
& = \left(1 + \frac{t}{\sqrt{n}}\frac{E(X^*)}{1!} + \frac{t^2}{n}\frac{E(X^{*2})}{2!} + \ldots\right)^n\\
&= \left(1 + \frac{t^2}{n} + \mathcal O(t^3)\right)^n
\end{align*}
$$

$\mathcal O(t^3)$ is taken to be small as $n$ grows large.

$$
M_{S^*}(t) \approx \left(1 + \frac{t^2}{n} + \right)^n \rightarrow e^{t^2 / 2}, \quad \text{as } n \to \infty
$$

Thus the sums of iid random variables has the MGF that tends towards the MGF of normal as $n$ grows large.