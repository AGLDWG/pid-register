import csv

from rdflib import Graph
from rdflib.namespace import RDF, SDO
import httpx


g = Graph().parse("patterns.ttl")

resolving = []
not_resolving = []

for s in g.subjects(RDF.type, [SDO.DefinedTermSet, SDO.Dataset]):
    print(s)
    try:
        r = httpx.get(str(s), follow_redirects=True)
    except Exception as e:
        not_resolving.append((s, 500))
        continue

    if r.is_success:
        resolving.append((s, r.status_code))
    else:
        not_resolving.append((s, r.status_code))


print(len(resolving), len(not_resolving))

with open("resolving.csv", "w") as f:
    writer = csv.writer(f)
    for x in resolving:
        writer.writerow(x)

with open("not_resolving.csv", "w") as f:
    writer = csv.writer(f)
    for x in not_resolving:
        writer.writerow(x)

for s in g.subjects(RDF.type, )