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

## Relations to Bernoulli Trials
The bernoulli distribution is the indicator decomposition of the hypergeometric distribution by letting $X$ be the hypergeometric random variable that is the number of times the bernoulli trial result in an event of $G$.

$$
I_k \sim \text{Bernoulli}(G/N)\\
X = \sum_{k=1}^n I_k
$$