---
title: Second Quantization
---

Let the set of annihilation and creator operators in both position and momentum be related by,

$$
\hat a_x = \frac{1}{\sqrt{V}} \sum_{p}\hat a(p) e^{i p \cdot x}\\
\hat a^\dagger_x = \frac{1}{\sqrt{V}} \sum_{p}\hat a(p)^\dagger e^{i p \cdot x}
$$

The number operator for the corresponding number of particles in some position and momentum be,

$$
\hat n_x = a^\dagger_xa_x\\
\hat n(p) = a^\dagger(p)a(p)
$$

The basic usage of these operators are simply by the examples below:

* Create a particle at position $x$ starting at a field with no particles $\ket 0$,

    $$
    \ket 1 = a_x^\dagger \ket 0\\
    $$

* Find the number of particles at position $x$ for a field with two particles

    $$
    \ket 2 = (a_x^\dagger)^2 \ket 0 \\
    n_x \ket 2 = 2 \ket 2
    $$

* Find the position of a particle at position $x$ by determining the position PDF with some general position state $\ket{x'}$,

    $$
    \ket 1 = a^\dagger\\
    \braket{x'}{1} = \delta(x-x')
    $$

    Thus the particle only exist at position $x'$.

## Second Quantization of an Operator

Similarly to how an single-particle operator in Hilbert space modifies the states of a single particle, in QFT we implore a set of Hilbert spaces called the **Fock space** which can describe our system of $N$ particles as the space $\mathcal F_N$. An operator that operates on the Fock space, thus operating on many particle is not surprisingly a matrix acted upon a single coordinate of the Fock space at $(\alpha, \beta)$. It can be compactly represented as

$$
\hat A = \sum_{\alpha \beta} A_{\alpha, \beta}a_\alpha^\dagger a_\beta
$$

* $\hat A_{\alpha, \beta}$ : Matrix element, $\bra{\alpha}\hat A\ket{\beta}$