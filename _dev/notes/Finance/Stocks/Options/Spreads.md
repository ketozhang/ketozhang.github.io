---
title: Spreads
---

Spreads are simulataneous buying and selling of options of the same stock at different strike prices. Here we will only focus on vertical spreads.

## Bull Call Spread (Debit)

A **bull call spread** is buying a call option at a strike price and selling another at a **higher** strike price expired on the same date

The maximum loss is the difference in the premiums gain and loss.

$$
[\text{Max Loss}] = \Delta[\text{Premium}] \,.
$$

The maximum gain is the difference between the stirke prices of both calls less the premium.

$$
[\text{Max Gain}] = \big([\text{Sell Call Strike}] - [\text{Buy Call Strike}]\big) + \Delta[\text{Premium}] \,.
$$

If the price is between the strike prices, the profit is

$$
\begin{align*}
[\text{Profit}] &= [\text{Strike Price}] - [\text{Buy Call Strike}] + \Delta[\text{Premium}] \,.
\end{align*}
$$

Therefore the break-even price is,

$$
 [\text{Break-Even Price}] = [\text{Buy Call Strike}] + \Delta[\text{Premium}]
$$

### Usage

- Profits when price stays the same or goes up
- Reduce the risk of loss compared to just buying a call.
- Implied from above, this also reduces the premium to enter a call
- Reduce break-even price

<!-- ## Bear Call Spread (Credit)

A **bull call spread** is buying a call option at a strike price and selling another at a **lower** strike price expired on the same date

The maximum loss is the difference in the premiums gain and loss.

$$
[\text{Max Loss}] = \mathrm{abs}\big([\text{Buy Call Strike}] - [\text{Sell Call Strike}]\big)- [\text{Buy Call Premium}]
$$

The maximum gain is the difference between the stirke prices of both calls less the premium.

$$
[\text{Max Gain}] = [\text{Buy Call Premium}] - [\text{Sell Call Premium}]~.
$$

## Usage

- Profits when price stays the same or goes down
- Reduce the risk of loss compared to just selling a call. -->
