---
title: Prediction by Expectation
---

We can take advantage of the Law of Averages if what we like to predict, $Y$, is a random variable. However, if all we have is some data that is a random variable $X$, then the prediction for $Y$ can be expressed as the conditional expectation on $X$,

$$
\hat y(x) = E(Y \mid X = x)
$$

$$
\hat y(X) = E(Y \mid X)
$$

Let's define the error to be the residual from the true value,

$$
\varepsilon = Y - \hat y(X)
$$

A few key facts:

* The expectation of the error is zero
	$$E(\varepsilon) = 0$$
* The expectation of the best estimator and true value is equal
	$$E(\hat y(X)) = E(Y)$$
* The best estimator and deviance are uncorrelated (not necessarily independent).
	$$\text{Cov}\left[ \hat y(X), \varepsilon \right] = 0$$


Let's take a look at the variance. We define two deviances of $Y$ and $\hat y$ as,

$$
D_Y = Y - E(Y)
$$

$$
D_{\hat y} = \hat y(X) - E(Y)
$$

They are related by,

$$
D_Y = D_{\hat y} + \varepsilon
$$

The two terms $D_{\hat y}$ and $\varepsilon$ are uncorrelated because $D_{\hat y}$ is a function of $X$. The variance of $D_Y$ is then,

$$
\text{Var}(D_Y) = \text{Var}(D_{\hat y}) + \text{Var}(\varepsilon)
$$

Some facts:

*	The variance of the deviance of $Y$ is the same as the variance of $Y$

	$$
	\text{Var}(D_Y) = \text{Var}(Y)
	$$

* 	The variance of the deviance of $\hat y$ is the same as the variance of the best estimator

	$$
	\text{Var}(D_{\hat y}) = \text{Var}(\hat y(X))
	$$

* The variance of the residual error is,

	$$
	\begin{align*}
	\text{Var}(\varepsilon) &= E(\varepsilon^2)	\\
	&= E(E(Y - \hat y(X))^2 \mid X)\\
	&= E(\text{Var}(Y \mid X))
	\end{align*}
	$$

	Where,

	$$
	\text{Var}(Y \mid X) \equiv E\left[(Y - E(Y \mid X))^2 \mid X \right]
	$$

	So,

	$$
	\text{Var}(\varepsilon) = E(\text{Var}(Y \mid X))
	$$

We can now fully express $\text{Var}(D_Y)$ as,

$$
\text{Var}(D_Y) = E(\text{Var}(Y \mid X)) + \text{Var}(E(Y \mid X))
$$