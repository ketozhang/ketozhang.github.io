---
title: Sampling without Replacement
---
We begin using sampling without replacement by considering a sample size of $k$ chosen out of a population of also size $n=k$. Each possible outcome of a sample is unique (we will be dealing with grouping later). Thus the total number of sequences is like shuffling a card of deck with each cards begin unique,

$$
|\text{sequence of $n$ samples}| = n!
$$

The probability of any particular sequence is then,

$$
P(\text{sequence of $n$ samples}) = \frac{1}{n!}
$$

## Symmetry (between slots)

Notice that the probability of any particular sequence does not depend on the actual elements in a sequence. Another way to state this is that every sequence has equal chances of occuring. Thus if you were to imagine a sequence of $n$ slots where each slot can be represented as a random variable $X_i$ for $1 \le i \le n$, then notice that any particular $X_i$ has the probability of being value $k$ by,

1. Fixing the value $k$ on slot $i$
2. Permutate the other slots which has $(n-1)!$ possibilities

$$
P(X_i = k) = \frac{(n-1)!}{n} = \frac{1}{n}
$$

Notice that the probability does not depend on the value of $k$ or the position of the slot $i$. In addition this implies that given any slot $i$, all possible outcomes are equally likely to occur at that slot. This type of relation is called symmetry as any slots are not distinguishable from other (i.e., $X_i$ is distributed the same as $X_{i+1}$)


You may use this symmetry relation between slots $i$ in the following ways:

* The order at which slot occurs does not matter:

    $$
    P(X_3, X_{12}) = P(X_1, X_2)
    $$

    $$
    P(X_1, X_2) = P(X_1 \mid X_2) P(X_2) = \frac{1}{n-1} \frac{1}{n}
    $$

## Simple Random Sample

Sampling without replacement for $k \le n$ is called a **simple random sample (SRS)**. Succinctly, an SRS creates a sample that is a subset of a finite population.

Once again consider a deck of size $n=52$ and we like a sample of size $k \le n$. The total number of possible ordered sequences is,

$$
|\text{ordered sequence of $k$ samples}| = \frac{n!}{k!}
$$

Because $k \le n$ it is possible that a sequence is the same as another if we don't care about the order.

$$
|\text{unordered sequence of $k$ samples}| = {n \choose k}
$$

Thus, the probability depends if you're counting ordered or unordred sequences.

### Hypergeometric Probability

Let's now consider grouping. It only makes sense to group something if the elements in a group are considered indistinguishable for the problem; in other words, we are dealing with unordered sequences. Let the size of such group be $G$ where $G \le N$ and $N$ is the size of the population. Let the number of samples be is $n$. Let the random variable $X$ be the number of outcomes that is part of the group of size $G$.

$$ P(X=g) = \frac{\binom{G}{g} \binom{N-G}{n-g}}{\binom{N}{n}} $$