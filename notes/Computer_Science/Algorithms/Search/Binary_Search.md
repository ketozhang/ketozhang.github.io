---
title: Binary Search
---

A logarithmic search algorithm to find a value in a sorted array.

|       | Best            | Worst                |
|-------|-----------------|----------------------|
| Time  | $\mathcal O(1)$ | $\mathcal O(\log n)$ |
| Space | $\mathcal O(1)$ | $\mathcal O(1)$      |

**Usage**
* Search a sorted array

## Algorithm

For the search key $k$ and a sorted array $v = [v_1, v_2, \ldots, v_n]$ where $v_1 \le v_2 \le \ldots v_n$, the following algorithm returns the index where $k$ exists otherwise fails.

1. Let $L = 0$ and $R = n-1$.
1. If $L > R$, the algorithm terminates unsuccessfully.
1. Set the current position to the floored midpoint of $[L, R]$

    $$
    i = \left\lfloor \frac{L + R}{2} \right\rfloor
 $$

1. If $v_i = k$. If value matches found, return the index $i$.
1. Else if the $v_i < k$ move to left bound above the current index

    $$
    L = i + 1
  $$

    Repeat step 2.

1. Else if the $v_i > k$ move to right bound below the current index

    $$
    R = i - 1
  $$

    Repeat step 2.
