from pathlib import Path
from rdflib import Graph, URIRef, Literal, Namespace, XSD
from rdflib.namespace import OWL, RDF, SDO, SKOS
import json
from operator import itemgetter


ASTATUS = Namespace("https://linked.data.gov.au/def/reg-statuses/")
LDG = Namespace("https://linked.data.gov.au")
PID = Namespace("https://linked.data.gov.au/def/pid/")
CAT = Namespace("https://linked.data.gov.au/person/")
STATUS = Namespace("https://linked.data.gov.au/def/reg-statuses/")

DIR = Path(__file__).parent


def make_pids_initial_from_json():
    j = json.load(open(DIR / "pids.json"))

    g2 = Graph()

    for pid in sorted(j, key=itemgetter("field_agldwg_identifier")):
        g = Graph()
        g.bind("pid", Namespace("https://linked.data.gov.au/def/pid/"))
        g.bind("status", STATUS)
        print(pid["field_agldwg_identifier"])
        if "environment.data.gov.au" in pid["field_agldwg_identifier"]:
            pid_iri = URIRef(pid["field_agldwg_identifier"])
        else:
            pid_iri = LDG[pid["field_agldwg_identifier"]]
        g.add((pid_iri, RDF.type, PID.PID))
        g.add((pid_iri, SDO.name, Literal(pid["title"])))
        usr_iri = CAT[pid["field_contact_person"]]
        g.add((pid_iri, SDO.creator, usr_iri))
        g.add((pid_iri, SDO.ownedFrom, LDG[pid["field_creator"]]))
        g2.add((usr_iri, SDO.memberOf, LDG[pid["field_creator"]]))
        g.add((pid_iri, SDO.status, STATUS[pid["field_registry_status"]]))
        if pid["field_date_accepted"] != "":
            g.add((pid_iri, SDO.dateIssued, Literal(pid["field_date_accepted"], datatype=XSD.date)))
        if pid["created"] != "":
            g.add((pid_iri, SDO.dateCreated, Literal(pid["created"], datatype=XSD.date)))
        if pid["changed"] != "":
            g.add((pid_iri, SDO.dateModified, Literal(pid["changed"], datatype=XSD.date)))

        if "environment.data.gov.au" in pid["field_agldwg_identifier"]:
            # http://environment.data.gov.au/def/ba/glossary
            file_name = pid["field_agldwg_identifier"].replace("http://environment.data.gov.au/", "")
            file_name = file_name.replace("/", "-") + ".ttl"
            file_name = DIR.parent / "resources" / "environment.data.gov.au" / file_name
        else:
            file_parts = f'{pid["field_agldwg_identifier"]}.ttl'.split("/")
            file_name = DIR.parent / "resources" / file_parts[1] / file_parts[2]
        g.serialize(destination=file_name, format="longturtle")

    g2.serialize(destination=DIR.parent / "resources" / "people.ttl", format="longturtle")


if __name__ == '__main__':

    make_pids_initial_from_json()
