---
title: Coin Flip
---

To get started, consider a fair coin where the probability flipping a head is equal to the probability of flipping a tail.

## Consecutive Heads
The probability of getting $k$ heads consecutively can be solved by noting multiplication rule on independent flips

$$
P(H \land H) = P(H_1)P(H_2 \mid H_1) = P(H_1)P(H_2) = P(H)^2\\
\boxed{P(\text{k heads}) = P(H)^k =  \left( \frac{1}{2} \right)^k}
$$

## $k$ Heads from $n$ Flips
The probability of getting $k$ heads with $n$ flips immediately becomes more difficult than consecutive heads.

We implore the strategy of counting all possible outcomes of a given event (size of the outcome space). The size of $k$ heads is the combination $C(n,k)$

$$
|\text{k heads}| = C(n,k) = \frac{n!}{k!(n-k)!}
$$

The size of the outcome of all possible flips is given by the binary representation,

$$
|\text{all flips}| = 2^n
$$

Thus, the probability of $k$ heads from $n$ flips is,

$$
\boxed{P(\text{k heads}) = \frac{|\text{k heads}|}{|\text{all flips}|} = \frac{n!}{k!(n-k)! 2^n}}
$$

### Half Heads Case

Consider the case where $k = n/2$. To make the math easier let $n$ be the number of heads and $2n$ be the number of flips:

$$
\begin{align}
k &\rightarrow n\\
n &\rightarrow 2n
\end{align}
$$

The probabilty function is then,

$$
P(\text{k heads}) = \frac{(2n)!}{n!n! 2^n}
$$

Still, the probability function is non-intuitive. This event is very intersting when you apply the **Stirling's approximation** which states,

$$
n! \sim \sqrt{2 \pi n} (n/e)^n
$$

Therefore,

$$
P(\text{k heads}) = \frac{\sqrt{4\pi n}(2n/e)^{2n}}{\sqrt{4\pi^2n^2}(n/e)^n 2^n} = \frac{1}{\sqrt{\pi n}}
$$

We can now see that $n \rightarrow \infty$ (large $n$ is where Stirling's approximation gets more accurate),

$$
P(\text{k heads}) \rightarrow 0
$$