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

$dV$ Cylindrical Coordinates
:	$$
	dV = r ~dzdrd\theta
	$$

Sine-Cosine Relative Phase
: Sine and Cosine are off by $\pi/2$ phase,

	$$
	\cos(x) = \sin(\pi/2 - x)
	$$

Derivative of Logarithm
:	$$
	\frac{\partial }{\partial x}\Big[\ln f(x)\Big] = \frac{f'(x)}{f(x)}
	$$

Hyperbolic Sine to Exponential
:	$$
	\sinh x = \frac{e^x - e^{-x}}{2}
	$$

Hyperbolic Cosine to Exponential
:	$$
	\cosh x = \frac{e^x + e^{-x}}{2}
	$$

Stirling Formula
:	The factorial as $n \rightarrow \infty$ goes as,

	$$
	\log(n!) \sim n \log n - n
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
	U = \frac{1}{2}kx^2
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
	\begin{gather*}
	x(t) = Ae^{-\beta t}\cos(\omega t - \delta)\\
	\omega = \omega_0^2 - \beta^2
	\end{gather*}
	$$
	2. Critically Damped ($\beta^2 = \omega_0^2$)
	3. Overdamped ($\beta^2 > \omega_0^2$)

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
:	For a single charge $Q$,

	$$
	W = Q \int_a^b E \cdot dr = QV_{ab}
	$$

	For multiple charges, a double counting factor is corrected. It is much easier and intuitive to write this for the discrete case

	$$
	W = \frac{1}{2} \sum q_i V(r_i)
	$$

Electric Field Energy
:	$$
	U_E = \frac{\epsilon_0}{2} \int \abs{E}^2 ~ d^3r
	$$

Electric Power
:	$$
	P = IV
	$$

Ohm's Law
:	$$
	V = IR
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
	\begin{gather*}
	\nabla \cdot \vec B = 0\\
	\nabla \times \vec B = \mu_0 \vec J
	\end{gather*}
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
: Opposite of the electric field, so only the parallel component exists. For a surface current $\vec K$ adjacent to the surface $\hat n$,

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

	The last equation is very useful relating to circular force

	$$
	\begin{gather*}
	qvB = m\frac{v^2}{r}\\
	B = \left(\frac{m}{q}\right)\frac{v}{r}
	\end{gather*}
	$$

	With the RHS, you can solve for the cyclotron radius $r$ and the angular frequency $v/r$.

## Electrodynamics

Maxwell Equations Corrections
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

## Circuits

## Waves

Wave Equation
:	$$
	\ddot f = \dot x^2 f''
	$$

Wave Solutions
: The solution of the wave equation is either traverse waves or standing waves:

	1. Traverse Waves
		$$
		f(x,t) = A\cos(kx - \omega t + \delta)
		$$

	2. Standing Waves
		$$
		g(x,t) = \frac{1}{2}\Big[f(x+vt) + f(x-vt)\Big]
		$$

Wavenumber and Wavelength Relation
: The wavenumber is the number of waves in the length of $2\pi$
	$$
	k = \frac{2\pi}{\lambda}
	$$

Frequency and Angular Frequency Relation
: The angular frequency is the number rotations in $2\pi$ per second.
	$$
	\omega = 2\pi f
	$$

Dispersion Relation
: The dispersion relation is the relation between $k$ and $\omega$

	$$
	\omega(k) = vk
	$$

Phase Velocity
: The dispersion relation for a single wavenumber

	$$
	v_\text{phase} = \frac{\omega}{k}
	$$

Group Velocity
: The dispersion relation for each wavenumber

	$$
	v_\text{group} = \frac{d\omega}{dk}
	$$

Index of Refraction
: By the dispersion relation,

	$$
	\frac{\omega}{k} = \frac{c}{n}
	$$

	The index of refraction is the amount at which light is slowed down to a velocity at some medium $v$ with index of refraction $n$.

	$$
	n = \frac{c}{v}
	$$

Malus' Law
: Light is comes out a polarizer in one direction giving the intensity a cosine relation due to the dot product

	$$
	I = I_0 \cos^2\theta
	$$

Brewster's Angle
: The angle at which incident light is split into a polarized reflected light and the refracted light is perpendicular to the reflected light

	$$
	\theta_B = \arctan\left(\frac{n_2}{n_1}\right)
	$$

Phase Difference from Path Length Differnce
: Two idendical waves in frequency emitted at the same time but end up travelling a different path length of difference $\Delta x$ has a phase difference of

	$$
	\Delta \delta = k \Delta x
	$$

Interference Phase and Path Length
: Two identical waves on collision will constructively or destructively intefere with each other at the even or odd $\pi$ phase difference respectively.

	$$
	\begin{gather*}
	\Delta \delta = 2m \pi \tag{constructive}\\
	\Delta \delta = (2m + 1)\pi \tag{destructive}\\
	\Big\Downarrow \\
	\Delta x = \lambda m \tag{constructive}\\
	\Delta x = \lambda \left(m + \tfrac{1}{2}\right) \tag{destructive}\\
	m \ge 0;
	\end{gather*}
	$$

Double Slit Interference
: The path length for Young's double slit experiment is

	$$
	\Delta x = d\sin\theta
	$$

	It's interference maxima and minima are whole and halve factors of the wavelength respectively

Single Slit Interference Minima
: 	It's interference maxima and minima are opposite of the classical rule. This time the minima is at whole wavelengths

	$$
	\begin{gather*}
	a \sin \theta = m\lambda \tag{minima}\\
	m \ge 1;
	\end{gather*}
	$$

Optical Path Length
: Wave going through a mediums of index of refraction $n$ has a phase shift depending on $n$ and how far its traveled in the medium $d$,

	$$
	\Delta \delta = knd
	$$

	This implies an effective or optical path length of,

	$$
	\Delta x = nd
	$$

Thin-Film Phase Shift
: In addition to optical path length, a wave traveling from a mediums $n_1$  to a thin film of $n=n_2$ can experience a $\pi$ phase shift if,

	$$
	\begin{gather*}
	n_2 > n_1 \tag{phase shift}\\
	n_2 < n_1 \tag{$\pi$ phase shift}
	\end{gather*}
	$$

	Thus the total phase shift for a wave through $n_2 > n_1$ of thickness $d$ and exitting is,

	$$
	\Delta \delta = 2kn_2d + \pi
	$$

Rayleigh Criterion (Circular Aperture)
: An emitter of two light sources of wavelength $\lambda$ separated at some distance $D$ is separable only if the angle follows,

	$$
	\sin\theta = 1.22 \frac{\lambda}{D}
	$$

	More often seen the time reversal of the setup, how close $d$ does two light sources separated by $\Delta x$ has to be for an aperature of diameter $D$.

	$$
	\tan \theta = \frac{\Delta x}{d} = 1.22 \frac{\lambda}{D}
	$$


Braggs Diffraction
: A crystal lattice with each node separated by distance $d$ has a index of refraction $n$ and experiences interference maxima at,

	$$
	d\sin\theta = \frac{n\lambda}{2}
	$$

Angle of Reflection
: The angle of incident is also the angle of reflection

	$$
	\theta_i = \theta_r
	$$

Angle of Refraction (Snell's Law)
:	$$
	\frac{n_1}{n_2} = \frac{v_1}{v_2} = \frac{\sin \theta_2}{\sin \theta_1}
	$$

	Often time used is use angles from the horizon $\alpha = \frac{\pi}{2} - \theta$,

	$$
	\frac{n_1}{n_2} = \frac{v_1}{v_2} = \frac{\cos \alpha_2}{\cos \alpha_1}
	$$

Focal Length
:	$$
	\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}
	$$

Lensmaker Equation
:	$$
	(n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)
	$$

Magnitifcation
:	$$
	m = -\frac{d_i}{d_o}; \qquad \begin{cases}m > 0 & \text{upright}\\ m < 0 & \text{inverted}\end{cases}
	$$

Rayleigh Scattering
:	$$
	I \propto I_0 \lambda^{-4}
	$$

Doppler Effect
:	$$
	\frac{f}{f_0} = \frac{\Delta v_r}{\Delta v_s} = \frac{c+v_r}{c-v_s}
	$$

	* $\Delta v_r$: Relative velocity of the wave to the receiver
	* $\Delta v_s$: Relative velocity of the wave to the source

## Thermodynamics

Canonical Ensemble
:	The set of all possible states (or outcome space) of an esemble of particles or microsystems given the following is fixed:

	* Number of particles
	* Volume
	* Temperature

Grand Canonical Ensemble
:	Same as canonical ensemble but the number of particles can change.


Maxwell-Boltzmann Statistics
:	The probability that a particle is in energy level $E_i$ is given by the Maxwell-Boltzmann distribution

	$$
	P(E_i) = \frac{e^{-\beta E_i}}{\sum_{i=1}^N e^{-\beta E_i}}
	$$

	Although inaccurate and prone to statistical errors, the LHS is often expressed as the expected proportion of particles in energy level $E_i$ or $P(E_i) = \avg{N_i}/{N}$

Boltzmann Factor
:	The numerator in the Maxwell-Boltzmann distribution. It's the unormalized likelihood that a particle is in some energy level $E_i$

	$$
	P(E_i) \propto e^{-\beta E_i}
	$$

Partition Function
:	Initially it's a tool to normalize the Maxwell-Boltzmann distribution, but it's found to be extremely useful in determining other quantities. The partition function is the sum of all Boltzmann factors

	$$
	Z = \sum e^{-\beta E_i}
	$$

Continuous Partition Function
:	$$
	Z = \frac{1}{N!h^{3N}}\int{\exp\Big[-\beta H(\Sigma p_i, \Sigma x_i)\Big]~\sum d^3p_id^3x_i}
	$$

Relativistic Non-Interacting Partition Function
:	Without potential energy, the Hamiltonian is just $E=\abs{\vec p}c$ which gives the partition function for one particle is

	$$
	\begin{align*}
	Z 	&=	\frac{V}{h^3N}\int{e^{-\beta \abs{\vec p} c} ~ d^3 p}\\
		&\propto VT^3
	\end{align*}
	$$

	In general the power rule is $T^{\dim \vec p}$ thus average energy is

	$$
	\avg{E} = (\dim \vec x) k_B T
	$$

Expectation of Energy from  Partition Function
:	The expectation of energy can be determined from the partition function.

	$$
	\avg{E} = \frac{\partial}{\partial \beta} \ln Z
	$$

Entropy
:	Entropy is simply defined as the \ln of the number of possible states $\Omega$ with the factor of Boltzmann constant:

	$$
	S = k_B \ln \Omega
	$$


Entropy from Partition Function
:	The entropy can be determined form the partition function.

	$$
	S = \frac{\partial}{\partial T}\left(k_B T \ln Z\right)
	$$

Equipartition Theorem
:	The internal energy of a system is contributed by a factor of $\frac{1}{2}k_B T$ for each degrees of freedom

	$$
	E_i = \frac{D}{2}k_B T
	$$

	A degree of freedom can be determined by the number of quadratic terms in the Hamiltonian

First Law of Thermodynamic
:	Internal energy of a system is increased by heat and decreased from the system doing work. Energy is not created or destroyed instead transfered from an external large resevoir

	$$
	\Delta U = Q - W
	$$

Second Law of Thermodynamic
:	Entropy cannot be decreased and obeys

	$$
	\Delta S \ge \int \frac{\delta Q}{T}
	$$

Third Law of Thermodynamic
:	At absolute zero $T=0$, the entropy is zero so the all particles collpase into one microstate.

Ideal Gas Law
:	The equation of state for non-interacting monoatomic particles of gas

	$$
	PV = Nk_B T
	$$

Van der Waals' Improvement of Ideal Gas
:	The equation of state adding particle interaction $b$ and size $a$ to the ideal gas.

Reversible Process
:	A quasistatic process which at first the system slowly does work into the system by slowly changing volume,

	$$
	\delta W = P d V
	$$

	In consequence,

	$$
	\delta Q = T \delta S
	$$

	The take away is that the entropy in the system changes at minimal

	$$
	\Delta S = \int  \frac{\delta Q}{T}
	$$

Quasistatic Process
:	A process that change very slowly that on every step it's in thermodynamic equilibrium

Adiabatic Process
:	A process that does not transfer heat

	$$
	\delta Q = 0
	$$

Isentropic Process
:	 A process that is both reversible and adiabatic so that entropy does not change

	$$
	\delta S = 0
	$$

Isentropic Ideal Gas
:	The ideal gas in an isentropic process follows

	$$
	\begin{gather*}
	PV^\gamma = \text{constant}\\
	\gamma = \frac{C_P}{C_V}
	\end{gather*}
	$$

Iso-Processes
:	Any problem with iso-something process often ask for work. To do this,

	1. Solve for work $\delta  W = P d V$ in terms of $P$
	2. Use $P$ from the equation of state.

Free Expansion of Ideal Gas
:	An adiabatic process at which the ideal gas eventually occupy the whole volume

	$$
	PV = \text{const}
	$$

	Additionally since $PV$ doesn't change, adiabatic ideal gas is also isothermal.

Fundamental Thermodynamic Identity
:	The differential form of the second law of thermodyanmic,

	$$
	dU = TdS - PdV
	$$

State Variables
:	The state variable can be dtermined from the thermodyanmic identity if you know the internal energy

	$$
	T = \frac{\partial U}{\partial S}\bigg\rvert_V
	$$

	$$
	P = -\frac{\partial U}{\partial V}\bigg\rvert_T
	$$

Heat Capacity
:	A material constant that is the amount of heat to change the temperature of the material.

	$$
	\begin{align*}
	C_V = \left(\frac{\partial Q}{\partial T}\right)_V \\
	C_P = \left(\frac{\partial Q}{\partial T}\right)_P
	\end{align*}
	$$

Heat Capcity from Equipartition Theorem
:	The equipartition theorem gives the internal energy as a function of temperature. This is useful to calculate heat capacity at constant volume

	$$
	C_V = \frac{\partial U}{\partial T}
	$$

Ideal Gas Heat Capacity
:	$$
	\begin{gather*}
	C_P - C_V = Nk_B\\
	\big\Downarrow\\
	\gamma = \frac{D+2}{D}
	\end{gather*}
	$$

Specific Heat
:	The heat capacity per mass
	$$
	c = \frac{C}{M}
	$$

	Useful for determining energy

	$$
	Q = mc\Delta T
	$$

Efficiency of Heat Engine
:	$$
	e = \frac{W}{Q_\text{in}} = 1 - \abs{\frac{Q_\text{out}}{Q_\text{in}}}
	$$

Carnot Efficiency
:	$$
	e = 1 - \frac{T_\text{out}}{T_\text{in}}
	$$

Carnot Cycle
:	Two isothermal process interleaved by two isentropic process. The internal energy at the beginning and end of the cycle is the same thus the work is

	$$
	\Delta W = \Delta T \Delta S
	$$

Ideal Gas Hamiltonian
:	$$
	H = \frac{p^2}{2m}
	$$

Ideal Gas Partition Function
:	$$
	\ln Z_N \propto N\ln\left(VT^{3/2}\right)
	$$

Ideal Gas Internal Energy
:	$$
	U = \avg{E} = \frac{3}{2}Nk_BT
	$$

Ideal Gas RMS Velocity
:	$$
	v_\text{rms} = \sqrt{\frac{(\dim \vec x) k_B T}{m}}
	$$

Ideal Gas Entropy
:	$$
	S = Nk_B \ln \frac{VT^{3/2}}{N} + \text{constants}
	$$

Speed of Sound in Ideal Gas
:	$$
	\begin{align*}
	c_s &= \sqrt{\gamma\frac{P}{\rho}}\\
		&= \sqrt{\gamma \frac{k_B T}{m}}
	\end{align*}
	$$

Occupation Number Distribution
:	The distribution of occupation number for an energy level $N_i$ is different depending on if the particles are bosons or fermions.

	$$
	F = \avg{N_i} = \frac{1}{\exp[\beta (E_i-\mu)] + 1} \qquad
	\begin{cases}
		+ & \text{Fermion} \\
		- & \text{Boson}
	\end{cases}
	$$

	The total average occupancy number sums across all possible energy level and all possible ways a particle can be at the energy level (i.e., the degeneracy)

	$$
	\avg{N} = \sum g(E_i)\avg{N_i}
	$$

Continuous Occupancy Number Distribution
:	The continuous distribution changes the degeneracy function to be the density of state function

	$$
	\begin{gather*}
	\rho = \frac{dg}{dE}\\
	\avg{N} = \int \rho(E)F(E)~dE
	\end{gather*}
	$$

Fermi Energy
:	$$
	E_F \propto \left(\frac{N}{V}\right)^{2/3}m^{-1}
	$$

## Special Relativity

Coordinate Tranform
:	For the person the S frame, the person sees the S' frame is moving away at velocity $v$.
	$$
	\begin{align*}
	t = \gamma (t' + \frac{v}{c^2}x)\\
	x = \gamma (x' + vt')\\
	\gamma = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}}
	\end{align*}
	$$

Simultaneity
:	Two events occuring at the same time for one frame, occurs at different times for the other

Time Dilation
:	Measuring time with fixed position $x'$

	$$
	\Delta t = \gamma \Delta t'
	$$

Length Contraction
:	Measure two points of an object with fixed time $t$
	$$
	L = \frac{L'}{\gamma}
	$$

Velocity Addition
:	$$
	\frac{v+u}{1 + \frac{vu}{c^2}}
	$$

Position Four-Vector
:	$$
	x^\mu = (ct, x, y, z)
	$$

Energy-Momentum Four-Vector
:	$$
	p^\mu = (E/c, p_x, p_y, p_z)
	$$

Lorentz Transform
:	$$
	\begin{pmatrix}
	\gamma & -\gamma \beta & 0 & 0\\
	-\gamma \beta & \gamma & 0 & 0\\
	0 & 0 & 1 & 0\\
	0 & 0 & 0 & 1\\
	\end{pmatrix}
	$$

Four-Vector Dot Products
:	The four-vector dot product is given by

	$$
	a \cdot b = a^0b^0 - a^1b^1 - a^2b^2 - a^3b^3
	$$

	Note that all four-vector dot product is Lorentz invariant

Energy-Momentum Formula
:	From expanding $p^2$ and taking the rest frame (the dot product is invariant)
	$$
	\begin{gather*}
	p^2 = m^2c^2\\
	E^2 = \abs{\vec p}^2 c^2 + m^2c^4
	\end{gather*}
	$$

Relativistic Doppler Shift
:	The doppler shift only depends on the relative velocity between the source and the observer
	$$
	\begin{gather*}
	\beta = \frac{v}{c}\\
	\frac{\lambda'}{\lambda} = \sqrt{\frac{1 + \beta}{1 - \beta}}
	\end{gather*}
	$$

Pythagorean Triples and Relativity
:	The pythagorean triples are useful for relativity to solve for $\gamma$ given $\beta$,

	$$
	(A,B,C) \to \left(\beta_1, \beta_2, 1 \right) \to (\gamma_2^{-1}, \gamma_1^{-1}, 1)
	$$

	A common one is $(3, 4, 5)$ such that,

	$$
	(\beta_1 = \tfrac{3}{5}, \beta_2=\tfrac{4}{5}, 1) \to (\gamma_2=\tfrac{5}{3}, \gamma_1=\tfrac{5}{4}, 1)
	$$

## Statistics

Error
: Error often mean the sample variance of some data sample $S = \set{X_1=x_1, X_2=x_2, \ldots, X_n=x_n}$. The error is whats known as the unbiased estimator of the underlying variance of the distribution $X_i$

	$$
	\sigma_S^2 = \frac{1}{n-1} \sum_{i=1}^n(x_i - \bar x)^2
	$$

	The unbiased estimator changes the normalization factor from $n \rightarrow n-1$. This effect disappears as the sample size reaches the population size $n \rightarrow N$.

	Errors are interpreted as Gaussian deviations from the true mean $x^*$ interpreted as the underlying true value.

	$$
	x^* = \bar x \pm \sigma_S
	$$

Error Propogation
:	Two measurements of the distribution $X$ and $Y$ has an effective error governed by error progation. If $X$ and $Y$ are independent,

	$$
	\sigma = \sqrt{\sigma_X^2 + \sigma_Y^2}
	$$

	Given the measurements are multivariate (i.e., the data points depends on more than one variable $z(x_1,x_2,\ldots x_n)$), the distributions are then multivariate.

	$$
	\sigma_z^2 = \sum_{i=1}^n \left(\frac{\partial z}{\partial x_i}\right)^2 \sigma_{x_i}^2
	$$

	Other rules of propgation for two measurements $A$ and $B$ are as follow

	$$
	\begin{gather*}
	\sigma(\alpha A) = \alpha \sigma_A\\
	\sigma(AB) = AB\sqrt{\left(\frac{\sigma_A}{A}\right)^2 + \left(\frac{\sigma_B}{B}\right)^2}\\
	\sigma(A/B) = \frac{A}{B}\sqrt{\left(\frac{\sigma_A}{A}\right)^2 + \left(\frac{\sigma_B}{B}\right)^2}
	\end{gather*}
	$$

Error of Poisson Process
:	The error (sample variance) in a sampling of a Poisson distribution is,

	$$
	\sigma_S = \sqrt{x}
	$$

	Where $x$ is the count of events occured within the sample period.

Poisson Waiting Time
:	The waiting time to observe a Poisson count or more mathematically the time between two Poisson count is distributed as the exponential part of Poisson.

	$$
	P(t) = \lambda e^{-\lambda t}
	$$

## Electronics

Impedence
: The impedence $Z$ is the phase and magnitude of a current given the source is AC of angular frequency $\omega$. The impedence ties into many classical E&M circuits.

	$$
	\begin{gather*}
	\text{Ohm's Law:} & V = IZ\\
	\text{Capcitor:} & Z = \frac{1}{i \omega C}\\
	\text{Inudctor:} & Z = i\omega L \\
	\text{Resistor:} & Z = R
	\end{gather*}
	$$

De-Morgan's Law
:	NAND and NOR gates and be disected as their individual OR and AND gates respectively

	$$
	\overline{A \cdot B} = \overline A + \overline B\\
	\overline{A + B} = \overline A \cdot \overline B
	$$

## Particle Interactions

Nuclei
: Facts about nuclei interactions

	* Are bigger than electrons thus gets stopped faster upon collision of particle field
	* Travel in straight lines because nuclei are heavier
	* Interact mostly with atomic electrons

Photons
: Facts about photon interactions

	* Photoabsorption is when photon is absorbed by the atom causing an electron to be emitted with energy,

		$$
		E_\text{max} = E_\gamma - \phi
		$$

	Where $\phi$ is the work function or more commonly the binding energy.

	* Compton Scattering is when photons elastically collide with an electron and both particles scatter. The scattered photon has the Compton wavelength

		$$
		\lambda = \frac{h}{m_ec}
		$$

	* At $E_\gamma \ge 2m_e c^2 \sim 10 \text{MeV}$, the nuclei's electric field can induce a photon to produce an electron-positron pair

Radioactive Decay
:	A substance of $N_0$ particles under radioactive decay, loses particles at the rate of exponential decay

	$$
	N = N_0 e^{-t / \tau}
	$$

	Where $\tau$ is the mean lifetime. Given multiple channels of decay the effective mean lifetime is

	$$
	\tau^{-1} = \sum_i\tau_i^{-1}
	$$

## Numbers to Remember

Hydrogen Ground State Energy
: $13.6$ eV

Electron Rest Mass Energy
: $511$ eV

Rayleigh Criterion Circular Coefficient
: $1.22$

Wein Displacement Constant
: $3 \times 10^{-3}$

CMB Temperature
: $2.7$ K

## Astrophysics

Redshift
:	The Doppler redshift is the factor that the observed wavelength expanded setting no expansion at $z=0$

	$$
	\frac{\lambda'}{\lambda} = 1 + z
	$$