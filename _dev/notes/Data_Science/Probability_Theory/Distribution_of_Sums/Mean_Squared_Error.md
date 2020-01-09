---
title: Mean Squared Error
---

The **mean squared error** or more appropriately **mean squared deviance** of random variables $X = [X_1, X_2, \ldots, X_n]$ is a type of sums notably for an array of random variables,

$$
\text{MSE}(X) = \frac{1}{n} \sum_{k=1}^n (X_k - \mu_k)^2
$$

## Unbiased Estimator of Variance
:	For iid random variables in $X$ with expectation $\mu$ and variance $\sigma^2$, we'd like to estimator the variance without knowing the expectation thus replacing $\mu_k$ with $\bar X$. This estimator is the biased estimator of variance denoted as $\hat \sigma^2$:

$$
\begin{align*}
E(\hat \sigma^2) &= \frac{1}{n} \sum_{k=1}^n (X_k - \bar X)^2\\
&= \frac{n-1}{n}\sigma^2
\end{align*}
$$

Correcting for the factor, the unbiased estimator $S^2$ of variance is,

$$
\boxed{S^2 = \frac{1}{n-1} \sum_{k=1}^n (X_k - \bar X)^2}
$$

### Relation to Chi-Square

The unbiased estimator $S^2$ is related the Chi-Square distribution with $n-1$ degrees of freedom. In fact, it is just a constant multiple of the Chi-Square random variable.

$$
\left(\frac{n-1}{\sigma^2}\right)S^2 \sim \chi^2_{n-1}
$$