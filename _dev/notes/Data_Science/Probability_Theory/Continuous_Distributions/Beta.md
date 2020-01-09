---
title: Beta Distribution
---

The Beta density function is given as,

$$
\text{Beta}(r,s)
$$

$$
f(x; r, s) = \frac{(r+s-1)!}{(r-1)!(s-1)!}x^{r-1}(1-x)^{s-1} \quad \text{for } r > 0, s > 0
$$

It is a important density function because many other density function are a version of the beta function. These density functions are said to be in the Beta family (e.g., Uniform).

## Uniform Ordered Statistics

Consider a number line of $[0,1]$. At uniformly random we select $n$ values from the number line. Let $U_{(k)}$ be the random variable for the value of $k$th lowest value on the number line. In otherwords, $U_{(k)}$ is the $k$th value in the number line when each of the $n$ values are ordered.

It is found that $U_{(k)}$ follows the beta distribution

$$
U_{(k)} \sim \text{Beta}(k, n-k+1)
$$

## Beta Integral

The beta integral is a type of integral in the form of,

$$
\int_0^1 x^{r-1}(1-x)^{s-1}~ dx= \frac{(r-1)!(s-1)!}{(r+s-1)!}
$$

This derives the normalization factor for the beta distribution.