# process-model-reporter

## One-Line Description
Write a results section for mediation, moderation, or conditional process analysis that meets journal standards, includes all necessary statistics, and tells a coherent story about the data.

## R — Required Input
- **Model output**: PROCESS or equivalent regression output tables.
- **Model type**: Simple mediation / multiple mediation / moderation / conditional process / multicategorical.
- **Variable names**: Actual construct names (not just variable labels).
- **Study design**: Experimental, cross-sectional, longitudinal, etc.
- **Journal target**: APA-style, specific journal requirements.

## I — Ideal Output
A publication-ready results subsection (300–800 words) containing:
1. **Model description**: Conceptual and statistical model stated in prose.
2. **Preliminary analyses**: Descriptive statistics, correlations, manipulation checks (if experimental).
3. **Primary results**: Regression coefficients, standard errors, CIs, and p-values for key paths.
4. **Indirect effect inference**: Point estimate + bootstrap CI for each indirect effect.
5. **Moderation probing**: Conditional effects at chosen moderator values with CIs.
6. **Visualization reference**: Figure number for simple slope plot or conditional effect plot.
7. **Caveat paragraph**: Design limitations affecting causal interpretation.

## A1 — Analysis & Reasoning Steps
1. **State the model conceptually**: "We tested whether M mediated the effect of X on Y." Or: "We tested whether W moderated the effect of X on Y, and whether this moderation was transmitted through M."
2. **Describe the statistical model**: Report the regression equation(s). For complex models, state which PROCESS model number was used.
3. **Report path coefficients**:
   - X→M path: b = [value], SE = [value], t(df) = [value], p = [value], 95% CI = [LL, UL].
   - M→Y path: b = [value], SE = [value], t(df) = [value], p = [value], 95% CI = [LL, UL].
   - X→Y direct effect: b = [value], SE = [value], t(df) = [value], p = [value], 95% CI = [LL, UL].
   - Total effect: b = [value], SE = [value], t(df) = [value], p = [value], 95% CI = [LL, UL].
4. **Report indirect effects**: "The indirect effect of X on Y through M was ab = [value], 95% bias-corrected bootstrap CI = [LL, UL] based on 5,000 samples."
5. **For moderation**: Report interaction coefficient first. Then report conditional effects: "The effect of X on Y was significant when W was low (b = [value], 95% CI = [LL, UL]) but not when W was high (b = [value], 95% CI = [LL, UL])."
6. **For conditional process**: Report conditional indirect effects table. Then conditional direct effects if moderated.
7. **Effect size**: Report ab/c (proportion mediated) or partially standardized effects if meaningful.
8. **Tell a story**: Connect statistics to theoretical claims. Do not just list numbers.

## A2 — Action Steps
1. Gather all necessary statistics from output before writing.
2. Draft the results section following the structure above.
3. Check that every number in the text matches the output exactly.
4. Ensure CIs are reported for all indirect and conditional effects.
5. Include a figure reference for the plot.
6. Add a limitation paragraph: "Because the data are cross-sectional, causal ordering cannot be established."
7. Have a colleague review for clarity and accuracy.

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| Output has many non-significant paths | Model may be misspecified | Report all paths honestly. Do not omit non-significant results selectively. |
| Bootstrap CI is very wide | Low power or small effect | Report exact CI. Interpret as inconclusive rather than null. |
| Conditional effects table is long | Many moderator values or multiple mediators | Report key comparisons in text. Put full table in appendix or supplementary materials. |
| Journal requires SEM reporting style | PROCESS output differs from SEM conventions | Adapt by reporting standardized effects and model fit indices (R², F) where appropriate. |
| Significance stars or p-values only | Insufficient for modern reporting | Always add CIs. p-values are optional when CIs are reported. |

## B — Boundary Conditions
- **This skill covers writing, not analysis**: The statistical output must already be correct. This skill does not fix analytical errors.
- **Journal-specific requirements vary**: Some journals require effect sizes (η², ω²), some require Bayes factors, some discourage p-values. Adapt accordingly.
- **Word limits**: Results sections may need to be condensed for journals with strict word limits. Prioritize indirect/conditional effects and CIs over individual path coefficients.
- **Supplementary materials**: Full PROCESS output tables, syntax, and datasets should often be deposited as supplementary materials or in open repositories.
- **Causal language**: Match causal claims to design strength. Randomized experiments support stronger causal language than cross-sectional surveys.

## References
- Hayes, A. F. (2022). Chapter 14: "How Do I Write about This?"
- American Psychological Association. (2020). *Publication manual of the American Psychological Association* (7th ed.).
