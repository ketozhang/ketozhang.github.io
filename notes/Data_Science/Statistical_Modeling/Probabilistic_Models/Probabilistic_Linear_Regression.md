---
title: Probabilistic Linear Regression
---
Linear regression on random variables (i.e., **probabilistic linear regression**) builds the foundation for linear regression on empirical data. Here on, take $Y$ and $X$ to be some random variable; for useful cases, these two random variables should not be independent.

The major difference between probabilistic and empirical linear regression other than nature of its variable is what we know about $X$ and $Y$. In probabilistic linear regression, one may have an insight on $X$ and/or $Y$. From here on, take the mean, SD, and correlation of $X, Y$ be $\mu_X,~ \mu_Y,~ \sigma_X,~ \sigma_Y,~ r(X,Y)$.

Because the best least squares predictor $\hat y(X) = E(Y \mid X)$ is rarely known, we'd like to model $E(Y \mid X)$. The linear regression model is any model in the form of,

$$
\hat y(X)  = g(X) ~ \theta
$$

* $X$: In general a random vector prepend with the intercept term $X_0=1$.

	$$X = \left[1, X_1, X_2, \ldots, X_p \right]$$
* $g(X)$: Some function/transformation of $X$. This function does not have to be linear.
* $\theta$: the parameter vector where $\theta_0$ is the intercept.

	$$
	\theta = \left[\theta_0, \theta_1, \ldots \theta_p \right]
	$$

## Linear Least Squares

The **linear least squares** or **ordinary least squares** (**OLS**) takes the linear model $\hat y(X)$ as,

$$
\hat y(X) = \theta_1 X + \theta_0
$$

The goal is to find the parameter $\theta$ to minimize the mean squared error (MSE),

$$
\min_\theta \text{MSE}(\hat y) = \min_\theta E\left[ (Y - \hat y(X))^2 \right]
$$

This problem is solvable by expanding the expectation resulting in the solution,

$$
\theta_1 = \frac{\text{Cov}(X, Y)}{\text{Var}(X, Y)} = r(X, Y) \frac{\sigma_Y}{\sigma_X}
$$

$$
\theta_0 = E(Y) - \theta_1 E(X)
$$

Therefore the best linear model $Y$ of $X$ is,

$$
\boxed{\hat y(X) = r(X, Y) \frac{\sigma_Y}{\sigma_X} X + \mu_Y - r(X, Y) \frac{\sigma_Y}{\sigma_X} \mu_X}
$$

### Standard Units

It is easier to work with standard units for the calculations above. Take $\theta^*$ to be the solution for th linear model $\hat y(X^*)$ with standard random variables $X^*, Y^*$,

$$
\hat y(X^*) = \theta X^*
$$

The best parameters are then,

$$
\theta_0 = 0
$$

$$
\theta_1 = r(X,Y)
$$

$$
\hat y(X^*) = r(X, Y) X
$$

You can check that $ \sigma_Y \hat y(X^*) + \mu_Y $ is indeed $\hat y(X)$.

::: Note
Notice that since $\hat y(X) = r(X,Y) X$,

$$
\hat y(X) \le X
$$

This is called the **regression effect**.
:::

::: Example
**Regression of Bivariate Normal**

The regression of the bivariate normal exactly follows the linear model. Recall that if $X^*$ and $Y^*$ is standard bivariate normal random variables with correlation $\rho$. Then we can write $Y^*$ as a function of two independent standard normal random variables $X^*$ and $Z$.

$$
Y^* = \rho X^* + \sqrt{1-\rho^2}Z,
$$

We can solve for the linear least squares parameters directly or, more quickly, you can just take the conditional expectation,

$$
\begin{align*}
\hat y(X^*) &= E(Y^* \mid X^*) \\
&= \rho X^*
\end{align*}
$$

You may check that $\theta_0 = 0$ and $\theta_1 = r(X, Y) = \rho$.

In general for all bivariate normal $X, Y$, we take the invert the standardized transformation,

$$
\begin{align}
E(Y \mid X) &= \sigma_Y E(Y^* \mid X^*) + \mu_Y \\
&= \sigma_Y \hat y(X^*) + \mu_Y \\
&= \sigma_Y \rho X^* + \mu_Y \\
&= \frac{\sigma_Y}{\sigma_X}\rho X + \mu_Y - \frac{\sigma_Y}{\sigma_X}\rho\mu_X
\end{align}
$$

Although it's the best predictor, that doesn't mean it's a good prediction. The prediction error (MSE) in standard units is given by,

$$
\text{Var}(Y^* \mid X^*) = 1-\rho^2
$$

It's not a surprise that the prediction error is depends on the correlation. At worst case, $\rho=0$ so the error is at maximum.
:::
