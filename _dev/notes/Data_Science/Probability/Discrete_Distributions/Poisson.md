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

MGF
:   $$
	M_X(t) = \exp\left[\mu(e^{t} - 1)\right]
	$$

	::: Proof
	Directly taking the expectation and noticing that it's the exponential taylor series,

	$$
	\begin{align*}
		M_X(t)	&= \sum_{k=0}^\infty e^{kt} \frac{e^{-\lambda}\lambda^k}{k!}\\
				&= e^{-\lambda}\sum_{k=0}^\infty \frac{e^{kt}\lambda^k}{k!} \\
				&= e^{-\lambda}\sum_{k=0}^\infty \frac{(\lambda e^t)^k}{k!} \\
				&= e^{-\lambda}e^{\lambda e^t} \\
		M_X(t)	&= e^{\lambda (e^t - 1)}
	\end{align*}
	$$
	:::

## Poissonization

Poissonization is the process of letting the number of trials $N \sim \text{Poisson}(\lambda)$. Doing so causes some families of distribution to inherit independence amongst their category. To get a better idea of what this mean let's take a look at few distributions

Binomial
: Let $S \sim \text{Binomial}(s; N, p)$. Because $N$ is a random variable we can calculate for a all $N$ (i.e., the marginal distribution of $S$) or the joint distribution of $N$ and $P$,

  $$
  \boxed{S \sim \text{Poisson}(s; \lambda p)}
  $$

  $$
  P(S=s, N=n): \text{Poisson}(s; \lambda p) \text{Poisson}(n-s; \lambda p)
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

## Poisson Process

The poisson distribution describes a process called the **Poisson process** which describe the chance that $k$ events occur if the rate of occurance is on average $\mu$ (a measure of number of events per unit time). However, this description does not seem complete. Let me motivate this confusion. Doesn't it make more sense to ask what's the chance that $k$ events occur in the next $t$ seconds. It is indeed a more natural question to ask.

### First Description - Number of Arrivals
The answer to that natural question is called the **first description** of the Poisson process.

Consider a unit interval such that:

* the number of events or arrivals $N_0$ in the unit interval has expectatation $E(N_0) = \mu$.
* The unit interval can be divided into $n$ subintervals.
* For each subinterval the indicator of arrival is given by $I_1, I_2, \ldots, I_n$ which are Bernoulli($p$) trials
* $p \to 0$ as $n \to \infty$ such that $np \to \mu$.

Given the assumption it must be that $N_0$ is distributed as $\text{Binomial}(n, p)$ with expectation $E(N_0) = np = \mu$. As $n \to \infty$,

$$
N_0 \sim \text{Poisson}(\mu)
$$

Now consider an interval of size $t$ (e.g., most commonly the interval $(0, t)$). It is made up of $t$ disjoint interval.

We make the assumption that disjoint interval are independent of each other (this is indeed the assumption made by the poisson distribution). The number of events $N$ is then the sum of events in $t$ unit intervals. Thus, $N$ is distributed as if there are $t$ IID $\text{Poisson}(\mu)$ denoted. By the sum of independent Poisson distribution,

$$
N \sim \text{Poisson}(\mu t)
$$

### Second Description - Waiting Time
<!-- TODO -->