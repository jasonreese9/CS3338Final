.PHONY: all clean

all: TestRail_Documents.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 