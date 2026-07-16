#!/usr/bin/env python3
"""
Generate the derived machine-readable index for Kubepedia KDS documents.

The documents under kb/ are the source of truth; index/ is a derived view
(KDS "Index"). This script regenerates it deterministically:

    index/documents.jsonl   one JSON object per document
    index/relations.jsonl   one JSON object per typed relation edge
    index/ids.txt           every document ID, sorted

Usage:
    python3 scripts/generate_index.py            # repo root inferred from script
    python3 scripts/generate_index.py REPO_ROOT
"""
import json
import os
import sys

import kdslib


def repo_root_from_args():
    if len(sys.argv) > 1:
        return os.path.abspath(sys.argv[1])
    here = os.path.dirname(os.path.realpath(__file__))
    return os.path.dirname(here)


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def main():
    repo = repo_root_from_args()
    kb_root = os.path.join(repo, "kb")
    index_dir = os.path.join(repo, "index")
    if not os.path.isdir(kb_root):
        print(f"kb/ not found: {kb_root}")
        return 2
    os.makedirs(index_dir, exist_ok=True)

    documents, relations, ids = kdslib.build_index(kb_root, repo)
    write_jsonl(os.path.join(index_dir, "documents.jsonl"), documents)
    write_jsonl(os.path.join(index_dir, "relations.jsonl"), relations)
    write_lines(os.path.join(index_dir, "ids.txt"), ids)

    print(f"documents: {len(documents)}  relations: {len(relations)}  ids: {len(ids)}")
    print(f"index written to {index_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
