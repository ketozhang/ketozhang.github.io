---
title: Variance
---

The variance is motivated by wanting to know how far away is $E[X] = \mu$ away from some true answer in the random variable $X$. That is, the variance is the expected value of the squared deviance of $\mu$ or the **root mean square** of $X$. The variance is defined as,

$$\text{Var}[X] =  E\left[ (X-\mu)^2 \right]$$

Non-negative
: The variance is alway non-negative because the random variable inside is a squared variable

	$$
	\text{Var}[X] \ge 0
	$$

Identity
: A more useful identity derived by expanding the square,

	$$
	\text{Var}[X] =  E[X^2] -  E[X]^2
	$$

Second Moment $\ge$ First Moment
: In corollary, the squared expected value is always greater or equal to the expected value squared,

	$$
	 E[X^2] \ge  E[X]^2
	$$

Standard Deviation
: Because the variance is some squared quantity, we'd like to take the square root to get a sense of the untis

	$$
	\text{SD}[X] = \sqrt{\text{Var}[X]}
	$$


Linearity
: Like the expected value, the variance has its own linearity rule. The variance is invariant by translation and linear by sretching

	$$
	\text{Var}(aX + b) = a^2\text{Var}[X]
	$$

	This is the same exact property as the magnitude of a vector.


Variance of Sums
: The variance of sums is the sum of individual variance and an extra term called the [covariance](#covariance)

	$$
	\text{Var}\left[\sum_i^n X_i\right] = \sum_i^n \text{Var}[X_i] + \sum_{i \neq j} \text{Cov}[X_i,X_j]
	$$

	If all random variable are independent:

	$$\text{Var}\left[\sum X_i\right] = \sum \text{Var}[X_i] $$

## Method of Indiciators
The variance of indicators are nice to use because,

$$
 E[I^2] =  E[I]
$$

Therefore we can easily solve for the variance of an indicator,

$$
\text{Var}[I] =  E[I] -  E[I]^2 = p(1-p)~,
$$

or simply,

$$
\boxed{\text{Var}[I] = pq}
$$

Now to use the method of indicators we actually need to rely on covariance. It's useful to know the covariance of two indicators that are generally dependent.

$$
\begin{align*}
\text{Cov}[I_j, I_k] &= E[I_jI_k] - E[I_j]E[I_k]\\
&= P(I_jI_k) - P(I_j)P(I_k)\\
&= p_{jk} - p_jp_k
\end{align*}
$$

By the variance of the sum of random variables,

$$
\begin{align*}
\text{Var}[I_j + I_k] &= \text{Var}[I_j] + \text{Var}[I_k] + 2\text{Cov}[I_j,I_k] \\
&= p_jq_j + p_kq_k + 2(p_{jk} - p_jp_k)
\end{align*}
$$

In general, for $n$ indicators,

$$
\text{Var}\left[\sum_{k=1}^n I_k \right] = \sum_{i=1}^n p_iq_i + n(n-1)\sum_{i \neq j}(p_{ij} - p_ip_j)
$$

## Variance by Conditioning

$$
\text{Var}(X) = E[\text{Var}(Y \mid X)] + \text{Var}[E(Y \mid X)]
$$

I'd like to call the "Var is EVar plus VarE".

<!-- TODO: Proof -->

### Conditional Variance
Like the expectation, the variance of a random variable can be conditioned on another. The conditional variance of some random variable $X$ given $Y=y$ is,

$$
\text{Var}(X \mid Y = y) = \sum_{x \in \Omega_X} (x-\mu_X)P(X=x \mid Y=y)
$$

Not fixing $Y$, we have the random variable $\text{Var}(X \mid Y)$ called the conditional variance.

$$
\begin{align*}
\text{Var}(X) &= \sum_{x \in \Omega_X} (x - \mu_X)P(X=x)\\
&= \sum_{x \in \Omega_X} (x - \mu_X) \sum_{y \in \Omega_Y} P(X=x \mid Y=y)P(Y=y)
\end{align*}
$$

## Mean Squared Error

The variance is related to the mean squared error if we replace the prediciton $\mu$ with some arbritrary constant $c$,

$$
\text{MSE}(c) =  E[(X-c)^2]
$$

By expanding $ E[(X-\mu+\mu-c)^2]$ out we get,

$$
\boxed{\text{MSE}(c) = \text{Var}[X] + (\mu-c)^2}
$$

Therefore any prediction $c$ is no better than $\mu$ and the MSE is at least the variance,

$$
\text{MSE}(c) \ge \sigma_X^2
$$

## Covariance

By the motivation of summing variances, the covariance is the expected value of the product of deviances of two random variables,

$$
\text{Cov}[X,Y] = E\big[(X-\mu_X)(Y-\mu_y)\big]
$$

Identity
: Expanding the covariance gives you a useful identity,

	$$
	\text{Cov}[X,Y] = E[XY] - \mu_X\mu_Y
	$$

Superset of Variance
: All variances are also covariance but with itself. This makes for a nice compact notation when needed.

	$$
	\text{Var}[X,X] = \text{Cov}[X,X]
	$$

Symmetric
: The covariance of $X$ and $Y$ is the same in reverse

	$$
	\text{Cov}[X,Y] = \text{Cov}[Y,X]
	$$

Addition by Distribution
: The addition rule for covariance is

	$$
	\text{Cov}[X+Y,Z] = \text{Cov}[X,Z] + \text{Cov}[Y,Z]
	$$

Bilinearity
:	Immediately we can see constant factors are taken out just like the variance

	$$
	\text{Cov}[aX, bY] = ab~\text{Cov}[X,Y]
	$$

	In general with the additon rule, the general covariance of two summed random variable is the sum of covariances for each pairwise terms.

	$$
	\text{Cov}[\vec a \cdot \vec X, \vec b \cdot \vec Y] = \sum_{i,j}a_ib_j\text{Cov}[X_i, Y_j]
	$$

Uncorrelated if Indepndent
:	If two random variables are independent then the covariance is zero,

	$$
	\begin{gather*}
	X \perp Y \\
	\big\Downarrow \\
	\text{Cov}[X,Y] = 0
	\end{gather*}
	$$

Positive covariance
:	If the covariance is positive, then the two deviance term must have the same sign.

	$$
	\text{Cov}[X,Y] > 0 \implies \begin{cases}\abs{X - E[X]} > 0 & \abs{Y - E[Y]} > 0 \\ \abs{X - E[X]} < 0 & \abs{Y - E[Y]} < 0 \end{cases}
	$$

Negative covariance
:	If the covariance is negative,t hen the two deviance term must have opposite signs.
	$$
	\text{Cov}[X,Y] > 0 \implies \Big( \abs{X - E[X]} > 0 \land \abs{Y - E[Y]} < 0 \Big) \lor \Big(\abs{X - E[X]} < 0 \land \abs{Y - E[Y]} > 0 \Big)
	$$

### Covariance of Random Vector
The random vector $X$ of size $n$ has a $n \times n$ positive semidefinite matrix called the **covariance matrix** $\Sigma$ where each element is,

$$
\Sigma_{i,j} = \text{Cov}(X_i, X_j)
$$

Linear Transformation
:	For a random vector $Y = AX + b$ where $A$ is a $m \times n$ matrix and $b$ is $m \times 1$ vector,

	$$
	\Sigma_Y = A\Sigma_X A^\top
	$$

## Correlation

$$
\text{Corr}[X, Y] \equiv \frac{\text{Cov}[X, Y]}{SD[X] SD[Y]}
$$

Standardized Random Variables
:	With standardized random variables $X^*$ and $Y^*$:

	$$ X^* = \frac{X -  E[X]}{\sigma(X)} $$
	$$ Y^* = \frac{Y -  E[Y]}{\sigma(Y)} $$

	$$ \text{Corr}[X,Y] = E[X^*Y^*]  $$

Unity Bound
:	$$ -1 \le \text{Corr}[X,Y] \le 1 $$

	Proof
	: Consider the standardize random variable $X^*$ and $Y^*$. By the Cauchy-Schwarz Inequality

	$$ \abs{ E[X^*Y^*]} \le \abs{ E[X^*]  E[Y^*]} = 1$$

	Thus,

	$$ -1 \le \text{Corr}[X,Y] \le 1  $$

Perfectly Correlated or Anticorrelated
: 	$$  X = Y \implies \text{Corr}[X,Y] = 1  $$
	$$  X = -Y \implies \text{Corr}[X,Y] = -1 $$
