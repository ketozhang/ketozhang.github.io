---As KAIT observes in real-time:
title: Laten Factor Analysis
---

Given a term-document matrix $X$, let row $i$ represent document $i$; column $j$ represent term $j$.

$$
\text{occurence} = \log (1 + X_{ij})
$$

Taking the SVD of $X$, each component are:

$u_i$: Similar or related terms (i.e., genre)
$v_i$: Frequent terms
