## Annihilation and Creation Operators

The annihilation and creation operators (or in collection called the harmonic operators) are given by:

$$
\hat a = \sqrt\frac{m \omega}{2 \hbar}\left(\hat x + \frac{i}{m\omega}\hat p\right)\\
\hat a^\dagger = \sqrt\frac{m \omega}{2 \hbar}\left(\hat x - \frac{i}{m\omega}\hat p\right)
$$

The Hamiltonian in terms of the harmonic operators is given by,

$$
\hat H = \frac{1}{2}h \omega \left(2\hat a^\dagger \hat a + 1\right)
$$

### Motivation

Recall the harmonic oscillator Hamiltonian,

$$
\hat H = \frac{\hat p^2}{2m} + \frac{1}{2}m\omega^2x^2
$$

You may be tempted to factor the Hamiltonian out to be,

$$
\frac{1}{2} m \omega^2 \left(\hat x - \frac{i}{m\omega}\hat p \right)\left(\hat x + \frac{i}{m\omega}\hat p \right)
$$

However, this is not $\hat H$ because $\hat x$ and $\hat p$ does not commute ($[\hat x, \hat p] = i\hbar$). Instead,

$$
\hat H = \frac{1}{2} m \omega^2 \left(\hat x - \frac{i}{m\omega}\hat p \right)\left(\hat x + \frac{i}{m\omega}\hat p \right) - \frac{i \omega}{2}[\hat x, \hat p]
$$

In the first term, the two factors along with some constant motivates the definition of $\hat a,\hat a^\dagger$ such that,

$$
\hat H = \frac{1}{2}h \omega \left(2a^\dagger a + 1\right)
$$

### Number Operator and Eigenstuff

$$
\hat H = h \omega \left(\hat N+ \frac{1}{2}\right)
$$

* $\hat N$: Number operator, $\hat N \equiv \hat a^\dagger \hat a$

The eigenvector of $\hat H$ are eigenvectors of then number operator. It is very useful to notate the eigenvector as $\ket n$ and eigenvalue as $n$.

$$
\hat H \ket n = E_n \ket n\\
\hat N \ket n = n \ket n
$$

Where $E_n$ is easily determined  by applying $\ket n$,

$$
\hat H \ket n = \frac{1}{2}\hbar \omega (2 \hat N \ket n + \ket n) = \frac{1}{2} \hbar \omega (2 n \ket n + \ket n)\\
\hat H \ket n = \underbrace{\left(n + \frac{1}{2} \right) \hbar \omega}_{E_n} \ket n
$$

### Lowering and Raising Operators

$\hat a$ and $\hat a^\dagger$ are also known as the **lowering and raising operator** respectively. This comes from applying the operator and determining the energy eigenvalue.

First using the raising operator, we find the eigenstate of $\hat N$ goes up by one,

$$
\hat N \hat a^\dagger \ket n = \hat a^\dagger \hat a \hat a^\dagger \ket n\\
\hat N \hat a^\dagger \ket n = (n+1) \hat a^\dagger \ket n
$$

### Normalization

Now we established that the lower and raising operator transform the state from $\ket{n+1}$ to $\ket{n}$ or reverse respectively, we need to actually define the operation,

$$
\hat a \ket n = \sqrt{n} \ket{n - 1}\\
\hat a^\dagger \ket n = \sqrt{n+1}\ket{n+1}
$$

### Eigenstates

We can now define the eigenstates

$$
\ket n = \frac{(\hat a^\dagger)^n}{\sqrt{n!}} \ket 0
$$

## Multiple Harmonic Oscillators
To discrete a general system of harmonic oscillator let's start out with uncoupled harmonic oscillators. The Hamiltonian for each oscillator is,

$$
\hat H_k = \frac{\hat p_k ^2}{2m_k} + \frac{1}{2}m_k \omega_k^2 x_k^2
$$

The harmonic operators $\hat a_k$ and $\hat a^\dagger_k$ only applies to the $k$th oscillator and does nothing to the rest.

The only commutation rule that is nonzero is,

$$
[\hat a_i, \hat a^\dagger_j] = \delta_{i,j}
$$

Equivalently, we can write the Hamiltonian as,

$$
\hat H = \sum_{k} \hbar w_k \left(\hat a_k^\dagger \hat a_k + \frac{1}{2} \right)
$$

The general eigenstate $\ket{n_1, n_2, \ldots}$ called the **occupation number representation** is then,

$$
\ket {n_1, n_2, \ldots} = \prod_{k} \frac{1}{\sqrt{n_k!}}\hat a_k^\dagger \ket{0,0,\ldots,0}
$$