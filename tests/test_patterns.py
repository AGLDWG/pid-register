from pathlib import Path
from rdflib import Graph
from rdflib.namespace import SDO

PIDS_DIR = Path(__file__).parent.parent.resolve() / "pids/resources"
APACHE_CONF_DIR = Path(__file__).parent.parent.resolve() / "tests/apache/conf"


def test_patterns():
    g = Graph()

    for f in sorted(PIDS_DIR.rglob("*.ttl")):
        g += Graph().parse(f)

    for iri, redir in g.subject_objects(SDO.location):
        print(str(iri).replace("https://linked.data.gov.au", ""))


if __name__ == "__main__":
    test_patterns()