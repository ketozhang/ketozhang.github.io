---
title: Probability Generating Function
---

## Polynomial

For $X$, a random variable with possible values $0, 1, \ldots, N$ of probability $p_k := P(X=k)$, the PGF of $X$ is,

$$
G_X(s) = \sum_{k=0}^N p_ks^k
$$

Which is a degree $N$ polynomial with coefficients as the probability of $X$. Notice that the PGF is also equivalent to $E(s^X)$.

Independent Joint Distribution
: The joint PGF for two independent non-negative random variables $X$ and $Y$ are,

	$$
	G_{X+Y}(s) = G_X(s)G_Y(s)
	$$

	Because $G_{X+Y}(s) = E(s^Xs^Y)$ is separable by independence.

Sums of an IID Sample
: For $S_n = X_1 + X_2 + \ldots X_n$ where the set of $X_k$ are iid random variables, the PGF is the $n$th power any one PGF.

	$$
	G_{S_n} = G_{X_1}^n
	$$