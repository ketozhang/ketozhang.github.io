---
title: Connectivity
---

Theorem: Minimum Edges
: A connected graph with $V$ vertices must have at least $E-1$ edges,,

  $$
  E \ge V + 1
  $$

  Do note that a disconnected graph can also have $E \ge V + 1$.

Theorem: Maximum Edges
: A connected graph with $V$ vertices has at maximum edges of a complete graph.

  $$
  E \le {V \choose 2} = \frac{V!}{2!(V-2)!}
  $$

## Cut Edge and Vertex
A cut edge is an edge that will increase the number of connected graphs when removed. The same goes for cut vertex.

### Bridge Algorithm

The bridge algorithm finds cut bridges by:

1. Start at any vertex, label it 0
2. We begin DFS. One each visit

    1. Mark it with increasing index.
    2. Store the path taken
3. For each vertex, determine it's low-link value.
    A low-link value is the vertex, along it's directed path that was previous stored, with the lowest index.

From here, all edges `(a,b)` where `id(a) < lowlink(b)`

### Articulation Algorithm

The articulation algorithm finds cut vertices by first running the bridge algorithm and noticing:

* If $V>=2$, `(u, v)` is a cut edge then either `u` or `v` are articulation points.
* If there is no bridge, check for cycles by checking any vertex has its own index as it's low-link value.
    * Except for the case where the starting node `id(v) == 0`, only has one outgoing edge. A cut vertex needs more than one outgoing edge.