from pathlib import Path
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import OWL, RDF, SDO, SKOS
import json

ASTATUS = Namespace("https://linked.data.gov.au/def/reg-statuses/")
ORG = Namespace("https://linked.data.gov.au/org/")
LDG = Namespace("https://linked.data.gov.au")

DIR = Path(__file__).parent

ORGS_HOME = Path("/Users/nick/work/agldwg/pid-proxy/conf/linked.data.gov.au/org")

pattern_iri = None
pattern_text = ""
i = 0
for f in sorted(ORGS_HOME.rglob("*.conf")):
    for line in f.read_text().splitlines():
        if line.startswith("# https://linked.data.gov.au"):
            if pattern_iri is not None:
                print(line)

                org_name = str(f.name).replace(".conf", "")
                file_name = line.replace("# https://linked.data.gov.au/", "")

                x = Graph().parse(Path(__file__).parent.parent / "resources" / f"{file_name}.ttl")
                x.add((pattern_iri, SDO.location, Literal(pattern_text.strip())))
                x.add((pattern_iri, SDO.ownedThrough, ORG[org_name]))
                print(x.serialize(format="longturtle"))

            pattern_text = ""
            pattern_iri = URIRef(line.split("# ")[1])
        elif line.startswith("#"):
            pass
        else:
            pattern_text += line + "\n"
    i += 1
    # if i > 5:
    #     break


# g_reg.serialize(destination=DIR / "reg-initial.ttl", format="longturtle")