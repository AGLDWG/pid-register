from pathlib import Path

for f in Path(__file__).parent.glob('*.ttl'):
    print(f)
    txt = f.read_text()

    new_txt = txt.replace("/org/abares", f"/org/{f.name.replace('.ttl', '')}")
    print(new_txt)

    f.write_text(new_txt)