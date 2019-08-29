---
title: Spectral Graph Clustering
---

Take a weighted, undirected graph $G(V,E)$ that has no self-edges where the weights are $w_{ij}$ of edge $(i,j) =  (j,i)$. The weight is zero if there is no edge between the vertices.

The goal is to cut $G$ into two or more graphs of similar sizes but don't cut too much edge weight. This is to minimize th sparcity:

$$
\frac{\text{Cut}(G_1, G_2)}{\text{Mass}(G_1)\text{Mass}(G_2)}
$$

* $\text{Cut}(G_1, G_2)$ : Total weight of the cut edges
    For every vertex $y = 1$ or $y = -1$ if it belongs to $G_1$ or $G_2$ respectively. Given $n = |V|$,

    $$
    \begin{align*}
    \text{Cut}(G_1, G_2) &= \sum_{(i,j) \in E} w_{ij} \frac{(y_i-y_j)^2}{4}\\
    &= \frac{1}{4} \sum_{(i,j) \in E} -2w_{ij}y_iy_j + \sum_{i=1}^n y_i^2 \sum_{k\neq i} w+{ik}\\
    &= \frac{y^\top L y}{4}\\
    \end{align*}
    $$

    Where the above is the **Laplacian  quadratic form** with the **Laplacian matrix**,

    $$
    L_{ij} = \begin{cases} -w_{ij}  & i \neq j \\ \sum_{k \neq i} w_{ik} & i=j \end{cases}
    $$
* $\text{Mass}(G)$ : Number of vertices in $G$ or assign vertex weights.

## Laplacian Matrix Properties

* The Laplacian matrix is a positive definite matrix.
* All Laplacian matrix has the eigenvector $\hat 1$. Since,

    $$
    \text{Cut}(G_1, G_2; y = \hat 1)  = 0
    $$

    Thus $y^\top L y = 0$.

## Bisection

A bisection occur when $|G_1| = |G_2| = \frac{n}{2}$. With the indicator vector $1^\top = 0$ is an equivalent definition.

### Bisection Minimization

The minimum bisection problem is to find $y$ that minimzes

$$y^\top L y; \qquad \forall i, (y_i = 1 \lor y_i = -1) \land 1^\top y = 0$$

The problem is NP-hard so an approximation allow $y_i$ to be fractional. However a better approximation is to let $y$ lying on a hypersphere of radius $\sqrt{n}$. In full

$$
\min y^\top L y; \quad y^\top y = n \land \hat 1^\top y = 0
$$

Equivalently, you can minimize the Rayleigh quotient for $L$ and $y$

$$
\min \frac{y^\top L y}{y^\top y}
$$

The solution is to let $\lambda_2$ be the second smallest eigenvalue of $L$ with eigenvector $v_2$ called the **Fielder vector**.


### Sweep Cut Alogirhtm

1. Compute the fielder vector $v_2$ of $L$
2. Sorting the component of $v_2$
3. Choose minimum sparsity cuts for the $n-1$ cuts between successive components.
    A cut here means choosing any successive coponents all components to the left is $G_1$ and to the right is $G_2$.

## Vertex Masses

Adding a mass to vertices gives $M$ a diagonal matrix. The sparsity minimization constraints changed by adding new constraints:

$$
\hat 1^\top M y = 0
$$

$$
y^\top M y = \mathrm{Tr}(M)
$$

* The changes to the Fielder vector solves for the generlized eigensystem
    $$
    Lv = \lambda M v
    $$
* In turn the sweep cut changes by including the Cheeger's Inequality
    $$
    \text{sparsity} \le \sqrt{2 \lambda_2 \max_i \frac{L_{ii}}{M_{ii}}}
    $$

    $$
    \text{sparsity} \ge \frac{\lambda_2}{2}
    $$

## Normalized Cut

Set vertix $i$'s mass $M_{ii} = L_{ii}$. This is popular for image segmentation (taking out objects or layers from an image).

## Spectral Vectors

Given multiple eigenvectors $V \in \mathbb R^{n,k}$ the **spectral vector** are the row vectors $V_j^\top$.

In k-means clustering, the set of spectral vectors for the individual clusters points along similar directions and orthogonal to other cluster's spectral vectors.