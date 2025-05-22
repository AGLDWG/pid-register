from pathlib import Path
import httpx
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import OWL, RDFS, SKOS

def get_label(iri):
    r = httpx.get(
        iri,
        headers={"Content-Type": "text/turtle"},
        follow_redirects=True
    )
    label = None
    if r.is_success:
        g = Graph().parse(data=r.text, format="turtle")
        label = g.value(URIRef(iri), SKOS.prefLabel)
        if label is None:
            label = g.value(URIRef(iri), RDFS.label)

    return label

files = sorted(Path(Path(__file__).parent.parent.resolve() / "resources").rglob("*.ttl"))

iris = []
for f in files:
    for l in f.read_text().splitlines():
        if l.startswith("<https://linked.data.gov.au/pid/"):
            iri = l.replace("/pid", "").strip("<>")
            iris.append((f, iri))

for iri in sorted(iris):
    print(f"{iri[0]},{iri[1]}")
