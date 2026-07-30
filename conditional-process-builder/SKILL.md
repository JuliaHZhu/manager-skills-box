# conditional-process-builder

## One-Line Description
Build a conditional process model by translating a conceptual diagram into a PROCESS model number, estimating conditional direct and indirect effects, and testing whether an indirect effect is moderated.

## R — Required Input
- **Conceptual diagram**: Drawing showing which paths are moderated (X→M, M→Y, X→Y) and by which variable(s).
- **Variable list**: X (antecedent), Y (consequent), M (mediator), W/Z/V/Q (moderators).
- **Data**: Measured variables for all entities in diagram.

## I — Ideal Output
A complete conditional process analysis report:
1. **Model identification**: PROCESS model number matched to conceptual diagram.
2. **Statistical equations**: Regression equations for each consequent (M, Y).
3. **Conditional indirect effect function**: Mathematical expression showing how indirect effect varies with moderator(s).
4. **Conditional direct effect function**: Same for direct effect, if moderated.
5. **Probing results**: Conditional indirect/direct effects at values of moderator(s) with 95% CIs.
6. **Visualization**: Plot of conditional indirect effect across moderator range.
7. **Test of moderated mediation**: Whether the indirect effect differs significantly across moderator values.

## A1 — Analysis & Reasoning Steps
1. **Draw the conceptual diagram**: Boxes for X, M, Y, W. Arrows for paths. Moderation shown as arrow from W pointing to another arrow.
2. **Map to PROCESS model**:
   - First-stage moderation (X→M moderated): Models 7, 8, 58, 59, etc.
   - Second-stage moderation (M→Y moderated): Models 14, 15, etc.
   - Direct effect moderated: Models 5, 6, etc.
   - Both stages moderated by same W: Model 8, 12, etc.
   - Both stages moderated by different variables: Model 17, 18, etc.
   - Multiple mediators with moderation: Models 85, 86, etc.
3. **Write statistical equations**:
   - Example (Model 7, first-stage moderation):
     - M = iM + a1X + a2W + a3XW + eM
     - Y = iY + c'X + bM + eY
   - Conditional indirect effect: θX→M × b = (a1 + a3W)b = a1b + a3bW
   - This is a linear function of W.
4. **Check mathematical form**: If both stages moderated by same W, indirect effect may be quadratic in W: (a1 + a3W)(b1 + b2W).
5. **Estimate model in PROCESS**: Use identified model number with `boot=5000`.
6. **Probe conditional indirect effect**: Use pick-a-point or JN at values of moderator(s). Report with CIs.
7. **Test moderated mediation**: In PROCESS, examine whether the function of the indirect effect across W is significant (bootstrap CI of the slope of the conditional indirect effect function — e.g., a3b for Model 7).

## A2 — Action Steps
1. In PROCESS: `process y=.../x=.../m=.../w=.../model=7/boot=5000.`
2. Examine output for:
   - Regression coefficients for each equation.
   - Conditional indirect effect table (at values of W).
   - Bootstrap CI for conditional indirect effects.
   - Index of moderated mediation (if available).
3. Create plot: X-axis = W values, Y-axis = conditional indirect effect. Add shaded CI band. Mark regions of significance (if JN used).
4. Interpret: "The indirect effect of X on Y through M was significant when W was low (θ = [value], 95% CI = [LL, UL]) but not when W was high (θ = [value], 95% CI = [LL, UL])."

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| Cannot find matching PROCESS model | Diagram is complex or unusual | Use Appendix B model customization. Write custom equations. |
| Conditional indirect effect CI includes zero at all W values | No moderated mediation | Consider whether W moderates the direct effect instead, or whether the model is misspecified. |
| Quadratic function in W produces U-shaped pattern | Both stages moderated by same W | Report effect at low, medium, high W. Do not linearly extrapolate. |
| Multiple moderators (W and Z) in model | Interpretation is multidimensional | Create conditional effect tables for combinations of moderator values. Consider 3D visualization. |
| Model fails to converge | Collinearity or small cell sizes | Check VIF. Remove unnecessary covariates. Ensure sufficient n per condition. |

## B — Boundary Conditions
- **Assumes linear moderation**: Moderation of paths is modeled linearly. Nonlinear moderation requires custom model specification.
- **Assumes single mediator or simple multiple mediator structure**: Complex serial chains with moderation at multiple points may exceed pre-programmed PROCESS models. Use custom models (Appendix B).
- **Assumes no three-way interactions in mediation paths**: PROCESS does not automatically handle three-way interactions in mediation equations without customization.
- **Causal interpretation**: Same caveats as simple mediation. Temporal ordering, manipulation, and design features are required for causal claims.
- **Sample size**: Moderated mediation models have many parameters. Minimum n = 100–200 recommended for stable bootstrap CIs.

## References
- Hayes, A. F. (2022). Chapters 11, 12, 13.
- Hayes, A. F. (2015). An index and test of linear moderated mediation.
- PROCESS documentation: Appendix A (model catalog) and Appendix B (customization).
