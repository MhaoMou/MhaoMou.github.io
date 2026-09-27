#!/usr/bin/env python3
"""Refresh the static Scholar card from a public Google Scholar profile."""

from datetime import date
from html import unescape
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
PROFILE_URL = "https://scholar.google.com/citations?user=lDU4ZtQAAAAJ&hl=en"
ABOUT = ROOT / "content/about.toml"


def fetch_profile() -> str:
    request = urllib.request.Request(
        PROFILE_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; academic-site-refresh/1.0)"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def value_after_label(html: str, label: str) -> int:
    pattern = rf'>{re.escape(label)}</a></td><td class="gsc_rsb_std">(\d+)'
    match = re.search(pattern, html)
    if not match:
        raise ValueError(f"Could not find Scholar value: {label}")
    return int(match.group(1))


def parse_stats(html: str) -> tuple[int, int, int, list[tuple[str, int]]]:
    citations = value_after_label(html, "Citations")
    h_index = value_after_label(html, "h-index")
    i10_index = value_after_label(html, "i10-index")
    points = []
    # The chart labels and bars are adjacent in the profile's histogram.
    years = re.findall(r'class="gsc_g_t"[^>]*>(\d{4})</span>', html)
    counts = [int(value) for value in re.findall(r'class="gsc_g_al">(\d+)</span>', html)]
    if years and counts and len(years) == len(counts):
        points = list(zip(years, counts))
    if not points:
        raise ValueError("Could not find Scholar citation trend")
    return citations, h_index, i10_index, points


def replace_card(text: str, stats: tuple[int, int, int, list[tuple[str, int]]]) -> str:
    citations, h_index, i10_index, points = stats
    block = (
        "[[sections]]\n"
        "id = \"scholar_widget\"\n"
        "type = \"scholar_card\"\n"
        "title = \"Google Scholar\"\n"
        "description = \"Citation profile and publication impact.\"\n"
        f"total_citations = {citations}\n"
        f"h_index = {h_index}\n"
        f"i10_index = {i10_index}\n"
        f"last_checked = \"{date.today().strftime('%B %-d, %Y')}\"\n"
        "trend = [\n"
        + "\n".join(f'  {{ year = "{year}", citations = {count} }},' for year, count in points)
        + "\n]"
    )
    pattern = r'\[\[sections\]\]\nid = "scholar_widget"\ntype = "scholar_card".*?(?=\n\[\[|\Z)'
    updated, count = re.subn(pattern, block, text, count=1, flags=re.DOTALL)
    if count != 1:
        raise ValueError("Could not locate scholar_widget section")
    return updated


def main() -> None:
    html = fetch_profile()
    updated = replace_card(ABOUT.read_text(), parse_stats(html))
    ABOUT.write_text(updated)


if __name__ == "__main__":
    main()
