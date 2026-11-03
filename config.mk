# -*- mode: makefile -*-
.PHONY: all clean docs

# 2. Dynamically gather all .tex files and define their matching .pdf targets
TEX_FILES := $(wildcard *.tex)
PDF_FILES := $(patsubst %.tex,%.pdf,$(TEX_FILES))

# 3. Standard entry targets
all:: $(PDF_FILES)

clean::

# build twice so we always get the TOC correct.
%.pdf:: %.tex
	@echo "Compiling $< -> $@"
	pdflatex -interaction=nonstopmode $<
	pdflatex -interaction=nonstopmode $<

clean::
	-rm -f $(PDF_FILES)
	-rm -f *.aux *.log *.out *.toc
