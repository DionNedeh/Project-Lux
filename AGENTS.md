# Project Lux publication instructions

- Use subagents only when the user explicitly requests them.
- Preserve the approved ivory/copper design and the distinction between Lux and Spira.
- The working research vault is separate. `research/` is a deliberate public snapshot, not an intake directory for raw papers.
- Do not publish raw downloaded papers, captured full article text, internal logs, personal workspace state, credentials, or browser profiles.
- Preserve original dates, conflicting findings, access limits, and the distinction between experiments, simulations, designs and announcements. Confidence metadata is not certification.
- Never claim that publishing the library revalidates all research, or that a control experiment proves whole-plant energy efficiency.
- Edit templates, styles, scripts and build inputs; regenerate the published HTML with `python tools/build_site.py`.
- Run the relevant renderer tests and browser checks. All source/generated changes must pass the build, local link and anchor checks, and clean rebuild check before deployment.
- Do not weaken a validation gate to get a passing result. Correct false test assumptions explicitly; retain meaningful coverage.
- External publication requires current authorisation. The user's explicit standing approval within a session remains valid for its stated scope.
- Report exactly which checks ran. Do not claim unrun builds, visual reviews, live checks or deployments.
