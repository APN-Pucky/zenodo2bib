# SPDX-FileCopyrightText: 2026-present Alexander Puck Neuwirth <alexander@neuwirth-informatik.de>
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

import re
import sys

import requests

RECORD_ID_PATTERNS = [
    re.compile(r"zenodo\.(\d+)", re.IGNORECASE),
    re.compile(r"zenodo\.org/records?/(\d+)", re.IGNORECASE),
]
 
def latest_zenodo_record_id(record_id: str) -> str:
    """Resolve a (possibly outdated) Zenodo record id to the latest version's id."""
    try:
        r = requests.get(f"https://zenodo.org/api/records/{record_id}/versions/latest", timeout=30)
        r.raise_for_status()
        latest_id = r.json().get("id")
        if latest_id is not None:
            return str(latest_id)
    except requests.RequestException:
        pass
    return record_id

def extract_record_id(query: str) -> str | None:
    query = query.strip()
    for pattern in RECORD_ID_PATTERNS:
        m = pattern.search(query)
        if m:
            return m.group(1)
    if query.isdigit():
        return query
    return None


def get_bibtex_for_record(record_id: str) -> str:
    url = f"https://zenodo.org/records/{record_id}/export/bibtex"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text


def search_zenodo(query: str, size: int = 10) -> list[str]:
    url = "https://zenodo.org/api/records"
    params = {"q": query, "size": size}
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    hits = r.json()["hits"]["hits"]
    return [str(hit["id"]) for hit in hits]


def get_zenodo_bibtex(query: str) -> str:
    record_id = extract_record_id(query)
    if record_id is not None:
        return get_bibtex_for_record(record_id)

    record_ids = search_zenodo(query)
    if not record_ids:
        msg = f"No Zenodo records found for query: {query!r}"
        raise ValueError(msg)
    return "\n".join(get_bibtex_for_record(rid) for rid in record_ids)


def main():
    query = " ".join(sys.argv[1:])
    print(get_zenodo_bibtex(query))


if __name__ == "__main__":
    main()
