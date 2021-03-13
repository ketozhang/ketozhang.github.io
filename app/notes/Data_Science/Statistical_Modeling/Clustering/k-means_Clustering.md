---
title: k-means Clustering
---

**k-means clustering** or **Lloyd's Algorithm** partitions $n$ points into $k$ disjoint clusters. Assign each input point $X_i$ a cluster label $y_i \in [1,k]$.

We assign each of the $k$ cluster with its mean $\mu_i$. The objective is to minimize each sample's Euclidean distance to the cluster mean.

$$
y =  \mathop{\arg\min}_y \sum_{i=1}^k\sum_{y_j = i}|X_j - \mu_i|^2
$$

The solution is unfortunatley NP-hard in $\mathcal O(nk^n)$.

## Heuristic Solution

Because the solution is NP-hard, we use the following algorithm:

1. Let $y_j$ be fixed and update $\mu_i$.
    Solved via letting $\mu_i$ be the mean of the points in cluster $i$
2. $\mu_j$ are fixed and update $y_j$.
    Solved via letting $y$ be the points where $X_j$ is closest to the center $\mu_j$.
3. Repeat 1-2 until no changes.

This algorithm will always terminate but the solution is not always the global minimum.

This algorithm is susceptible to initial clustering. There are a few methods that works:

* **Forgy method**: Choose $k$ ranodm sample points to be initial the set of $\mu$ then go to step 2.
* **Random partition**: Randomly assign each sample point to  cluster then go to step 1.
* **k-means ++**: Like Forgy, but biased distribution

## Alternative Objective Function

$$
y = \mathop{\arg\min}_y \sum_{i=1}^k \frac{1}{n_i}\sum_{y_j=i}\sum_{y_m=i} |X_j - X_m|^2
$$

## k-Medroids
**k-Medroids** does not use Euclidean distance but some general distance function $d(X_i, X_j)$.

The mean is replace with the **medoid** $\mu$ which is the sample point that minimizes the total distance to other points in the same cluster.