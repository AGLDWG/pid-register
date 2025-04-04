import json
from rdflib import URIRef, Namespace, Literal, Graph
from rdflib.namespace import RDF, SDO, XSD
import re
from pathlib import Path
LDG = Namespace("https://linked.data.gov.au")

DIR = Path(__file__).parent

def remove_html_tags(text):
    txt = re.sub(r'<.*?>', '', text)

    return txt.replace("\r", "").strip()


j = json.load(open(DIR / "orgs.json"))

cat = Graph()
cat.parse(DIR.parent / "catalogue.ttl", format="turtle")

for org in j:
    g = Graph()
    org_iri = LDG[org["path"][0]["alias"]]
    org_id = org["path"][0]["alias"].replace('/org/', '')
    g.add((org_iri, RDF.type, SDO.Organization))
    g.add((org_iri, SDO.name, Literal(org["title"][0]["value"])))
    g.add((org_iri, SDO.description, Literal(remove_html_tags(org["body"][0]["value"]))))

    if len(org["field_homepage"]) > 0:
        g.add((org_iri, SDO.url, Literal(org["field_homepage"][0]["uri"], datatype=XSD.anyURI)))

    if len(org["field_unit_of"]) > 0:
        g.add((org_iri, SDO.isPartOf, LDG[org["field_unit_of"][0]["url"]]))

    if len(org["field_agor_identifier"]) > 0:
        g.add((org_iri, SDO.identifier, Literal(org["field_agor_identifier"][0]["value"], datatype=LDG["/org/agorId"])))

    if len(org["field_ror_identifier"]) > 0:
        g.add((org_iri, SDO.identifier, Literal(org["field_ror_identifier"][0]["uri"], datatype=LDG["/org/rorId"])))

    if len(org["field_crs_identifier"]) > 0:
        g.add((org_iri, SDO.identifier, Literal(org["field_crs_identifier"][0]["value"], datatype=LDG["/org/crsId"])))

    if len(org["field_grid_identifier"]) > 0:
        g.add((org_iri, SDO.identifier, Literal(org["field_grid_identifier"][0]["uri"], datatype=LDG["/org/gridId"])))

    g.bind("o", "https://linked.data.gov.au/org/")
    g.serialize(destination=DIR.parent / f"resources/{org_id}.ttl", format="longturtle")
    print(f"Created {org_id}")

    cat.add((URIRef("https://linked.data.gov.au/org"), SDO.hasPart, org_iri))

cat.serialize(destination=DIR.parent / "catalogue.2.ttl", format="longturtle")