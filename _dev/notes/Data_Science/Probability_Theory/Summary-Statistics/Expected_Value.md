---
title: Expected Value
---

The **expected value** (aka **expectation**) is defined as,

$$
E[X] \equiv \sum_{x \in \Omega_X}xP(X=x)
$$

Existence
: The expected value exists only if,

	$$
	E[\abs{X}] = \sum_{x \in \Omega_X}\abs{x} P(X=x) \lt \infty
	$$

Linearity of Expectation
: The linear transformation of $X$ has the expectation,

	$$
	E(aX + b) = aE(X) + b
	$$

## Method of Indicators

If a random variable $X$ can be expressed as a sum of indicators then its expected value also follows by linearity.

$$
E[X] = \sum_{k=1}^N E[I_k]
$$

## Function Rule

If the random variable at interest is a function of another random variable $X = f(Y)$ then the function rule applies as following to the range of $Y$

$$
E[X] = \sum_{y \in \Omega_Y} f(y) P(Y=y)
$$

Moments of $X$ (Corollary)
: All powers of $X$ has the expected value called the **$k$-th moment** of $X$ is given by,

	$$
	E[X^k] = \sum_{x \in \Omega_X}X^k P(X=x)
	$$

## Tail Sum Formula
If the random variables $X$ is non-negative, then the expected value can be expressed as the sum of the right tail of the distribution,

$$
E[X] = \sum_{x \in \Omega_X} P(X > x)
$$

## Expectation by Conditioning

The expected value can be expressed in conditional probabilities. Consider the random variable $X$ and $Y$, the expected value can be expressed using both random variable using the marginal probability

$$
E[X] = \sum_{x \in \Omega_X} x \left[\sum_{y \in \Omega_Y} P(X=x \mid Y=y)P(Y=y)\right]
$$

Motivated by this we define the **conditional expectation** as,

$$
\boxed{E[X \mid Y=y] = \sum_{x \in \Omega_X} x P(X=x \mid Y=y)}
$$

The conditional expectation is a random variable because the conditional expectaiton is a function of the random variable $Y$.

Most useful is the fact that the conditional expectation has the expected value,

\[
\begin{align}
	E \Big[E[X \mid Y] \Big] &= \sum_{y \in \Omega_Y} E[X \mid Y=y] P(Y=y)\\
	&= \sum_{x \in \Omega_X}x \left[\sum_{x \in \Omega_Y} P(Y=y \mid X=x)P(Y=y)\right]\\
\end{align}
\]

\[
	\boxed{E[X] = E \Big[E[X \mid Y] \Big]}
\]

### Expectation with Known Conditional Expectation

The expected value of $X$ conditioned on $Y$ can be determined if we know exactly the conditional expectation as some function of the range of $g(y)$,

$$
\begin{gather*}
E[X \mid Y=y] = g(y)\\
\big\Downarrow\\
E[X \mid Y] = g(Y)
\end{gather*}
$$

Then the expectation of $X$ is,

$$
E[X] = E\big[g(Y)\big]
$$

This makes more sense if we do a few examples:

Conditional Expectation of Binomial
: Take for instance the conditional expectation is found to be the expectation of binomial,

	$$
	E[X \mid Y=y] = (n-y)p
	$$

	That is to say the events $\set{X \mid Y = y}$ are distributed as binomial of $n' = n-y$ trials with $p'$ chance of trial succeed.

	Then, it's simple to determine $E[Y]$, after replacing $y$ with $Y$

	$$
	\begin{align*}
		E[E(X \mid Y)] &= E \big[(n-Y)p\big]\\
		&= (n-E[Y])p
	\end{align*}
	$$

Conditional Expectation of Sums
: Let the sum of some event be $S = X_1 + X_2 + \ldots X_N$ for iid $X_k$ with mean $\mu_X$. $N$ is the random variable independent from $X$ representing the count of sampling with $\mu_N$.

	The expected value of the sum is more easily written first as the conditional expectation

	$$
	\begin{gather*}
	E(S \mid N=n) = n\mu_X\\
	E(S \mid N) = N\mu_X\\
	\end{gather*}
	$$

	The expectation of $S$ is then,

	$$
	E(S) = E[E(S \mid N)] = \mu_N \mu_X
	$$

## Expectation of Random Vectors

For a random vector $X$ the expectation is applied element-wise,

$$
\mu = E(X) \equiv [E(X_1), E(X_2),\ldots, E(X_n)]^\top
$$

Linear Transformation
:	For a random vector $Y = AX + b$ where $A$ is a $m \times n$ matrix and $b$ is $m \times 1$ vector,
	$$
	E(Y) = A\mu_X + b
	$$