## Motivating Example

Consider a coin where we do not know the chance of heads $p$. Let's take the prior that $p$ is uniformally any value between 0 and 1. That is,

$$
p \sim \text{Uniform}(0, 1)
$$

The chance that the coin lands head depends on the value of $p$ which is random. We can marginalize over all possible values of $p$,

$$
P(H) = \int_0^1 P(H, p) ~dp = \int_0^1 P(H \mid p) f(p) ~dp
$$

In fact this looks like an expected value as a function of $p$,

$$
P(H) = E(P(H \mid p))
$$

The chance of head given $p$ is of course $p$ itself so,

$$
\boxed{P(H) = E(p) = \frac{1}{2}}
$$

This is not so surprising since $p$ is uniform, a large sample of $p$ would neither be advantageous to getting heads or tails.

However, what's the chance of getting two heads $P(HH)$ out of two tosses?

We know that $P(HH \mid p) = p^2$ therefore,

$$
\boxed{P(HH) = E(p^2) = \int_0^1 p^2 ~dp = \frac{1}{3}}
$$

The answer is **not** $1/4$ as we should expect. That must mean the two tosses of coins are not independent when $p$ is random. To see why we need to look at the conditional probability that the second coin lands head if we know the first one lands heads for a random $p$

$$
P(H_2 \mid H_1) = \frac{P(H_1, H_2)}{P(H_1)} = \frac{2}{3}
$$

Where did the $2/3$ come from? Let's take a look at what happens to the chance of $p$ given we know the first coin lands head. We would need to apply Bayes rule,

$$
f(p \mid H_1) = \frac{P(H_1 \mid p) f(p)}{P(H_1)} \propto p
$$

Normalizing we find that,

$$
f(p \mid H_1) = 2p
$$

Thus,

<!-- TODO: WHAT? -->
$$
P(H_2 \mid H_1) = \int_0^1 P(H_2 \mid p) \cdot f(p \mid H_1) ~dp = \frac{2}{3}
$$