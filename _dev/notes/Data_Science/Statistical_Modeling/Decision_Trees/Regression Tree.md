---
title: Regression Tree
---

Decision tree on regression differs by the loss function and the last step when predicting $\hat y$ given some sample point $z$.

Cross entropy no longer makes sense but we do wish to reduce the variance of error,

$$
L = \sigma^2 = \text{Var}[y-\hat y] = \text{Var}[\epsilon]
$$

$$
\sigma^2 = \frac{1}{n}\sum_{i \in S} \epsilon_i - \langle \epsilon \rangle
$$

$$
\text{gain} = \sigma^2 - \frac{n_L\sigma_L^2 + n_R\sigma_R^2}{n_L + n_R}
$$

$S$ is the set of indices representing the training sample point that landed in that node. Thus the objective function is still

$$
\mathop{\arg\max}_{S_L,\, S_R}(\text{gain})
$$

Given a decision tree and sample point $z$, a prediction is made by taking some aggregate (usually the mean) of the $y$ values in the leaf.

$$
z = \frac{1}{n}\sum_{i \in S} y_i
$$

## Tree Depth

At the edge case where there are $n$ leaves where every set $S_i, ~ \forall i$ are disjoint the decision tree perfectly classifies the training set.