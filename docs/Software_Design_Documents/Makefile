# -*- mode: makefile -*-
MAKEFILE_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
# Use sed to chop off everything after CS3338Final
BASE_DIR := $(shell echo "$(MAKEFILE_DIR)" | sed 's/\(.*\/CS3338Final\).*/\1/')

# Include the file relative to the base directory
include $(BASE_DIR)/config.mk
