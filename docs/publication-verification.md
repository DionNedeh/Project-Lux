# Initial publication verification

Prepared 11 November 2026 for Project Lux's first GitHub Pages release.

## Content and provenance

- Published snapshot: 282 complete research notes (46 syntheses, 48 source notes, 75 concepts, 106 entities and 7 topic guides), plus eight bounded citation briefs.
- Source Markdown retains its frontmatter, dates, qualifications, conflicting findings and access limitations. The manifest records both original byte hashes and line-ending-normalised text hashes.
- The source wiki lint completed with no broken links, orphan pages, thin pages, stubs, frontmatter defects, tag defects or new length-ceiling failures. Six grandfathered length exceptions and 98 below-target-length records were reported; this publication does not represent those as newly resolved.
- Raw third-party papers, full article captures, internal logs and personal workspace state are excluded from the public repository and deployment artifact.

## Checks performed before publication

| Check | Observed result |
|---|---|
| Static build and all-page validation | 295 HTML pages; 16,863 local link and asset references checked; zero reported errors |
| Original source text hashes | All 282 published notes matched the recorded normalised text hashes |
| Repeat generation | All 298 tracked generated outputs were unchanged on a repeat build |
| Markdown renderer and cross-platform asset regression tests | 7 passed |
| JavaScript syntax checks | Passed for the homepage and catalogue scripts |
| Browser suite | 20 passed using installed Microsoft Edge in headless mode on Windows |
| All-note HTTP and heading check | All 282 complete research pages returned successfully in the local publication preview |
| Automated accessibility | Eight representative pages had no axe WCAG 2 A/AA or WCAG 2.1 A/AA violations reported |
| Responsive layout checks | Eight representative pages checked at 1440, 768, 390 and 320 pixels; no page-level horizontal overflow |
| Interaction checks | Homepage panels, full-text and exact-phrase search, filters, sort, URL state, citations, source downloads, keyboard skip link, reduced motion and custom 404 passed |
| Progressive enhancement | Full research reading and homepage explanatory content remained available with JavaScript disabled |
| Runtime network behaviour | No third-party browser requests observed in the tested pages |

Manual screenshot review covered the desktop homepage, mobile catalogue, a full source note's results and limitations, and a mobile research table. Wide tables deliberately scroll within their own container. Automated browser checks are not a full manual screen-reader evaluation or real-device test.

## Deployment verification

The GitHub Actions workflow independently installs the pinned dependencies on Linux, rebuilds the site, checks that committed output is current, runs the renderer and Chromium browser suites, and then deploys the checked artifact. The workflow history records the actual result for each commit; this document does not substitute a local pass for a successful hosted run.

The initial hosted run caught a Windows/Linux line-ending difference in asset version hashes and stopped before deployment. The generator was corrected to hash normalised text, with a regression test covering both line endings and real content changes. The clean-generation deployment gate remains in place.

Live verification uses the same browser suite with `LUX_TEST_URL=https://dionnedeh.github.io/Project-Lux/`. See the release commit's workflow and the task handoff for the observed deployment and live-check result.

## Limits

This work validates publication, navigation, rendering and provenance. It does not newly reproduce the scientific experiments, revalidate every scientific claim, recheck every external publisher URL, or certify the library's confidence metadata. Research records remain individually dated; earlier forecasts and company announcements are preserved as dated evidence. Lux does not claim demonstrated whole-plant energy savings or an operating fusion power plant.
