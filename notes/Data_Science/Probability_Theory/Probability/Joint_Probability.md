---
title: Joint Probability
---
The **joint probability distribution** describes the chance of the values of multiple random variables. The joint distribution is denoted as,

$$
P(X_1 = x_1, X_2 = x_2, \ldots, X_n = x_n)
$$

* Equivalently the comma can be replaced with interesection $\cap$ or "logical and" $\land$

There are many different ways to write joint events:

* Random variables take singular values,

    $$
    P(X=x, Y=y)
    $$

* Equality and inequality of random variables,

    $$
    P(g(X) \ge h(Y))
    $$

* In general all joint distribution can be described by set of all possible values that makes the event true,

    $$
    \begin{gather}
    P((X,Y) \in S), S = \set{(x_1,y_1), (x_2,y_2), \ldots}
    \end{gather}
    $$

## Derived from Conditional Probability

Take two random variables $X$ and $Y$. The joint probability for some value $x,y$ can be determined by the relationship with the conditional probability,

$$
\boxed{\begin{align*}
P(X=x,Y=y) &= P(X=x \mid Y=y)P(Y=y)\\
&= P(Y=y \mid X=x)P(X=x)
\end{align*}}
$$

The equality of the two lines comes from the divisoin rule or **Bayes rule**:

$$
P(X=x \mid Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)}\\
P(Y=y \mid X=x) = \frac{P(X=x, Y=y)}{P(Y=y)}
$$

In general the probability of a joint probability is given by the **chain rule**,

$$ \boxed{P\left(\bigcap_{i=1}^n X_i\right) = \prod_{i=1}^n P\left(X_i \Bigg\lvert \bigcap_{j\neq  i}^{n}X_j \right)}$$

## Independent Joint Probability

Random variables are considered independent if the their probability distribution are separable. For instance for $X$ and $Y$,

$$ P_{XY}(x,y) = P_X(x)P_Y(y) $$

A more compact notation,

$$ P(x,y) = P(x)P(y) $$

Alternatively two random variables are independent if the conditional probability is the probability of itself,

$$
    P(x \mid y) = P(x)
$$

## Marginal Probability

The marginal probability is a posterior probability summing over all joint probability for each prior event. For instance given that $X$ is a random variable of the posterior and $Y$ of the prior

$$
    P_X(x) = \sum_{y \in \Omega_Y} P(x, y) = \sum_{y \in \Omega_Y}{P(x \mid y)P(y)}
$$

## Expectation Value

The expectation value of a joint probability follows linearity such that,

$$ \mathbb E[aX+bY+c] = \sum_{x \in X}{\sum_{y \in Y}}{P(x,y)(ax+by+c)} $$

## Union Probability

### Inclusion-Exclusion Formula

The inclusion exclusion formula defines the probability of the union of two or more events.

Let's start simply with the union of two events which states:

<center> **"The probability of any event of $A$ or $B$ occuring."** </center>

$$
    P(A \cup B) = P(A) + P(B) - P(A, B)
$$

In general,

$$
    P\left(\bigcup_{i=1}^n A_i\right) = \sum_i^n P(A_i) - \mathop{\sum\sum}\limits_{1\le i < j \le n}P(A_iA_j) + \ldots + (-1)^{n+1}P(A_1,A_2, \ldots, A_n)
$$

### Boole's Inequality

**Boole's Inequality** is an upper bound for the union of two or more events. It's simply says that the probability of a collection of event is no greater than the sum of all its probabilities,

$$
    P\left(\bigcup_{i=1}^nA_i\right) \le \sum_{i=1}^{n} P(A_i)
$$

