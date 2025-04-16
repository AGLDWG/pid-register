from pathlib import Path
from rdflib import Graph
from rdflib.namespace import SDO

PIDS_DIR = Path(__file__).parent.parent.resolve() / "pids/resources"
APACHE_CONF_DIR = Path(__file__).parent.parent.resolve() / "tests/apache/conf"

g = Graph()

for f in sorted(PIDS_DIR.rglob("*.ttl")):
    print(f"loading {f}")
    g += Graph().parse(f)
    print(f"# {len(g)}")

conf_file = ""

for iri, redir in g.subject_objects(SDO.location):
    conf_file += f"# {iri}\n"
    conf_file += f"{redir}\n\n"

open(APACHE_CONF_DIR / "pids.conf", "w").write(conf_file)
