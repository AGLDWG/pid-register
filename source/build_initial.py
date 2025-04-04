# This script parses the .conf files in a locally-cloned copy of https://github.com/AGLDWG/pid-proxy
# and presents the PID patterns in RDF data

from pathlib import Path
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import OWL, RDF, SDO, SKOS
import json

ASTATUS = Namespace("https://linked.data.gov.au/def/reg-statuses/")
ORG = Namespace("https://linked.data.gov.au/org/")
LDG = Namespace("https://linked.data.gov.au")

DIR = Path(__file__).parent

g_def = Graph()
g_dataset = Graph()
g_reg = Graph()
g_org = Graph().parse(DIR / "org-pre.ttl")


ORGS_HOME = Path("/Users/nick/work/agldwg/pid-proxy/conf/linked.data.gov.au/org")

ADDITIONAL_TYPES = {
    "vocabulary": SKOS.ConceptScheme,
    "ontology": OWL.Ontology,
    "dataset": SDO.Dataset,
    "organisation": SDO.Organization,
    "register": SDO.DataCatalog,
}

pattern_iri = None
pattern_text = ""
for f in sorted(ORGS_HOME.rglob("*.conf")):
    for line in f.read_text().splitlines():
        if line.startswith("# https://linked.data.gov.au"):
            if pattern_iri is not None:
                x = Graph()
                x.add((pattern_iri, SDO.location, Literal(pattern_text.strip())))
                x.add((pattern_iri, SDO.publisher, ORG[str(f.name).replace(".conf", "")]))

                if "/dataset/" in pattern_iri:
                    g_dataset += x
                elif "/def/" in pattern_iri:
                    g_def += x
                elif "/reg/" in pattern_iri:
                    g_reg += x

            pattern_text = ""
            pattern_iri = URIRef(line.split("# ")[1])
        elif line.startswith("#"):
            pass
        else:
            pattern_text += line + "\n"

j = json.load(open(DIR / "resources.json"))

for pat in j:
    if pat["type"] != "organisation":
        pattern_iri = LDG[pat["field_agldwg_identifier"]]
        if "environment.data.gov.au" in str(pattern_iri):
            pattern_iri = URIRef(str(pattern_iri).replace("https://linked.data.gov.auhttp://environment.data.gov.au", "https://environment.data.gov.au"))

        x = Graph()
        x.add((pattern_iri, SDO.name, Literal(pat["title"])))
        x.add((pattern_iri, SDO.additionalType, ADDITIONAL_TYPES[pat["type"]]))
        x.add((pattern_iri, SDO.dateCreated, Literal(pat["created"])))
        x.add((pattern_iri, SDO.dateModified, Literal(pat["changed"])))
        if pat["field_registry_status"] != "":
            x.add((pattern_iri, SDO.status, ASTATUS[pat["field_registry_status"].strip('"')]))
        if pat["field_date_accepted"] != "":
            x.add((pattern_iri, SDO.datePublished, Literal(pat["field_date_accepted"])))

        if pat["type"] == "dataset":
            g_dataset += x
        elif pat["type"] == "vocabulary" or pat["type"] == "ontology":
            g_def += x
        elif pat["type"] == "register":
            g_reg += x


g_def.serialize(destination=DIR / "def-initial.ttl", format="longturtle")
g_dataset.serialize(destination=DIR / "dataset-initial.ttl", format="longturtle")
g_org.serialize(destination=DIR / "org-initial.ttl", format="longturtle")
g_reg.serialize(destination=DIR / "reg-initial.ttl", format="longturtle")