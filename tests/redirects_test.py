from pathlib import Path
from rdflib import Graph
from rdflib.namespace import SDO
import json
import httpx

PIDS_DIR = Path(__file__).parent.parent.resolve() / "pids/resources"
TEST_PIDS_DIR = Path(__file__).parent.parent.resolve() / "tests/pids"

REDIRECTOR_BASE_URL = "http://localhost:8080"


def make_pid_graph():
    g = Graph()

    for f in sorted(PIDS_DIR.rglob("*.ttl")):
        g += Graph().parse(f)
        print(len(g))

    return g


def iri_2_path(iri):
    fn = str(iri).replace("https://linked.data.gov.au/pid/", "")
    fn = fn.replace("https://reference.data.gov.au/", "")
    fn = fn.replace("https://environment.data.gov.au/", "")
    return TEST_PIDS_DIR / f"{fn}.json"


def iri_2_local(iri):
    local = str(iri).replace("https://linked.data.gov.au", REDIRECTOR_BASE_URL)
    local = local.replace("https://reference.data.gov.au", "")
    local = local.replace("https://environment.data.gov.au", "")
    return local


def get_testable_pids():
    g = make_pid_graph()

    testables = {}

    for iri, redir in sorted(list(g.subject_objects(SDO.location))):
        test_file = iri_2_path(iri)
        if test_file.is_file():
            testables[str(iri)] = json.load(open(test_file))

    return testables


def test_redirects():
    for k, v in get_testable_pids().items():
        print(k)
        for t in v:
            label = t['label']
            local_from = iri_2_local(t['from'])
            expected = t['to']

            r = httpx.get(local_from, headers=t['headers'])
            actual = r.next_request.url

            err = f"""{label}:
{iri_2_local(t['from'])} did not redirect to 
{expected} but 
{actual}"""

            assert actual == expected, err


def test_one_redirect(iri):
    test_file = iri_2_path(iri)
    print(test_file)
    if test_file.is_file():
        for t in json.load(open(test_file)):
            label = t['label']
            local_from = iri_2_local(t['from'])
            expected = t['to']

            r = httpx.get(local_from, headers=t['headers'])
            actual = r.next_request.url

            err = f"""{label}:
            {iri_2_local(t['from'])} did not redirect to 
            {expected} but 
            {actual}"""

            assert actual == expected, err
    else:
        raise ValueError(f"No test file for IRI {iri}")


if __name__ == "__main__":
    test_redirects()
    # test_one_redirect("https://linked.data.gov.au/def/plot")