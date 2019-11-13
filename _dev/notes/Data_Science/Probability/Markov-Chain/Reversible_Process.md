---
title: Reversible Process
---

A Markov chain is considered a reversible chain if its reverse sequence $Y_0, Y_1, \ldots, Y_n$ has the same one-step transition probability as the forward sequence $X_0, X_1, \ldots, X_n$. This implies, a chain is reversible if the chain is in detailed balance with positive solution $\pi(i)$ for all states $i$,

$$
\pi(i) P(i,j) = \pi(j)P(j,i)
$$

## Proof

Given a sequence, the probability of the next step in the reverse sequence can be related to the foward sequence

$$
P(Y_{m+1} = j \mid Y_{m < i}, Y_i = i) = \frac{\pi(j)}{\pi(i)}P(j,i)
$$

Since the RHS does not depend on the intermediate states $m < i$,

$$
P(Y_{m+1} = j \mid Y_i = i) = \frac{\pi(j)}{\pi(i)}P(j,i)
$$

Thus, the Markov chain is reversible if the probability of the foward step $P(i, j)$ is the same as the probability of stepping backward from $i$ back to $j$ or $P(Y_{m+1} = j \mid Y_i = i)$,

$$
\begin{gather*}
    P(Y_{m+1} = j \mid Y_i = i) = P(i,j)\\
    \Downarrow\\
    \frac{\pi(j)}{\pi(i)}P(j,i) = P(i,j)
\end{gather*}
$$

This is exactly the balanced equation,

$$
\pi(i) P(i,j) = \pi(j)P(j,i)
$$

## Birth and Death Chain

A birth and death is one that can only go to 3 states: up $i+1$, down $i-1$, and stay $i$.

This simple process makes it not surprising that all birth and death chain are all reversible processes. As we can abritrarily swap out $i$ and $k$ and the process is reversed.