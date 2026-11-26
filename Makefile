# -*- mode: makefile -*-
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

.PHONY: all clean docs mermaid

all:: docs
	@echo

docs::
	$(MAKE) -C docs

mermaid::
	$(MAKE) -C docs mermaid

clean::
	$(MAKE) -C docs clean
