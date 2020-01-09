---
title: Central Limit Theorem
---

The Central Limit Theorem (CLT) states that given a sum distribution $S_n$ as a sum of $n$ iid random variables $X$ of mean $\mu$ and standard deviation $\sigma$,

$$
\begin{gather*}
S_n = X_1 + X_2 + \ldots + X_n\\
E(X_n) = n\mu\\
\text{SD}(X_n) = \sqrt{n}\sigma
\end{gather*}
$$

As $n \to \infty$, $S_n$ approaches normal distribution.

$$
S_n \to \text{Normal}(N\mu, N\sigma^2)
$$

Concentration Corollary
: Since the distribution of the sum tends to normal at large $N$, its CDF as well,

	$$
	\begin{gather*}
	P(S_n \le s) \approx \Phi\left(\frac{s-N\mu}{\sqrt{N}\sigma}\right)
	\end{gather*}
	$$

	More used is the central bulk concentration,

	$$
	\begin{align*}
	P(\abs{S_n - N\mu} \le c) &= P(S_n \le N\mu + c) - P(S_n \le N\mu - c)\\
	&\approx \Phi\left(\frac{c}{\sqrt{N}\sigma}\right) - \Phi\left(\frac{c-2N\mu}{\sqrt{N}\sigma}\right)
	\end{align*}
	$$