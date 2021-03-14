---
title: Properties
---

## Communication

* A state $i$ **leads** to state $j$ denoted as $i \to j$ if one state can get to another. Formally if $i$ leads to $j$ then there exist a time $t$ where,

    $$
    P_{i,j}(t) > 0;
    $$

* Two states **communicates** if $i \to j  \land j \to i$ compactly denoted as $ i \leftrightarrow j$.

* The chain is irreducible if all $i,j$ communicates.

## Period

The **period** $T$ of a state $i$ exists if the chain can only start and end at the same state at the interval of $T$.

* Slicing out any subset of communicating states in the transition matrix helps you determine its periodicity
* If $P_{ii} \neq 0$, then the state $i$ is aperiodic.
* All states of irreducible transition matrix must be all share the same period.

## Stationarity

A chain of $N$ individual states is considered to be in stationarity if for all states $j$, the transition to state $j$ is independent of the previous state $i$.

$$
P_{ij}(n) = \text{const}, \quad \text{for fixed $i$ and all $j$}
$$

We express this formally as a state has stationarity as the number of steps $n \to \infty$

$$
\begin{gather*}
P_{i,j}(n) \rightarrow \pi(j), \quad \text{as }n \to \infty\\
\sum_{j \in S} \pi(j) = 1
\end{gather*}
$$

Stationarity of Irreducible Aperiodioc Markov Chain
: All irreducible and aperiodic Markov chain converges to stationarity

Stationarity States are Positive
:   $$
    \pi(j) > 0
    $$

Balance Equation
: Satisfies the balance equation for $\vec \pi$ the probability row vector for all states $j$:

    $$
    \pi(j) = \sum_{i \in S} P(i,j)\pi(i)
    $$

    $$
    \vec \pi P = \vec \pi
    $$

    Any constant factor of the RHS also satisfies the balance equation.

Steady/Stationary State Distribution
: If $X_n$ is distributed as $\pi(j)$  then $X_m$, for $m > n$, is also distributed as $\pi(j)$.

    $$
    \begin{gather*}
    P_{ij}(n+1) = P_{ij}(n) = \pi(j)\\
    \big\Downarrow\\
    P_{ij}(m) = \pi(j); \quad m > n
    \end{gather*}
    $$

Long Run Expected Proportion of Time in State
: Let $I_t(j)$ be the indicator of the event $\set{X_m = j}$, for some time until $t_f$, the total proportion of time spent on state $j$ is given by,

    $$
    \frac{1}{t_f} \sum_{t=1}^{t_f} I_m(j)
    $$

    The expected proportion of time the chain spent on $j$ is then,

    $$
    \mathbb E\left[\frac{1}{t_f} \sum_{t=1}^{t_f} I_m(j) \right] = \frac{1}{t_f}\sum_{t=1}^{t_f} P_{ij}(t)
    $$

    As $t_f = n \to \infty$,

    $$
    \frac{1}{n}\sum_{t=1}^n P_{ij}(t) = \pi(j)
    $$

    Thus the expected value of the proportion of time spent on state $j$ in the long run is given by the steady state proportion $\pi(j)$.

