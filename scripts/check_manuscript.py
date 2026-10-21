#!/usr/bin/env python3
"""Check bibliography references and prohibited publication artifacts without third-party dependencies."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
paper = (root / "paper/main.tex").read_text(encoding="utf-8")
make = (root / "Makefile").read_text(encoding="utf-8")
bib = re.findall(r"\\bibitem\{([^}]+)\}", paper)
cited = [key.strip() for group in re.findall(r"\\parencite\{([^}]+)\}", paper) for key in group.split(",")]
problems = []
if len(bib) != len(set(bib)):
    problems.append("duplicate bibliography keys")
unknown = sorted(set(cited) - set(bib))
if unknown:
    problems.append("undefined citations: " + ", ".join(unknown))
uncited = sorted(set(bib) - set(cited))
if uncited:
    problems.append("uncited bibliography entries: " + ", ".join(uncited))
if "Rockt\"aschel" in paper:
    problems.append("malformed Rocktaschel author accent")
if "/Users/" in make:
    problems.append("machine-specific Makefile path")
if re.search(r"\\begin\{(?:equation|align)\}", paper):
    problems.append("unintended manuscript equations")
if "This intersection suggests five analytically distinct layers:" in paper:
    problems.append("four dimensions incorrectly described as five layers")
if not (root / "tests/test_mismatch_exploration.py").exists():
    problems.append("missing exploratory-tooling test suite")
if problems:
    for p in problems:
        print("FAIL:", p)
    sys.exit(1)
print(f"PASS: {len(bib)} bibliography entries, {len(set(cited))} cited, no undefined/uncited keys")
