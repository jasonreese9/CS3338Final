# -*- mode: makefile -*-
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

# Define all subdirectories in one clean list
SUBDIRS := Software_Requirement_Specification \
           Software_Design_Document \
           TestRail_Document \
           Workflow_Diagram \
           User_Manual \
           Snapshot_Objectives

all:: project_design_spec.pdf
	@for dir in $(SUBDIRS); do $(MAKE) -C $$dir all; done

clean::
	@for dir in $(SUBDIRS); do $(MAKE) -C $$dir clean; done
