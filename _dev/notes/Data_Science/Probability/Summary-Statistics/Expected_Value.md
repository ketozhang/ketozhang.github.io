---
title: Expected Value
---

The **expected value** (aka **expectation**) is defined as,

$$
\mathbb E[X] \equiv \sum_{x \in \Omega_X}xP(x)
$$

## Method of Indicators

If a random variable $X$ can be expressed as a sum of indicators then its expected value also follows by linearity.

$$
\mathbb E[X] = \sum_{k=1}^N \mathbb E[I_k]
$$

## Function Rule

If the random variable at interest is a function of another random variable $X = f(Y)$ then the function rule applies as following to the range of $Y$

$$
\mathbb E[X] = \sum_{y \in \Omega_Y} f(y) P(Y=y)
$$

Moments of $X$ (Corollary)
: All powers of $X$ has the expected value called the **$k$-th moment** of $X$ is given by,

	$$
	\mathbb E[X^k] = \sum_{x \in \Omega_X}X^k P(X=x)
	$$

## Tail Sum Formula
The expected value can be expressed equivalently as the sum of the right tail of the distribution,

$$
\mathbb E[X] = \sum_{x \in \Omega_X} P(X > x)
$$

## Expectation and Conditioning

The expected value can be expressed in conditional probabilities. Consider the random variable $X$ and $Y$, the expected value can be expressed using both random variable

$$
\mathbb E[X] = \sum_{x \in \Omega_X} xP(Y \mid X=x) P(X=x)\\
\mathbb E[X] = \sum_{y \in \Omega_y} xP(X \mid Y=y) P(Y=y)
$$

Motivated by this we define the **conditional expectation** as,

$$
\boxed{\mathbb E[X \mid Y=y] = \sum_{x \in \Omega_X} x P(X=x \mid Y=y)}
$$

The conditional expectation is a random variable because the conditional expectaiton is a function of the random variable $Y$.

Most useful is the fact that the conditional expectation has the expected value,

\[
\begin{align}
	\mathbb E \Big[\mathbb E[X \mid Y] \Big] &= \sum_{x \in \Omega_X}\left[\sum_{y \in \Omega_Y} y P(Y=y \mid X=x)\right]P(X=x)\\
	&= \sum_{x \in \Omega_X} \mathbb E[Y \mid X=x] P(X=x)
\end{align}
\]

\[
	\boxed{\mathbb E[X] = \mathbb E \Big[\mathbb E[X \mid Y] \Big]}
\]

### Expectation by Condition of Known Expectations

The expected value of $X$ conditioned on $Y$ can be determined if we know exactly the conditional expectation as some function of the range of $f(Y=y)$,

$$
\begin{gather*}
\mathbb E[X \mid Y=y] = f(Y=y)\\
\big\Downarrow\\
\mathbb E[X \mid Y] = f(Y)
\end{gather*}
$$

If $f(Y)$ is a linear function, solving for $\mathbb E[X]$ is simpy applying the linearity rule,

$$
\mathbb E[X] = \mathbb E\big[f(Y)\big]
$$

This makes more sense if we do a few examples:

Conditional Expectation of Binomial
: Take for instance the conditional expectation is found to be the expectation of binomial,

	$$
	\mathbb E[X \mid Y=y] = (n-y)p
	$$

	That is to say the events $\set{X \mid Y = y}$ are distributed as binomial of $n' = n-y$ trials with $p'$ chance of trial succeed.

	Then, it's simple to determine $E[Y]$, after replacing $y$ with $Y$

	$$
	\begin{align*}
		\mathbb E[X \mid Y] &= \mathbb E \big[(n-Y)p\big]\\
		&= (n-\mathbb E[Y])p
	\end{align*}
	$$

Conditional Expectation of Sums
: Let the sum of some event be $S = X_1 + X_2 + \ldots X_N$ for iid $X_k$. $N$ is the random variable independent from $X$ representing the count of sampling with $\mathbb E[N]$.

	Notice that the conditional expectation is can be easily written as,

	$$
	\begin{gather*}
	\mathbb E[S \mid N = n] = n \cdot \mathbb E[S]\\
	\mathbb E[S \mid N] = N \cdot \mathbb E[S]
	\end{gather*}
	$$

	then it follows that

	$$
	\begin{gather*}
	\mathbb E[S] = \mathbb E(\mathbb E[S \mid N])\\
	\mathbb E[S] = \mathbb E[S]\mathbb E[N]
	\end{gather*}
	$$

	Let's call this the **separation of expectation by conditioning**.
