---
title: Joint Probability
---
A **joint probability** or **joint distribution** is the probability of multiple random variables.

$$
    P(X_1, X_2, \ldots, X_n)
$$

* Equivalently the comma can be replaced with interesection $\cap$ or "logical and" $\land$

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

### Mutually Independent

To generalize to a set of $n$ random variables $\set{X_1,X_2,\ldots,X_n}$, these random variables are independent only if all subsets $i \in I \subseteq {1,2,\ldots,n} \land \abs{I} > 2$ follows,


$$ \boxed{P\left(\bigcap_{i\in I} X_i\right) = \prod_{i\in I} P_{X_i}\left(x\right)}$$

* **NOTE**: It is not enough that $P(\cap_i^n X_i = \prod_i^n P_{X_i}(x))$ to prove $\set{X_1,X_2,\ldots,X_n}$ is mutually independent.

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