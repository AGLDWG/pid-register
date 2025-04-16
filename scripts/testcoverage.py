from pathlib import Path
from rdflib import Graph
from rdflib.namespace import SDO

PIDS_DIR = Path(__file__).parent.parent.resolve() / "pids/resources"
TEST_PIDS_DIR = Path(__file__).parent.parent.resolve() / "tests/pids"

g = Graph()

for f in sorted(PIDS_DIR.rglob("*.ttl")):
    g += Graph().parse(f)


def iri_2_path(iri):
    fn = str(iri).replace("https://linked.data.gov.au/", "")
    fn = fn.replace("https://reference.data.gov.au/", "")
    fn = fn.replace("https://environment.data.gov.au/", "")
    return TEST_PIDS_DIR / f"{fn}.json"

pids = 0
tests = 0
notests = []
for iri, redir in g.subject_objects(SDO.location):
    pids += 1
    if iri_2_path(iri).is_file():
        tests += 1
    else:
        notests.append(str(iri))

print(f"Test coverage is {round((tests / pids) * 100)}%")
print(f"No. of PIDs without tests is {pids - tests}")
# print("IRIs missing tests are:")
# for iri in sorted(notests):
#     print(iri)

