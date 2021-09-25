---
title: Extinction
---

## Total Extinction

The **absolute extinction** is the amount of magnitude reduced from the intrinsic magnitude. Like all extinctions, this depends on the emitted wavelength.
By definition, the absolute extinction is the difference between the observed and intrinsic magnitudes, and is always zero or positive.

\[
  A(\lambda) \equiv m_\text{observed} - m_\text{intrinsic}
\]

This definition applies to either absolute or apparent magnitude.

## Reddenning

Because bluer light is more attenuated by dust, the spectral density on the bluer side is reduced. This effect is called **reddening**. Do not confuse this with **redshift** as the spectral lines due to reddenning is unaffected by dust.

### Color Excess
In practice, with filter passbands, the measured difference between the bluer and redder side of the spectral density is done by calculating the difference of two passbands. This is called the **color index**. The color index after extinction will increase observed color index. Taking the difference between the two gives you a quantity for reddenning called the **color excess**.

Historically, the common passbands derived in the 1950s were the UBV photometric bands. Because of this, most literature express color index and excess using the two most abundant observation passbands (B and V) therefore the most common color index is the $B-V$ color. The order of these bands set so that positive values are redder.

\begin{align}
  E(B-V) &\equiv (B-V)_\text{observed} - (B-V)_\text{intrinsic} \\
  &= A(B) - A(V)
\end{align}

## Absolute Extinction
The absolute extinction is the total extinction normalized by a chosen standard total extinction to allow comparison between other wavelengths. Historically the standard is the V-band therefore the absolute extinction compares how sensitive the wavelength is to dust compared to the V-band.

As a function of $\lambda$, this is called the **extinction law** which gives sensitivity to dust across all wavelengths.

\[
  f(\lambda) = \frac{A(\lambda)}{A(V)}
\]

### Extinction Law

## Extinction Parameter

The extinction parameter $R$, is a useful quantity because it correlates with dust grain size

\begin{align}
  R_V &\equiv \frac{A(V)}{E(B-V)} \\
  &\equiv \frac{A(V)}{A(B) - A(V)}
\end{align}