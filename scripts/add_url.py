from pathlib import Path


for f in Path(Path(__file__).parent.parent.resolve() / "pids" / "resources" / "environment.data.gov.au").rglob('*.ttl'):
    txt = f.read_text()
    # txt = txt.replace('.\n', f'    schema:url "https://linked.data.gov.au/org/{f.name.replace(".ttl", "")}"^^xsd:anyURI ;\n.')
    txt = txt.replace('.\n', f'    schema:url "https://environment.data.gov.au/{f.name.replace(".ttl", "")}"^^xsd:anyURI ;\n.')
    f.write_text(txt)