# -*- mode: makefile -*-
# Generates api.mmd from openapi-v1.yaml, then renders it to a .png, .svg and .pdf
# using the mermaid rules in config.mk.
# openapi-v1.yaml is the API specification and is not built.
# Relative include so this works in paths containing spaces.
include ../../config.mk

# api.mmd is generated from the specification with the Python standard library only.
PYTHON ?= python3.14

api.mmd: openapi-v1.yaml openapi_to_mermaid.py
	$(PYTHON) openapi_to_mermaid.py openapi-v1.yaml api.mmd
