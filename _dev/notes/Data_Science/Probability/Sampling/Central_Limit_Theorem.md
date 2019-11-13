---
title: Central Limit Theorem
---

The Central Limit Theorem (CLT) states that given a sum distribution $S_N$ as a sum of $n$ iid random variables $X$ of mean $\mu$ and standard deviation $\sigma$,

$$
\begin{gather*}
S_N = X_1 + X_2 + \ldots + X_N\\
E(X_N) = N\mu\\
\text{SD}(X_N) = \sqrt{N}\sigma
\end{gather*}
$$

As $n \to \infty$, $S_N$ approaches normal distribution.

$$
S_N \to \text{Normal}(N\mu, N\sigma^2)
$$

Concentration Corollary
: Since the distribution of the sum tends to normal at large $N$, its CDF as well,

	$$
	\begin{gather*}
	P(S_N \le s) \approx \Phi\left(\frac{s-N\mu}{\sqrt{N}\sigma}\right)
	\end{gather*}
	$$

	More used is the central bulk concentration,

	$$
	\begin{align*}
	P(\abs{S_N - N\mu} \le c) &= P(S_N \le N\mu + c) - P(S_N \le N\mu - c)\\
	&\approx \Phi\left(\frac{c}{\sqrt{N}\sigma}\right) - \Phi\left(\frac{c-2N\mu}{\sqrt{N}\sigma}\right)
	\end{align*}
	$$