# indirect-effect-inference

## One-Line Description
Infer the significance and magnitude of indirect effects using bootstrap confidence intervals, and choose between bootstrap and Monte Carlo methods based on data characteristics.

## R — Required Input
- **Point estimates**: Regression coefficients for paths a (X→M) and b (M→Y), or the indirect effect ab directly.
- **Standard errors**: SEs for a and b (needed for Monte Carlo, optional for bootstrap).
- **Sample size (n)**: Required for power considerations.
- **Software**: PROCESS macro, R (mediation/boot packages), or SPSS/SAS.

## I — Ideal Output
A statistical inference report containing:
1. **Indirect effect point estimate**: ab (or specific indirect effect aibi).
2. **Confidence interval**: Bias-corrected bootstrap 95% CI (or Monte Carlo CI).
3. **Significance decision**: Significant if CI excludes zero; not significant if includes zero.
4. **Effect size**: ab/c (proportion mediated) if total effect is non-zero and meaningful.
5. **Contrast results** (if multiple mediators): Difference between specific indirect effects with CI.
6. **Recommendation**: Whether the evidence supports mediation, and strength of evidence.

## A1 — Analysis & Reasoning Steps
1. **Verify model specification**: Confirm mediation model is correctly estimated (simple, parallel, or serial).
2. **Select inference method**:
   - **Bootstrap** (default): Use 5,000–10,000 resamples. Preferred when raw data are available.
   - **Monte Carlo**: Use when only a, b, and their SEs are available (e.g., from published tables). Generate 100,000 random draws from normal distributions with means a, b and variances SEa², SEb². Compute product for each draw. Use 2.5th and 97.5th percentiles as CI.
3. **Set bootstrap parameters**:
   - Samples: 5,000 minimum; 10,000 recommended for publication.
   - Method: Bias-corrected (default in PROCESS) or percentile.
   - Seed: Set random seed for reproducibility.
4. **Interpret the CI**:
   - CI entirely above zero → positive significant indirect effect.
   - CI entirely below zero → negative significant indirect effect.
   - CI includes zero → no statistically significant indirect effect.
5. **Do NOT use**: Sobel test (z-test), causal steps procedure (Baron & Kenny 4-step), or joint significance test (Yzerbyt et al., 2018).
6. **For multiple mediators**: Test total indirect effect and each specific indirect effect. Test pairwise contrasts if theoretically relevant.

## A2 — Action Steps
1. In PROCESS: add `boot=5000` (or higher) to command. Default is bias-corrected.
2. In R (mediation package): `mediate(model.m, model.y, treat="X", mediator="M", boot=TRUE, sims=5000)`
3. In R (manual bootstrap): Resample with replacement n observations → re-estimate a and b → store ab → repeat 5,000× → compute percentiles.
4. For Monte Carlo (when raw data unavailable): Use R code:
   ```r
   a <- coef_a; sea <- se_a; b <- coef_b; seb <- se_b
   ab <- rnorm(100000, a, sea) * rnorm(100000, b, seb)
   quantile(ab, c(0.025, 0.975))
   ```
5. Report: "The indirect effect of X on Y through M was ab = [value], 95% BCa CI = [LL, UL]."

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| Bootstrap CI is extremely wide | Small sample or weak effects | Increase bootstrap samples to 10,000+. Report cautiously. |
| Bootstrap CI barely excludes zero | Marginal significance | Report exact CI. Do not overstate. Replicate if possible. |
| Only a and b coefficients available from a paper | Cannot run bootstrap on raw data | Use Monte Carlo CI as approximation. |
| Path a significant, path b not | Joint significance would fail | Ignore joint significance. Test ab directly with bootstrap. |
| Both paths a and b non-significant | Likely no mediation | Check if ab CI also includes zero. If yes, conclude no evidence. |
| Contrast CI includes zero | No difference between indirect effects | Mediators are not differentially important. |

## B — Boundary Conditions
- **Bootstrap assumes independence** of observations. For clustered/nested data, use cluster bootstrap or multilevel methods.
- **Bootstrap assumes sufficient sample size**. With n < 50, bootstrap CIs may be unstable. Monte Carlo may be preferable if SEs are reliable.
- **Bias-corrected bootstrap can have inflated Type I error** in small samples (n < 100). Use percentile bootstrap as conservative alternative.
- **Monte Carlo assumes normality** of a and b sampling distributions. Violated with small samples or extreme coefficients.
- **Effect size ab/c is unstable** when total effect c is near zero. Report with caution or avoid.

## References
- Hayes, A. F. (2022). Chapters 3, 4, 5.
- Preacher, K. J., & Hayes, A. F. (2004, 2008). SPSS and SAS procedures for estimating indirect effects.
- Hayes, A. F. (2018). Introduction to mediation, moderation, and conditional process analysis (2nd ed.). Appendix: Monte Carlo confidence intervals.
