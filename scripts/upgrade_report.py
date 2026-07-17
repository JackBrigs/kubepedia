#!/usr/bin/env python3
"""Upgrade & Change Report generator (Kubepedia prototype).

Given two Kubespray versions, walk the chain of KDS UPGRADE-* documents between
them and assemble a consolidated, source-linked change report.

Usage:
    python scripts/upgrade_report.py --from v2.29.0 --to v2.31.0
    python scripts/upgrade_report.py --from v2.30.0 --to v2.31.0 -o report.md

Data source: the verified UPGRADE-V*__V* / RELEASE-V* / CONCEPT-* docs in kb/.
This is not KDS content; it reads the KB and emits a report.
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index", "documents.jsonl")


def load_docs():
    docs = {}
    with open(INDEX) as f:
        for line in f:
            d = json.loads(line)
            docs[d["id"]] = d
    return docs


def id_to_version(vtok):
    # "V2_29_0" -> "v2.29.0"
    return "v" + vtok[1:].replace("_", ".")


def version_key(v):
    # "v2.29.0" -> (2, 29, 0)
    return tuple(int(x) for x in v.lstrip("v").split("."))


def parse_upgrade_edges(docs):
    """Return {from_version: (to_version, doc_id)} for each UPGRADE-V*__V* doc."""
    edges = {}
    for did in docs:
        m = re.match(r"^UPGRADE-(V[0-9_]+)__(V[0-9_]+)$", did)
        if m:
            fr = id_to_version(m.group(1))
            to = id_to_version(m.group(2))
            edges[fr] = (to, did)
    return edges


def build_chain(frm, to, edges):
    """Follow single-step upgrade edges from `frm` to `to`. Returns list of doc_ids."""
    chain = []
    cur = frm
    guard = 0
    while cur != to:
        if cur not in edges:
            raise SystemExit(
                f"No upgrade path continues from {cur} toward {to} "
                f"(available starts: {sorted(edges, key=version_key)})"
            )
        nxt, did = edges[cur]
        chain.append(did)
        cur = nxt
        guard += 1
        if guard > 50:
            raise SystemExit("upgrade chain too long / cycle")
    return chain


def read_sections(path):
    """Split a KDS markdown body into {section_title: text} on '## ' headers."""
    full = open(os.path.join(ROOT, path)).read()
    body = full.split("---", 2)[-1]  # drop YAML frontmatter
    sections, cur, buf = {}, None, []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            if cur:
                sections[cur] = "\n".join(buf).strip()
            cur, buf = h.group(1).strip(), []
        elif cur:
            buf.append(line)
    if cur:
        sections[cur] = "\n".join(buf).strip()
    return sections


def wikilinks(text):
    return set(re.findall(r"\[\[([A-Z][A-Z0-9_]*-[A-Z0-9_]+)\]\]", text))


def render(frm, to, chain, docs):
    out = []
    out.append(f"# Upgrade & Change Report — Kubespray {frm} → {to}\n")
    out.append(
        f"_Generated from Kubepedia KDS docs. {len(chain)} upgrade step(s) on the path._\n"
    )
    cited = set()

    for did in chain:
        d = docs[did]
        sec = read_sections(d["path"])
        hop = d["title"].replace("Upgrade report ", "")
        out.append(f"\n## Step: {hop}\n")
        if sec.get("Summary"):
            out.append(sec["Summary"] + "\n")
        if sec.get("Implementation"):
            out.append("**Version deltas**\n")
            out.append(sec["Implementation"] + "\n")
        if sec.get("Upgrade Notes"):
            out.append("**Required actions / breaking changes**\n")
            out.append(sec["Upgrade Notes"] + "\n")
        if sec.get("Compatibility"):
            out.append("**Compatibility constraints**\n")
            out.append(sec["Compatibility"] + "\n")
        cited |= {did}
        for s in sec.values():
            cited |= wikilinks(s)

    # Cross-cutting layer: point at the Kubernetes-layer change docs
    out.append("\n## Cross-cutting (Kubernetes layer)\n")
    xrefs = [
        ("CONCEPT-K8S_API_REMOVALS", "API removals crossing K8s minors"),
        ("CONCEPT-K8S_FEATURE_GATES", "feature-gate graduations/removals"),
        ("CONCEPT-COMPONENT_VERSION_SELECTION", "which component versions move, and why"),
        ("PRACTICE-UPGRADE_PREFLIGHT", "pre-upgrade checklist"),
        ("PRACTICE-GRACEFUL_UPGRADE", "drain/serial/pause mechanics"),
    ]
    for cid, desc in xrefs:
        if cid in docs:
            out.append(f"- **{docs[cid]['title']}** — {desc}  `[{cid}]`")
            cited.add(cid)

    # Sources: every KDS doc this report is built from / links to
    out.append("\n## Sources (KDS documents)\n")
    for cid in sorted(cited):
        if cid in docs:
            out.append(f"- `{cid}` — {docs[cid]['title']}  ({docs[cid]['path']})")
        else:
            out.append(f"- `{cid}` — (referenced; resolve in kb/)")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Kubepedia Upgrade & Change Report")
    ap.add_argument("--from", dest="frm", required=True, help="from version, e.g. v2.29.0")
    ap.add_argument("--to", dest="to", required=True, help="to version, e.g. v2.31.0")
    ap.add_argument("-o", "--out", help="write report to file (default: stdout)")
    args = ap.parse_args()

    frm = args.frm if args.frm.startswith("v") else "v" + args.frm
    to = args.to if args.to.startswith("v") else "v" + args.to
    if version_key(frm) >= version_key(to):
        raise SystemExit(f"--from ({frm}) must be lower than --to ({to})")

    docs = load_docs()
    edges = parse_upgrade_edges(docs)
    if not edges:
        raise SystemExit("no UPGRADE-* docs found in the index")
    chain = build_chain(frm, to, edges)
    report = render(frm, to, chain, docs)

    if args.out:
        with open(args.out, "w") as f:
            f.write(report)
        print(f"wrote {args.out} ({len(chain)} steps)", file=sys.stderr)
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
