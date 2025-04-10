# Organisations Catalogue

This catalogue is the organisation and person management system for the AGLDWG. It reuses organisation PIDs stored in the PID Catalogue.

This catalogue (will be) online at <https://linked.data.gov.au/org>

The content of this catalogue is as follows:

| Resource                                                    | Role                                                                                                                    | Description                                                                                            |
|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| Catalogue Definition:<br />[`catalogue.ttl`](catalogue.ttl) | [Catalogue Data](https://prez.dev/ManifestResourceRoles/CatalogueData)                                                  | The definition of, and metadata for, the catalogue object                                              |
| Resource Data:<br />[`resources/*.ttl`](resources/*.ttl)    | [Resource Data](https://prez.dev/ManifestResourceRoles/ResourceData)                                                    | The individual resources - one per RDF (Turtle) file - in the resources/ folder                        |
| Ontology Labels:<br />[`labels.ttl`](labels.ttl)            | [Incomplete Catalogue and Resource Labels](https://prez.dev/ManifestResourceRoles/IncompleteCatalogueAndResourceLabels) | An RDF file containing all the labels for ontology elements - predicates & classes - in this catalogue |
