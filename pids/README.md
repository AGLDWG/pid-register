# PID Catalogue

This catalogue acts as a register of the the AGLDWG's Persistent Identifiers - PIDs.

The AGLDWG issues PIDs as per our [Guidelines](https://www.linked.data.gov.au/guidelines).

This catalogue (will be) online at the following locations:

* <https://linked.data.gov.au/dataset> - Linked Data datasets
* <https://linked.data.gov.au/def> - Definitional Objects, e.g. ontologies & vocabularies
* <https://linked.data.gov.au/org> - Organisations

The content of this catalogue is as follows:

| Resource                                                    | Role                                                                                                                    | Description                                                                                            |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Catalogue Definition:<br />[`catalogue.ttl`](catalogue.ttl) | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData)                                                  | The definition of, and metadata for, the catalogue object                                              |
| Resource Data:<br />[`resources/*.ttl`](resources/*.ttl)    | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                    | The individual resources - one per RDF (Turtle) file - in the resources/ folder and subfolders of it   |
| Ontology Labels:<br />[`labels.ttl`](labels.ttl)            | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing all the labels for ontology elements - predicates & classes - in this catalogue |
