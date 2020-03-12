---
title: Bayes Decision Rule
---

For some loss function $L$ the **Bayes Decision Rule** simply chooses the class with the maximum posterior distribution scaled by the loss of misclassification. For the cases of two classes, the decision rule looks like,

$$
\hat y(x) = \mathop{\arg\max}_A L(\neg A,A)P(A\mid x)
$$

A motivation why the sign is greater than is because we assign a greater loss if say class $A$ was classified wrong. If it was classified wrong, there should be a greater chance that the classifier will change its decision rule to choose classify $A$ better.

## Zero-One Loss

The risk function for the 0-1 loss is,

$$
R(\hat y) = P(\hat y(x)\text{ is wrong})
$$

This suggest that the decision boundary is the set of all points where $\set{x : P(A \mid x) = 0.5}$

## Gaussian Decision Rule

For the case of two classes $Y \in \set{1,2}$ such that each class has a $\text{Normal}(\mu_y, \sigma_y^2)$ distribution and a possible prior for the chance that a sample comes from a class $P(Y=y)$ called the mixing parameter, the probability of a sample $x$ is,

$$
P(X=x) = P(X=x \mid Y=1)P(Y=1) + P(X=x \mid Y=1)P(Y=2)
$$

Thus the decision rule follows,

$$
\hat y(x) = \mathop{\arg\max}_y P(X=x\mid Y=y) P(Y=y)
$$