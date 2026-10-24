.PHONY: all clean

all: project_design_spec.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 