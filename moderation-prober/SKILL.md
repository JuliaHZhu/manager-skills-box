# moderation-prober

## One-Line Description
Probe a significant interaction effect using pick-a-point or Johnson–Neyman technique to estimate conditional effects, report their confidence intervals, and produce simple slope visualizations.

## R — Required Input
- **Regression output**: Coefficients for X, W, and XW from a moderation model: Y = iY + b1X + b2W + b3XW + eY.
- **Moderator descriptive statistics**: Mean, SD, minimum, maximum of W.
- **Significance of interaction**: b3 must be statistically significant (or at least interpretable) before probing.

## I — Ideal Output
A moderation probing report containing:
1. **Conditional effects table**: Effect of X on Y at chosen/modal values of W, with standard errors, t-values, and 95% CIs.
2. **Significance regions** (JN only): Range(s) of W where conditional effect is significant.
3. **Visualization**: Simple slope plot showing regression of Y on X at representative values of W.
4. **Interpretation paragraph**: Narrative explaining when/how X relates to Y based on moderator values.

## A1 — Analysis & Reasoning Steps
1. **Confirm interaction significance**: Verify b3 is significant (p < .05 or CI excludes zero). If not, probing is generally not recommended unless there is strong a priori theoretical reason.
2. **Choose probing method**:
   - **Pick-a-point** (default): Select meaningful/modal values of W. Standard choice: mean, mean ± 1 SD, or specific theoretically meaningful values (e.g., age = 30, 50, 70).
   - **Johnson–Neyman (JN)**: Use when W is continuous and you want to identify exact transition points where conditional effect moves from significant to non-significant. Particularly useful when moderator is continuous and theory does not specify particular values.
3. **For pick-a-point**: Compute conditional effect θX→Y = b1 + b3W at each chosen W value. Compute SE using variance/covariance matrix: SE(θ) = sqrt(Var(b1) + W²Var(b3) + 2WCov(b1,b3)). Test with t = θ/SE, df = n - k - 1.
4. **For JN technique**: Solve for W where θX→Y = t_critical × SE(θ). Values of W outside the resulting region(s) produce significant conditional effects. PROCESS automates this with `jn=1` option.
5. **Do NOT artificially categorize W** into low/medium/high groups. This discards information and produces biased estimates.
6. **Mean-centering check**: Remember that mean-centering does not affect the interaction test. If you centered X and W, conditional effects are interpreted at mean-centered values.

## A2 — Action Steps
1. In PROCESS: `process y=.../x=.../w=.../model=1/moments=1/boot=5000.`
   - `moments=1` adds pick-a-point at mean ± 1 SD.
   - `jn=1` adds Johnson–Neyman output.
2. In R (interactions package): `interact_plot(model, pred = X, modx = W, modx.values = c(...))`
3. In R (manual): Extract vcov matrix. Compute conditional effects and SEs. Use qt() for critical t.
4. Create plot: X-axis = X, Y-axis = predicted Y, separate lines for each W value. Include observed data as background scatter (optional).
5. Write interpretation: "The effect of X on Y was significant at W = [value] (b = [value], 95% CI = [LL, UL]), but not at W = [value] (b = [value], 95% CI = [LL, UL])."

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| JN technique produces no real solution within W range | Conditional effect never crosses significance threshold | Report pick-a-point results instead. |
| JN produces two regions of significance | Conditional effect significant at low and high W, not in middle | Report both regions with interpretation. |
| Conditional effect CIs all include zero | Interaction b3 may be marginally significant | Report honestly. Do not overstate. |
| Moderator is dichotomous | JN technique is inappropriate | Use pick-a-point at the two levels of W. |
| Chosen W values fall outside observed range | Extrapolation | Choose W values within min/max range. |

## B — Boundary Conditions
- **Assumes linear moderation**: The model assumes the effect of X changes linearly with W. For nonlinear moderation, polynomial or spline terms are needed.
- **Assumes continuous or dummy-coded X**: If X is multicategorical, conditional effects are relative effects between groups, conditional on W. Use models 2 or 3 in PROCESS.
- **Assumes homoscedasticity**: Heteroscedasticity-consistent SEs (`hc=3` in PROCESS) may be needed.
- **Pick-a-point is arbitrary**: The choice of W values influences interpretation. Justify theoretically or use standard values (mean ± 1 SD).
- **JN technique assumes symmetric distribution of W**: Highly skewed moderators may produce regions at extreme, unobserved values.

## References
- Hayes, A. F. (2022). Chapters 7, 8, 9.
- Bauer, D. J., & Curran, P. J. (2005). Probing interactions in fixed and multilevel regression.
- Johnson, P. O., & Neyman, J. (1936). Tests of certain linear hypotheses.
