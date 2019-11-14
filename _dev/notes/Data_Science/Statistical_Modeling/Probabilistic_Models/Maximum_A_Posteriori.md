## Uniform Prior

Using a uniform prior, the MAP becomes the MLE

::: Example
Suppose we want to find the chance of head $p$ of a possibly unfair coin. However we have no reason to expect the coin to be unfair as most coin tosses are fair-ish. We take the uniform prior.

$$
p  \sim \text{Uniform}(0,1)
$$

We perform $n$ trials with the coin and got $H=k$ heads. The likelihood is binomial. The posterior distribution is then,

$$
\begin{align*}
	P(p \mid H = k)  &= \frac{1 \cdot P(H=k \mid p)}{P(H=k)}\\
					 &\propto P(H=k \mid p) \\
	P(p \mid H = k)  &\propto p^{k}(1-p)^{n-k}
\end{align*}
$$

Since $p$ is a random variable the posterior distribution is,

$$
(p \mid H=k) \sim \text{Beta}(k+1, n-k+1)
$$

With expectation and MAP,

$$
E(p \mid H=k) = \frac{k+1}{n+2}
$$

$$
\text{mode} (p \mid H=k) = \frac{k}{n}
$$

At large $n$, these two are nearly equal. We have found that the observed propotion of heads is the MAP.
:::

## Disproportionate Prior

Suppose you want to determine the chance of an event $p$. If you believe the event is disproportionate, that is, you believe on average there is $x$ events out of $n$.

$$
E(p) = \frac{x}{n}
$$

In general the proposed $E(p)$ does not have to be a rational number.

$$
p \sim \text{Beta}(x, n-x)
$$

::: Example
Using the unfair coin example above, suppose in life, we have experience a lot of cheating so we think that the coin is unfair. Our prior knowledge motivates us to propose the coin lands head at chance $70\%$,

$$
E(p) = \frac{7}{10}
$$

We take the prior distribution to be $p \sim \text{Beta}(7, 3)$.
:::