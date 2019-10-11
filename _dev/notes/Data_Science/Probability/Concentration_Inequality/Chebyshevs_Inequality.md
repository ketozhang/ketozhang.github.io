---
title: Chebyshev's Inequality
---

Corollary of the Markov's inequality is the Chebyshev's inequality. Suppose $X$ (not necessarily non-negative) has a finite expected value then its deviation from the mean follows,

$$
P(\abs{X-\mathbb E[X]} \ge c) \le \frac{\text{Var}[X]}{c^2}
$$

In terms of the number of standard deviations ($\sigma$),

$$
P(X - \mathbb E[X] \ge n\sigma) = \frac{1}{n^2}
$$

Proof
: Taking the advantage that the meaning of the probability is no different if take the square and applying Markov's inequality,

$$
P((X-E[X])^2 \ge c) \le \frac{E[(X-E[X])^2]}{c^2}
$$

$$
P(\abs{X-\mathbb E[X]} \ge c) \le \frac{\text{Var}[X]}{c^2}
$$
