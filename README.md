# README

This is the CS3338 Final project based on 
[AI-Powered University Information System](https://ascent.cysun.org/project/project/view/253
)

# Pre-requisites
This project requires `make` and `pdflatex`, these can be installed using [homebrew](https://brew.sh) on a mac by running the `./setup.sh` script.

## Building
`make` will build the pdfs from LaTex files within the docs directory.

All documentation is written in LaTex in the form of a `.tex` file which is then compiled to a pdf using `pdflatex`.

The docker images are built using docker compose.


# Layout

The layout is as follows:
```
.
├── assets
│   ├── SDD_images
│   └── SRS_images
├── docs
│   ├── Snapshot_Objectives
│   ├── Software_Design_Documents
│   ├── Software_Requirement_Specifications
│   ├── TestRail_Documents
│   ├── User_Manual
│   └── Workflow_Diagram
├── reference
└── src
    ├── backend
    │   └── node_modules
    └── frontend
        ├── node_modules
        ├── public
        └── src
```

## /assets
This directory contains any images referenced in the documents.

## /docs
This directory contains all of the documentation written for the project.


### /docs/Snapshot_Objectives
### /docs/Software_Design_Documents
### /docs/Software_Requirement_Specifications
### /docs/TestRail_Documents
### /docs/User_Manual
### /docs/Workflow_Diagram

## /reference
This folder contains the reference files from [AI-Powered University Information System](https://ascent.cysun.org/project/project/view/253
).

## /src
This directory contains the Docker files to build the runtime.

## /src/backend
This directory contains the Docker image for the backend.

## /src/frontend
This directory contains the Docker image for the frontend.

