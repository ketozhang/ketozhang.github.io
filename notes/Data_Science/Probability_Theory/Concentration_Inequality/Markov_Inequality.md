---
title: Markov's Inequality
---

Markov's inequality at its simplest deals with the expected value (or first moment) of the distribution. For a non-negative random variable $X$ with a finite expected value $\mathbb E[X]$, the probability that its at least the constant constant $c$ is,

$$
\boxed{P(X \ge c) \le \frac{\mathbb E[X]}{c}}
$$

In terms of the expected value,

$$
P(X \ge n\mu) \le \frac{1}{n}
$$

Proof
: Let $I$ be the indicator that $X \ge c$. The expected value is also its probability,

  $$
  \mathbb E[I(X\ge c)] = P(X \ge c)
  $$

  Consider the function $f(X) = X/c$ which is always bigger than $I(X \ge c)$. Because the expected value of a linear function is linear, the larger function has the higher expected value,

  $$
  E[f(X)] \ge E[I(X \ge c)]
  $$

  $$
  \frac{E[X]}{c} \ge P(X \ge c)
  $$

  Thus we've proven Markov's inequality,

  $$
  P(X \ge c) \le \frac{E[X]}{c}
  $$


## Markov's Inequality - Monotonically Increasing Function

To generalize the simple Markov's inequality, we allow the first moment to be of any monotonically increasing function $\varphi(X)$,

$$
P(X \ge c) \le \frac{\mathbb E[\varphi(X)]}{\varphi(c)}
$$

## General Moment Markov Inequality

Any $k$-th moment is also a monotonically increasing function thus w e can generalize the moment to any $k$,

$$
P(X \ge c) \le \frac{\mathbb E[X^k]}{c^k}
$$

Bound on random variable deviates from some value.

$$
P(\abs{Y} \ge c) \le \frac{\mathbb E[\abs{Y}^k]}{c^k}
$$
