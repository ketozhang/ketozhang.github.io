---
title: Geometric Distribution
---

The probability of the first success given by $p$ to be at position $n$.

$$
\begin{gather*}
    X \sim \text{Geometric}(p)\\
    P (X = n) = (1-p)^{n-1}p
\end{gather*}
$$

* **Expected Value**

    $$ E[X] =\sum_{n=1}^\infty n (1-p)^{n-1}p = \frac{1}{p} $$


* **Variance**

    $$E[X^2] = \frac{1-p}{p^2} $$

    Proof
    : Use

        $$\frac{\mathrm d}{\mathrm d p}\left[(1-p)\frac{\mathrm d }{\mathrm d p}(1-p)^n\right] = n^2(1-p)^{n-1}$$

## Coupon Collection Problem

Let's say there are $n$ types of coupons and you need all $n$ to win a prize. To get a coupon you must buy some product.

1. What is the expected number of buys to get all $n$ coupons given uniform probability of getting any coupon.

    Let $X_i$ be the random variable of the number of buys to get a unique coupon. You need $n$ unique coupons so the number of buys to win a prize is the sum of $X_i$.

    $$
    \mathbb E[X_i] = \frac{1}{p_i} = \frac{n}{n-(i-1)}\\
    \mathbb E\left [\sum{X_i} \right] = n \sum_{k=1}^n \frac{1}{k}
    $$

## Expected Value (Proof)

The expected value of first success after $W$ can be done quickly by noticing

* There must be at least one trial.
* If the first trial succeeds (with probability $p$), $W=1$.
* If the first trial fails (with probability $q$), the remaining trials is also distributed equallty to $W$.


Let $W = 1 + R$ where $R$ is the random variable for the number of trials after the first. Let $W'$ be distributed equallty to $W$.

$$
W = 1 + R\\
$$

$$
\begin{align}
    \mathbb E[W] &= 1 + \mathbb E[R]\\
    &= 1 + q\mathbb E[W']\\
    &= 1 + q\mathbb E[W]\\
\end{align}
$$

$$
\mathbb E[W] = \frac{1}{q}
$$