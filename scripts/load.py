import httpx

q = """
    SELECT DISTINCT ?g
    WHERE {
        GRAPH ?g {
            ?s ?p ?o
       }
    }
    ORDER BY ?g
    """
r = httpx.get(
    "https://fuseki.dev.kurrawong.ai/agldwg/",
    params={"query": q},
    auth=httpx.BasicAuth(username="kn", password="kn"),
)

for grf in list(r.json()["results"]["bindings"]):
    g = grf["g"]["value"]
    print(g)
    r = httpx.post(
        "https://fuseki.dev.kurrawong.ai/agldwg/",
        content=f"ADD <{g}> TO DEFAULT",
        auth=httpx.BasicAuth(username="kn", password="kn"),
        headers={"Content-Type": "application/sparql-update"},
    )
    print(r.status_code)
