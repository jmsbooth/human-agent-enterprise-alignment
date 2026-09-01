PYTHON ?= python3
# The bundled runtime is used in this workspace; override TECTONIC for a
# different installation or CI runner.
TECTONIC ?= /Users/jamesbooth/.codex/plugins/cache/openai-bundled/latex/0.2.6/bin/tectonic
BUILD_DIR ?= build
EXPERIMENT_OUTPUT ?= $(BUILD_DIR)/mismatch-exploration.json

.PHONY: check test experiment paper all

test:
	$(PYTHON) -m unittest discover -s tests -v

experiment:
	mkdir -p $(BUILD_DIR)
	$(PYTHON) -m experimental.mismatch_exploration --output $(EXPERIMENT_OUTPUT)

check: test experiment

paper:
	mkdir -p $(BUILD_DIR)/paper
	$(TECTONIC) -X compile --outdir $(BUILD_DIR)/paper --keep-logs paper/main.tex

all: check paper
