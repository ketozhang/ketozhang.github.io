The **coherent state** is the exponential expansion of some state $\ket{f}$ such that its the eigenstate of the annihilation operator,

$$
\hat a \ket{f} = f \ket{f}
$$

This property comes from defining the coherent state as the exponential of the eigenstate with the creation operator,

$$
\ket{f} = e^{f^*f/2}e^{f a^\dagger}\ket{0}
$$

## Motivation

We first motivate the coherent state by recalling the uncertainty for the harmonic oscillator,

$$
\Delta x \Delta p = \frac{\hbar}{2}(2n + 1)
$$

Where $\Delta$ represents the RMSE operator,

$$
\Delta A = \sqrt{\avg{A^2} - \avg{A}^2}
$$

We run to a problem when $n \gg 1$ because in the classical limit, it doesn't make sense since the uncertainty doesn't match what we expect in classical measurements.

On the other hand, the coherent state has uncertainty in $n$,

$$
\Delta n = \sqrt{x}
$$

## State Probability

The probability for the coherent state to have the state $n$ occur follows the probability mass function of the Poisson distribution,

$$
\abs{\braket{n}{f}}^2 = \frac{(f^*f)^n}{n!}e^{-f^*f}
$$

Recall the expectation value of $n$ for the Poisson distribution to be the numerator factor inside the $n$ power,

$$
\avg{n} = f^*f
$$

## Traveling Harmonic Oscillator

A very interesting coherent state is in moving the harmonic oscillator.

Recall the Hamiltonian of the harmonic oscillator to be,

$$
\hat H = \frac{p^2}{2m} + \frac{1}{2} m \omega^2 x^2
$$

Classically, let's apply a force to the harmonic oscillator such that we equivalently moved the harmonic oscillator to a distance the the right of the center $x' = x - x_0$. Equivalently the force we apply is equivalent to Hook's law

$$
\Delta F = - m \omega^2 x_0
$$

The change in potential is then,

$$
\Delta V = \int{\Delta F \mathrm d x} = m \omega^2 x_0x\\
V + \Delta V = \frac{1}{2} m \omega^2 (x-x_0)^2 - \underbrace{\frac{1}{2}m \omega^2 x_0^2}_{\text{set to 0}}
$$

We ignore the second term because we can abritrarily ignore terms that do not involve both $x_0$ and $x$ (it's the zeropoint anyways).

The new Hamiltonian becomes,

$$
H' = \frac{p^2}{2m} + \frac{1}{2}m \omega^2 (x-x_0)^2
$$

We'd like to hold the state of the oscillator, equivalently stopping it from moving. Mathemtically, this is represented by the stationary state of them momentum across space or the stationary state of the potential across time. Solving for the stationary state gives $x = x_0$

$$
\dot p = (V + \Delta V)' = 0 \implies x = x_0
$$

Thus we get back the old Hamiltonian except $x = x_0$. Upon release of the oscillator (stop the holding). The Hamiltonian would move as a harmonic oscillator,

$$
x(t) = x(0) \cos \omega t + p(0) \frac{1}{m \omega} \sin \omega t
$$

Moving this to quantum realm, the new Hamiltonian has a new groundstate $\ket{0}'$ which has the affect of changing the ladder operators,

$$
a' = \sqrt{\frac{m\omega}{2\hbar}\left((x-x_0) + \frac{ip}{m\omega}\right)} = a - \sqrt\frac{m\omega}{2\hbar}x_0
$$

$$
a\ket{0}' = \sqrt\frac{m\omega}{2\hbar}x_0\ket{0}'
$$

Thus the excursion on the state $\ket{0} \rightarrow \ket{0}'$ causes the new state to be the eigentstate of $a$. Thus this new state is the coherent state. Let's redefine the state using the eigenvalue of $a$,

$$
\ket{\sqrt\frac{m\omega}{2\hbar}x_0} := \ket{0}'
$$

To have the quantum harmonic oscillator travel, we need to time evolve it. Normally we'd use the time part of the Schrodinger equation, but this time the Heisenberg equation is easier,

$$
i\hbar \dot a = [a, H] = \hbar \omega a
$$

Solving for $a$,

$$
a(t) = a(0)e^{i\omega t}
$$

Solving for $x(t), p(t)$ and defining $a(0) = a$,

$$
x(t) = \sqrt{\frac{\hbar}{2m\omega}}(\hat a(t) + \hat a^\dagger(t)) = \sqrt\frac{\hbar}{2m\omega}(ae^{-i\omega t} + a^\dagger e^{i\omega t})\\
p(t) = -i\sqrt{\frac{m\omega\hbar}{2}}(\hat a(t)- \hat a(t)^\dagger) = -i\sqrt\frac{m\hbar\omega}{2}(ae^{-i\omega t} - a^\dagger e^{i\omega t})
$$

To get the classical pendulum motion we need to take the expectation value across position and momentum with the coherent state,

$$
\bra{f} x(t) \ket{f} = x_0 \cos \omega t\\
\bra{f} p(t) \ket{f} = -m\omega x_0 \sin \omega t
$$

The uncertainty is then,

$$
\Delta x = \sqrt\frac{\hbar}{2 m \omega}\\
\Delta p = \sqrt\frac{m \hbar \omega}{2}\\
\Delta x \Delta p \le \frac{\hbar}{2}
$$

Thus we consider the classical observation to be the observation of the coherent state (on average).

## General Wavefunction from Coherent States

Given a coherent state, we'd like to determine the usual wavefunctions of some state $\ket{x}$.

We continue by being careful about noncommutative properties in exponentials. Using the Baker-Campbell-Hausdoroff formula, which states that we can expand the exponential of an separable operator into many commutators

$$
e^Z = e^Xe^Y \rightarrow Z = X + Y + \frac{1}{2}[X,Y] + \frac{1}{12}\Big([X,[X,Y]] - [Y,[X,Y]]\Big) + \ldots
$$

* Note while it is habitual, **this statement is false**:

    $$
    e^Z = e^Xe^Y \implies Z = X+Y
    $$

    Due to the noncommutative propertiy of a general $X$ and $Y$ (a property of Lie algebra).

The next step is to relate some $X$ and $Y$ to our coherent state exponential $e^{fa^\dagger}$.

$$
X = f\sqrt\frac{m\omega}{2\hbar}, \qquad Y = f\frac{-ip}{\sqrt{2\hbar m \omega}}\\
[X,Y] = f^2/4
$$

Plugging this into the exponential expansions (note, only two term survives),

$$
e^{fa^\dagger} = e^Xe^Y = \exp\left[X + Y + \frac{1}{2}[X,Y]\right]
$$

Now we can solve for the probability density function (PDF),

$$
\braket{x}{f} = \bra{x}e^{f a^\dagger}\ket{0} = \left(\frac{m\omega}{\pi \hbar}\right)^{1/4}\exp\left[-\left(\sqrt\frac{m\omega}{2\hbar}x - f\right)^2 + \frac{1}{2}(f^2 - f^*f)\right]
$$

Notice that this PDF is very similar to a Gaussian with an extra exponential term.

## Properties

* Because coherent state are eigenvectors of a non-hermitian operator $a$, their states are not necessarily orthogonal.

    Given some coherent states $f \neq g$,

    $$
    \braket{g}{f} = e^{g^*f}e^{-\abs{g}^2/2}e^{-\abs{f}^2/2}
    $$

    Therefore coherent states do not form orthogonal or complete sets. Instead coherent states form **overcomplete sets**.