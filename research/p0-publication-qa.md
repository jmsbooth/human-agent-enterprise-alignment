# P0 publication QA evidence

Date: 2026-10-21 (UTC)
Repository: `jmsbooth/human-agent-enterprise-alignment`
Branch: `paper/p0-publication-qa`
Validated manuscript commit: `4423000ce67b3aa8d2c969ca75a6f9c0c56366a1`
Scope of subsequent change: README TeX font dependency documentation only (`95b286f107ab019a25babaf402cae7c86088f6c7`).

## Execution context

- Isolated disposable Vercel sandbox initialized from the GitHub branch at the exact revision above.
- Ubuntu 26.04 with Python 3.14.4 and TeX Live 2025 package set.
- Installed test/build dependencies: `make`, `texlive-latex-base`, `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-pictures`, `cm-super`, and `poppler-utils`.
- The first TeX compilation failed with `pdfTeX error (font expansion): auto expansion is only possible with scalable fonts` when `cm-super` was absent. Installing `cm-super` resolved the failure; README updated to document this prerequisite.

## Actual validation results

| Check | Result | Evidence |
| --- | --- | --- |
| `python3 scripts/check_manuscript.py` | PASS | 48 bibliography keys, 48 cited, no undefined or unused keys |
| `python3 -m unittest discover -s tests -v` | PASS | 6 of 6 unit tests |
| `python3 -m experimental.mismatch_exploration --output /tmp/paper-mismatch.json` | PASS | Exploratory JSON written |
| `make check` | PASS | Manuscript check, unit tests, and exploratory JSON export |
| `make paper` | PASS | Two `pdflatex` passes after installing scalable fonts |
| PDF metadata | PASS | 21 pages, U.S. Letter, 375,682 bytes |
| LaTeX diagnostics | PASS | No `Overfull`, `Missing character`, `Citation ... undefined`, or `LaTeX Warning` patterns in final log |
| PDF text extraction | PASS | `pdftotext -layout` recovered the framework figure caption, Tables 1-3 captions, and references |
| Visual spot-check | PARTIAL | Page 12 (mismatch catalog) rendered to JPEG and inspected at reduced resolution; no obvious clipping observed |

## Boundaries

- The source has been compiled from GitHub at the validated commit, not reconstructed from an older uploaded manuscript.
- The PDF generated within the disposable sandbox is not currently committed to GitHub. Production/release PDF publication is a separate packaging action.
- Visual inspection was a reduced-resolution spot-check of one page, not a full-resolution inspection of all 21 pages. A final all-page visual pass is recommended before labeling the archival PDF final.
- Bibliography structural consistency and selected external source metadata were checked; checking all 48 external source claims against full papers was not completed in this execution.
- No empirical validation is claimed. This remains a conceptual research paper.

## Disposition

Source and reproducibility P0 gates pass. Publication artifact's exhaustive visual review and independent source-to-claim verification should be completed before the first archival release.
