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

## Tail Sum Formula
The expected value can be expressed equivalently as the sum of the right tail of the distribution,

$$
\mathbb E[X] = \sum_{x \in \Omega_X} P(X > x)
$$

## Unbiased Estimator

Consider iid random variables $X_1, X_2, \ldots, X_n \sim \text{Uniform}(N)$ where each random variable can take the values $1,2,\ldots,N$. Notice that

$$
\mathbb E[X_k] = \sum_{i=1}^n i = \frac{N+1}{2}
$$

Let the sample mean be,

$$
\bar X \equiv \frac{1}{n}\sum_{i=1}^n X_i
$$

The expectation value of the sample mean is

$$
\mathbb E[\bar X] = \frac{N+1}{2}
$$

## Expectation and Conditioning

The expected value can be expressed in conditional probabilities. Consider the random variable $X$ and $Y$, the expected value can be expressed using both random variable

$$
\mathbb E[X] = \sum_{x \in \Omega_X} xP(Y \mid X=x) P(X=x)\\
\mathbb E[X] = \sum_{y \in \Omega_y} xP(X \mid Y=y) P(Y=y)
$$

Furthermore, the **conditional expectation**

$$\mathbb E[X \mid Y=y] = \sum_{x \in \Omega_X} x P(X=x \mid Y=y)$$

is a random variable because the conditional expectaiton is a function of the random variable $Y$.

The conditional expectation can also have an expectation value,

\[
\begin{align}
    \mathbb E \Big[\mathbb E[X \mid Y] \Big] &= \sum_{x \in \Omega_X}\left[\sum_{y \in \Omega_Y} y P(Y=y \mid X=x)\right]P(X=x)\\
    &= \sum_{x \in \Omega_X} \mathbb E[Y \mid X=x] P(X=x)
\end{align}
\]

This is exactly the same as $E[X]$.

### Conditional Expectation of Sums

Let the sum of some event be $S = X_1 + X_2 + \ldots X_N$ for iid $X_k$. $N$ is the random variable independent from $X$ representing the count of sampling.

Notice that the conditional expectation is can be easily written as,

$$
\mathbb E[S \mid N = n] = n \cdot \mathbb E[S]\\
\mathbb E[S \mid N] = N \cdot \mathbb E[S]
$$

then it follows that

$$
\mathbb E[S] = \mathbb E(\mathbb E[S \mid N])\\
\boxed{\mathbb E[S] = \mathbb E[S]\mathbb E[N]}
$$

Let's call this the **separation of expectation by conditioning**.