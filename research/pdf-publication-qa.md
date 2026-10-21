# Reader PDF publication verification

- Date: 2026-10-21
- Source commit: `c3ff87f1fbbfdb65db963b182ed8295836ad1003` (main, after P0 manuscript corrections).
- Compiled from the exact commit in an isolated Ubuntu 26.04 sandbox with TeX Live 2025, `cm-super`, and `pdflatex`.
- Source commands: `make check` and `make paper`; both succeeded.
- Reader PDF: `paper/cross-layer-alignment.pdf` (21 U.S.-Letter pages).
- Optimization: Ghostscript `pdfwrite`, compatibility 1.7, prepress settings; vector and searchable text retained.
- PDF size: 180,624 bytes.
- SHA-256: `f7ab7362a84098aa775257bee66f6e274cc7bfcbef99958fa96bb522f6d4cd9b`.
- Git blob SHA-1: `07e0cc845a5b496ba3a5a30edc3d258046fdbeee`, independently matched by GitHub when uploaded.
- Structure: 21 pages; 8,556 normalized extracted words before and after optimization, matching word-for-word as multisets.
- Hyperlinks: 52 URL annotations before and after optimization.
- Raster comparison: all 21 pages rendered at reduced resolution. Re-encoding alters approximately 0.66% to 4.05% of pixels per page, consistent with font/rasterization changes; not a pixel-identical PDF.
- LaTeX warnings: no overfull boxes, missing characters, or unresolved citations in the final build log.

The committed PDF is a reading artifact, not a replacement for the LaTeX source. Full-resolution human visual review and independent claim-by-claim citation validation remain separate publication acceptance activities.
