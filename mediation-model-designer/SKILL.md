# mediation-model-designer

## One-Line Description
Design a mediation model from a theoretical hypothesis by selecting variables, drawing the conceptual diagram, and choosing the correct statistical model (simple, parallel, or serial mediation).

## R — Required Input
- **Theoretical hypothesis**: A statement of how X affects Y, and through what mechanism(s).
- **Variable inventory**: List of measured variables available in the dataset.
- **Study design**: Experimental vs. observational, cross-sectional vs. longitudinal.

## I — Ideal Output
A complete mediation analysis plan containing:
1. **Conceptual diagram**: Boxes and arrows showing X → M → Y and any direct path X → Y.
2. **Statistical diagram**: Regression equations for each consequent variable.
3. **Model type**: Simple (1 M), parallel multiple (2+ M simultaneously), or serial multiple (M1 → M2 chain).
4. **Inference strategy**: Bootstrap CI for indirect effects (default: 5,000 samples, bias-corrected).
5. **PROCESS command skeleton** (if using PROCESS): `process y=.../x=.../m=.../model=4/boot=5000.`
6. **Anticipated output table**: Direct effect, indirect effect(s), total effect, with interpretation template.

## A1 — Analysis & Reasoning Steps
1. **Identify X and Y** from the theoretical hypothesis. Confirm they are measured in the data.
2. **Identify the mediator(s) M** — the mechanism(s) linking X to Y. Ask: "How does X influence Y?"
3. **Count mediators**:
   - If 1 mediator → Simple mediation model (PROCESS model 4).
   - If 2+ mediators operating simultaneously → Parallel multiple mediator model (PROCESS model 4 with multiple m).
   - If mediators form a causal chain → Serial multiple mediator model (PROCESS model 6).
4. **Draw the conceptual diagram**: X → M → Y with direct path X → Y. For multiple mediators, draw all parallel paths or serial chains.
5. **Write the statistical equations**:
   - Simple: M = iM + aX + eM; Y = iY + c'X + bM + eY
   - Parallel: Add equations for each M; Y includes all M terms.
   - Serial: M1 = iM1 + a1X + eM1; M2 = iM2 + a2X + d21M1 + eM2; Y = iY + c'X + b1M1 + b2M2 + eY
6. **Choose inference method**: Bootstrap CI for indirect effects. Do NOT use Sobel test or causal steps.
7. **Check for suppression**: If a and b have opposite signs, the direct effect may exceed the total effect. This is valid mediation.

## A2 — Action Steps
1. Open dataset and verify variables are correctly coded.
2. Run correlation matrix to verify expected associations (optional, for sanity check).
3. Execute PROCESS command (or equivalent OLS regression) to estimate model.
4. Examine bootstrap CI for indirect effect(s). If CI excludes zero → significant mediation.
5. Examine direct effect c'. If c' CI excludes zero → partial mediation; if includes zero → complete mediation (tentatively).
6. For multiple mediators, examine specific indirect effects and contrasts. Report which mediator(s) carry the effect.
7. For serial mediators, examine the chain indirect effect (a1 × d21 × b2).

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| Total effect c is not significant | Suppression or masking | Proceed with indirect effect test. Do NOT stop. |
| Bootstrap CI includes zero for ab | No evidence of mediation | Reconsider mediator choice or check for confounds. |
| Indirect effects have opposite signs | Competing mediators | Report specific effects separately; consider theoretical meaning. |
| Path a significant but b not (or vice versa) | Joint significance unclear | Bootstrap CI for ab is still the criterion. Joint significance is insufficient. |
| Multiple M are highly correlated | Multicollinearity concern | Check VIF. If VIF < 10, proceed. Consider reducing mediators. |

## B — Boundary Conditions
- **Assumes continuous Y**. For dichotomous/ordinal/count/survival outcomes, OLS is inappropriate. Use logistic regression or SEM instead (not covered by this skill).
- **Assumes single-level data**. For multilevel/nested data, use multilevel SEM.
- **Assumes cross-sectional or simple experimental design**. For longitudinal mediation, use cross-lagged panel models.
- **Assumes no latent variables**. If variables have measurement error, SEM with latent variables is preferred.
- **Causal interpretation requires design features**: Random assignment establishes X→M and X→Y; temporal ordering of M and Y requires longitudinal design or experimental manipulation of M.

## References
- Hayes, A. F. (2022). *Introduction to mediation, moderation, and conditional process analysis* (3rd ed.). Guilford Press. Chapters 3, 5, 6.
