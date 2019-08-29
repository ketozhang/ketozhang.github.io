---
title: Principle Component Analysis
---

**Principle Component Analysis (PCA)** reduces the dimension by projecting onto another subspace that captures as much variation of the data as possible.

## Gaussian Components

Given cenetered data $X$, the covariance matrix is given by

$$
\hat \Sigma = \frac{1}{n}X^\top X
$$

Project $X$ onto the principle coordinates of dimension $k$ which are the eigenvectors $v_1 \ldots v_k$ associated with a set of the largest eigenvalues $\lambda_1 \ldots \lambda_k$

## Variability Accounted

The percentage of variability accounted for is given by the proportion of the sum of the eigenvalues accounted for.

$$
\frac{\sum_i^k \lambda_i}{\sum_i^d \lambda_i}
$$

## General PCA

In general, a gaussian fit to the data is not needed. The goal of PCA once again is to find the direction of projection that maximizes variance. This can be written as a maximization problem:

$$
\begin{align}
\text{Var}(X_1', \ldots X_n') &= \frac{1}{n}\sum_{i=1}^n \left(X_i \frac{w}{|w|}\right)^2\\
&= \underbrace{\frac{1}{n}\frac{w^\top X^\top X w}{w^\top w}}_\text{Rayleigh Quotient}
\end{align}
$$

The identity is the Raleigh quotient of $X^\top X$ and $w$. Therefore if $w$ is an eigenvector $v_i$ then the Rayleigh quotient is $\lambda_i$.

Restricting $w$ to be an eigenvector $v_d$ maximizes the variance to $\lambda_d / n$

Not restricting $w$ to be an eigenvector, because $w$ is a linear combination of the eigenvectors $v$, the Raleyigh quotient is a linear combination of the eigenvalues.

## Deriving PCA Using Projection Error

The sum of squared error is the projection error of PCA. We want to minimize the projection error.

$$
\min \sum_{i=1}^n \left | X_i - X_i' \right |^2 = \sum|X_i|^2 - \underbrace{\sum\left(X_i \cdot \frac{w}{|w|}\right)^2}_\text{Variance}
$$

## Eigenfaces

Given $X$ containing $n$ faces of $d$ grayscale pixels each, find the nearest neighbor to the training set. This is a slow process of $\Theta(nd)$. PCA can reduce this dimension by projection $d$ to $d'$.

## Random Projections

An alternative to PCA as a preprocess. Choosing a small $\epsilon$ and $\delta$ create a random subspace $S \in \mathbb R^d$ of dimension $k$ where

$$
k = \frac{2 \log \delta}{\epsilon^3 / 3 - \epsilon^2 / 2}
$$

For any point $q$, let $\hat q$ be the orthogonal projection of $q$ onto $S$  multiplied by $\sqrt{d/k}$.

For any two points $q$, $w \in \mathbb R^{d}$

$$
(1-\epsilon)|qw|^2 \le |\overline{\hat q \hat w}|^2 \le (1+\epsilon)|\overline{qw}|^2
$$

with probability $\mathbb P \ge 1 - 2\delta$

The typical hyperparameters are:

$$
\varepsilon \in [0.02, 0.5]\\
\delta \in [1/n^3, 0.05]
$$