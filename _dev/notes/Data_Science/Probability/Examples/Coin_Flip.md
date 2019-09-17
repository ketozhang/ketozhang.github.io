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
|\text{k heads}| = {n \choose k}
$$

The number of possible sequences can be thought of as coutning unordered without replacement where each of the $n$ flips have 2 choices,

$$
|\text{all flips}| = 2^n
$$

Thus, the probability of $k$ heads from $n$ flips is,

$$
\boxed{P(\text{k heads}) = \frac{|\text{k heads}|}{|\text{all flips}|} = {n \choose k} / 2^n}
$$

### Probabilistic Proof

An alternative proof is to use probability instead of combinatorics. We rely on the fact that of the $n$ tosses, any $k$ set of tosses have an equally likely chance to land all heads thus we can apply the additive rule.

1. The $k$ slots that the head can land on is,

    $$
    |\text{$k$ slots}| = {n \choose k}
    $$

2. Among the $k$ slots, the probability of having $k$ heads is,

    $$
    P(\text{$k$ heads in $k$ slots}) = 2^{-k}
    $$

3. The remaining tosses must be tail,

    $$
    P(\text{$n-k$ tails}) = 2^{-(n-k)}
    $$

Thus,

$$
\begin{align}
P(\text{$k$ heads}) &= |\text{$k$ slots}| \cdot P(\text{$k$ heads in $k$ slots}) \cdot P(\text{$n-k$ tails})\\
&= {n \choose k} / 2^n
\end{align}
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