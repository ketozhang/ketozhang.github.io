---
title: Intrinsic Value
---

The intrinsic value is an estimate on a company's worth based on fundamental factors (e.g., cash flows, future growth, risk). Methodology that attempts to estimate the intrinsic value are called **valuation models**.

The intrinsic value is often compared to the market price to determine undervalued/overvalued stocks. The percentage difference is called the **margin** and the minimum percentage risk you're willing to take on the margin is more aptly called the **margin of safety**.

## Discounted Cash Flow

The discounted cash flow (DCF) model takes as inputs the current cash flow value, growth rate, and discount rate. The cash flow value is some metric that determine how much money the company is making (often the EPS is used). The growth rate is the extrapolated rate of growth one expects the company is to grow. The discount rate is the allowed margin of error subtracted from the growth rate.

$$
[\text{Intrinisc Value}] = \frac{[\text{Year T Terminal Value}]}{\left(1 + [\text{Discount Rate}]\right)^T}
$$

The idea behind DCF for valuation is to determine the equivalent stock price for the same potential at year $T$ but at a often much lower and safer growth rate called the discount rate.

### Growth Rates

Using the EPS as the cash flow value, there's a few ways to calculate the growth rate:

- **Historical Growth Rate**
  Take the growth rate to be the historical average of the EPS percentage change.
- **Industry Average Growth Rate**
  Instead of the stock, take the industrial historical growth rate. Under the model assumption, over a long run, these two growth rates will eventually converge.

### Terminal Value

Because the extrapolation using a positive growth rate expands infinitely, the terminal value quantifies the expectation of the stock value after the projection period $T$. The terminal value is calculated as,

$$
[\text{Year T Terminal Value}] = [\mathrm{Year~T~EPS}] \cdot [\text{Exit Multiple}] \,,
$$

where the exit multiple is some measure often the P/E ratio. Recall the P/E ratio estimates the current price an investor would pay for a share for each dollar amount earning. The terminal value is then the product of projected Year $T$ EPS and P/E ratio giving you the price an investor would pay in $T$ years. The assumption here is the P/E ratio is persistent throughout the projection period.

### Discount Rate

The discount rate is an negative adjustment to the growth rate to account for risk. One way to calcualte the discount rate is the **capital asset pricing model** (**CAPM**) which calculates the expected rate of return $E[R_i]$:

$$
E[R_i] = R_f + \beta_i (R_m - R_f)
$$

- $R_f$ : Risk free rate, the zeropoint assuming the minimum rate of return from investing. This value is usually the 30-year rate of return from Treasury bond.
- $R_m$ : Market rate of return usually taken from the S&P 500 annual return.
- $\beta_i$ : The beta volatility value of the stock.
