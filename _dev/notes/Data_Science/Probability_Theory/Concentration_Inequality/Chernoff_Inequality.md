---
title: Chernoff Inequality
---

Because, Markov's inequality may take any monotonically increasing function, the function $g(X) = e^{tX}$ is a good choice since the RHS has the moment generating function $E(e^{tX}) = M_X(t)$,

$$
P(X \ge c) \le \frac{M_X(t)}{e^{tc}}
$$

## Right Tail Bound

Since the MGF is a function of $t$ we can choose any $t$ and preferably the one that minimizes the RHS,

$$
\boxed{P(X \ge c) \le \min_{t \gt 0} \frac{M_X(t)}{e^{tc}}}
$$

## Left Tail Bound

$$
\boxed{P(X \le c) \le \min_{t \gt 0} \frac{M_X(-t)}{e^{-tc}}}
$$