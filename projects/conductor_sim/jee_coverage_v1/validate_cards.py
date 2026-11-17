"""JEE-30 preregistration integrity, NOT a numerical or JEE coverage test.

Standard library only. A passing result means thirty original cards are
schema-complete and UNGRADED, not that any can be simulated.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys

FAMILIES = {
    "field_potential": "F", "conductors": "C", "work_energy": "W",
    "motion_events": "M", "model_exploration": "X", "limitations": "R",
}
SUPPORT = {"likely_supported", "partially_supported", "likely_unsupported", "draft_only"}
GRADES = {"not_evaluated", "not_applicable", "pass", "partial", "fail"}


def unique_pairs(pairs):
    d = {}
    for k, v in pairs:
        if k in d:
            raise ValueError("duplicate JSON property: " + k)
        d[k] = v
    return d


def load(path):
    content = path.read_bytes()
    data = json.loads(content, object_pairs_hook=unique_pairs)
    if type(data) is not dict or data.get("schema") != "conductor_sim.jee30_preregistered_cards.v1":
        raise ValueError("wrong JEE-30 preregistration schema")
    if data.get("status") != "preregistered_unexecuted" or data.get("count") != 30:
        raise ValueError("the original preregistration MUST remain unscored and contain thirty cards")
    if data.get("source_syllabus") != "https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf":
        raise ValueError("syllabus source anchor changed")
    if data.get("released_engine_base_commit") != "a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde":
        raise ValueError("do not evaluate a floating or draft production version")
    cases = data.get("cases")
    if type(cases) is not list or len(cases) != 30:
        raise ValueError("wrong card count")
    ids, counts = set(), Counter()
    for card in cases:
        if type(card) is not dict:
            raise ValueError("card must be an object")
        cid, family = card.get("id"), card.get("family")
        if family not in FAMILIES or type(cid) is not str:
            raise ValueError("invalid card family/identity")
        counts[family] += 1
        expected_prefix = FAMILIES[family]
        if cid != f"{expected_prefix}{counts[family]:02d}" or cid in ids:
            raise ValueError("card IDs must be sequential within frozen strata")
        ids.add(cid)
        if card.get("source_type") != "new_original_teacher_style_not_previous_year":
            raise ValueError("misattributed genuine JEE source")
        for name in ("title", "prompt", "independent_reference", "desired_visualization",
                     "candidate_engine_api", "risk_or_exclusion"):
            if type(card.get(name)) is not str or not card[name].strip():
                raise ValueError(f"{cid}: missing required {name}")
        if len(card["prompt"]) < 90:
            raise ValueError(f"{cid}: prompt too under-specified to assess faithfully")
        if type(card.get("givens")) is not dict or not card["givens"]:
            raise ValueError(f"{cid}: no explicit teacher-authored SI givens")
        if type(card.get("observables")) is not list or not card["observables"] or not all(
            type(o) is str and o.strip() for o in card["observables"]
        ):
            raise ValueError(f"{cid}: physical observables required")
        if card.get("provisional_support") not in SUPPORT:
            raise ValueError(f"{cid}: unsupported provisional label")
        assessment = card.get("assessment")
        if type(assessment) is not dict:
            raise ValueError(f"{cid}: missing distinct five-dimensional assessment")
        keys = ("interpretation_fidelity", "physical_correctness",
                "simulation_coverage", "educational_usefulness", "textbook_answer_completeness")
        if tuple(assessment.keys()) != keys:
            raise ValueError(f"{cid}: original five dimensions changed or conflated")
        if any(assessment[k] != "not_evaluated" for k in keys[:-1]):
            raise ValueError(f"{cid}: preregistration must NOT preassign a PASS")
        if assessment["textbook_answer_completeness"] != "not_attempted":
            raise ValueError(f"{cid}: written solution status prematurely claimed")
        if type(card.get("evidence")) is not list or card["evidence"]:
            raise ValueError(f"{cid}: original preregistration must contain NO fake evidence")
    if any(counts[f] != 5 for f in FAMILIES) or dict(counts) != data.get("strata_count"):
        raise ValueError("wrong six-stratum distribution")
    return {
        "schema": "conductor_sim.jee30_registration_check.v1",
        "bank_sha256": sha256(content).hexdigest(),
        "cards_preregistered": len(cases),
        "cards_simulated": 0,
        "cards_physics_verified": 0,
        "cards_interpretation_graded": 0,
        "cards_visualization_graded": 0,
        "strata": dict(counts),
        "status": "REGISTERED_UNEVALUATED",
        "warning": "This registration check does not execute physics or establish JEE problem coverage.",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--bank", type=Path, default=Path(__file__).with_name("cases.json"))
    p.add_argument("--output", type=Path, default=Path("output/jee30-registration.json"))
    args = p.parse_args()
    report = load(args.bank)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
