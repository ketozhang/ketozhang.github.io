---
title: Poisson Distribution
---

The Poisson distribution describes the process where $k$ events occur at a unit interval given that the average number of events per unit interval is $\lambda$.

$$
P(X=k) = e^{-\lambda} \frac{\lambda^k}{k!}
$$

Expected Value
: $$\mathbb E[X] = \lambda$$

Variance
: $$\text{Var}[X] = \lambda$$

Sums of IID Poisson
: $$\sum{X_i} \sim \text{Poisson}\left(\textstyle\sum \lambda_i\right)$$

Mode
: The mode of the Poisson is the integer part of $\lambda$ only if $\lambda$ is not an integer,

$$
\text{mode}[\text{Poisson}(\lambda)] = \begin{cases}\lfloor \lambda \rfloor ~\text{and}~ \lceil \lambda \rceil, & \lambda \in \mathbb Z^+ \cup \set{0}\\ \lfloor \lambda \rfloor, & \text{otherwise.} \end{cases}
$$

MGF
:   $$
	M_X(t) = \exp\left[\lambda(e^{t} - 1)\right]
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

## Binomial
Let $S \sim \text{Binomial}(N, p)$. The marginal distribution on $N$ shows that

  $$
  \boxed{S \sim \text{Binomial}(N, p) = \text{Poisson}(\lambda p)}
  $$

Independence of Success and Failures
:   If the number of success is $S=s$ and number of failures is $F=f$ then $N = s + f$ then,

    $$
    \begin{gather*}
    P(S=s, F=f) = P(S=s)P(F=f)\\
    S \sim \text{Poisson}(\lambda p) \quad F \sim \text{Poisson}(\lambda q)
    \end{gather*}
    $$

    ::: Proof
    $$
    \begin{align*}
    P(S=s, F=f) &= P(N=s+f, S=s) \\
    &= P(N=s+f) P(S=s \mid N=s+f) \\
    &=e^{-\lambda}\frac{\lambda^{s+f}}{(s+f)!} \frac{(s+f)!}{s!f!}p^sq^f\\
    &= \left[e^{-\lambda p} \frac{(\lambda p)^s}{s!}\right] \left[e^{-\lambda q} \frac{(\lambda q)^f}{f!}\right]
    \end{align*}
    $$
    :::

  This suggest $S$ and $F$ are independent!

## Multinomial
The same as the binomial occurs with multionmial. For some category $X$,

  $$
  P(X=x) = \text{Poisson}(s; \lambda p_x)
  $$

  All categories are independent from each other and distributed as $\text{Poisson}(x_i; \lambda_{x_i})$.

## Poisson Process

The poisson distribution describes a process called the **Poisson process** which describe the chance that $k$ events occur if the rate of occurance is on average $\lambda$ (a measure of number of events per unit time). However, this description does not seem complete. Let me motivate this confusion. Doesn't it make more sense to ask what's the chance that $k$ events occur in the next $t$ seconds. It is indeed a more natural question to ask.

### First Description - Number of Arrivals
The answer to that natural question is called the **first description** of the Poisson process.

Consider a unit interval such that:

* the number of events or arrivals $N_0$ in the unit interval has expectation $E(N_0) = \lambda$.
* The unit interval can be divided into $n$ subintervals.
* For each subinterval the indicator of arrival is given by $I_1, I_2, \ldots, I_n$ which are Bernoulli($p$) trials
* $p \to 0$ as $n \to \infty$ such that $np \to \lambda$.

Given the assumption it must be that $N_0$ is distributed as $\text{Binomial}(n, p)$ with expectation $E(N_0) = np = \lambda$. As $n \to \infty$, the Poisson limit of the Binomial applies:

$$
N_0 \sim \text{Poisson}(\lambda)
$$

Now consider an interval of size $t$ (e.g., most commonly the interval $(0, t)$). It is made up of $t$ disjoint unit interval.

We make the assumption that disjoint interval are independent of each other (this is indeed the assumption made by the poisson distribution). The number of events $N$ is then the sum of events in $t$ unit intervals. Thus, $N$ is distributed as if there are $t$ IID $\text{Poisson}(\lambda)$ denoted. By the sum of independent Poisson distribution,

$$
N \sim \text{Poisson}(\lambda t)
$$

### Second Description - Inter-Arrival Waiting Time

Let $G_k$ be the inter-arrival time that is the length of the time interval between $T_k$ and $T_{k-1}$, where $T_i$ is the time of the $i$th arrival

$$
G_k = T_k - T_{k-1}
$$

Exponential
: 	$G_k$ is has the exponential distribution since,

	$$
	P(G_1 > t) = P(N_{(0, t)} = 0) = e^{\lambda t}
	$$

	This is the survival function of the exponential distribution. The same can be shown for all $k$ since $N_{(T_{k-1}, T_{k})}$ are disjoint.

Memoryless property
: Because each time interval is disjoint $G_k$ is mutually independent of each other $k$ for all $k$.