---
title: The Lagrangian and Calculus of Uariations
---

Let's begin with motivation of the use of calculus of variations in physics by Fermat's Principle.

---

## Fermat's Principle - Path of Least Time

Fermat's principle is a successful explanation of Snell's Law. The principle states that light wishes to travel the least time and to do so when changing medium, light wishes to get out of the slow medium as fast as possible; this is done by traveling at an angle where the path length in the slower medium is the shortest.

The length between two points in a plane follows the equation,

$$
\begin{equation}
    \d s = \sqrt{\d x^2 + \d y^2}
\end{equation}
$$

From the definition of the derivative of $y$, solving for $\d y$ gives

$$
\begin{equation}
    \d y = y'(x)\d x
\end{equation}
$$

Plugging this into the path length differential,

$$
\d s = \sqrt{\d x^2 + y'(x)^2\d x^2} = \sqrt{1 + y'(x)^2}~\d x
$$

We are now ready to write the length between two points as a function of $y'(x)$,

$$ \begin{align}
    S &= \int_1^2{ds} = \int_{x_1}^{x_2}{\sqrt{1+y'(x)^2}~\d x}
\end{align} $$

---

To get the the Lagrangian, unfortunately we need more calculus. We need calculus of variations which starts out by learning about functional derivatives.

## Functional Derivatives

A function is formally defined as taking some value input that lives in the one space to another value that lives in possibly another.

$$
f: \mathbb S_1 \rightarrow \mathbb S_2
$$

It is not at all a surprise that functions can take functions as an input. You learn this as composite functions,

$$
h'(x) = f \circ g = f(g(x))
$$

The derivative of the composite function $h$ is given by the chain rule,

$$
h'(x) \equiv \frac{\d h}{\d x} = f'(g(x))g(x) + f(g(x))g'(x)
$$

What I want you to pay attention to is that your typical derivative is always a differential with respect to $x$.

What happens if you expand that to not change $x$ but literally change the function $g(x)$ (e.g., $g(x) = x \rightarrow x+1$)? How does $h$ respond to this? This kind of change is the basis for **functional derivatives**. As we all started derivatives with the limits, the functional derivative version is which we replace the differential $\d$ with the functional differential $\delta$,

$$
h = F[g(x)]\\
\frac{\delta h}{\delta g(x)} = \lim_{\epsilon \rightarrow 0} \frac{F[g(x') + \epsilon \delta(x-x')] - F[g(x')]}{\epsilon}
$$

* Note that you should be very explicity the WRT is $g(x)$ not just $g$.

The rules of applying the functional differential operator perculiar. I recommend looking at a calculus book for rules and examples. An important identity we will be using is,

$$
F[g] = \int \left(\frac{\d g}{\d x}\right)^2~ \d x\\
\frac{\partial F}{\partial g(x)} = -2g''(x)
$$

## Lagrangian and the Principle of Least Action

Now, the **Lagrangian** is a function that is simply the difference between work and potential. Intuitively though not commonly phrased, the Lagrangian amount of activity relative to its potential.

$$
\mathcal L \equiv K - U
$$

Objects with a large amounts of kinetic energy compared to its potential has done a lot of work to get there (so think of this case as activeness). Objects with high potential has the potential to do more (so think of this case as laziness).

The definition of the Lagrangian was motivated by the functional derivative of the time-average kinetic and potential energies,

$$
\avg{K} = \frac{1}{T}\int_{0}^{T} \frac{1}{2} m \dot x^2 ~\d t\\
\frac{\delta \avg{K}}{\delta x} = - \frac{m \ddot x}{T}
$$

$$
\avg{U} = \frac{1}{T}\int_{0}^{T} U[x(t)] ~\d t\\
\frac{\delta \avg{U}}{\delta x} = \frac{U'[x(t)]}{T}
$$

Notice that these two are equal since $U'[x(t)] = m\ddot x(t)$,

$$
\frac{\delta \avg{K}}{\delta x} = \frac{\delta \avg{U}}{\delta x}\\
\frac{\delta}{\delta x}\left(\avg{K} - \avg{U}\right) = 0
$$

The average difference of the kinetic and potential energy does not change over space; We assign the name of the general energy difference to be the Lagrangian.

However, this motivation itself has not consider the motion of an object (its trajectory) which requires the time part. We define **action** $S$, to be the integral of the Lagrangian across some period $T$ (a given trajectory)

$$
S = \int_{0}^{T} L~ \d t
$$

The integral can be easily solved in terms of the average energies and notice the derivative goes to zero,

$$
S = \tau(\avg{K} - \avg{U})\\
\frac{\delta S}{\delta x(t)} = 0
$$

This relation states that objects prefer to choose a trajectory $x(t)$ that gives an extreme (or stationary) action. Intuitively this extrema should be the minimum (this is not always the case) thus this relation is called the **principle of least action**.