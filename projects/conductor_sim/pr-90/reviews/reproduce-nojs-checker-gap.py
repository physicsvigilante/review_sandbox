"""Reproduce M37b PR #90 no-JS initial-marker integrity blind spot.

Run from a pinned conductor_sim PR #90 checkout, with the package, pytest
dependencies and Playwright Chromium installed (the real production runner).
This intentionally changes ONLY HTML, not the independently validated JSON.
It demonstrates an issue with the *browser release checker*, not Kelvin physics.
"""
from __future__ import annotations

import re
from pathlib import Path
from tempfile import TemporaryDirectory

from tools.check_m37b_prescribed_browser import check as browser_check
from tools.m37b_source_approach import run_all

with TemporaryDirectory(prefix="m37b-review-marker-") as temporary:
    directory = Path(temporary)
    run_all(directory)
    browser_check(directory)  # Genuine artifact is valid.

    page = directory / "p8-ground-current.html"
    original = page.read_text(encoding="utf-8")
    forged, replaced = re.subn(
        r'(<circle id="m37b-current-marker" cx=")[^"]+',
        r'\g<1>500',
        original,
        count=1,
    )
    assert replaced == 1
    page.write_text(forged, encoding="utf-8")

    # CURRENT-BUG: the source checker accepts the forged HTML, because JS
    # show(0) repairs the marker before normal checks run; the no-JS branch
    # checks Q/current but does not compare SVG marker coordinates.
    browser_check(directory)
    print("REPRODUCED: browser checker accepted no-JS-forged marker cx=500")

    # Required after fixing: this second browser_check must instead REFUSE
    # this HTML-only mutation, while the baseline remains passing.
