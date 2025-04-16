from pathlib import Path
import json

JSON_DIR = Path(__file__).parent.resolve() / "json"

TEST_PIDS_DIR = Path(__file__).parent.parent.resolve() / "tests/pids"

d = dict()

for f in sorted(JSON_DIR.glob("*.json")):
    d.update(json.load(open(f)))

for k, v in d.items():
    if "reference.data.gov.au" in k:
        fn = k.replace("https://reference.data.gov.au/def/", "") + ".json"
        folder = "reference.data.gov.au/def"
    elif "environment.data.gov.au" in k:
        fn = k.replace("https://environment.data.gov.au/def/", "") + ".json"
        folder = "environment.data.gov.au/def"
    elif "/dataset/" in k:
        fn = k.replace("https://linked.data.gov.au/dataset/", "") + ".json"
        folder = "dataset"
    elif "/def/" in k:
        fn = k.replace("https://linked.data.gov.au/def/", "") + ".json"
        folder = "def"
    elif "/org/" in k:
        fn = k.replace("https://linked.data.gov.au/org/", "") + ".json"
        folder = "org"

    open(TEST_PIDS_DIR / folder / fn, "w").write(json.dumps(v, indent=4))