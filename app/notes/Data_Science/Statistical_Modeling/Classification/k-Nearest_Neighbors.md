---
title: k-Nearest Neighbors
---

**k-Nearest Neighbors** (**k-NN**) is used in both classification and regression. The predictor predicts the aggregate of the $k$ nearest training label using some distance metric $d(z,x)$.

Specifically for classification, the mode of the k-NN is often used as the predicted label, while for regression, the mean of the k-NN is often used.

## Algorithm

Given a query point $z$:

* Scan through all $n$ sample points.
* Add neighbors to $k$ size max-heap.

The computation time is $\mathcal O(nd + n \log k)$

## Low Dimension Algorithm

* In very small dimensions ($~2-5$)
    Use Voronoi diagrams.
* In medium dimensions ($\lesssim30$)
    Use k-d trees.
* Otherwise use traditional algorithm or preprocessing.


### Vornoi Diagrams

Let $X$ be a point set. The Voronoi cell of $w \in X$ is

$$\text{Vor} w = \{ |\overline{pw}| \le |\overline{pv}| \forall v \in X \}$$

For $k=1$,
* In 2D, using the Vornoi diagram and trapezoidal map for point location the k-NN can be reduced to $\mathcal O(\log n)$
* In $\dim d$, use binary space partition tree for point location.

Other than that, the Vornoi diagram isn't feasible for k-NN.

### k-D Trees

Very similar to decision trees with the follow differences:

* Choose splitting feature is chosen by the feature of greatest width which maximizes $X_{ji} - X_{ki}$.
    * Alternatively rotate the features.
* Choose splitting value by either:
    * Median (shortest tree builds in $\mathcal O(nd \log n)$ )
    * Pairwise midpoint (builds in $\mathcal O(n \log n)$ )
* Each internal node stores a sample point at the split.
* Each subtree can be seen as a box region with values of its node and sub-nodes.

1. Given a query point $z$ ,find a sample point such that $|\overline{zw}| \le (1 + \epsilon)|\overline{zs}|$ where $s$ is the true nearest neighbor.
    The algorithm maintains:

    * Nearest neighbor found so far
    * Binary heap of unexplored subtrees, keyed by distance from the query.
2. A better nearest point is obtained by going through the binary heap and exploring the subtree no further than the distance to the nearest neighbor so far.

## Facts and Heuristics

Theorem (Cover & Hart 1967)
: As $n \rightarrow \infty$, $k=1$ has the error rate bounded by $< B(2-B)$ where $B$ is the Bayes risk.

    If $k=2$, then error is $\le 2B(1-B)$.

Theorem (Fix & Hodges 1951)
: As $n \rightarrow \infty$, $k \rightarrow \infty$, and $\frac{k}{n} \rightarrow 0$ then k-NN error rate converges to $B$ the Bayes risk.