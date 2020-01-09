---
title: Exponential Decay Distribution
---

The exponential decay distribution is a continuous distribution,

$$
f(t) = \lambda e^{-\lambda t}~, \qquad t \ge 0
$$

* Continuous analogy to the geometric distribution.
* $\lambda$ : Interpret as the probability frequency of the event.

	You can see this setting $x = 1/\lambda$ then $P(X>x) = 1/e$. So $1/\lambda$ is the period to decrease the probability that $P(X>x)$ by a factor of $e^{-1}$.

CDF
:	$$
	F(t) = 1 - e^{-\lambda t}~
	$$

Survival Function
: The compelement of the CDF is known as the survival function because it is the chance that the event occurs (usually some death) after some time $t$.
	$$
	P(T>t) = e^{-\lambda t}
	$$

Expectation
: By the tail sum formula, we can use the survival function for the expectation

	$$
	E(T) = \int_0^\infty P(X > t)~ dt = \int_0^\infty e^{-\lambda t}~ dt = \frac{1}{\lambda}
	$$

Variance
: Since the second moment is,

	$$
	E(T^2) = \frac{2}{\lambda}
	$$

	The variance is

	$$
	\text{Var}(T) = \frac{1}{\lambda^2}
	$$

Median
: The median of the exponential occurs when

	$$
	F(t) =  0.5
	$$

	Equivalently when the survival and cdf intersects

	$$
	P(T > t_{0.5}) = P(T \le t_{0.5})
	$$

	This allows us to simply solve $t$ when letting the survival function go to $50\%$,

	$$
	\begin{gather*}
	e^{-\lambda t_{0.5}} = 0.5\\
	\Big\Downarrow\\
	t_{0.5} = \frac{\log(2)}{\lambda} = \log(2)E(T)
	\end{gather*}
	$$

Memoryless Property
:	Given an event has occur at $T > t_1$, the chance that another event occur afterwards $T > t_1 + t_2$ is independent of the first

	$$
	P(T > t_1 + t_2 \mid T > t_1) = P(T > t_2)
	$$

	::: Proof

	$$
	\begin{align*}
	P(T > t_1 + t_2 \mid T > t_1) &= \frac{P(T > t_1 + t_2, T > t_1)}{P(T > t_t)} \\
	&= \frac{P(T > t_1 + t_2)}{P(T > t_t)} \\
	&= e^{-\lambda t_2}\\
	&= P(T > t_2)
	\end{align*}
	$$
	:::

## Relationship to Poisson Distribution
See [Poisson Process](../Discrete_Distributions/Poisson#Poisson_Process).