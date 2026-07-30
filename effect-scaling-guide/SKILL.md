# effect-scaling-guide

## One-Line Description
Choose the appropriate effect scaling (unstandardized, completely standardized, partially standardized) for regression coefficients in mediation, moderation, and conditional process analysis, and report them correctly.

## R — Required Input
- **Variable types**: Continuous vs. dichotomous vs. multicategorical for X, M, W, Y.
- **Coefficient estimates**: Unstandardized regression coefficients (b) from OLS output.
- **Descriptive statistics**: Means, SDs for continuous variables; group sizes for categorical variables.
- **Research context**: Whether comparison across studies or within-model comparison is desired.

## I — Ideal Output
A scaling decision report for each coefficient in the model:
1. **Scaling recommendation**: Unstandardized, partially standardized, or completely standardized for each path.
2. **Converted values**: Actual scaled coefficients and their standard errors (if computable).
3. **Interpretation template**: Sentence explaining the effect in the chosen metric.
4. **Warning flags**: Any coefficients that should NOT be completely standardized.

## A1 — Analysis & Reasoning Steps
1. **Identify variable type for each coefficient**:
   - Is X (or M, or W) continuous or categorical?
   - Is Y continuous or categorical?
2. **Apply the decision tree**:

```
Is X dichotomous or multicategorical?
├── YES → Do NOT use completely standardized (β̃)
│   ├── Report: unstandardized b (mean difference in raw units)
│   └── Alternative: partially standardized bps = b / SDY
│       (effect size in SD units of Y)
└── NO (X is continuous)
    ├── Is Y continuous?
    │   ├── YES → Can use completely standardized β̃ = b × (SDX / SDY)
    │   │   └── Use for: comparing relative importance within model
    │   └── NO → Use unstandardized or partially standardized
    └── Is comparison across studies needed?
        ├── YES → Partially standardized (bps) preferred (avoids SDX dependency)
        └── NO → Unstandardized preferred (most interpretable)
```

3. **For moderation models**: The interaction coefficient b3 represents the change in X's effect per unit change in W. Standardizing b3 is problematic because it depends on SDX, SDW, and SDY. Report b3 unstandardized.
4. **For indirect effects (ab)**: Report unstandardized ab with bootstrap CI. Completely standardized indirect effect = ab × (SDX / SDY). This is acceptable when X is continuous. Partially standardized indirect effect = ab / SDY.
5. **For conditional effects**: Report at chosen values of moderator. If X is continuous and Y is continuous, can report completely standardized conditional effect. If X is dichotomous, report partially standardized or unstandardized.

## A2 — Action Steps
1. Compute descriptive statistics for all variables in the model.
2. Classify each coefficient by predictor type (continuous/dichotomous/multicategorical).
3. Apply decision tree above to each coefficient.
4. Compute scaled values as needed:
   - Completely standardized: β̃ = b × (SDpredictor / SDY)
   - Partially standardized: bps = b / SDY
5. In PROCESS: Use `stand=1` for completely standardized effects (but verify X is continuous).
6. In report: State metric explicitly. Example: "For every 1-unit increase in X, Y increased by b = 0.42 units (95% CI = [0.18, 0.66]), which corresponds to an increase of 0.31 standard deviations in Y."

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| β̃ for dichotomous X reported in a paper | Methodological error | Re-interpret as b or bps. Note the limitation. |
| SDY = 0 or near-zero | Y has no variance | Check data coding. Impossible to standardize. |
| SDpredictor differs wildly between studies | β̃ not comparable across studies | Use bps or unstandardized b with explicit metric. |
| Requested to compare indirect effects across models with different Y | Different SDY | Not directly comparable even with β̃. Use meta-analytic methods. |
| Interaction b3 is tiny in unstandardized but large in standardized | Scaling artifact | Always report unstandardized b3. Standardized interaction coefficients are misleading. |

## B — Boundary Conditions
- **Standardization assumes interval/ratio scales**: For ordinal variables with uneven intervals, standardization is questionable.
- **Completely standardized effects are model-specific**: β̃ depends on the full set of predictors in the model (through SDY, which is conditional on model R²).
- **Partial standardization (bps) is robust to group split**: For dichotomous X, bps = b/SDY does not depend on the proportion in each group. This makes it comparable across studies.
- **For mediation models**: ab/c (proportion mediated) is a common effect size but is unstable when c ≈ 0. Report with caution or report ab/SDY instead.

## References
- Hayes, A. F. (2022). Chapters 3 (Section 3.3), 4, 9 (Section 9.2).
- Cheung, G. W. (2009). Standardized coefficients in SEM.
- Friedman, J., & Wall, M. (2005). Graphical views of suppression and multicollinearity.
