.PHONY: all clean

all: Snapshot_Objectives.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 