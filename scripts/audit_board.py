"""Inventory unchanged user references and export .const facts without filling gaps."""
import csv
import hashlib
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]


def main():
    source=ROOT/"Zynq7020"; out=ROOT/"evidence/preflight"; out.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for path in sorted(source.rglob("*")):
        if path.is_file():
            manifest.append({"path":path.relative_to(ROOT).as_posix(),"bytes":path.stat().st_size,
                             "sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                             "inspection":"Visual read of PNG / full XML text read of .const"})
    (out/"board_manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding="utf-8")
    rows=[]
    for path in sorted((source/"constrain").glob("*.const")):
        for port in ET.parse(path).getroot().findall("Port"):
            rows.append({"source":path.relative_to(ROOT).as_posix(),"package_pin":port.attrib["Name"],
                         "function_verbatim":port.attrib["Function"],"direction":port.attrib["Inout"],
                         "io_standard":"UNKNOWN", "bank_vcco":"UNKNOWN"})
    with (out/"documented_pin_candidates.csv").open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=rows[0].keys());writer.writeheader();writer.writerows(rows)
    print(f"Inventoried {len(manifest)} references, extracted {len(rows)} pin records (not board constraints)")


if __name__=="__main__":main()
