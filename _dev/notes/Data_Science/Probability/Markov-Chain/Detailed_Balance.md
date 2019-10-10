---
title: Detailed Balance
---

Consider a Markov chain where on the long run, for all states $i$ and $j$, the proportion (or chance) of states moving from $i$ to $j$ is the same as from $j$ to $i$. This suggest the following relation,

$$
\pi(i) P(i,j) = \pi(j) P(j,i) \quad \forall i, j \in S
$$

We call this Markov chain to be detailed balanced and it turns out this satisfies the balance equation,

$$
\begin{align*}
\pi(j) &= \sum_{i \in S}\pi(i)P(i,j)\\
&= \sum_{i \in S}\pi(j)P(j,i)\\
&= \pi(j)\sum_{i \in S}P(j,i) \\
&= \pi(j)
\end{align*}
$$