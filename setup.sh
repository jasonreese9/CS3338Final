#!/bin/bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# pdflatex
brew install --cask mactex
# mmdc for making pretty diagrams from mermaid.
brew install mermaid-cli

# make sure we have tex plugins we need:
sudo tlmgr update --self
sudo tlmgr install enumitem titling
