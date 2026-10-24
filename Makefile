.PHONY: all clean docs

all: docs
	

docs:
	$(MAKE) -C docs

clean:
	$(MAKE) -C docs clean
