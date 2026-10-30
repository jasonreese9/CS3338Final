.PHONY: all clean

all: Workflow_Diagram.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 