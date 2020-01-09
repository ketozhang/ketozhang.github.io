---
title: Average
---

The average of random variables $X = [X_1, X_2, \ldots, X_n]$ is a type of sums notably,

$$
\bar X \equiv \frac{1}{n}S =  \frac{1}{n} \sum_{k=1}^n X_k
$$

* This is very different from the sum is that $\bar X$ is continuous thus more useful in some contexts.
* Strictly textbook, this is identical to the **sample average** which is only correct in the context of samples (we will get to samples later). Since all $X_k$ are random variables, $\bar X$ is also a random variable hence should never be called sample average when dealing with random variables.

Expectation
:	Using the expectation of sums,

	$$
	E(\bar X) = \frac{1}{n}\sum_{k=1}\mu_k
	$$

Variance
:	$$
	\text{Var}(\bar X) = \frac{\sigma^2}{n}
	$$

Unbiased Estimator of the Mean
:	$\bar X$ is the unbiased estimator of the expectation $\mu$.

	$$
	E(\bar X) = \mu
	$$

## Central Limit Theorem

At the limit of large $n$,

$$
\bar X \to \text{Normal}(\mu,~ \sigma^2/n)
$$

$$
P(\bar X \le x) \approx \Phi\left(\frac{x-\mu}{\sigma / \sqrt{n}}\right)
$$

### Confidence Intervals

As $\bar X$ is most commonly useful for the unbiased estimator of the mean, thus it is also commonly used to generate the confidence interval of the estimate.

Let $p$ be the chance for $X$ to be in the confidence interval $c$ away from the mean $\mu$ :

$$
P(\bar X \in \mu \pm c) = P\left( \mu \in \bar X \pm c\right) = P\left( \abs{\bar X - \mu} \le c \right)
$$

* We take preference of the RHS for notation here on since it's more algebraically useful.
* The center expression is more accurate as it implies "the chance that the random interval $\bar X \pm c$ contains the mean $\mu$".
* More often, the numerical value is used post-calculation. This value is called the **p-value**

At large $n$, CLT holds so that

$$
\begin{align*}
p &= P\left( \abs{\bar X - \mu} \le c \right) \\
&= P(\bar X \le \mu + c) - P(\bar X \le \mu - c)\\
&= \Phi\left(\frac{c}{\sigma/\sqrt{n}}\right) - \Phi\left(\frac{c-2\mu}{\sigma/\sqrt{n}}\right)
\end{align*}
$$

Number of SDs
: More conveniently we can replace $c$ with the number $z$ of SDs away from the mean,

	$$
	p \equiv P\left( \abs{\bar X - \mu} \le z\frac{\sigma}{\sqrt{n}} \right); \qquad z = \frac{c}{\sigma/\sqrt{n}}
	$$

	The left bound of the interval is at $\mu - z \cdot \sigma/\sqrt{n}$ where we know the CDF to that bound is,

	$$
	\Phi\left(-z\right) = \frac{1-p}{2}
	$$

	To solve for $z$, we need the inverse CDF of the standard normal,

	$$
	\boxed{z = \abs{\Phi^{-1}\left(\frac{1-p}{2}\right)}}
	$$

	Alternatively, we can use the right bound of the interval to get,

	$$
	\boxed{z = \Phi^{-1}\left(p + \frac{1-p}{2}\right)}
	$$

## Sample Average

Now let $X_1, X_2, \ldots, X_n$ be an array of independent samples of the random variable $X$ with mean $\mu$ and variance $\sigma^2$.

### Law of Averages

$$
P(\abs{\bar X - \mu} < \epsilon) \rightarrow 1, \quad \text{as } n \to \infty
$$

Proof
: Since,

	$$
	P(\abs{\bar X - \mu} < \epsilon) = 1 - P(\abs{\bar X - \mu} \ge \epsilon)
	$$

	By Chebyshev's inequality,

	$$
	P(\abs{\bar X - \mu} \ge \epsilon) = \frac{\sigma^2}{n \epsilon^2} \to 0, \quad \text{as } n \to \infty
	$$