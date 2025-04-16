# AGLDWG PID Register

This repository contains the source data for the [Australian Government Linked Data Working Group](https://www.linked.data.gov.au) (AGLDWG)'s Persistent Identifier (PID) and Organisations catalogues. The register maintains PIDs within the `linked.data.gov.au` namespace.

## PID Catalogue

The AGLDWG created PIDs for three types of thing:

* Datasets
    * Linked Data datasets online
* Definitional Items
    * Linked Data ontologies, vocabularies, profiles, etc.
* Organisations
    * for any organisation that submits PID requests to the AGLDWG

## Creating PIDs

PIDs for all these items redirect to their human- and machine-readable home locations online which are provided by the PID registers, not the AGLDWG.

The AGLDWG creates PIDs according to its [Guidelines](https://www.linked.data.gov.au/guidelines). PIDs, once approved, are automatically enabled through extraction of redirect information from this catalogue and automated deployment to the PID Proxy server at `linked.data.gov.au`.

Please refer to the [AGLDWG website](https://www.linked.data.gov.au) for more details about who can and how to make PIDs.

## Organisation Catalogue

The Organisations catalogue maintains information about organisations and people beyond just PID information, such organisation relations and PID management details. 

Organisations can be added to the catalogue by request - directly to the AGLDWG. All organisations involved with PIDs will also be added to the catalogue.

## License

All the content of this repository is licensed with the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license with the following copyright notice:

&copy; Commonwealth of Australia (Australian Government Linked Data Working Group), 2025

## Contact

For all matters relating to this repository and the registry that it supports, please contact:

**Australian Government Linked Data Working Group**  
<linkeddatairi@ardc.edu.au>  
<https://www.linked.data.gov.au>  


## Operating Instructions

Many of the operational tasks required to maintain the PID Register are coded into Docker and Python scripts that can be run via the "Task" task runner / build tool.

All the tasks available are listed in Taskfile.yml, e.g. `rdf2conf`, `aup` & `adown`.

They are run simply by typing `task aup` etc. on the (Linux-like) command line.

### Adding a new PID

### Testing a new PID

1. Run the RDF-to-conf script

```bash
task rdf2conf
```

2. Start the test server container

```bash
task aup
```