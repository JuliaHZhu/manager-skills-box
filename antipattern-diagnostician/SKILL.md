# antipattern-diagnostician

## One-Line Description
Diagnose common methodological errors in mediation, moderation, and conditional process analysis, explain why they are wrong, and recommend the correct approach based on Hayes (2022).

## R — Required Input
- **Described analysis plan or reported results**: What a researcher did or plans to do.
- **Context**: Study design, variables, software used, journal target.

## I — Ideal Output
A diagnostic report containing:
1. **Identified anti-patterns**: List of errors detected.
2. **Severity rating**: Critical (will invalidate conclusions), Major (substantially weakens conclusions), Minor (suboptimal but not fatal).
3. **Explanation**: Why each anti-pattern is problematic, with reference to statistical reasoning.
4. **Corrective action**: Specific steps to fix the problem.
5. **Prevention advice**: How to avoid this error in future analyses.

## A1 — Analysis & Reasoning Steps
1. **Check inference method for indirect effects**:
   - Did they use Sobel test? → CRITICAL. Replace with bootstrap CI.
   - Did they use Baron & Kenny causal steps? → CRITICAL. Replace with direct ab test.
   - Did they use joint significance (Yzerbyt et al., 2018)? → MAJOR. Use bootstrap instead.
2. **Check moderation analysis**:
   - Did they mean-center X and W claiming it is "necessary"? → MINOR. Clarify that centering is optional.
   - Did they split continuous W into groups (median split)? → CRITICAL. Use pick-a-point or JN instead.
   - Did they use hierarchical entry to test moderation? → MINOR. Simultaneous entry is equivalent.
   - Did they report β̃ for dichotomous X? → MAJOR. Use unstandardized or partially standardized.
3. **Check mediation logic**:
   - Did they require total effect significance before testing mediation? → CRITICAL. Direct test of ab is sufficient.
   - Did they confuse mediator and moderator? → CRITICAL. Redesign conceptual diagram.
   - Did they test mediated moderation without theoretical justification? → MAJOR. Focus on moderated mediation.
4. **Check conditional process analysis**:
   - Did they let data choose the PROCESS model? → MAJOR. Model selection must be theory-driven.
   - Did they report conditional effects without CIs? → MAJOR. Always include CIs.
   - Did they interpret a non-significant interaction as "no moderation" without probing? → MINOR. May still be worth probing with strong theory.
5. **Check reporting**:
   - Did they report p-values without CIs for indirect effects? → MAJOR. CIs are required.
   - Did they use causal language with cross-sectional data? → MINOR to MAJOR depending on strength of claims. Add caveats.

## A2 — Action Steps
1. Read the described analysis or paper carefully.
2. Run through the 5 diagnostic checks above systematically.
3. For each issue found, provide a concrete fix with PROCESS syntax or analytical steps.
4. Rate severity and prioritize fixes.
5. If the analysis is pre-registration or a plan: provide revised analysis plan.
6. If the analysis is already completed: assess whether errors are fixable with reanalysis or require data collection changes.

## E — Error Handling
| Scenario | Diagnosis | Fix |
|----------|-----------|-----|
| Multiple critical errors found | Analysis is fundamentally flawed | Recommend starting over with corrected framework. |
| Software other than PROCESS used | May or may not support correct methods | Verify software can do bootstrap CIs for indirect effects. If not, switch to PROCESS or R. |
| Reviewer demanded causal steps or Sobel test | Reviewer is using outdated standards | Cite Hayes (2022) and recent methodological literature. Explain why bootstrap is standard. |
| Dataset too small for bootstrap (n < 30) | Unstable CIs | Use Monte Carlo if SEs are available. Acknowledge limitation. Consider larger sample. |
| All checks pass | Analysis appears sound | Provide positive confirmation and minor suggestions for improvement. |

## B — Boundary Conditions
- **This skill diagnoses methodological errors, not statistical violations**: It does not check assumptions (normality, homoscedasticity, linearity). Those are separate checks.
- **Does not cover SEM or multilevel models**: Anti-patterns specific to structural equation modeling or multilevel analysis are outside scope.
- **Cultural differences in methodological standards**: Some fields still favor causal steps. This skill follows the consensus in social/behavioral sciences as represented by Hayes (2022).
- **Does not provide legal or ethical advice**: Issues of research integrity (fabrication, plagiarism) are outside scope.

## References
- Hayes, A. F. (2022). Chapters 4, 9, 12, 14; Preface.
- Yzerbyt, V., Muller, D., Batailler, C., & Judd, C. M. (2018). New recommendations for testing indirect effects.
