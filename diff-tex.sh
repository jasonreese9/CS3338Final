#!/bin/zsh
# a simple git diff to diff only the tex files.
# this filters out all of the toc's and pdfs.
git diff main '*/*.tex' '*/*/*.tex'