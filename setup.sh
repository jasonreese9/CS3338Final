#!/bin/bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install --cask mactex


# make sure we have tex plugins we need:
sudo tlmgr update --self
sudo tlmgr install enumitem titling
