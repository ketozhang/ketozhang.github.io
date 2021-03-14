---
title: Adaptive Boosting
---

**Adaptive boosting** or **AdaBoost** is an ensemble method that:

* trains multiple leanrers on weighted sample points
* use different weight for each learner
* incraese weight of misclassified sample  points
* give bigger votes to more accurate learners

Let's take the binary classification example $y$ with design matrix $X$.

* Train $T$ classifiers $G_1, \ldots, G_T$
* The weight for sample point $X_i$ in $G_t$ grows according to how $G_1, \ldots G_{t-1}$ misclassified it and shrinks on correct classification.
* Train $G_t$ to try harder to correctly classify points with larger weights.
* The metalearner is a linear combination of the ensemble.

    $$
    M(z) = \sum_{t=1}^T \beta_t G_t(z)
    $$

## Algorithm

On each iteration $t$:

1. Initialize weights $w_i = \frac{1}{n}$

2. Find $G_t$ that minimizes the metalearner:
    $$
    L(\rho, \ell) = e^{-\rho \ell} \qquad \ell \in \{-1, 1\}
    $$

    $$
    \begin{align*}
    \mathcal L &= \frac{1}{n}\sum_{n=1}^n L(M(X_i), y_i), \qquad M(X_i)=\sum_{t=1}^T \beta_t G_t (X_i)\\
    &= \sum{w_i^{(T)}}e^{-\beta_Ty_iG_T(X_i)}
    \end{align*}
    $$

    $$
    w_i^{(T)} = \prod_{t=1}^{T-1}\exp\left[-\beta_ty_iG_t(X_i)\right]
    $$

    $$
    \mathcal L  = e^{-\beta_T}\sum_{i=1}^n w_i^{(T)} + (e^{\beta_T} - e^{-\beta_T})\underbrace{\sum_{y_i \neq G_T(X_i)}w_i^{T}}_\text{sum of misclassified weights}
    $$

    $$
    w_i^{(T+1)} = w_i^{(T)}e^{-\beta_Ty_iG_T(X_i)}
    $$

3. Find $\beta_t$ that minimizes the metalearner:

    $$
    \frac{\partial}{\partial \beta_T}\mathcal L = -e^{-\beta_T}\sum_{i=1}^{n}w_i^{(T)}+\left(e^{\beta_T}+e^{-\beta_T} \right)\sum_{y_i \neq G_T(X_i)}w_i^{(T)}
    $$

    $$
    0 = -1 + (e^{2\beta_T} + 1)\text{err}_T, \qquad \text{err}_T
    = \frac{\text{weight wrong}}{\text{all weight}}
    $$

    $$
    \beta_T = \frac{1}{2}\log\left(\frac{1-\text{err}_T}{\text{err}_T}\right)
    $$

3. Reweight points $w_i = w_i e^{\beta_t y_i G_t(i)}$

## Facts and Heuristics

* Best for short tree (depth ~3-5) ensembles.

* Posterior probability can be approximated via:

    $$
    P(Y \mid x) \approx \frac{1}{1 + e^{-2M(x)}}
    $$

* If every learner has $s \ge \mu \ge 50$ accuracy score, the metalearner training accuracy will be 100%.