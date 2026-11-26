# -*- mode: makefile -*-
# this has to be set before the include so we can find project_macros.tex
# for project_design_spec.pdf.
PROJECT_MACROS = project_macros.tex

# Relative include so this works in paths containing spaces.
include ../config.mk

.PHONY: mermaid

# Define all subdirectories in one clean list
SUBDIRS := Software_Requirement_Specification \
           Software_Design_Document \
           TestRail_Document \
           Workflow_Diagram \
           User_Manual \
           Snapshot_Objectives


all:: project_design_spec.pdf
	@for dir in $(SUBDIRS); do $(MAKE) -C $$dir all; done

mermaid::
	@for dir in $(SUBDIRS); do $(MAKE) -C $$dir mermaid; done

clean::
	@for dir in $(SUBDIRS); do $(MAKE) -C $$dir clean; done
