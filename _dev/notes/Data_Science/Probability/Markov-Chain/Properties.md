---
title: Properties
---

## Communication

* A state $i$ **leads** to state $j$ denoted as $i \to j$ if one state can get to another. Formally any $i,j$ constrained by,

    $$
    P_{i,j}(n) > 0
    $$

* Two states **communicates** if $i \to j  \land j \to i$ compactly denoted as $ i \leftrightarrow j$.

* The chain is irreducible if all $i,j$ communicates.

## Period

The **period** $T$ of a state $i$ exists if the chain can only start and end at the same state at the interval of $T$.

* Slicing out any subset of communicating states in the transition matrix helps you determine its periodicity
* If $P_{ii} \neq 0$, then the state $i$ is aperiodic.

## Stationarity

A chain of $N$ individual states is considered to be in stationarity if all states are equally probable in $P(n)$

$$
P(n) = \frac{1}{N^2} I
$$

A converegence to stationarity is expressed as $n \to \infty$,

$$
P_{i,j}(n) \rightarrow p(j)
$$

Balance Equation
: Satisfies the balance equation for $\vec p$ the probability row vector for all states $j$:

    $$
    \vec p P = \alpha \vec p
    $$

Steady/Stationary State Distribution
: If $X_n$ is distributed as $p(j)$  then $X_m$, for $m > n$, is also distributed as $p(j)$.

Long Run Expected Proportion of Time in State

Let $I_t(j)$ be the indicator of the event $\set{X_m = j}$, for some time until $t_f$, the total proportion of time spent on state $j$ is given by,

$$
\frac{1}{t_f} \sum_{t=1}^{t_f} I_m(j)
$$

The expected proportion of time the chain spent on $j$ is then,

$$
\mathbb E\left[\frac{1}{t_f} \sum_{t=1}^{t_f} I_m(j) \right] = \frac{1}{t_f}\sum_{t=1}^{t_f} P_{ij}(t)
$$

As $n \to \infty$,

$$
\sum_{t=1}^{t_f} P_{ij}(t) = p(j)
$$

Thus the expected value of the proportion of time spent on state $j$ in the long run is given by the steady state proportion $p(j)$.