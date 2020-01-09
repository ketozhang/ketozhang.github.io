---
title: Gamma Distribution
---

The gamma distribution is given by,

$$
f_X(x; \lambda, r) = \frac{\lambda^r}{\Gamma(r)}x^{r-1}e^{-\lambda x}, \quad \text{for } x \ge 0
$$

Where $\Gamma(r)$ is the gamma function given by,

$$
\Gamma(r) = \int_0^\infty x^{r-1}e^{-x} ~dx
$$

Expectation
: The expected value is given by,
    $$
    E(X) = \frac{r}{\lambda}
    $$

Variance
: The variance is given by,

    $$
    \text{SD}(X) = \frac{\sqrt{r}}{\lambda}
    $$

Sums
: The sum of iid gamma distributions have the distribution

    * For fixed rate $\lambda$

        $$
        \sum_k^n X_k \sim \text{gamma}\left(\sum_k^n r_k, \lambda \right)
        $$

MGF
:   $$
    M_X(t) = \left( \frac{\lambda}{\lambda-t} \right)^r, \quad \text{for } t < \lambda
    $$

## Rate Parameter
The rate parameter $\lambda$ is the scale parameter of the distribution

## Shape Parameter
The parameter $r$ is known as the shape parameter of the distribution.

* $r=1$ gives the exponential distribution
* $r \to \infty$ gives the normal distribution

## Gamma Function

The gamma function,

$$
\Gamma(r) = \int_0^\infty x^{r-1}e^{-x} ~dx
$$

has solutions that follow,

$$
\Gamma(r+1) = r\Gamma(r)
$$

Which implies two sets of solutions:

* For positive integer $r$,
    $$
    \Gamma(r) = (r-1)!
    $$
* For non-integers,
    * For rationals of $\frac{1}{2} + r$ for $r \ge 0$
        $$
        \Gamma\left(\frac{1}{2} + r\right) =
        \begin{cases}
        \dfrac{1}{\sqrt{\pi}}\\
        \prod_\limits{k=1}^{r} \left(\frac{1}{2} + k - 1\right)\dfrac{1}{\sqrt{\pi}}
        \end{cases}
        $$