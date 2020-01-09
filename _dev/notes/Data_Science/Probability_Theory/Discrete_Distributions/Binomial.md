---
title: Binomial
---

The binomial distribution is given as,

$$ P(X=k; p,n) = {n \choose k} p^k(1-p)^k $$

Expected Value
: $$ \mathbb E[X] = np $$

Variance
:   $$
    \text{Var}(X) = npq
    $$

Moment Generating Function
: The product of $n$ Bernoulli MGF,
    $$
    M_X(t) = (q+pe^t)^n
    $$

## Relations to Bernoulli Trials

The bernoulli distribution is the indicator decomposition of the Binomial distribution by letting $X$ be the binomial random variable that is the number of times the bernoulli trial succeeds:

$$
I_k \sim \text{Bernoulli}(p)\\
X = \sum_{k=1}^n I_k
$$

## Poisson Limit

The poisson distribution can be derived by the limit of the binomial distribution as $np$ tends to some constant $\lambda$. Let $np \rightarrow \lambda$ where $n \rightarrow \infty$ and $p \rightarrow 0$.

$$
\begin{gather*}
    p_k = P(X=k) = {n \choose k}p^k(1-p)^{n-k}\\
    p_0 \approx e^{-\lambda}\\
    \frac{p_k}{p_{k-1}} \approx \frac{\lambda}{k}\\
    p_k = p_0 \prod_{l=1}^k \frac{P_l}{P_{l-1}} \approx e^{-\lambda}\frac{\lambda^k}{k!}
\end{gather*}
$$

$$
X \sim \text{Poisson}(k; np)
$$

Hence you may interpret the Poisson distribution as the binomial distribution of a rare event in the limit of large number of trials.

Now there's another limit where $n \rightarrow \infty$ and $p \rightarrow 1$ such that $n(1-p) \rightarrow n-\lambda$. In this case, the proof is easier by solving "$q$ failures from $n$ trials",

$$
q_{l} := p_{k} \quad k + l = n\\
$$

$$
\begin{align*}
    q_l &= {n \choose l}q^l(1-q)^{n-l}\\
    &\approx e^{-(n-\lambda)}\frac{(n-\lambda)^l}{l!}
\end{align*}
$$

$$
p_k = e^{-(n-\lambda)}\frac{(n-\lambda)^{(n-k)}}{(n-k)!}
$$

$$
\boxed{P(X=k) \approx \text{Poisson}(n-k;nq)}
$$

## Normal Limit of the Binomial Distribution
Because the binomial distribution is $n$ IID Bernoulli trials of chance $p$, at large number of trials the central limit theorem applies such that distribution converges,

$$
X \to \text{Normal}(np,~ npq)
$$
