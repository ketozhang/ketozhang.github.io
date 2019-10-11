---
title: Variance
---

The variance is motivated by wanting to know how far away is $\mathbb E[X] = \mu$ away from some true answer in the random variable $X$. That is, its the expected value of the squared deviance of $\mu$ or the **root mean square** of $X$. The variance is defined as,

$$\text{Var}[X] = \mathbb E\left[ (X-\mu)^2 \right]$$

Non-negative
: The variance is alway non-negative because the random variable inside is a squared variable

    $$
    \text{Var}[X] \ge 0
    $$

Identity
: A more useful identity derived by expanding the square,

    $$
    \text{Var}[X] = \mathbb E[X^2] - \mathbb E[X]^2
    $$

Second Moment $\ge$ First Moment
: In corollary, the squared expected value is always greater or equal to the expected value squared,

    $$
    \mathbb E[X^2] \ge \mathbb E[X]^2
    $$

Standard Deviation
: Because the variance is some squared quantity, we'd like to take the square root to get a sense of the untis

    $$
    \text{SD}[X] = \sqrt{\text{Var}[X]}
    $$


Linearity
: Like the expected value, the variance has its own linearity rule. The variance is invariant by translation and linear by sretching

    $$
    \text{Var}(aX + b) = \abs{a}\text{Var}[X]
    $$

    This is the same exact property as the magnitude of a vector.


Variance of Sums Random Variables
:   $$
    \text{Var}\left[\sum X_i\right] = \sum \text{Var}[X_i] + \sum_{i \neq j} \text{Cov}[X_i,X_j]
    $$

    If all random variable are independent:

    $$\text{Var}\left[\sum X_i\right] = \sum \text{Var}[X_i] $$

## Method of Indiciators
The variance of indicators are nice to use because,

$$
\mathbb E[I^2] = \mathbb E[I]
$$

Therefore we can easily solve for the variance of an indicator,

$$
\text{Var}[I] = \mathbb E[I] - \mathbb E[I]^2 = p(1-p)
$$

## Mean Squared Error

The variance is related to the mean squared error if we replace the prediciton $\mu$ with some arbritrary constant $c$,

$$
\text{MSE}(c) = \mathbb E[(X-c)^2]
$$

By expanding $\mathbb E[(X-\mu+\mu-c)^2]$ out we get,

$$
\boxed{\text{MSE}(c) = \text{Var}[X] + (\mu-c)^2}
$$

Therefore any prediction $c$ is no better than $\mu$ and the MSE is at least the variance,

$$
\text{MSE}(c) \ge \sigma_X^2
$$

## Covariance

### Properties

* Positive covariance:

    $$
    \text{Cov}[X,Y] > 0 \implies \abs{X - E[X]} > 0 \land \abs{Y - E[Y]} > 0
    $$

* Negative covariance:

    $$
    \text{Cov}[X,Y] > 0 \implies \Big( \abs{X - E[X]} > 0 \land \abs{Y - E[Y]} < 0 \Big) \lor \Big(\abs{X - E[X]} < 0 \land \abs{Y - E[Y]} > 0 \Big)
    $$

* Bilinearity:

    $$
    \text{Cov}[\boldsymbol{a \cdot X}, \boldsymbol{b \cdot Y}] = \sum_{i}\sum_{j}a_ib_j \text{Cov}[X_i,X_j]
    $$

## Correlation

### Properties

* **Standardized Random Variables**
    With standardized random variables $X'$ and $Y'$:

    $$ X' = \frac{X - \mathbb E[X]}{\sigma(X)} $$
    $$ Y' = \frac{Y - \mathbb E[Y]}{\sigma(Y)} $$

    $$ \text{Corr}[X,Y] = E[X'Y']  $$

* **Unity Bound**

    $$ -1 \le \text{Corr}[X,Y] \le 1 $$

    Proof
    : Consider the standardize random variable $X'$ and $Y'$. By the Cauchy-Schwarz Inequality

    $$ \abs{\mathbb E[X'Y']} \le \abs{\mathbb E[X'] \mathbb E[Y']} = 1$$

    Thus,

    $$ -1 \le \text{Corr}[X,Y] \le 1  $$

* **Perfectly Correlated or Anticorrelated**

$$ \text{Corr}[X,Y] = 1 \implies X = Y $$
$$ \text{Corr}[X,Y] = -1 \implies X = -Y$$
