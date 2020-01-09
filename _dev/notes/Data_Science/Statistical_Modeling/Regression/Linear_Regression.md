---
title: Linear Regression
---

Consider a dataset as a matrix of $X \in \mathbb{R}^{n\times d+1}$ where we've extracted $n$ numbers of data records/rows and $d$ numbers of feature columns along with one extra column for the intercept. For each row, we have a measurement or response $y \in \mathbb R^{n \times 1}$

$$ \hat y = f(X) \theta $$

* $\hat y$ : Length $n$ vector of dependent values
* $X$ : The feature matrix of dimension $d+1$ where $d$ is the number of features.
* $f(X)$ : Optional function applied to the feature matrix. This is sometimes referred to as the design matrix otherwise $X$ is sometimes also called the design matrix.

## Motivation of Linear Regression Through Probability
Whenever you see the statement of the confidence interval and/or the p-value, it comes from probability theory. The foundation of applying linear regression to empirical data comes from the theory of linear regression applied to random variables. That must mean there is an underlying assumption of probability in our data. (See [Probabilistic Linear Regression](../Probabilistic_Models/Probabilistic_Linear_Regression)).

The most common assumption is can be stated as the empirical data we've taken comprise of signal (the truth value) and random noise (the error). Once again, the randomness is in its error (this error may be natural or artificial/empirical error). We look at the world and measure $y$ knowing that it's not always truth but instead,

$$
y = y^* + \varepsilon
$$

where $y^*$ is the truth and $\varepsilon$ is a random variable representing the error.

Therefore, **the underlying assumption of our world is that the data contains randomness and that randomness is in its error**.

## The Assumption of Error

The most common assumption for the error is:

* a random vector
* distributed as $\text{Normal}(\vec 0, \sigma^2)$ where $\sigma^2 = (\sigma_1^2, \sigma_2^2, \ldots, \sigma_n^2)$

That is to say the error for every measurement is normally distributed (aka gaussian white noise), independent from each other.

## Ordinary Least Squares

The **linear least squares** or **ordinary least squares** (**OLS**) is a linear regression model that takes $f(X) = X$, the lost function as $\mathbb L_2$ (aka the squared deviance) and the cost function as the mean squared error (aka mean of $\mathbb L_2$ for all rows of $X$). The linear model is given by,

$$
\hat y(X) = X \theta
$$

The optimization problem is then given by,

$$
\begin{align}
\hat \theta &= \mathop{\arg\min}_{\hat \theta} \frac{1}{n} \sum_{i=1}^n \left[y_i - X_i^\top\hat \theta\right]^2\\
&= \mathop{\arg\min}_{\hat \theta} \frac{1}{n} |y-X\hat \theta|^2
\end{align}
$$

Solving for best parameters $\hat \theta$, in general, gives the equation

$$
X^TX \hat \theta = X^T y
$$

Therefore we see two types of solution dependent on $X$:

* $X^\top X$ is invertible with a simple solution.
* $X^\top X$ is not invertible that are not all solvable.

### Invertible Solutions
Given the square of the feature matrix $X^\top X$ is invertible then the solution  is what's known as the **normal equation**,

$$
\hat \theta = (X^\top X)^{-1}X^\top y
$$

::: Note
$(X^\top X)^{-1}X^\top$ : This is called the **pseudoinverse** of $X$ often notated as $X^+$. Notice that,

$$ X^+X = I $$

Hence $X^+$ is also known as the **left inverse**

Additionally also observe that,

$$ \hat y = X\hat \theta = XX^+ y $$

Where $XX^+$ is called the **hat matrix** often notated as $H$.
:::

### Solution by Projection - Normal Equation

Why is it called the normal equation? Answering that leads to an alternative way to solve for $\hat \theta$ without the need to optimize by calculus. Recall the objective was to essentially minimize $|y-X\hat \theta|^2$ (drop the $1/n$ since it doesn't matter). We define the residual vector to be $\epsilon = y - X\hat \theta = y - \hat y$. Because $\hat y$ is the linear combination of the feature columns, it's span is the feature space while $y$ is does not have to be. Therefore the $\epsilon$ must be a vector orthogonal to $\hat y$ thus also $X$:

$$
\begin{align*}
X^\top\epsilon &= X^\top\left[y-X(X^\top X)^{-1}X^\top y\right] \\
&= X^\top y - X^\top y \\
&= 0
\end{align*}
$$

## Polynomial Least Squares

Let the design matrix be denoted as $\Phi(X)$ that transform add polynomials features to the feature matrix.

For example, we can do a degree $k$ polynomial transformation with no cross terms. It's easier to write this consider every row of $X$ as $X_i$.

$$
\Phi(X_i^\top) = \begin{bmatrix}
    X_{i1} & X_{i1}^2 & \ldots & X_{i1}^k & \ldots & X_{id} & X_{id}^2 & \ldots & X_{id}^k
\end{bmatrix}
$$

## Weighted Least Squares

Sometimes you may want to weigh your data by some sort of importance or confidence metric (e.g., inverse of the data's error).

For simplicity we are only going to weigh each row. In this case, the weight can be represented as a diagonal weight matrix $\Omega$ such that $\omega_i$ is the weight the row $X_i$.

The optimization becomes,

$$
\mathop{\arg\min}_{\theta} \sum_{i=1}^n \omega_i(X_i^\top \theta - y_i)^2 = \mathop{\arg\min}_{\theta} (X\theta - y)^\top \Omega (X\theta - y)
$$