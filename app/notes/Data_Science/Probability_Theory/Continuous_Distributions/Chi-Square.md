---
title: Chi-Square Distribution
---

The chi-square distribution is given by,

$$
\frac{\frac{1}{2}^{n/2}}{\Gamma(n/2)} x^{\frac{n}{2} - 1}e^{- \frac{1}{2}x}
$$

## Member of the Gamma Distribution

The chi-square distribution is a member of the gamma distribution,

$$
\chi^n_k = \text{gamma}(n/2, 1/2)
$$

## Relation to Normal Distribution
The $\chi^2_n$ distribution with $n$ degrees of freedom is the sum of squares of $n$ iid standard normal random variables $Z_1, Z_2, \ldots, Z_n$,

$$
\chi^2_n = \sum_k^n Z_k^2
$$


Motivating Example - The Squared Standard Normal
: Consider the standard normal random variable $Z$. We can determined its PDF $X=Z^2$ by properties of two-to-one function transformation $g(x)$:

    $$
    \begin{gather*}
    g(x) = z^2\\
    g'(x) = 2z
    \end{gather*}
    $$

    $$
    \begin{align*}
    f_X &= \frac{f_Z(\sqrt{x})}{g'(\sqrt{x})} + \frac{f_Z(-\sqrt{x})}{\abs{g'(-\sqrt{x})}}\\
    &= \frac{1}{\sqrt{2\pi^2}}\left[\frac{e^{-\frac{1}{2}x}}{2\sqrt{x}} + \frac{e^{-\frac{1}{2}x}}{2\sqrt{x}}\right]\\
    &= \frac{1}{\sqrt{2\pi^2}}x^{-\frac{1}{2}}e^{-\frac{1}{2}x}\\
    f_X &= \frac{\tfrac{1}{2}^\tfrac{1}{2}}{\pi}x^{\frac{1}{2}-1}e^{-\frac{1}{2}x}
    \end{align*}
    $$

    We now see that $Z^2 = \chi_1^2$ the squared standard normal is the chi-square with one degree of freedom.

## Unbiased Estimator of SD with Known Mean
Given iid $\text{Normal}(\mu, \sigma^2)$ random variables $X_1, X_2, \ldots, X_n$, the unbiased estimator of $\sigma$ is,

$$
\begin{gather*}
    Y = \frac{\sigma^2}{n}\sum_{i=1}^n\\
    E(Y) = \sigma^2
\end{gather*}
$$