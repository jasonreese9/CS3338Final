.PHONY: all clean

all: User_Manual.pdf

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 