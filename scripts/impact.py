#!/usr/bin/env python3
"""Kubepedia graph impact analysis — query the KDS relation graph.

Answers questions like "what depends on etcd?" or "what breaks if I change the CNI?"
straight from `index/relations.jsonl` (typed edges) + `index/documents.jsonl`.

  * inbound  edges  = documents that point AT the target (depend on / reference it)
  * outbound edges  = what the target itself points at (its dependencies)
  * --depth N       = transitive inbound closure = the impact radius of a change

Resolve the target by ID, alias, tag, or a title/ID substring.

Usage:
    scripts/impact.py etcd                     # what relates to etcd (1 level)
    scripts/impact.py COMPONENT-CILIUM --depth 2
    scripts/impact.py --tag cni                # everything tagged 'cni'
    scripts/impact.py "kube-proxy" --json
"""
import argparse
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IDX = os.path.join(ROOT, "index")

STR = {
    "ru": {
        "title": "# Impact-анализ: {id} — {t}",
        "meta": "тип: `{type}` · {path}",
        "inbound": "\n## Зависят от этого / ссылаются на него (входящие) — {n}\n",
        "outbound": "\n## От чего зависит сам (исходящие) — {n}\n",
        "radius": "\n## Радиус влияния (транзитивно, глубина {d}) — {n} документ(ов)\n",
        "none_in": "Ничего не ссылается на этот документ.",
        "none_out": "Документ ни на что не ссылается.",
        "ambiguous": "Неоднозначно — уточните (совпадений: {n}):",
        "notfound": "Не найдено: {q}",
    },
    "en": {
        "title": "# Impact analysis: {id} — {t}",
        "meta": "type: `{type}` · {path}",
        "inbound": "\n## Depends on / references this (inbound) — {n}\n",
        "outbound": "\n## What it depends on (outbound) — {n}\n",
        "radius": "\n## Impact radius (transitive, depth {d}) — {n} document(s)\n",
        "none_in": "Nothing references this document.",
        "none_out": "This document references nothing.",
        "ambiguous": "Ambiguous — be more specific ({n} matches):",
        "notfound": "Not found: {q}",
    },
}


def load():
    docs = {}
    with open(os.path.join(IDX, "documents.jsonl")) as f:
        for line in f:
            d = json.loads(line)
            docs[d["id"]] = d
    edges = []
    with open(os.path.join(IDX, "relations.jsonl")) as f:
        for line in f:
            edges.append(json.loads(line))
    return docs, edges


def resolve(query, docs, tag=None):
    """Return a list of matching doc IDs (exact id/alias -> 1; tag/substring -> many)."""
    if tag:
        return sorted(d["id"] for d in docs.values() if tag in (d.get("tags") or []))
    if query in docs:
        return [query]
    q = query.lower()
    for d in docs.values():                                   # exact alias
        if q in [str(a).lower() for a in (d.get("aliases") or [])]:
            return [d["id"]]
    hits = [d["id"] for d in docs.values()                    # substring id/title
            if q in d["id"].lower() or q in str(d.get("title", "")).lower()]
    return sorted(hits)


def title(docs, did):
    return docs[did]["title"] if did in docs else "(unknown)"


def transitive_inbound(target, by_target, depth):
    """BFS over inbound edges: every doc that (transitively) depends on `target`."""
    seen, frontier = set(), {target}
    for _ in range(depth):
        nxt = set()
        for t in frontier:
            for src, _typ in by_target.get(t, []):
                if src not in seen and src != target:
                    seen.add(src)
                    nxt.add(src)
        frontier = nxt
        if not frontier:
            break
    return seen


def render(did, docs, edges, depth, lang):
    S = STR[lang]
    by_target, by_source = {}, {}
    for e in edges:
        by_target.setdefault(e["target"], []).append((e["source"], e["type"]))
        by_source.setdefault(e["source"], []).append((e["target"], e["type"]))
    out = [S["title"].format(id=did, t=title(docs, did)),
           S["meta"].format(type=docs[did].get("type"), path=docs[did].get("path"))]

    inbound = sorted(by_target.get(did, []), key=lambda x: (x[1], x[0]))
    out.append(S["inbound"].format(n=len(inbound)))
    if inbound:
        curtype = None
        for src, typ in inbound:
            if typ != curtype:
                out.append(f"**{typ}:**")
                curtype = typ
            out.append(f"- `{src}` — {title(docs, src)}")
    else:
        out.append(S["none_in"])

    outbound = sorted(by_source.get(did, []), key=lambda x: (x[1], x[0]))
    out.append(S["outbound"].format(n=len(outbound)))
    if outbound:
        curtype = None
        for tgt, typ in outbound:
            if typ != curtype:
                out.append(f"**{typ}:**")
                curtype = typ
            out.append(f"- `{tgt}` — {title(docs, tgt)}")
    else:
        out.append(S["none_out"])

    if depth > 1:
        radius = transitive_inbound(did, by_target, depth)
        out.append(S["radius"].format(d=depth, n=len(radius)))
        for r in sorted(radius):
            out.append(f"- `{r}` — {title(docs, r)}")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Kubepedia graph impact analysis")
    ap.add_argument("query", nargs="?", help="doc ID, alias, or title/ID substring")
    ap.add_argument("--tag", help="resolve by tag instead (may match many)")
    ap.add_argument("--depth", type=int, default=1,
                    help="transitive inbound depth (impact radius); >1 to expand")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    if not args.query and not args.tag:
        ap.error("give a query or --tag")

    docs, edges = load()
    matches = resolve(args.query or "", docs, tag=args.tag)
    S = STR[args.lang]
    if not matches:
        raise SystemExit(S["notfound"].format(q=args.query or args.tag))
    if len(matches) > 1:
        print(S["ambiguous"].format(n=len(matches)))
        for m in matches[:40]:
            print(f"- {m} — {title(docs, m)}")
        return

    did = matches[0]
    if args.json:
        by_target = {}
        for e in edges:
            by_target.setdefault(e["target"], []).append(e["source"])
        print(json.dumps({
            "id": did, "title": title(docs, did),
            "inbound": [{"source": s, "type": t} for e in edges
                        if e["target"] == did for s, t in [(e["source"], e["type"])]],
            "outbound": [{"target": e["target"], "type": e["type"]} for e in edges
                         if e["source"] == did],
            "impact_radius": sorted(transitive_inbound(did, {
                k: [(s, "") for s in v] for k, v in by_target.items()}, args.depth)),
        }, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render(did, docs, edges, args.depth, args.lang))


if __name__ == "__main__":
    main()
