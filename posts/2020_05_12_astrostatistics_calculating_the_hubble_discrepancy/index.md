---
title: "Astrostatistics — Calculating the Hubble Discrepancy"
tag: ["astronomy", "statistics"]
description: "We take a look at the famously used metric to compare Hubble constant predictions, the Hubble discrepancy."
image: /static/default.jpg
---

Reiss et al. (2019) stated that their $H_0$ estimate ($74.03 \pm 1.42~\mathrm{km/s/Mpc}$) has a difference of $4.4\sigma$ compared to Planck CMB 2018 estimate ($67.4 \pm 0.5~\mathrm{km/s/Mpc}$).

> Removing any one of these anchors changes $H_0$ by less than 0.7%. The difference between $H_0$ measured locally and the value inferred from Planck CMB and ΛCDM is $6.6 \pm 1.5\mathrm{km~s^{-1}~Mpc^{-1}}$ or $4.4\sigma$ ($P = 99.999\%$ for Gaussian errors).<br>-- Reiss et al. (2019)

This is a statement of discrepancy with $4.4\sigma$ being the value called the "difference in sigma" (hereon called the discrepancy to prevent confusion). Naturally, the difference between the experiment's estimates is a good start to get a sense of how to experiment disagree with each other.

$$
\Delta = H_0^R - H_0^P
$$

Where $H_0^R$ and $H_0^P$ are the Hubble estimate from Reiss et al. (2019) and Planck CMB respectively. The estimates has a distribution where $74.03~\text{km/s/Mpc}$ and $67.4~\text{km/s/Mpc}$ are their respetive mean and the errors comes from their respective standard deviations (SDs). The difference $\Delta$ being compose of two estimates with distribution also has its own distribution with mean and SD:

$$
\begin{align*}
\text{Mean}(\Delta) &= E\left(H_0^R\right) - E\left(H_0^P\right) = 6.6~\mathrm{km/s/Mpc}\\
\text{SD}(\Delta) &= \sqrt{SD\left(H_0^R\right)^2 - SD\left(H_0^P\right)^2} = 1.5~\mathrm{km/s/Mpc}
\end{align*}
$$

The discrepancy $z$ (letter used for reasons explained in the next section), is calculated by dividing the two,

$$
z = \abs{\frac{\text{Mean}(\Delta)}{\text{SD}(\Delta)}} = 4.4 \sigma
$$

Though it may be obvious from the equation, to explain why it's in units of sigma and why we can treat it the same way as $N$-sigma significance (i.e., with arguments from hypothesis test), you need to look at what discrepancy tells you other than this equation.

### Diving into the Statistics
Because we have a confidence interval for an estimate of $H_0$, we are assuming the estimate has a probability distribution. In many cases such as this, the probability distribution comes from posterior distribution or the likelihood distribution.

Consequently, $\Delta$ being the difference of two estimates means $\Delta$ also has its own probability distribution, aptly composed of the joint probability of the two estimates. The distribution of $\Delta$ represents the chance that the two estimate differ by an amount for all possible amounts.

To make an argument of discrepancy is to argue whether or not two experiments agree with each other; that is, to make a hypothesis that the two experiment agrees (the null hypothesis) or that they disagree (the alternative hypothesis). We cannot reject that two experiment agrees with each other if their discrepancy is small. We quantify this discrepancy setting it to be a statistics of their difference $\Delta$ called the z-score* (hence why it's called $z$).

$$
z = \abs{\frac{\text{Mean}(\Delta) - 0}{\text{SD}(\Delta)}} = \abs{\frac{\text{Mean}(\Delta)}{\text{SD}(\Delta)}}
$$

The z-score or discrepancy is the number of SDs that the difference under the null hypothesis (i.e., $\Delta = 0$ the two experiment fully agrees) is away from the observed distribution of $\Delta$.

> *We only care about the absolute value of the z-score as the negative signs do not matter.

<!-- ### Misconception: Discrepancy is Relative
A common misconception that authors contributed to is not directly stating the reference hypothesis.

For the Hubble tension, while Reiss et al. (2019) claims Planck CMB 2018 is $4.4\sigma$ away, Planck CMB 2018 can claim Reiss et al. (2019) to be,

 $$
 \begin{align*}
 \frac{74.03 - 67.4}{1.42} = 4.48 \approx 4.4 \\
 \frac{74.03 - 67.4}{0.5} = 15.1 \approx 15
 \end{align*}
 $$ -->