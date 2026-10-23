# Paper 0 technical build evidence

Build date: 23 October 2026. Source revision (manuscript): `be5354146d9ddb459e29383d9f21e46d698a7002`. Later commits changed documentation and publication packaging only.

## Commands and environment

- Isolated Ubuntu 26.04 sandbox checked out from the exact GitHub revision.
- Dependencies: TeX Live, `cm-super`, Poppler and Ghostscript.
- `make check`: **PASS**, including 57 defined and cited bibliography entries, zero uncited references, six Python regression tests, and exploratory catalog export.
- `make paper`: **PASS** (two `pdflatex` passes).
- `make publish-pdf`: **PASS**, optimized vector PDF.
- LaTeX: no unresolved citations, overfull boxes, undefined controls, fatal errors, missing glyphs, or duplicate labels after a second revision removed a redundant old framework figure.

## Publication binary

- Path: `paper/cross-layer-alignment.pdf`.
- Pages: 29, U.S. Letter.
- Size: 239,039 bytes.
- SHA-256: `832fdd919547320f20614d7e8681a5a34ab46daa992cfabe95d5f9b3b14e4b68`.
- Git blob SHA: `2961b5fd4c900f19f9a6afdfcdb9c09b6e9ae7d8`.
- Word multiset in `pdftotext -raw` before and after optimization: identical.
- URL annotations: 65 before and 65 after optimization.
- Paper 1 design specification: `research/paper-1-execution-spec.md`.


## Review PDF access and page inspection

- The GitHub review-branch raw PDF responded HTTP 200 with 239,039 bytes, 29 pages, and the expected SHA-256.
- All 29 pages were rasterized and reviewed as a numbered contact sheet. There were no obviously blank, truncated, or rearranged pages.
- The framework page and dense table pages were separately checked by `pdftotext -layout` for expected labels, captions, continuation text, and section order.
- `pdftotext -bbox` found 12,004 word bounding boxes. None fell outside conservative page coordinates (x 20-594, y 14-780 pt on U.S. Letter).
- A high-resolution, page-by-page reader inspection remains advisable before a release is labeled archival or peer reviewed.

## Remaining scholarly and publication work

This build confirms PDF integrity and compilation, not full scholarly acceptance. Before declaring an archival edition, complete all-page visual inspection, independent claim-to-source review, and author's substantive review of the new sections. The `main` branch continues serving the earlier PDF until the revised paper is accepted and merged.
