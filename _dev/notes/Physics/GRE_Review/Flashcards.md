## Mathematics

Cartesian to Spherical Coordinates
: $$
  \begin{gather}
  z = r \sin \theta\\
  x = r \cos \phi\\
  y = r\ sin \phi
  \end{gather}
  $$

$dV$ in Polar Coordinates
: $$
  dV = r^2 \sin\theta ~ dr d\theta d\phi
  $$

$dV$ Rotating Circle
: Imagine rotating a circle with some area mapping out the sphere
  $$
  dV = 2 \pi r^2 \sin\theta ~ dr d\theta
  $$

$dV$ Radial shell
: Imagine a spherical shell with some surface area expanding out to a bigger sphere
  $$
  dV = 4\pi r^2 dr
  $$

## Momentum

Solving Conservation of Momentum
: 1. Try dimension analysis
  2. Try direction conservation
  3. Otherwise, algebra


Angular Momentum (Cartesian)
: $$ \vec L = \vec r \times \vec p $$


Angular Momentum (Polar)
: $$ \vec L = I \vec \omega $$

Moment of Inertia (Point Particle)
: $$ I = mr^2 $$

Moment of Inertia (Continuous Object)
: $$ I = \int r^2 dm $$

Mass Form Density
: $$ M = \int \rho dV $$

Parallel Axis Theorem
: The moment of inertia at the center of mass can describe any moment of inertia at another parallel axis
  $$
  I_\parallel = I_\text{CM} + Mr_\perp^2
  $$

Torque from Force
: $$
  \vec \tau = \vec r \times \vec F
  $$

Torque from Angular Momentum
: $$
  \vec \tau = \frac{d}{dt} \vec L
  $$

Center of Mass
: Think the expectation value of the radius with respect to mass,
  $$
  r_\text{CM} = \avg{r}_m = \frac{1}{M}\int{r ~ dm}
  $$

## Lagrangian and Hamiltonian

Lagrangian
: 1. Solve for the kinetic term
    $$
    K = \frac{1}{2}m(\dot x^2 + \dot y^2 + \dot z^2)
    $$
  2. Convert the kinetic term and potential term into natural and easier coordinate system  (e.g., polar)
  3. Write the Lagrangian
    $$
    \mathcal{L}(q, \dot q, t) = K - U
    $$

Euler-Lagrange Equation
: $$
  \frac{d}{dt}\frac{\partial \mathcal L}{\partial \dot q} = \frac{\partial \mathcal L}{\partial q}
  $$


Conjuagte Momentum
: $$
  p = \frac{\partial \mathcal L}{\partial \dot q}
  $$

When is the Conjugate Momentum Conserved?
: When the Lagrangian or Hamiltonian is independent of $q$
  $$
  \frac{\partial \mathcal L}{\partial q} = \frac{\partial \mathcal H}{\partial q} = 0
  $$

Hamiltonian
: 1. Check for time or velocity independence in the potential
    $$
    \frac{d}{dt} U = 0 \quad \text{or} \quad \frac{d}{d\dot q} U = 0
    $$
  2. If potential is time-independent,
    $$
    H = K + U
    $$
  3. Otherwise use the full definition by first writing the Lagrangian
    $$
    \sum_{i}p_i \dot q_i - \mathcal L
    $$


## Orbits

Lagrangian (Polar)
: Used heavily in orbital mechanics
  $$
  \mathcal L = \frac{1}{2}m\dot r^2 + \frac{1}{2} mr^2 \dot\theta^2 + \frac{1}{2}mr^2 \sin \theta \dot\phi^2 - U(r, \theta, \phi)
  $$

Effective Lagrangian of Orbits
: By conservation of angular momentum, $\dot L=0$ allows us to choose a plane where the motion is only within the plane $\theta = \frac{\pi}{2}$.
  $$
  \mathcal L = \frac{1}{2}m \dot r^2 + \frac{1}{2} m \dot r^2 \dot \phi^2 - U(r, \phi)
  $$

Orbital Angular Momentum
: The conjugate angular momentum
  $$
  \begin{align*}
  \ell &= \frac{\partial L}{\partial \dot \phi} \\
  &= mr^2 \dot \phi \\
  &= mvr
  \end{align*}
  $$

Effective Force of Orbits
: From the Euler-Lagrange equation,
  $$
  F = m \ddot r = \frac{\ell^2}{mr^2} - U'(r)
  $$

Effective Potential of Orbits
: $$
  U_\text{eff}(r) = \frac{\ell^2}{2mr^2} + U(r)
  $$

Reduced Mass
: The mass of the barycenter in the reduced mass frame.
  $$
  \mu = \frac{m_1m_2}{m_1 + m_2}
  $$