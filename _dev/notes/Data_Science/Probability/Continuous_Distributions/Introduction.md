---
title: Introduction
---

A probability density function (PDF) defines the continuous probability distribution. The PDF follows two basic rules,

1. 	$$
	\int_{-\infty}^{\infty} f(x) ~dx = 1
	$$

2.	$$
	P(a < X \le b) = \int_a^b f(x)~ dx
	$$

Where $f(x)$ is the conventional syntax for PDF.

## Cumulative Distribution Function

The cumulative distribution function (CDF) is defined the left limit to negative infinity,

$$
F(x) = P(X \le b) = \int_{-\infty}^b f(x)~ dx
$$

Where $F(x)$ is the conventional syntax for CDF.

Relation to PDF
: By the fundamental theorem of calculus,

	$$
	\begin{gather*}
	P(a < X \le b) = \int_a^b f(x)~ dx = F(b) - F(a)\\
	\Big\Downarrow\\
	f = \frac{dF}{dx}
	\end{gather*}
	$$

## Infinitestimal Interpretation

Treating integrals as Rienmann integrations, we can treat $dx$ as a infinitesimal (very tiny) interval around $x$. Using this we can now treat an event as $\set{X \in dx}$. The Reinmann trapezoid allows,

$$
P(X \in dx) = f(x) dx, \quad\text{as } dx \to 0
$$

Thus we define,

$$
f(x) = \frac{P(X \in dx)}{dx}, \quad\text{as } dx \to 0
$$

## Expectation

Analgous to discrete case, the expectation is,

$$
E(g(X)) = \int_{-\infty}^\infty g(x)f(x)~dx
$$

Existence
: The expectation exists only if the integral exists. A useful theorem is if,

	$$
	E(g(X)) = \int_{-\infty}^\infty \abs{g(x)}f(x)~dx < \infty
	$$

	then the expectation exists.