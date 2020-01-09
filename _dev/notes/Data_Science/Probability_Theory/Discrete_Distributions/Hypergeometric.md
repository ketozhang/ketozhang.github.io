---
title: Hypergeometric
---

The hypergeomtric distribution is given as,

$$
P(X=g; n, G, N) = \frac{{G \choose G}{N-G \choose n-g}}{N \choose n}
$$

Expected Value
: $$\mathbb E[X] = np; \quad p = \frac{G}{N}$$

Variance
: $$ \text{Var}[X] = \underbrace{npq}_{\text{Binom. Var}} \frac{N-n}{N-1} $$

## Sums of Dependent Bernoulli Trials
The hypergeometric is the sum of $n$ **dependent** identical $\text{Bernoulli}(G/N)$ trials,

$$
X = \sum I_k
$$

$$
I_k \sim \text{Bernoulli}(G/N)\\
$$

The dependency comes from the fact that the hypergeometric process samples with replacement. On the other hand, its cousin is the binomial process that samples without replacement hence the independency.