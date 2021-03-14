---
title: Bernoulli
---
$$
I \sim \text{Bernoulli}(p)
$$

The Bernoulli probability distribution is

$$
P(I=k) = kp + (1-k)(1-p)
$$

more naturally,

| $I=k$ | $P(I=k)$ |
|---|---|
|  $1$ | $p$ |
|  $0$ | $1-p$  |

Expected Value
:	$$
	\mathbb E[I] = p
	$$

Variance
: $$ \text{Var}[I] = pq $$

Covariance
: $$ \text{Cov}[I_1,I_2] = P(I_1=1, I_2=1) -P(I_1=1)P(I_2=1) $$

MGF
: 	$$
	M_X(t) = pe^t + q
	$$