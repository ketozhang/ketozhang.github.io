---
title: Gaussian or Normal Distribution
---

The most prevalent distribution appearing in countless fields is the Gaussian or normal distribution.

$$X \sim \text{Normal}(\mu, \sigma)$$
$$f(x) = \frac{1}{\sqrt{2\pi \sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

Standard Normal Distribution
: The standard normal distribution is $N(0,1)$ which plays an important role in motivating why we standardize random variables. Say for a Gaussian random variable $X$,

	$$ Z = \frac{X-\mu_X}{\sigma_X} \iff Z \sim N(0,1)$$

	Where $Z$ has the PDF known as the **standard normal distribution**,

	$$
	\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-\frac{1}{2}z^2}
	$$

Cumulative Density Function
: The CDF of the normal distribution is,

$$
\Phi(x) = \int_{-\infty}^{x} \phi\left(\frac{x-\mu}{\sigma}\right) dx
$$

Expectation
: The expected value of the normal distribution is famously $\mu$,

	$$
	\text{E}(X) = \mu
	$$

Variance
: The variance of the normal distribution is famously $\sigma^2$

	$$
	\text{Var}(X) = \sigma^2
	$$

Sum
: The sum of multiple normal random variables is also normal with mean and variance

	$$
	\begin{gather*}
	\sum_k^n X_k \sim \text{Normal}(\mu, \sigma)\\
	\mu = \sum_k^n{\mu_k}\\
	\sigma^2 = \sum_k^n{\sigma_k^2}
	\end{gather*}
	$$

Independent Joint Probability (Rotational Invariant)
:	Due to the distribution's property of rotational invariance, the joint property of two iid Gaussian is a Gaussian however you rotate the random variable axes. Even better the Gaussian has the mean and variance of the sums of the two Gaussians.

	$$
	P(X,Y) = \text{N}(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2)
	$$

MGF
: For the standard normal random variable $Z$,

	$$
	M_Z(t) = e^{t^2/2}
	$$

	We can apply linear transformation to find the MGF for the normal distribution for the random variable $X = \sigma Z + \mu$,

	$$
	M_{\sigma Z + \mu}(t) = e^{\mu t + \sigma^2 t^2/2}
	$$

	Notably, any distribution with an MGF that is the exponential of a degree 2 polynomial is a normal distribution

Characteristics Function
:	$$\tilde p(x) = \exp{\left[-ik\mu -\frac{k^2\sigma^2}{2}\right]} $$

Cumulants and Moments
:	$$
		\avg{x}_c = \mu ,\quad \avg{x^2}_c = \sigma^2,\quad \avg{x^n}_c = 0, \quad \ldots,\quad  \avg{x^n}_c = 0\\
		\avg{x} = \mu ,\quad \avg{x^2} = \sigma^2 + \mu^2,\quad \avg{x^n} = 3\sigma^2\mu + \mu^3, \quad \ldots
	$$

## Multivariate Normal
Let $X$ have the multivariate normal distribution with mean vector $\mu$ and covariance matrix $\Sigma$. Let $x$ represent the vector value of at some $X$,

$$
f(x) = ([2 \pi]^n \det \Sigma)^{-1/2}\exp\left[-\frac{1}{2}(x - \mu)^\top \Sigma^{-1} (x - \mu)\right]
$$

* $\Sigma$ : The covariance matrix

:::Note
More compact is to treat $(\vec x- \vec \mu)^T \Sigma^{-1} (\vec x- \vec \mu)$ as the squared distance of some vector $\Sigma^{-1/2} \vec \Delta$ where $\vec\Delta = \vec{x} - \vec{\mu}$ which is known as the **deviation vector**. This compact form is given as,

$$
P(\vec\Delta) = ([2 \pi]^n \det \Sigma)^{-1/2}\exp\left[-\frac{1}{2}\left\lvert\Sigma^{-1/2} \vec \Delta\right\rvert^2\right]
$$
:::

Multivariate Normal Are Made of Normal Random Variables
:	All multivariate normal distributions only describe a joint distribution of normal random variables. In other words, the marginal distribution of any random variable using the multivariate normal distribution is the normal distribution.

	$$
	X_k \mid X_1, \ldots, X_{k-1}, X_{k+1}, \ldots , X_n \sim \text{Normal}(\mu_k, \Sigma_{kk})
	$$

	However, the reverse is not always true. The joint distribution of normal random variables need not to be multivariate normal.

Joint Distribution of Linear Combinations of Normal
:	The joint distribution of linear combinations of normal random variables is multivariate normal.

	$$
	\sum AX + b
	$$

Multivariate Standard Normal Transformation
: All multivariate normal can be expressed as a linear transformation of the multivariate standard normal,

	$$
	X = AZ + b
	$$

	By close inspection of the $Z$ as a function of $X$ (aka the preimage), we find that

	$$
	\Sigma = AA^\top
	$$

	$$
	\mu = b
	$$

### Covariance Matrix

The covariance matrix $\Sigma$ is a semipositive definite (symmetric) matrix

Independence and Diagonal Covariance Matrix
:	We have a special case: **the multivariate normal random variables are independent <u>if and only if</u> they are not uncorrelated**. Equivalently, the covariance matrix is a diagonal matrix

	$$ P(\vec{x}) = \prod{P(X_i)} $$

### Independence out of Bivariate Normal
The multivariate normal has interesting independence properties emerge from a collection of dependent normal random variables.

Consider two independent standard normal random variable $X$ and $Z$. The surface of the joint distribution maps a perfect circle. We may always define another normal random variable dependent of $X$ and/or $Z$ by taking the following linear combination,

$$
Y = \rho X + \sqrt{1-\rho^2}~ Z
$$

such that $\mu_Y = 0,~ \sigma_Y = 1, ~ \text{Cov}(X, Y) = \rho, ~ r(X,Y) = \rho$.

Therefore, all bivariate normal distribution can express its normal random variables as the sum of two independent random variables.


## Relation to Rayleigh Distribution
Given two independent random variable $X,Y$ with standard normal distribution, let

$$
R = \sqrt{X^2 + Y^2}
$$

Then $R$ is a the Rayleigh distribution of scale $\sigma = 1$,

$$
f_R(r) = re^{-\frac{1}{2}r^2}, \quad \text{for } r>0
$$

## Relation to Chi-Square Distribution
See [Chi-Square](./Chi-Square#Relation_to_Normal_Distribution).