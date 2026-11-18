from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

from tools.m36a_jee30_audit import (
    ROOT, SOURCE_PDF_SHA256, audit_inventory, load_inventory,
    verify_pdf_bytes,
)

original = load_inventory(ROOT / "docs/m36a_jee30_coverage.json")
historic = load_inventory(ROOT / "docs/m21a_coverage.json")
assert audit_inventory(original, historic)["frozen_apparatus_anchors"] == 30

def reject(label, callback, message):
    try:
        callback()
    except ValueError as exc:
        assert message in str(exc), (label, str(exc))
        print("EXPECTED REJECT:", label)
    else:
        raise AssertionError("FALSE ACCEPT: " + label)

for name, field, value in [
    ("fabricated source", "source", "fabricated-source.pdf#legacy-archive"),
    ("printed extra Q11", "printed_anchor",
     "Paper 1 Questions 9–10 and 11 (one two-charge apparatus)"),
    ("2021 plus Q11", "official_apparatus",
     {"paper": "JEE Advanced 2021 Paper 1",
      "question_ids": ["Q9", "Q10", "Q11"]}),
]:
    forged = deepcopy(original)
    forged["cases"][-1][field] = value
    reject(name, lambda f=forged: audit_inventory(f, historic),
           "2021 apparatus identity or grouping changed")

for refusal_id in ["p11-linked-28", "p70-cavity-offset",
                   "p70-three-cavities"]:
    forged = deepcopy(original)
    refusal = next(c for c in forged["cases"] if c["id"] == refusal_id)
    donor = next(c for c in forged["cases"]
                 if c["candidate_route"] == "supported_scoped"
                 and c["id"] != "p01-single-08")
    refusal["candidate_route"] = "supported_scoped"
    donor["candidate_route"] = "unsupported"
    assert sum(c["candidate_route"] == "unsupported"
               for c in forged["cases"]) == 3
    reject("balanced route swap " + refusal_id,
           lambda f=forged: audit_inventory(f, historic),
           "frozen local-3D refusal reclassified")

colluding = deepcopy(original)
colluding_old = deepcopy(historic)
name = "02_conductors_half_size.pdf"
colluding["frozen_baseline"]["original_pdf_sha256"][name] = "f" * 64
colluding_old["source_sha256"][name] = "f" * 64
reject("two matching forged metadata digests",
       lambda: audit_inventory(colluding, colluding_old),
       "historic PDF metadata differs")

with TemporaryDirectory() as directory:
    for filename, frozen_digest in SOURCE_PDF_SHA256.items():
        actual = ROOT / filename
        verify_pdf_bytes(actual, frozen_digest)
        copied = Path(directory) / filename
        shutil.copyfile(actual, copied)
        with copied.open("r+b") as handle:
            handle.seek(copied.stat().st_size // 2)
            old_byte = handle.read(1)
            assert old_byte
            handle.seek(-1, 1)
            handle.write(bytes([old_byte[0] ^ 0x01]))
        reject("midpoint byte flip " + filename,
               lambda p=copied, h=frozen_digest: verify_pdf_bytes(p, h),
               "source PDF bytes changed")

print("ALL NOVEL PYTHON CONTROLS PASSED")
