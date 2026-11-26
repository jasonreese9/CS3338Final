# -*- mode: makefile -*-
.PHONY: all clean docs mermaid

# 2. Dynamically gather all .tex files and define their matching .pdf targets
# Except for project_macros.tex
TEX_FILES := $(filter-out project_macros.tex,$(wildcard *.tex))
PDF_FILES := $(patsubst %.tex,%.pdf,$(TEX_FILES))
PROJECT_MACROS ?= ../project_macros.tex

# Mermaid diagrams: every .mmd file is rendered to a .png and .svg with mmdc.
MMDC ?= mmdc
# Use the installed Chrome instead of puppeteer's downloaded headless shell.
CHROME ?= /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
MMD_FILES := $(wildcard *.mmd)
# Only render when both mermaid-cli and Chrome are installed; otherwise skip
# and keep the existing images.
HAVE_MMDC := $(shell command -v "$(MMDC)" >/dev/null 2>&1 && echo yes)
HAVE_CHROME := $(shell test -x "$(CHROME)" && echo yes)
ifeq ($(HAVE_MMDC)$(HAVE_CHROME),yesyes)
MMD_OUTPUTS := $(MMD_FILES:.mmd=.png) $(MMD_FILES:.mmd=.svg)
else
MMD_OUTPUTS :=
endif

# 3. Standard entry targets
all:: mermaid $(PDF_FILES)

# `make mermaid` regenerates just the diagram images.
mermaid:: $(MMD_OUTPUTS)
ifneq ($(strip $(MMD_FILES)),)
ifeq ($(strip $(MMD_OUTPUTS)),)
	@echo "Skipping mermaid diagrams: mermaid-cli ($(MMDC)) or Chrome ($(CHROME)) not found"
endif
endif

clean::


$(TEX_FILES): $(PROJECT_MACROS)

$(PDF_FILES): $(PROJECT_MACROS) $(TEX_FILES) $(MMD_OUTPUTS)

%.png: %.mmd
	@echo "Rendering $< -> $@"
	PUPPETEER_EXECUTABLE_PATH="$(CHROME)" $(MMDC) -i $< -o $@ --scale 3

%.svg: %.mmd
	@echo "Rendering $< -> $@"
	PUPPETEER_EXECUTABLE_PATH="$(CHROME)" $(MMDC) -i $< -o $@

# build twice so we always get the TOC correct.
%.pdf:: %.tex
	@echo "Compiling $< -> $@"
	pdflatex -halt-on-error -interaction=nonstopmode $< | grep -v /usr/local/texlive
	pdflatex -halt-on-error -interaction=nonstopmode $< | grep -v /usr/local/texlive

clean::
	-rm -f $(PDF_FILES)
	-rm -f *.aux *.log *.out *.toc
