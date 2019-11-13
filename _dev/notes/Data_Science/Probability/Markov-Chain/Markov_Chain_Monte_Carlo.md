---
title: Markov Chain Monte Carlo
---

The MCMC is a sampling algorithm to determine some underlying probability distribution often the posterior distribution representing the outcome or sample space $S$. In terms of the Markov chain, the desired probability distribution is the long-run proportion of state distribution $\pi$ of some stationary Markov chain of sample space $S$ (e.g., some paramter space) satisfying the balance equation:

$$
\pi \mathbb P  = \pi
$$

* $\mathbb P$: the transition matrix of the Markov chain.
* $\pi$: A vector of size $\abs{S}$ representing the proportion of time at long-run the chain spent on each state $i \in S$

Recall that, the balance equation satisfies for as $t \rightarrow \infty$, stepping from $i$ to $j$ is the long-run proportion of state distribution completely independent from the initial state $i$.

$$
P(X_{t+1} = j \mid X_t = i) = \pi(j)
$$

## Metropolis-Hastings Algorithm

Known as the classical and easiest to understand algorithm of MCMC, the **Metroplis-Hastings Algorithm** takes advantage of detailed balance in Markov chains.

Recall a Markov chain is in detailed balance if at the long wrong for all states in the state space $(i,j \in S)$, the long-run proportion of steps in state $i$ entering state $j$ is equivalent to the long-run proportion of steps in state $j$ entering state $i$:

$$
\pi(j)P(j, i) = \pi(i)P(i,j)
$$

An equivalent expression is,

$$
\frac{\pi(j)}{\pi(i)} = \frac{P(i,j)}{P(j,i)}
$$

This condition will come up many times throughout the algorithm so let's give it a name called the **acceptance ratio**:

$$
r(i,j) := \frac{\pi(j)}{\pi(i)}
$$

The transition matrix for the Markov chain in question is called the **proposal matrix** $\mathbb Q$ which is a transition matrix that is symmetric and irreducible. It is called a proposal matrix because its job is to propose the next step (i.e., its next guess for what you want to sample). For each guess it makes, we need to somehow decide if it's a good guess or not. The Metropolis-Hastings algorithm thus defines the rules of what to do for every guess (formally from here on a guess is called a proposal).

Algorithm
: The Metropolis-Hastings algorithm goes as so:

	For every step $t$ of the algorithm, $\mathbb Q$ proposes $X_{t+1} = j$ where the previous step is $X_{t}=i$. This proposal occurs at chance $\mathbb Q_{ij}$ (the matrix element $i,j$ of $\mathbb Q$)

	* If $r(i,j) \ge 1$, accept the proposal $X_{t+1} = j$
	* If $r(i,j) < 1$, toss a p-coin with chance $p=r(i,j)$

		* On head, accept the proposal $X_{t+1}=j$.
		* On tails, reject the proposal $X_{t+1}=i$.
	* Repeat until you're satisfied (in some cases this is when the chain converges; in many others it's when your deadline is coming or you run out of patience).

### Proof of Metropolis-Algorithm Gives Detailed Balance

Now, does this algorithm develop a Markov chain that satisfy detailed balance:

$$r(i,j) = \frac{P(i,j)}{P(j,i)} ~?$$

Let's take a look at all the possible states at step $t$ assuming we've ran the algorithm for long enough  $t \rightarrow \infty$,

* $r(i,j)=1 \implies \pi(i) = \pi(j)$. The probability of transition is

	$$
	\begin{align*}
	P(i,j) &= \mathbb Q_{ij}\\
	P(j,i) &= \mathbb Q_{ji}
	\end{align*}
	$$

	Since $\mathbb Q$ is symmetric, the RHS is $1$ thus the ratio of transition probabilities is $r(i,j)$:

	$$
	r(i,j) = \frac{P(i,j)}{P(j,i)} = 1
	$$

	This satisfies the detailed balance condiiton since $r(i,j) = 1$

* $r(i,j) < 1 \implies \pi(j) < \pi(i)$, the transition probabilities are

	$$
	\begin{align*}
	P(i,j) &= \mathbb Q_{ij}r(i,j) \tag{accept after flipping coin}\\
	P(j,i) &= \mathbb Q_{ji} \tag{accept since $\pi(i) > \pi(j)$}
	\end{align*}
	$$

	The ratio of transition probabilities is $r(i,j)$ since $\mathbb Q$ is symmetric

	$$
	r(i,j) = \frac{P(i,j)}{P(j,i)}
	$$

* $r(i,j) \ge 1 \implies \pi(j) \ge \pi(i)$, equivalent to the previous case if you swap $i$ and $j$.