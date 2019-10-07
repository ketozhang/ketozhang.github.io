---
title: Matrix Formalism
---

## Transition Matrix

For simplicity, consider that $X_t:\set{1,2,3}$ for all $t \ge 0$ composes a stationary Markov chain. We can repesent a transition from $X_t$ to $X_{t+1}$ as a matrix with entries as probability $P_{ij} = P(i \to j)$ of changing from state $i$ to $j$,

$$
P =
\begin{bmatrix}
P_{11} & P_{12} & P_{12}\\
P_{21} & P_{22} & P_{22}\\
P_{31} & P_{32} & P_{32}
\end{bmatrix}
$$

The transition matrix is simple to use just by multiplying the corresponding entries of every link in the chain.

For $n$-steps, we define the probability as ending up at some state $j$ given the initial state $i$,

$$
P_{i,j}(n) = P(X_n = j \mid X_0 = i)
$$

Because $P_{i,j}(n)$ can be represented as entries $(i,j)$ of a matrix, again we can create a transition matrix $P(n)$. We can express this transition matrix as a function of the initial transition matrix $P(1) = P$. Let's start with $n=2$,

$$
\begin{align}
    P_{ij}(2) &= P(X_2 = j \mid X_0 = i)\\
    &= \sum_{k} P(X_1 = k, X_2 = j \mid X_0 = i)\\
    &= \sum_{k} P(X_1=k \mid X_0 = i)P(X_2=j \mid X_1k)\\
    &= \sum_{k} P_{ik}P_{kj}
\end{align}
$$

$$
P_{ij}(2) = P_i^\top P_j
$$

Thus for all entries $i,j$,

$$
P(2) = P^2
$$

You can prove by induction,

$$
P(n) = P^n
$$

## Probability of State

The probability of a state in some iteration $t$ is the state $i_n$,

$$ \mathbb P(X_t = i) = \mathbb P_i(t) = \left[\vec P(0)  P^t\right]_{i} $$
$$\vec P(t) = \vec P(0) P^t$$

* $\vec P(0)$ : Initial state vector
* $P$ : Transition Probability matrix (constant throughout iteration)

## First Step Equation

The average time $\tau = \avg{t}$ it takes for some state in all the possible states ($i \in \Omega$) to end up in some subset of that state ($\Omega_f \subset \Omega$) is given by the **first step equation**:

$$ \tau(f) = 0 \qquad f \in \Omega_f$$
$$ \tau(i) = 1 + \sum_{j \in \Omega} P_{ij}\tau(j) $$

* The problem of average time to reach some state $f$ in Markov chain is called the **Hitting Time** problem.

## Probability of Hitting One Before the Other

Let $\Omega_A$ and $\Omega_B$ be two disjoint subsets of $\Omega$. The probability $\alpha(i)$ that starting at the initial state $i \in \Omega$, we reach a state in $\Omega_A$ before $\Omega_B$ is:

$$
\begin{align*}
    \alpha(a) = 1 \quad &a \in \Omega_A\\
    \alpha(b) = 0 \quad &b \in \Omega_B\\
    \alpha(i) = \sum_{j\in\Omega} P_{ij}\alpha(j) \quad &i \not\in \Omega_A \cup \Omega_B
\end{align*}
$$

## Stationary Distribution

When running the Markov chain we can end up at some state $i$ at some iteration $t$ such that the distribution $P_i(t)$ is stationary meaning it's invariant under the transition probability matrix $P$:

$$
P_i(t) = P_i(t)P
$$

Formally we have the **theorem:**

$P(t_0)$ is invariant if and only if the distribution,

$$
\vec P(t) = \vec P(t_0) \qquad t \ge t_0\\
$$