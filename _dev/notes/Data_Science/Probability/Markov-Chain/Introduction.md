---
title: Introduction
---

Let the chain be a set of random variables with element $X_t$ for the step $t \ge 0$ (or link) of the chain. The chain is aid to be a Markov chain if $X_{t+1}$ is only dependent on $X_t$ for all $t > 0$

## Stationary Transition

A transition in a Markov-chain is a step from $X_t$ to $X_{t+1}$. A **stationary transition** has the probability of transition that is independent on the step $t$. That must mean there is no difference between transition probability at any step,

$$
P(X_{t+1}=j \mid X_t=i) = P(X_1=j \mid X_0=i)
$$

A more compact way to write a transition probability is,

$$
P(x_t \rightarrow x_{t+1}) := P(X_t=x_t \mid X_{t+1} = x_{t+1})
$$

This simplify the probability of any Markov chain,

$$
P(X_0=x_0, X_1=x_1, \ldots X_N=x_N) = P(x_0)P(x_0 \rightarrow x_1)\cdots P(x_{n-1} \rightarrow x_n)
$$