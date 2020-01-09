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

## Formalism

To deal with the existential crisis that the chance of a single-value event $\set{X=x}$ is,

$$
P(X = x) = 0
$$

because the area for at $X=x$ is zero (rather poorly defined), we develop the Reynmann interpretation of integrals to the formalism of continuous probability. Take $dx$ as some small infinitestimal width for some interval $(x-dx, x+dx)$ and define $dx$ to be an event such that,

$$
P(X \in dx) \equiv P(x-dx < X \le x+dx) = \int_{x - dx}^{x+dx} f(x) dx
$$

Asymptotically, as $dx \to 0$ the integral dissapears to become the Reinman integral,

$$
\boxed{P(X \in dx) \sim f(x) dx}
$$

::: Note
A physics formality defines the differential form of the probability ,

$$
dP = fdx
$$
:::

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