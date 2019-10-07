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

## Poissonization

Poissonization is the process of letting the number of trials $N \sim \text{Poisson}(\lambda)$. Doing so causes some families of distribution to inherit independence amongst their category. To get a better idea of what this mean let's take a look at few distributions

Binomial
: Let $S \sim \text{Binomial}(s; N, p)$. Because $N$ is a random variable we can calculate for a all $N$ (i.e., the marginal distribution of $S$) or the joint distribution of $N$ and $P$,

  $$
  \boxed{P(S=s) = \text{Poisson}(s; \lambda p)}
  $$

  $$
  P(S=s, N=n) = \text{Poisson}(s; \lambda p) \text{Poisson}(n-s; \lambda p)
  $$

  Remarkably since $P(S=s, N=n) = P(S=s, F=f)$ for $F$ is the number of failed trials,

  $$
  \boxed{P(S=s, F=f) = \text{Poisson}(s; \lambda p) \text{Poisson}(f; \lambda p) = P(S=s) P(F=f)}
  $$

  This suggest $S$ and $F$ are independent!

Multinomial
: The same as the binomial occurs with multionmial. For some category $X$,

  $$
  P(X=x) = \text{Poisson}(s; \lambda p_x)
  $$

  All categories are independent from each other and distributed as $\text{Poisson}(x_i; \lambda_{x_i})$.