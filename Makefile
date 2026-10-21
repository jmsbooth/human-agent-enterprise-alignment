PYTHON ?= python3
# Use a portable installed TeX engine; override LATEX_ENGINE if needed.
LATEX_ENGINE ?= pdflatex
BUILD_DIR ?= build
EXPERIMENT_OUTPUT ?= $(BUILD_DIR)/mismatch-exploration.json
GHOSTSCRIPT ?= gs
PUBLISHED_PDF ?= paper/cross-layer-alignment.pdf

.PHONY: check test experiment paper all publish-pdf

test:
	$(PYTHON) -m unittest discover -s tests -v

experiment:
	mkdir -p $(BUILD_DIR)
	$(PYTHON) -m experimental.mismatch_exploration --output $(EXPERIMENT_OUTPUT)

check: manuscript test experiment

.PHONY: manuscript
manuscript:
	$(PYTHON) scripts/check_manuscript.py

paper:
	mkdir -p $(BUILD_DIR)/paper
	$(LATEX_ENGINE) -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=$(BUILD_DIR)/paper paper/main.tex
	$(LATEX_ENGINE) -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=$(BUILD_DIR)/paper paper/main.tex

publish-pdf: paper
	$(GHOSTSCRIPT) -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.7 -dPDFSETTINGS=/prepress -sOutputFile=$(PUBLISHED_PDF) $(BUILD_DIR)/paper/main.pdf

all: check paper
