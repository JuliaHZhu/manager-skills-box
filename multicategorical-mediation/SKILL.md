# multicategorical-mediation

## One-Line Description
Extend mediation, moderation, and conditional process analysis to multicategorical antecedent variables (3+ groups) using indicator coding, orthogonal contrasts, and relative effect interpretation.

## R — Required Input
- **Multicategorical X**: Variable with g ≥ 3 groups (e.g., control, treatment A, treatment B).
- **Coding scheme choice**: Indicator (dummy), sequential, or Helmert coding.
- **Reference group**: Which group serves as the reference for comparisons.
- **Outcome Y, mediators M, moderators W**: Continuous or appropriately coded.

## I — Ideal Output
A multicategorical analysis report containing:
1. **Coding matrix**: g-1 codes representing group comparisons.
2. **Relative total effects**: Differences in Y between groups, controlling for other groups.
3. **Relative direct effects**: Same, controlling for M.
4. **Relative indirect effects**: Differences in Y mediated through M, expressed relative to reference group.
5. **Relative conditional effects** (if moderation): Group differences at specific moderator values.
6. **Interpretation**: Each effect is "the effect of being in Group j vs. Reference group."

## A1 — Analysis & Reasoning Steps
1. **Choose coding scheme**:
   - **Indicator (dummy) coding** (default): Each code compares one group to reference group. Use when reference group is meaningful (e.g., control condition).
   - **Sequential coding**: Each code compares a group to the previous group in a natural order. Use when groups are ordered (e.g., low/medium/high dose).
   - **Helmert coding**: Each code compares a group to the mean of all subsequent groups. Use when interested in cumulative comparisons.
2. **Set reference group**: The group coded 0 on all g-1 variables. Typically the control or baseline condition.
3. **Compute relative total effects**: Regress Y on all g-1 codes. Each coefficient is the mean difference in Y between that group and reference, ignoring M.
4. **Compute relative direct effects**: Regress Y on all g-1 codes + M. Each coefficient is the direct effect of that group relative to reference, controlling for M.
5. **Compute relative indirect effects**: For each group j, indirect effect = (total effect j) − (direct effect j) = relative indirect effect of group j vs. reference.
6. **For moderation with multicategorical X**: The interaction is between the set of g-1 codes and W. Test with an omnibus F-test for the set of interaction terms. If significant, probe conditional relative effects at values of W.
7. **For conditional process with multicategorical X**: Relative conditional indirect effects are computed at values of moderator(s). Each relative effect compares one group to reference at a specific W value.

## A2 — Action Steps
1. In PROCESS: `process y=.../x=.../m=.../w=.../model=.../xmodval=1/boot=5000.`
   - `xmodval=1` tells PROCESS X is multicategorical.
   - PROCESS defaults to indicator coding with the lowest value as reference.
   - Use `contrast=1` for custom contrasts (advanced).
2. In R: Manually create g-1 dummy codes. Run regression with `lm()`. Compute relative indirect effects as differences.
3. For bootstrap inference: Bootstrap the difference (total − direct) for each group.
4. Report: "Relative to the control group, the indirect effect of treatment A on Y through M was ab = [value], 95% CI = [LL, UL]."

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| Omnibus F for interaction not significant | No moderation by W of any group difference | Do not probe individual interactions. Report omnibus result. |
| One group has very small n | Unstable estimates for that group's relative effect | Consider collapsing groups or using Bayesian methods. |
| Reference group is not theoretically meaningful | Interpretation is arbitrary | Re-code with a more meaningful reference group. |
| Sequential coding used but order is arbitrary | Coefficients are meaningless | Use indicator or Helmert coding instead. |
| Relative indirect effect negative while relative total and direct are positive | Suppression pattern | Valid statistically. Interpret carefully. |

## B — Boundary Conditions
- **Assumes equal variances across groups**: If variances differ, heteroscedasticity-consistent SEs (`hc=3` in PROCESS) are recommended.
- **Assumes no empty cells**: All g groups must have sufficient n for stable estimation.
- **Reference group dependence**: Relative effects are always relative to the chosen reference. Changing reference changes all coefficients.
- **Complexity increases with g**: With many groups, the number of relative effects grows quickly. Consider whether all pairwise comparisons are needed.
- **Continuous moderators with multicategorical X**: Conditional relative effects are computed at values of W, but the number of combinations (g-1 groups × W values) can be large. Focus on theoretically key comparisons.

## References
- Hayes, A. F. (2022). Chapters 6, 10, 13.
- Hayes, A. F., & Preacher, K. J. (2014). Statistical mediation analysis with a multicategorical independent variable.
