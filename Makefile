# -*- mode: makefile -*-
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

.PHONY: all clean docs

all:: docs
	@echo

docs::
	$(MAKE) -C docs

clean::
	$(MAKE) -C docs clean
