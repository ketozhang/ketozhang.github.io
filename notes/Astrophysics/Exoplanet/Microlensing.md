---
title: Microlensing
---

Here we introduce discovering exoplanet with microlensing.

## Pros and Cons

* Does not depend on the flux of the host star and planet therefore we can detect faint ones
* However, distant and faint host star and planet makes it harder to characterize its properties
* Does not need accurate position (astrometry) or trajectory (radial velocity) to detect microlensing events.
* Since microlensing is short lasting, we barely see the planet orbits the host star thus there is little information about its orbit.
* The planet must lie within the eintsein radius. For typical microlensing setup, this places the planet at about $2$ to $4$ $\text{AU} (M/M_\odot)^{1/2}$
* Microlensing events are rare and unpredictable. Events where the planet and background star aligns are even more rare therefore we need high density regions like galactic bulges
* High density regions are susceptible to photometric noise and require high angular resolution to distinguish light signals.

## Gravitational Lensing Review

### Lens Equation for Point Mass

In the setup where the lens is a point mass, we have the observer (O), lens (L), background source (S), and the observed image (I). The lensing equation relates the angular of separations

\[
  \alpha = \theta_{IL} - \beta
\]

* $\alpha$, angle between I and S
* $\beta$, angle between S and L

All angles above is relative to the observer.

In terms of the actual deflection angle $\hat \alpha$ (i.e., relative to the lens and not the observer), we use the small angle approximation

\[
  \hat\alpha (D_S - D_L) = \alpha D_S\\
  \hat\alpha = \frac{D_S}{D_S - D_L} \beta
\]

With these observed properties, we can determine the gravitational properties from solving how much light bends at a distance $b$ away from the point mass lens. Now treating $\hat{\boldsymbol\theta}_{IS}$ and $\boldsymbol b$ as positonal vectors with the lens as the origin.

\[
  \hat{\boldsymbol \alpha} = \frac{4GM}{|\boldsymbol{b}|^2 c^2} \boldsymbol{b}
\]

> **Note**: Although not stated, this equation seems to assume the source light ray comes in parallel to the line of sight between the observer and lens. This is true if the $D_L$ is sufficiently large.

### Len Equation for Multiple Point Masses
For $N$ lens of mass $m_i$ and angular position $\theta_{m,i}$ all located on a plane (i.e., face-on the observer) at distance $D_L$, the effective deflection angle is additive

\[
  \boldsymbol \alpha(\theta_{IL}) = \frac{4G}{D_\text{rel} c^2} \sum_i^N{m_i \frac{\boldsymbol\theta - \boldsymbol\theta_{m,i}}{\lvert\boldsymbol\theta - \boldsymbol\theta_{m,i}\rvert^2}}\\
  D_\text{rel}^{-1} \equiv D_L^{-1} - D_S^{-1}
\]

## Gravitational Microlensing
### Single Lens

\[
  \theta = \beta + \frac{4GM}{c^2D_\text{rel}\theta}
\]

If the lens and source are exactly aligned ($\beta = 0$) then the image is a ring of the given angular radius known as the Einstein ring radius,

\[
  \theta_E \equiv \sqrt{\frac{4GM}{D_\text{rel}c^2}}
\]

The Einstein ring radius is a useful quantity to normalize all angles. In this scale, we define $u \equiv \beta/\theta_E$ and $y \equiv \theta/\theta_E$. Then the lens equation becomes,

\[
  u = y - y^{-1}
\]

The solution to this is similar to the quadratic equation,

\[
  \boxed{y_{\pm} = \frac{u \pm \sqrt{u^2 + 4}}{2}}
\]

Therefore if the source and lens are misaligned ($\mu \neq 0$) then there exist two images: the positive solution (major image) is on the same side as the lens and source; the negative solution (minor image) is on the opposite side.

The magnification is the determinant of the Jacobian of $u, y$. For small sources, the image elongates the source tangentially by the amount $y_\pm/u$ but compressed radially by the amount $dy_\pm/du$. Therefore the magnitifcation equation is,

\[
\boxed{
A_{\pm} = \left\lvert \frac{y_\pm}{u}\frac{dy_\pm}{du} \right\rvert = \frac{1}{2}\left[\frac{u^2}{u \sqrt{u^2 + 4}}\pm 1 \right]
}
\]

and total magnification,

\[
  A(u) = \frac{u^2 + 2}{u \sqrt{u^2 + 4}}
\]

A few edge cases for magnitification,

* If the source-lens separation is much smaller than the Einstein radius
  \[u \ll 1 \implies A \simeq 1/u\]
* If the source-lens separation is much larger than the Einstien radius
  \[u \gg 1 \implies A \simeq 1 + 2u^{-4}\]
* If the source-lens separation approaches infinity, the major image is the unlensed source and the minor image vanishes behind the lens.
  \[ u \to \infty \implies (y_+ \to u\,, A_+ \to 1); (y_- \to 0 \,, A_- \to 0)  \]

#### Paczynski light curve

For the single lens, the light curve is called the **Pacyzynski curve**.

The observer, source, and lens are all in relative motion. Regardless, of the actual motion in the perspective of the source and lens, what makes affects the image is the angular separation as seen by the observer. In other words we can only have to focus on the proper motion $\mu_\text{rel}$ which can be approximated as a constant.

\[
  \boxed{u(t) = \sqrt{\left(\frac{t-t_0}{t_E}\right)^2 + u_0^2}}\\
\]

where $t_E$ is the Einstein ring crossing time at a constant proper motion,

\[
  t_E = \frac{\theta_E}{\mu_\text{rel}}
\]

### Multiple Lens
For $N$ lens, we define $\boldsymbol{u}$ and $\boldsymbol{y}$ as the angular position vector of the lens-source and lens-image respectively. Like, single lens, these values are normalized by $\theta_E$ which in this case is the Einstein angular radius for the total lens mass $M \equiv \sum M_i$ as if it was a point source.

The lens equation is given by,

\[
  \boldsymbol{u} = \boldsymbol{y} - \sum_i^N \frac{M_i}{M} \frac{\boldsymbol y - \boldsymbol y_i}{|\boldsymbol y- \boldsymbol y_i|^2}
\]

TODO ...

### Planetary Lens