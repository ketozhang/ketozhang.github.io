---
title: Population Mean
---

Naturally we should be able to get an idea of the population mean $\mu$ by using the sample mean $\bar X$,

$$
\begin{gather*}
\bar X = \frac{S_n}{n}\\
E(\bar X) = \mu, \quad \text{SD}(\bar X) = \frac{\sigma}{\sqrt{n}}
\end{gather*}
$$


## Law of Averages

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



## Central Limit Theorem

In fact, $\bar X$ is an unbiased estimator of the population mean.

Because it's a linear transformation of $S_n$, it's not a surprise that the CLT applies.

$$
P(\bar X \le x) \rightarrow \Phi\left(\frac{s-\mu}{\sigma / \sqrt{n}}\right)
$$

### Confidence Intervals

When stating confidence intervals, the random variable at interest is often the sample mean. We define the $p$ confidence interval as the interval $\bar X \pm c$ that satisfies,

$$
P\left( \abs{\bar X - \mu} \le c \right) = P\left( \mu \in \bar X \pm c\right) = p
$$

At large $n$, CLT holds so that

$$
p = \Phi\left(\frac{c}{\sigma/\sqrt{n}}\right) - \Phi\left(\frac{c-2\mu}{\sigma/\sqrt{n}}\right)
$$

Number of SDs
: More conveniently we can replace $c$ with the number $z$ of SDs away from the mean,

	$$
	P\left( \abs{\bar X - \mu} \le c \right) = P\left( \abs{\bar X - \mu} \le z\frac{\sigma}{\sqrt{n}} \right); \qquad z = \frac{c}{\sigma/\sqrt{n}}
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

---

Proven using the argument of number of SDs above,

$$
c = \frac{\sigma}{\sqrt{n}}\abs{\Phi^{-1}\left(\frac{1-p}{2}\right)}
$$