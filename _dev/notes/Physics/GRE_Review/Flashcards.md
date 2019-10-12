## Mathematics

Cartesian to Spherical Coordinates
:	$$
	\begin{gather}
	z = r \cos \theta\\
	x = r \sin \theta \cos \phi \\
	y = r \sin \theta \sin \phi
	\end{gather}
	$$

$dV$ in Polar Coordinates
:	$$
	dV = r^2 \sin\theta ~ dr d\theta d\phi
	$$

$dV$ Rotating Circle
: Imagine rotating a circle with some area mapping out the sphere
	$$
	dV = 2 \pi r^2 \sin\theta ~ dr d\theta
	$$

$dV$ Radial Spherical Shell
: Imagine a spherical shell with some surface area expanding out to a bigger sphere
	$$
	dV = 4\pi r^2 dr
	$$

## Rotational Mechanics

Solving Conservation of Momentum
: 1. Try dimension analysis
	2. Try direction conservation
	3. Otherwise, algebra


Angular Momentum (Linear)
:	$$ \vec L = \vec r \times \vec p $$


Angular Momentum (Rotational)
:	$$ \vec L = I \vec \omega $$

Moment of Inertia
:	The second mass moment of radius (the first mass moment is the center of mass)
	$$ I = \int r^2 dm $$

Mass From Density
:	$$ M = \int \rho dV $$

Parallel Axis Theorem
: The moment of inertia at the center of mass can describe any moment of inertia at another parallel axis
	$$
	I_\parallel = I_\text{CM} + Mr_\perp^2
	$$

Torque from Force
:	$$
	\vec \tau = \vec r \times \vec F
	$$

Torque from Angular Momentum
:	$$
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
:	$$
	\frac{d}{dt}\frac{\partial \mathcal L}{\partial \dot q} = \frac{\partial \mathcal L}{\partial q}
	$$


Conjuagte Momentum
:	$$
	p = \frac{\partial \mathcal L}{\partial \dot q}
	$$

When is the Conjugate Momentum Conserved?
: When the Lagrangian or Hamiltonian is independent of $q$
	$$
	\frac{\partial \mathcal L}{\partial q} = \frac{\partial \mathcal H}{\partial q} = 0
	$$

Hamiltonian
:	$$
	\sum_{i}p_i \dot q_i - \mathcal L
	$$

When is Hamiltonian Time-Independent?
: When potential energy is indepndent of time or velocity.
	$$
	\frac{d}{dt} U = 0 \quad \text{or} \quad \frac{d}{d\dot q} U = 0
	$$

Time-Independent Hamiltonian
:	$$
	H = K + U
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
:	$$
	U_\text{eff}(r) = \frac{\ell^2}{2mr^2} + U(r)
	$$

Reduced Mass
: The mass of the barycenter in the reduced mass frame.
	$$
	\mu = \frac{m_1m_2}{m_1 + m_2}
	$$

## Springs

Hooke's Law
:	$$
	F = -kx
	$$

EOM of Hooke's Law
:	$$
	x(t) = A \cos(\omega t + \phi); \qquad \omega = \sqrt{\frac{k}{m}}
	$$

Potential Energy of Hooke's Law
:	$$
	U = \frac{1}{2}kx
	$$

Springs in Series and Parallel
: Same rule as capcictors in electricity

Solving System of Springs
: For a system of springs with mass $m_i$ and $k_i$, the EOM has the LHS depending on the mass diagonal tensor and RHS  on the spring stiffness tensor

	$$
	M\ddot x = -Ax\\
	$$

	$$
	\begin{gather*}
	x(t) = ae^{i \omega t} \tag{anzatz}\\
	\Downarrow\\
	M \omega^2 a = Aa\\
	\end{gather*}
	$$

	Solving for $\omega^2$ by taking the determinant of,

	$$
	\det\left(A - M\omega^2 \right) = 0
	$$

Synchronous Oscillation Frequency
: For a system of springs, the lowest frequency mode is the synchronous oscillation.

Force of Dampening
:	$$
	F_\text{damp} = -b\dot x
	$$

Dampened Spring Solutions
: For $\beta = b/2m$ and $\omega_0 = \sqrt{k/m}$,
	1. Underdamped ($\beta^2 < \omega_0^2$)
	$$
	x(t) = Ae^{-\beta t}\cos(\omega t - \delta); \qquad \omega = \omega_0^2 - \beta^2
	$$
	2. Critically Damped ($\beta^2 = \omega_0^2$)
	$$
	x(t) = Ae^{i \omega_0 t}
	$$
	3. Overdamped ($\beta^2 > \omega_0^2$)
	$$
	x(t) = Ae^{-i \beta t}
	$$

Harmonic Driven Spring
: We can only write the differential equation,

	$$
	\ddot x + 2\beta \dot x + \omega_0^2 x = A\cos\omega t
	$$

Harmonic Resonating Frequency
:	$$
	\omega_R^2 = \omega_0^2 - 2\beta^2
	$$

Harominc Driven Amplitude
: We can only write the proportionality
	$$
	D \propto \frac{1}{\abs{\omega_0^2 - \omega^2}}
	$$

## Fluid Mechanics

Bernoulli's Principle
:	$$
	\frac{v^2}{2} + gz + \frac{P}{\rho} = \text{constant}
	$$

Fluid Conservation
:	$$
	\rho v A \Delta t = \text{constant}
	$$

Pressure Force
:	$$
	F = PA
	$$

Buoyant Force
:	$$
	F_B = \rho V_d g
	$$

	* $V_d$ : Volume dispersed

## Electrostatics

Maxwell Equations for Electrostatics
:	$$
	\begin{gather*}
	\nabla \cdot \vec E = \frac{\rho}{\epsilon_0}\\
	\nabla \times \vec E = 0
	\end{gather*}
	$$

Electric Field
:	$$
	\vec E(\vec r) = \frac{1}{4\pi\epsilon_0}\frac{Q}{r^2}
	$$

Coulomb Force
:	$$
	\vec F = q \vec E
	$$

Electric Potential Field
: Because the elecric field is conservative, its electric potential which is its gradient is a scalar field.
	$$
	\vec E = - \nabla V
	$$
	Alternatively you may use,
	$$
	V(\vec r) = \frac{1}{4\pi\epsilon_0} \int \frac{\rho(\vec r')}{\abs{\vec r - \vec r'}} d^3\vec r
	$$

Voltage
: The electric potential to create a electrical configuration moving a charged particle from often $a=\infty$ to $b$.
	$$
	V_{ab} = \int_a^b \vec E \cdot d \vec l
	$$

Gauss' Law
:	$$
	\oint \vec E(\vec r) \cdot d \vec S = \frac{Q_\text{enc}}{\epsilon_0}
	$$

E-field of an Infinite Plane
:	$$
	\vec E = \frac{\sigma}{2 \epsilon_0} \hat n
	$$

E-field of a Line and Cylinder
:	$$
	\vec E = \frac{\lambda}{2\pi \epsilon_0 r} \hat r
	$$

Facts about Conductors
: * Electric field inside is zero
	* Net charge density inside is zero
	* Any net charge is at the surface
	* Electric field is always perpendicular to the surface
	* Electric potential is continuous at all boundaries

Method of Images
: Follow two rules:

	* Don't count the energy created in the image
	* Directly calculate the electric field inside the image

Electric Work
:	$$
	W = \frac{1}{2} \int V(\vec r) ~ dQ
	$$

Electric Field Energy
:	$$
	\begin{align*}
	U_E &= \frac{\epsilon_0}{2} \int \abs{E}^2 ~ d^3r\\
	&= qV
	\end{align*}
	$$

Electric Power
:	$$
	\begin{align*}
	P &= IV\\
	&= I^2 R
	\end{align*}
	$$

Capacitance
:	$$
	C = \frac{Q}{V}
	$$

Parallel Plate Capacitance
:	$$
	C = \frac{A\epsilon_0}{d}
	$$

Capcitance Energy
:	$$
	U_C = \frac{1}{2}CV^2
	$$

## Magnetostatics

Maxwell Equations for  Magnetostatics
:	$$
	\nabla \cdot \vec B = 0\\
	\nabla \times \vec B = \mu_0 \vec J
	$$

Ampere's Law
:	$$
	\oint_C \vec B \times d\vec l = \mu_0  I_\text{enc}
	$$

Lorentz Force
:	$$
	\begin{align*}
	\vec F &= q (\vec v \times \vec B)\\
	&= I (d\vec l \times \vec B)
	\end{align*}
	$$

Biot-Savart Law
:	$$
	\vec B(\vec r) = \frac{\mu_0 I}{4 \pi}\int\frac{d\vec l \times \hat{\vec r'}}{r'^2}
	$$

3 Standard Problems of Magnetostatics
:	1. Find B-field given current configuration
		Use Ampere's law if symmetric else Biot-Savart
	2. Find forces on a wire given charge in a B-field
		Use Loretnz force
	3. Find energy of the B-field
		Integrate

B-field of Infinite Wire
: Using Ampere's law on a cylinder
	$$
	\vec B = \frac{\mu I}{2 \pi r}
	$$

B-field of Solenoid
: Using Ampere's law on a square loop of size $l$, where $n$ is the number of windings per length.
	$$
	B = \mu_0 n I
	$$

B-field of Toroid
: A curved and closed loop solenoid with $N$ windings,
	$$
	B(r) = \frac{\mu_0 N I}{2\pi r}; \qquad R_\text{in} < r < R_\text{out}
	$$

B-field Work
: The magnetic field does no work as the Lorentz force is perpendicular to the magnetic field.

B-field Energy
:	$$
	\mu_B = \frac{1}{\mu_0}\int{B^2 ~d^3\vec r}
	$$

Boundary Condition
: Opposite of the magnetic field, so only the parallel component exists. For a surface current $\vec K$ adjacent to the surface $\hat n$,

	$$
	\Delta B_\parallel = \mu_0 \vec K \times \hat n
	$$

Cyclotron Force
: A charged partricle moving non-parallel to a uniform magnetic field experience a force on the axis perpendicular to both the velocity and magnetic field,

	$$
	\begin{gather*}
	\text{dir}(B) = \hat z, \quad \text{dir}(v) = \hat y\\
	\vec F = qvB(\hat y \times \hat z) = qvB\hat x
	\end{gather*}
	$$

Cyclotron Radius
:	$$
	R = \frac{mv}{qB}
	$$

Cyclotron Angular Frequency
:	$$
	\omega = \frac{qB}{m}
	$$

## Electrodynamics

Maxwell Equations Correctoins
:	$$
	\begin{align*}
	\nabla \times \vec E &= -\frac{\partial \vec B}{\partial t}\\
	\nabla \times \vec B &= \mu_0 \vec J + \mu\epsilon_0 \frac{\partial \vec E}{\partial t}
	\end{align*}
	$$

Faraday's Law
: A changing magnetic field produces an electric field,

	$$
	\oint \vec E \cdot d \vec l = -\frac{d \Phi_B}{d t}
	$$

Electromotive Force
: A misnomer for the electric potential produced by a changing magnetic field,

	$$
	\varepsilon = \frac{d\Phi_B}{dt}
	$$

Inductance
:	$$
	L = \frac{\Phi_B}{I}
	$$

Solenoid Inductance
:	$$
	L = \frac{\mu_0 N^2 A}{l}
	$$

Solenoid Energy
: The energy stored in the solenoid is generated from the magnetic field
	$$
	U_L = \frac{1}{2}LI^2
	$$

Ampere's Law for Electrodynamics
: The charge enclosed is now dependent on the electric flux,

	$$
	\oint_C \vec B \cdot d \vec l = \mu_0 \epsilon_0 \dot\Phi_E
	$$

Electric Dipoles
:	$$
	\vec p = \int \vec r ~ dQ
	$$

Electric Dipole Potential
:	$$
	V(\vec r) = \frac{1}{4\pi\epsilon_0} \frac{\vec p \cdot \vec r}{r^2}
	$$

Torque of Electric Dipole in External E-field
:	$$
	\tau = \vec p \times \vec E
	$$

Electric Dipole Energy
:	$$
	U = -\vec p \cdot \vec E
	$$

E-field of an Electric Dipole
:	$$
	E \propto \frac{\vec p}{r^3}
	$$

Magnetic Dipole
:	$$
	\vec m = I\vec A
	$$

Torque of Magnetic Dipole in External B-Field
:	$$
	\tau = \vec m \times \vec B
	$$

Magnetic Dipole Energy
:	$$
	U = -\vec m \cdot \vec B
	$$

B-field of a Magnetic Dipole
:	$$
	B \propto \frac{\vec m}{r^3}
	$$

Charge Density from Polarization
: For the poalrization vector $\vec P$,

	$$
	\begin{gather*}
	\frac{dq}{dA} = \vec P \cdot \hat n\\
	\frac{dq}{dV} = -\nabla \cdot \vec P
	\end{gather*}
	$$

Dielectric Capacitance
:	$$
	\begin{gather*}
	\epsilon = \kappa \epsilon_0\\
	C = \frac{\kappa \epsilon_0 A}{d}
	\end{gather*}
	$$

## Electromagnetic Waves

Wave Equation
: The laplacian if the E-field and B-field is related to its own acceleration

	$$
	\begin{gather*}
	\nabla^2E = \mu_0 \epsilon_0 \ddot E\\
	\nabla^2B = \mu_0 \epsilon_0 \ddot B
	\end{gather*}
	$$

Speed of Light
:	$$
	c = 1/\sqrt{\mu_0\epsilon_0}
	$$

Wave Solution
:	$$
	\begin{align*}
	\vec E &= E_0 e^{i(kr - \omega t)} \\
	\vec B &= \vec E / c
	\end{align*}
	$$

Poynting Vector
:	The vector of propogration that points along the wave's momentum

	$$
	\vec S = \frac{1}{\mu_0}(\vec E \times \vec B)
	$$

Radiant Flux
:	Magnetude of the poynting vector

	$$
	F = \abs{\vec S}
	$$

Intensity
:	Time-average flux

	$$
	\avg{F} = \frac{1}{2}c\epsilon_0E_0^2
	$$

Radiation Power of Accelerating charge
:	$$
	P \propto q^2 \ddot x^2
	$$

Oscillating Electric Dipole Intensity
:	$$
	\avg{S} \propto \frac{p_0^2\omega^4\sin^2\theta}{r^2}
	$$

Oscillating Electric Dipole Average Power
:	$$
	\avg{P} \propto P_0^2\omega^4
	$$

Oscillating Magnetic Dipole Average Power
:	$$
	\avg{P} = m_0^2\omega^4
	$$

