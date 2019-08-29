## Summary Statistics
Total Variation Difference
: Given the residual between the model and sample, a good metric to measure the distance between the two is the **TVD**:

    $$
    \frac{1}{2}\sum_i|\hat Y_i - y_i|
    $$

    This is often used when the distribution interested $y$ is multi-dimensional (e.g., ethnicities). A boilerplate example can be given with a three-sided dice:

    | Face Value  | Model  | Sample  |
    |---|---|---|
    | 1  | 1/3  | 0.25  |
    | 2  | 1/3  | 0.50  |
    | 3  | 1/3  | 0.25  |

    $$
    \text{TVD(Model, Sample)} = \frac{0.0833 + 0.1667 + 0.0833}{2} = 0.1666
    $$


## Regression by Correlation

Given $n$ samples of $x$ and $y$ the regression line is modeled by first transforming the sample to standard units,

$$
x' = \frac{x - \mu_x}{\sigma_x}; \qquad y' = \frac{y - \mu_y}{\sigma_y}
$$

$$
\hat y = ax + b
$$

Where the parameters $a$ and $b$ are given by,

$$
a = r\frac{\sigma_y}{\sigma_x}
$$

$$
r \equiv \mathrm{Corr}[x',y'] = \frac{1}{n}\sum_{i=1}^{n} x_i' y_i'
$$

$$
b = \mu_y - a\mu_x
$$

Notice that the RHS of $b$ is equivalent to the average of residual $\mu_\epsilon = 0$.

### RMSE

The **root mean square error** is given by defining the residual to be $\epsilon = y - \hat y$,

$$
\text{RMSE} = \sqrt{\sum_{i}^n \epsilon_i^2}
$$

However given the correlation, a dual problem exist without needing $\hat y$,

$$
\text{RMSE} \equiv \text{SD}[\epsilon] = \sqrt{1-r^2} \cdot \text{SD[y]}
$$

## 95% Confidence Interval

$$
\text{Confidence Interval} = \big[\text{2.5% percentile}, \text{97.5% percentile}\big]
$$

## Chebyshev Bound on SDs

$$
P(|X-\mu| \le z\sigma) \ge 1 - \frac{1}{z^2}
$$