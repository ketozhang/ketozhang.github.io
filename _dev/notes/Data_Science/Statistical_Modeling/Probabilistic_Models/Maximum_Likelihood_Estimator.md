---
title: Maximum Likelihood Estimator
---

The maximum likelihood estimator (MLE)

## Motivation from Probability Theory
The MLE often used without proof whether or not the underlying system is probabilistic. To understand why we are allowed to do this we need to first understanda truly probablistic system.

We assume each point in of our sample comes from an IID sample $X:~X_1, X_2, \ldots, X_n$. Our goal is to determine the underlying distribution where the sample came from. For simplicity let the distribution only be dependent on one parameter $\theta$ (e.g., Bernoulli, Poisson, Exponential). The objective is stated as:

> Of all possible values of the parameter $\theta$, which value maximizes the likelihood of obtaining the sample?

Mathematically this statement solves the objective:

$$
\max_{\theta} \mathcal L(\theta)~, \quad\text{for}~ \mathcal L(\theta) = P( X_1, X_2, \ldots, X_n \mid \theta)
$$

Where $\mathcal L$ is called the **likelihood function**

::: Example
Let $X$ be a sample of $n$ IID $\text{Normal}(\mu, \sigma^2)$. Though the normal has two parameters, we just want to find out what's the best guess for $\mu$.

The likelihood function for this sample is,

$$
\begin{align*}
\mathcal L(\mu) &= \prod_{i=1}^n \frac{1}{\sqrt{2\pi \sigma^2}}\exp\left[-\frac{1}{2}\left(\frac{X_i-\mu}{\sigma}\right)^2\right]\\
				&= (2\pi \sigma^2)^{n/2} \exp\left[-\frac{1}{2\sigma^2}\sum_{i=1}^{n} \left(X_i-\mu\right)^2\right]
\end{align*}
$$

It looks like taking the log of the likelihood would make the objective function easier to solve. Let $L$ be the log likelihood:

$$
L(\mu) = \log{\left[(2\pi \sigma^2)^{n/2}\right]} -\frac{1}{2\sigma^2}\sum_{i=1}^{n} \left(X_i-\mu\right)^2
$$

Because the objective function is only dependent of $\mu$ we can remove all constant terms:

$$
L(\mu) \propto -\frac{1}{2\sigma}\sum_{i=1}^{n} \left(X_i-\mu\right)^2
$$

Let the extremum $\hat \mu$ be the estimator for $\mu$,

$$
\begin{gather*}
\frac{d}{d\mu} L = \frac{1}{\sigma}\sum_{i=1}^{n} \left(X_i-\mu\right) \\
\Big\Downarrow\\
\frac{1}{\sigma}\sum_{i=1}^{n} \left(X_i-\hat \mu\right) = 0\\
\Big\Downarrow\\
\boxed{\hat \mu = \frac{1}{n}\sum_{i=1}^n X_i = \bar X}
\end{gather*}
$$

We end up with the unbiased estimator for $\mu$.

For $\sigma^2$, keep $\mu=\hat\mu$ fixed and the extremum $\hat \sigma^2$ is the estimator for $\sigma^2$

$$
\boxed{\hat \sigma^2 = \frac{1}{n}\sum_{i=1}^n \left(X_i - \bar X\right)^{2}}
$$

We end up with the biased estimator for $\sigma^2$.
:::

::: Example
Now for a coin toss. Let $X$ be a sample of $n$ IID $\text{Bernoulli}(p)$. The likelihood function is,

$$
\mathcal L(p) = \prod_{X_i = 1} p\prod_{X_i = 0} (1-p)
$$


This function can be simplified by noticing there if there are $s$ successes with chance $p^s$ then there are $n-s$ failures with chance $(1-p)^{n-s}$. This motivate us to define the random variable $S = \sum_{i=1}^n X_i$.

$$
\mathcal L(p) = p^{S}(1-p)^{n-S}
$$

Noticeably, this is the binomial distribution (if $p$ was fixed) without the binomial coefficient. This is because our observed data is one sequence of $n$ Bernoulli trials. However this technical detail is not necessary because the binomial coefficient dissapears when maximizing the likelihood.

$$
L(p) = S \log p +  (n-S) \log(1-p)
$$

Finding the extremum $\hat p$,

$$
\begin{gather*}
\frac{d}{dp}L = \frac{S}{p} - \frac{n-S}{1-p}	\\
\frac{S}{\hat p} - \frac{n-S}{1-\hat p} = 0		\\
\boxed{\hat p = \frac{S}{n} = \bar X}
\end{gather*}
$$
:::