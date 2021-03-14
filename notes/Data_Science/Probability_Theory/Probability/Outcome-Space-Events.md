---
title: Outcome Space and Events
---

We begin with introducing probability theory by thinking about how do we think the world works --- or at least a part of it. In probability theory, we assume there's **a world that has outcomes occurring by chance**. It is said that in this world, random processes exists.

## Outcome Space
For a system or process in this world, there exist all possible outcomes that can occur from the system. We denote this a distinct set of outcomes $\Omega = \set{\omega_1, \omega_2, \ldots, \omega_n}$ known as the **set of outcomes**, **sampling space**, or **outcome space**.

* A distinct set of outcomes means there cannot be two outcomes that can both occur at the same time (e.g., a coin is either lands heads or tails, it is either past 5:00 PM or before 5:00 PM).


## Event
We need a way to describe joint outcomes (e.g., a dice rolls even can occur from three possible outcomes: 2, 3, 4). We call these joint outcomes **events**, although no strictly since any one outcome can also be an event.

Thus, we define an event $A$ to be a subset of the outcome space:

$$A \subseteq \Omega $$

## Probability

What is the chance that an event occurred? Well, using the foundation we've just built, the chance of an event occurring must depend on the chance that each outcome occurs. The probability of one outcome is denoted as,

$$
P(\omega)
$$

 Because each outcome is distinct from one another
The probability of event $A$ is the sum of each outcome probability of $A$,

$$P(A) = \sum_{\omega \in A} P(\omega)$$

::: Example
**Outcomes with Equal Chance**

If it so happens that the probability of $P(\omega)$ is equal for all $\omega$ then the outcome space is said to have a uniform distribution. This simplifies the probability of an event which is the number of outcomes in $A$ out of the total number of possible outcomes.,

$$ P(A) = \frac{\abs{A}}{\abs{\Omega}} $$
:::