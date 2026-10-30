.PHONY: all clean

all: project_design_spec.pdf
	$(MAKE) -C Software_Requirement_Specifications all
	$(MAKE) -C Software_Design_Documents all
	$(MAKE) -C TestRail_Documents all
	$(MAKE) -C Workflow_Diagram all
	$(MAKE) -C User_Manual Snapshot_Objectives all

%.pdf: %.tex
	pdflatex  $<

clean:
	rm *.pdf *.log 
	$(MAKE) -C Software_Requirement_Specifications clean
	$(MAKE) -C Software_Design_Documents clean
	$(MAKE) -C TestRail_Documents clean
	$(MAKE) -C Workflow_Diagram clean
	$(MAKE) -C User_Manual Snapshot_Objectives clean
