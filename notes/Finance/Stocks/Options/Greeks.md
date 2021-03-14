---
title: Greeks
---

## Delta

Delta is the change in option price per change in stock price,

$$
\Delta = \pm \frac{\Delta[\text{Option Price}]}{\Delta[\text{Stock Price}]}
$$

A positive delta describes calls and negative delta describes puts.

* Delta also describes moneyness.
  * Out the Money $\Delta < 0.50$
  * In the Money $\Delta > 0.50$
* Delta can be thought of as the probability to the ITM

## Gamma

Gamma is the rate of change of Delta with respect to the stock price,

$$
\Gamma = \frac{\mathrm d\Delta}{\mathrm d[\text{Stock Price}]}
$$

More practically,

$$
\Gamma_{t+1} = \frac{\Delta_{t+1} - \Delta_t}{\Delta[\text{Stock Price}]}
$$

* Gamma is larger near the market
* Gamma increases as the expiration date approaches

## Theta

The amount the option price changes each day if it were to stay the current price.

* Theta exponentially increases as the expiration date approaches.

## Vega

The change in option price for each change in implied volatility. This is a measure of the sensitivity to IV.

$$
V = \frac{\Delta[\text{Option Price}]}{\Delta[\text{IV}]}
$$

## Rho

The change in option price for each change in interest rate.