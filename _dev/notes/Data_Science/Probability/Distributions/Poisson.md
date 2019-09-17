---
title: Poisson Distribution
---

$$
P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}
$$

Expected Value
: $$\mathbb E[X] = \lambda$$

Variance
: $$\text{Var}[N] = \lambda$$

Sums
: $$\sum{X_i} \sim \text{Poisson}\left(\sum \lambda_i\right)$$

Mode
: The mode of the Poisson is the integer part of $\mu$ only if $\mu$ is not an integer,

$$
\text{mode}[\text{Poisson}(\mu)] = \begin{cases}\lfloor \mu \rfloor ~\text{and}~ \lceil \mu \rceil, & \mu \in \mathbb Z^+ \cup \set{0}\\ \lfloor \mu \rfloor, & \text{otherwise.} \end{cases}
$$

## Limit of the Binomial Distribution

The poisson distribution can be derived by the limit of the binomial distribution. Let $np = \lambda$ where $\lambda$ is set constant. Let $n$ head to infinity and $p$ to zero.

Hence you may interpret the Poisson distribution as the binomial distribution of a rare event in the limit of large number of trials.

$$
\begin{gather*}
    P_k = P(X=k) = {n \choose k}p^k(1-p)^{n-k}\\
    P_0 \approx e^{-\lambda}\\
    \frac{P_k}{P_{k-1}} \approx \frac{\lambda}{k}\\
    P_k = P_0 \prod_{l=1}^k \frac{P_l}{P_{l-1}} \approx e^{-\lambda}\frac{\lambda^k}{k!}
\end{gather*}
$$

## Relationship with Bernoulli and Binomial

Given many random bernoulli trials where the number of trials is distributed as $N \sim \text{Poisson}(\lambda)$ and the number of successes is $S \sim \sum X_i$ where $X_i \sim \text{Bernoulli}(p)$, the joint distribution is captures the binomial,

$$
P(N=n, S=s) = \text{Poisson}(\lambda) \text{Binomial}(n, p)\\
\boxed{P(S=s \mid N=n) = \text{Binomial}(n, p)}
$$

The distribution of $S$ can now be determined,

$$
\begin{align}
P(S=s) &= \sum_{n=0}^\infty P(N=n, S=s) \\
&= \sum_{n=s}^\infty P(N=n, S=s)\\
\end{align}
$$

$$
\boxed{P(S=s) = \text{Poisson}(\mu p)}
$$

What's amazing is that success $S$ and failure $F$ are independent,

$$
\boxed{P(S=s, F=f) = \text{Poisson}(\mu p)\text{Poisson}(\mu q)}
$$

This is due to the effect of randomization of a parameter (trial size) of a distribution (multiple Bernouli trials).

## Relationship with Multinomial

Recall the multinomial distribution as an extension of the binomial distribution.

To get started, let's write a multinomial trial of three random variables $X, Y, Z$ such that representing the number of outcomes of their individual categories such that $N=X+Y+Z$.

$$
\begin{align}
P(X,Y,Z) &= {N \choose x} {N-x \choose y} (p_x)^x(p_y)^y(p_z)^z\\
&= {N \choose x} {N-x \choose y} (p_x)^x(p_y)^y(p_z)^{n-x-y}
\end{align}
$$

In general we can make an even more simple expression,

$$
P(N_1, N_2, \ldots) = n!\prod_k\frac{p_k}{n_k!}
$$