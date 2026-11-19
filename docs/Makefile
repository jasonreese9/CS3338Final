# -*- mode: makefile -*-
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

# Use sed to chop off everything after CS3338Final
BASE_DIR := $(shell echo "$(MAKEFILE_DIR)" | sed 's/\(.*\/CS3338Final\).*/\1/')

# Include the file relative to the base directory
include $(BASE_DIR)/config.mk

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
