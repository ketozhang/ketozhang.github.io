---
title: Posterior Estimator
---

With an assumption of the likelihood function (i.e., the distribution of the data), we can determine the distribution of the parameters which is the posterior distribution. Using Bayes rule we find that,

$$
P(\theta \mid X) = \frac{P(X \mid \theta) P(\theta)}{P(X)}
$$

* $ P(X \mid \theta) $ : the likelihood function
* $ P(X) $ : the normalization distribution called the evidence.

## Expectation of Posterior
If there must be one value instead of a distribution, the expectation is one natural choice

## Maximum a Posterior
If there must be one value, then the mode or **maximum a posteriori** (**MAP**) is a another natural choice.

## Bayesian Update

## Motivating Example

Consider a coin where we do not know the chance of heads $p$. Let's take the prior that $p$ is uniformally any value between 0 and 1. That is,

$$
p \sim \text{Uniform}(0, 1)
$$

The chance that the coin lands head depends on the value of $p$ which is random. We can marginalize over all possible values of $p$,

$$
P(H) = \int_0^1 P(H, p) ~dp = \int_0^1 P(H \mid p) f(p) ~dp
$$

In fact this looks like an expected value as a function of $p$,

$$
P(H) = E(P(H \mid p))
$$

The chance of head given $p$ is of course $p$ itself so,

$$
\boxed{P(H) = E(p) = \frac{1}{2}}
$$

This is not so surprising since $p$ is uniform, a large sample of $p$ would neither be advantageous to getting heads or tails.

However, what's the chance of getting two heads $P(HH)$ out of two tosses?

We know that $P(HH \mid p) = p^2$ therefore,

$$
\boxed{P(HH) = E(p^2) = \int_0^1 p^2 ~dp = \frac{1}{3}}
$$

The answer is **not** $1/4$ as we should expect. That must mean the two tosses of coins are not independent when $p$ is random. To see why we need to look at the conditional probability that the second coin lands head if we know the first one lands heads for a random $p$

$$
P(H_2 \mid H_1) = \frac{P(H_1, H_2)}{P(H_1)} = \frac{2}{3}
$$

Where did the $2/3$ come from? Let's take a look at what happens to the chance of $p$ given we know the first coin lands head. We would need to apply Bayes rule,

$$
f(p \mid H_1) = \frac{P(H_1 \mid p) f(p)}{P(H_1)} \propto p
$$

Normalizing we find that,

$$
f(p \mid H_1) = 2p
$$

Thus,

<!-- TODO: WHAT? -->
$$
P(H_2 \mid H_1) = \int_0^1 P(H_2 \mid p) \cdot f(p \mid H_1) ~dp = \frac{2}{3}
$$

## Beta and Binomial Update
We are interested in $n$ IID Bernoulli trials where we define the sum as $S = \sum{I_k}$.

The Bayesian update rule is,

$$(p \mid S=k) \sim \text{Beta}(r+k, s+n-k)$$

::: Proof
Let the prior for the parameter $p$ be distributed as,

$$
\begin{gather*}
p \sim \text{Beta}(r,s)\\
f(p) = C(r,s) \cdot p^{r-1}(1-p)^{s-1}
\end{gather*}
$$

the likelihood  for $S$ is then the binomial distribution,

$$
P(S=k \mid p) = {n \choose s} p^k (1-p)^{n-k}
$$

Hence, the posterior distribution is,

$$
f(p \mid S=k) = C(r+k, s+n-k) p^{r+k-1} (1-p)^{n+s-k-1}
$$

Thus, the Bayesian update adds the number of successes $k$ and the number of failures $n-k$.

$$
\boxed{(p \mid S=k) \sim \text{Beta}(r+k, s+n-k)}
$$
:::

Expectation
: $$E(p \mid S=k) = \frac{r+k}{r+s+n}$$

MAP
: $$\text{mode}(p \mid S=k) = \frac{r+k-1}{r+k+n-2}$$

Transition Rule
: $$ P(S_{n+1} = k+1 \mid S_n = k) = E(p \mid S_n=k) $$

Evidence
:	The chance of $k$ heads after $n$ tosses using the beta prior is the beta-binomial distribution.

	$$
	P(S_n = k) = {n \choose k}\frac{C(r,s)}{C(r+k, s+n-k)}
	$$
