#!/usr/bin/env python3
"""
Validate Kubepedia KDS documents under kb/ (see standards/validation.md).

Layers implemented here:
  1. Structure     — YAML parses; section profile for the type is present
  2. Metadata      — frontmatter matches schema/kds.schema.json (needs jsonschema)
  3. Identity      — ID grammar, prefix matches type, global uniqueness
  4. Versions      — required version dimension is non-null for the type
  5. Sources       — at least one source (schema-enforced; re-checked here)
  6. Relations     — every relation target resolves to an existing ID
  9. Index         — index/ equals a fresh recompute from the documents

Usage:
    python3 scripts/validate_kds.py            # repo root inferred from script
    python3 scripts/validate_kds.py REPO_ROOT

Exit: 0 all hard checks pass; 1 failures; 2 kb/ missing.
Metadata schema validation needs PyYAML + jsonschema; without jsonschema the
schema layer degrades to a warning, the rest still run.
"""
import json
import os
import sys

import kdslib

try:
    import jsonschema
    HAVE_JSONSCHEMA = True
except Exception:
    HAVE_JSONSCHEMA = False


class Report:
    def __init__(self):
        self.hard = 0
        self.warn = 0

    def fail(self, msg):
        self.hard += 1
        print(f"[FAIL] {msg}")

    def warned(self, msg):
        self.warn += 1
        print(f"[WARN] {msg}")

    def ok(self, msg):
        print(f"[PASS] {msg}")


def repo_root_from_args():
    if len(sys.argv) > 1:
        return os.path.abspath(sys.argv[1])
    here = os.path.dirname(os.path.realpath(__file__))
    return os.path.dirname(here)


def load_schema(repo):
    path = os.path.join(repo, "schema", "kds.schema.json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def version_ok(doc_type, fm):
    def nn(key):
        return fm.get(key) is not None
    rule = kdslib.VERSION_RULE.get(doc_type, "any")
    if rule == "kubespray":
        return nn("kubespray_version")
    if rule == "kubernetes":
        return nn("kubernetes_version")
    if rule == "component":
        return nn("component_version") and nn("kubespray_version")
    return any(nn(k) for k in kdslib.VERSION_KEYS)


def main():
    repo = repo_root_from_args()
    kb_root = os.path.join(repo, "kb")
    if not os.path.isdir(kb_root):
        print(f"kb/ not found: {kb_root}")
        return 2

    r = Report()
    schema = load_schema(repo)
    print(f"kb: {kb_root}")
    print(f"jsonschema: {'yes' if HAVE_JSONSCHEMA else 'NO (metadata schema layer skipped)'}")
    print("-" * 64)

    paths = kdslib.iter_doc_paths(kb_root)
    docs = []  # (path, fm, sections)
    for path in paths:
        rel = os.path.relpath(path, repo)
        try:
            fm, sections, _body = kdslib.parse_doc(path)
        except Exception as e:  # noqa: BLE001
            r.fail(f"{rel}: YAML/parse error: {e}")
            continue
        if not isinstance(fm, dict) or not fm:
            r.fail(f"{rel}: missing or empty front matter")
            continue
        docs.append((path, rel, fm, sections))

    all_ids = {}
    for path, rel, fm, sections in docs:
        did = fm.get("id")
        if did:
            all_ids.setdefault(did, []).append(rel)

    # per-document checks
    for path, rel, fm, sections in docs:
        did = fm.get("id")
        dtype = fm.get("type")

        # 2. Metadata schema
        if schema is not None and HAVE_JSONSCHEMA:
            errs = sorted(
                jsonschema.Draft202012Validator(schema).iter_errors(fm),
                key=lambda e: e.path,
            )
            for e in errs:
                loc = "/".join(str(p) for p in e.path) or "(root)"
                r.fail(f"{rel}: schema: {loc}: {e.message}")

        # 3. Identity
        if not did:
            r.fail(f"{rel}: missing id")
        else:
            if not kdslib.ID_RE.match(did):
                r.fail(f"{rel}: id '{did}' violates ID grammar")
            prefix = kdslib.TYPE_PREFIX.get(dtype)
            if prefix and not did.startswith(prefix + "-"):
                r.fail(f"{rel}: id '{did}' prefix does not match type '{dtype}' (expected {prefix}-)")

        # 1. Structure — section profile
        if dtype in kdslib.PROFILE:
            missing = [s for s in kdslib.required_sections(dtype) if s not in sections]
            if missing:
                r.fail(f"{rel}: type '{dtype}' missing required sections: {missing}")
        elif dtype is not None:
            r.fail(f"{rel}: unknown type '{dtype}'")

        # 4. Versions
        if dtype in kdslib.VERSION_RULE and not version_ok(dtype, fm):
            r.fail(f"{rel}: version fields do not satisfy the '{kdslib.VERSION_RULE[dtype]}' rule for type '{dtype}'")

        # 5. Sources
        if not (isinstance(fm.get("sources"), list) and fm.get("sources")):
            r.fail(f"{rel}: at least one source is required")

    # 3b. ID uniqueness
    for did, locs in sorted(all_ids.items()):
        if len(locs) > 1:
            r.fail(f"duplicate id '{did}' in: {locs}")

    # 6. Relations resolve
    known = set(all_ids)
    for path, rel, fm, sections in docs:
        for edge in fm.get("relations") or []:
            if isinstance(edge, dict):
                tgt = edge.get("target")
                if tgt and tgt not in known:
                    r.fail(f"{rel}: relation target '{tgt}' does not resolve to a known document")

    # graph orphan (warning): no inbound and no outbound edges.
    # Leaf reference types (variable, ansible_tag) are intentionally reached by
    # tag/alias facet and full-text, NOT by graph edge (decisions.md D-018), so an
    # orphan there is expected, not debt — exempt them and keep the warning
    # actionable for types that *should* be in the graph.
    GRAPH_EXEMPT = {"variable", "ansible_tag"}
    linked = set()
    for path, rel, fm, sections in docs:
        for edge in fm.get("relations") or []:
            if isinstance(edge, dict) and edge.get("target"):
                linked.add(fm.get("id"))
                linked.add(edge["target"])
    if len(docs) > 1:
        for path, rel, fm, sections in docs:
            if fm.get("type") in GRAPH_EXEMPT:
                continue
            if fm.get("id") not in linked:
                r.warned(f"{rel}: document '{fm.get('id')}' is not connected to the graph")

    # 7. Consistency guards (warnings — encode the bug classes found by hand)
    import re as _re

    def _vt(s):
        return tuple(int(x) if x.isdigit() else 0 for x in str(s).split("."))

    # 7a. broken body [[wikilinks]] (forward-refs are allowed → warning, not failure)
    for path, rel, fm, sections in docs:
        try:
            body = open(path).read().split("---", 2)[-1]
        except OSError:
            continue
        for w in sorted(set(_re.findall(r"\[\[([A-Z][A-Z0-9_]*-[A-Z0-9_]+)\]\]", body))):
            if w not in known:
                r.warned(f"{rel}: body wikilink [[{w}]] does not resolve")

    # 7b. duplicate titles across docs (a real collision signal, e.g. the old
    # COMPONENT-ETCD vs ROLE-ETCD both titled "etcd"). Cross-type *alias* sharing
    # (COMPONENT/TAG/VARIABLE for the same tech) is intentional, so aliases are
    # not flagged — only identical titles.
    title_map = {}
    for path, rel, fm, sections in docs:
        t = str(fm.get("title") or "").strip().lower()
        if t:
            title_map.setdefault(t, set()).add(fm.get("id"))
    for t, ids in sorted(title_map.items()):
        if len(ids) > 1:
            r.warned(f"title '{t}' shared by {len(ids)} docs: {sorted(ids)}")

    # 7c. version-envelope sanity (well-formed range, low <= high)
    for path, rel, fm, sections in docs:
        for field in ("kubespray_version", "kubernetes_version", "component_version"):
            val = fm.get(field)
            if not isinstance(val, str) or ">=" not in val or "<=" not in val:
                continue
            m = _re.search(r">=\s*v?([0-9][0-9.]*)\D+<=\s*v?([0-9][0-9.]*)", val)
            if m and _vt(m.group(1)) > _vt(m.group(2)):
                r.warned(f"{rel}: {field} range looks inverted: {val}")

    # 9. Index consistency
    index_dir = os.path.join(repo, "index")
    documents, relations, ids = kdslib.build_index(kb_root, repo)
    tags, aliases = kdslib.build_facets(kb_root, repo)
    expected = {
        "documents.jsonl": [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in documents],
        "relations.jsonl": [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in relations],
        "ids.txt": ids,
        "tags.jsonl": [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in tags],
        "aliases.jsonl": [json.dumps(x, ensure_ascii=False, sort_keys=True) for x in aliases],
    }
    for name, exp_lines in expected.items():
        fpath = os.path.join(index_dir, name)
        if not os.path.exists(fpath):
            r.fail(f"index/{name} missing — run scripts/generate_index.py")
            continue
        got = kdslib.read(fpath).splitlines()
        got = [ln for ln in got if ln.strip() != ""]
        if got != exp_lines:
            r.fail(f"index/{name} is stale — regenerate with scripts/generate_index.py")

    print("-" * 64)
    print(f"documents: {len(docs)}   hard failures: {r.hard}   warnings: {r.warn}")
    if r.hard == 0:
        r.ok("KDS validation passed")
    return 1 if r.hard else 0


if __name__ == "__main__":
    sys.exit(main())
