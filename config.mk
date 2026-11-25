# -*- mode: makefile -*-
.PHONY: all clean docs

# 2. Dynamically gather all .tex files and define their matching .pdf targets
# Except for project_macros.tex
TEX_FILES := $(filter-out project_macros.tex,$(wildcard *.tex))
PDF_FILES := $(patsubst %.tex,%.pdf,$(TEX_FILES))
PROJECT_MACROS ?= ../project_macros.tex

# 3. Standard entry targets
all:: $(PDF_FILES)

clean::


$(TEX_FILES): $(PROJECT_MACROS)

$(PDF_FILES): $(PROJECT_MACROS) $(TEX_FILES)

# build twice so we always get the TOC correct.
%.pdf:: %.tex
	@echo "Compiling $< -> $@"
	pdflatex -halt-on-error -interaction=nonstopmode $< | grep -v /usr/local/texlive
	pdflatex -halt-on-error -interaction=nonstopmode $< | grep -v /usr/local/texlive

clean::
	-rm -f $(PDF_FILES)
	-rm -f *.aux *.log *.out *.toc
