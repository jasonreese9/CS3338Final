.PHONY: all clean

all: Software_Requirement_Specifications.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 