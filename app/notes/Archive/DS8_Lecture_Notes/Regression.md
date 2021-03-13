---
title: Regression
---

$$
\begin{gather}
r = \text{Corr}[x', y'] = \mathbb E[x'y']\\
m = r \cdot \frac{\text{SD}[y]}{\text{SD}[x]}\\
b = \mathbb E[y'] - m \cdot \mathbb E[x']
\end{gather}
$$

## Residuals

Residuals from a linear regression always have:
* Zero mean
* Zero correlation with $x'$
* Zero correlation with $\hat y'$

Fitted values $\hat y$ from a linear regression always have:
* 1 correlation with $\hat y$
* Related to the correlation and variance of $y$ by:

    $$
    \text{Var}[\hat y] = r^2 \cdot \text{Var}[y]
    $$

### Variance Decomposition

$$
\text{Var}[y] = \text{Var}[\hat y] + \text{Var}[\epsilon]
$$