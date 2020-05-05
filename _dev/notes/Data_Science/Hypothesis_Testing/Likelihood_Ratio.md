---
title: Likelihood Ratio
---

The likliehood ratio statistics is used as a benchmark for m odel solution. The likelihood ratio is defined as the difference between the log-likelihood of the null $L_0$ and alternative hypothesis $L$.

$$
\Lambda \equiv L - L_0
$$

In most cases, the likelihood ratio refers to the maximum likelihoods of each hypothesis.

$$
\Lambda^* \equiv \mathop{\arg\max}_{H} L - \mathop{\arg\max}_{H_0} L_0
$$

## Relation to Chi-Squared Distribution

By **Wilks' theorem**, as the sample size grows large assuminng the null hypothesis is true, the following test statistics $D$ approaches the $\chi^2_k$ distribution

$$
\begin{gather*}
D = -2\log(\Lambda)&\\
D \sim \chi^2_k\,. \tag{as $N \to \infty$}
\end{gather*}
$$

* $k$: The degrees of freedom. It equals the difference in size of the free parameter space,

  $$
  k = \dim{\Theta} - \dim{\Theta_0} \,.
  $$