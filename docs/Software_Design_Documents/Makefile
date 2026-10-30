.PHONY: all clean

all: Software_Design_Documents.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 