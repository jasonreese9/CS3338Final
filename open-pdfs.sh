#!/bin/zsh
# find all pdfs in the current directory that are not in diagrams or references and open them.
open $(find . -name '*.pdf' -not -path '*/diagrams/*' -not -path '*/reference/*')