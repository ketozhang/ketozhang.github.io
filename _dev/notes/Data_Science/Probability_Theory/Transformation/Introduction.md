---
title: Introduction
---

## Linear Transformation

Consider the linear transformation,

$$
Y = aX + b
$$

then the PDF of $Y$ follows

$$
f_Y(y) = \frac{1}{\abs{a}}f_X\left(\frac{y-b}{a}\right)
$$

Proof (for $a>0$)
: For any value $y$ in the range of $Y$, the CDF of $Y$ is then

	$$
	F_Y(y) = P(aX + b \le y) = P\left(X \le \frac{y-b}{a}\right) = F_X\left(\frac{y-b}{a}\right)
	$$

	By chain rule,

	$$
	\begin{align*}
	f_Y(y) &= \frac{dF_Y}{dy} \\
	&= \frac{dF_Y}{dx}\frac{dx}{dy}\\
	&= f_X\left(\frac{y-b}{a}\right)\frac{1}{a}\\
	\end{align*}
	$$

Proof (for $a<0$)
: Using the same prove as before, you can see that only the inequality sign flips which we can take the complement where the derivative ignores the complement.

## Examples

* Normal Density

	For $Z$ is the standard normal random variable, $X$ is the $\text{Normal}(\mu, \sigma)$ which is the linear transformation of $Z$,

	$$
	X = \sigma Z + \mu
	$$

* Uniform Density

	For $U_1$ is $\text{Uniform}(0,1)$ and $U$ is $\text{Uniform}(a,b)$, then $U$ is the linear transformation of $U_1$,

	$$
	U = (b-a)U_1 + a
	$$

## Monotonic Transformation

Let's begin by witha motivating example. Given uniform function $U \sim \text{Uniform}(0,1)$. and a monotonically increasing function $F$, we define $U$ to be the monotonically increasing trasnformation of $X$,

$$
X = F^{-1}(U)
$$

Then CDF of $X$ is,

$$
F_X(x) = F(x)
$$

In general let $g$ be a monotonically increasing function such that for any random variable $X$,

$$
Y = g(X)
$$

Then the CDF of $Y$ is,

$$
\boxed{F_Y(y) = F_X(g^{-1}(y))}
$$

Thus the PDF of $Y$ is,

$$
\boxed{f_Y(y) = \frac{f_X(x)}{g'(x)}; \qquad x = g^{-1}(y)}
$$

$$
\begin{align*}
f_Y(y) &= \frac{dF_Y}{dy}\\
&= \frac{dF_Y}{dx}\frac{dx}{dy}\\
&= \frac{f_X(x)}{g'(x)} \tag{Derivative of Inverse Functions}
\end{align*}
$$

## Bitonic Transformation

The name Bitonic isn't convention name so let's define it. A **bitonically increasing function** a function $g(x)$ that the absolute value of $g(x)$ increase as $x$ increases for the function $g(x_0 + x)$ where $g(x_0)$ is some global minima.

## Two-to-One Transformation
A **Two-to-One function** is a function $g(x)$ that for every value $y$, there exists two $x$ that satisfies $g(x) = y$.
An example of a two-to-one function is $g(x)=x^2$ since to the right of $x_0=0$, the function is monotinically increasing and to the left the function is monotonically decreasing. Thus, the absolute value of $g(x)$ is increasing on both sides.

Using the square as the motivating example let,

$$
Y = X^2
$$

That implies that the PDF of $Y$ must consider when $X=\sqrt{y}$ and $X=-\sqrt{y}$ where we assign those values to be $x_1$ and $x_2$ respectively. Since both sides are monotonically increasing functions, we can apply monotonic transformation for the PDF to be,

$$
\begin{align*}
f_Y(y) &= \frac{f_X(x_1)}{g'(x_1)} + \frac{f_X(x_2)}{g'(x_2)}\\
&= \frac{f_X(x_1)}{2x_1} + \frac{f_X(x_2)}{\abs{2x_2}}
\end{align*}
$$