#!/usr/bin/env python3
"""Per-tag component version lookup (Kubepedia).

Answers the question that comes up most often in practice: *which version of X does
Kubespray ship at each tag, how is that version defined (a static pin or something
computed), and does the knowledge base agree?*

It deliberately reuses the resolver from `check_versions.py` — the one that already
knows the two traps we got wrong by hand:

  * a `*_version` can be a **static pin** (`runc_version: v1.2.6`) or a **computed
    first-checksum-key** (`{{ (runc_checksums['amd64'] | dict2items)[0].key }}`);
  * the defaults role is `kubespray-defaults` (hyphen) before v2.28.0 and
    `kubespray_defaults` (underscore) from v2.28.0.

Usage:
    python scripts/versions_lookup.py cilium
    python scripts/versions_lookup.py runc --tags v2.29.0,v2.31.0
    python scripts/versions_lookup.py etcd            # per-Kubernetes-minor component
    python scripts/versions_lookup.py --list          # what can be looked up
Exit code is 0 unless the component cannot be resolved at all.
"""
import argparse
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load_check_versions():
    path = os.path.join(HERE, "check_versions.py")
    spec = importlib.util.spec_from_file_location("_kp_check_versions", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


CV = _load_check_versions()

# how a mechanism reads in the output
HOW = {
    "literal-pin": "static pin",
    "computed-first-key": "computed (first checksum key)",
    "checksum-first-key": "first checksum key",
    "computed-unresolved": "computed (not resolvable statically)",
    "var-absent": "variable absent at this tag",
    "checksum-absent": "checksum table absent at this tag",
    "computed-per-k8s": "per Kubernetes minor",
}


def kb_tags():
    """Tags the KB has RELEASE docs for, oldest first."""
    tags = []
    for fn in sorted(os.listdir(CV.REL_DIR)):
        if not fn.endswith(".md"):
            continue
        tag, _ = CV.parse_release(os.path.join(CV.REL_DIR, fn))
        if tag:
            tags.append(tag)
    return sorted(set(tags), key=CV.vtuple)


def kb_claim(tag, component):
    """What the KB's RELEASE doc for `tag` claims for `component` (or None)."""
    for fn in sorted(os.listdir(CV.REL_DIR)):
        if not fn.endswith(".md"):
            continue
        t, comps = CV.parse_release(os.path.join(CV.REL_DIR, fn))
        if t == tag:
            return comps.get(CV.norm(component))
    return None


def target_for(component, dl, cs):
    """(kind, name) for a component: the RESOLVE map first, then guesses from source."""
    key = CV.norm(component)
    if key in CV.RESOLVE:
        return CV.RESOLVE[key]
    var = component if component.endswith("_version") else f"{component.replace('-', '_')}_version"
    if re.search(rf"^{re.escape(var)}:", dl or "", re.M):
        return ("var", var)
    for cand in (component, component.replace("-", "_")):
        for suffix in ("_checksums", "_binary_checksums", "_archive_checksums"):
            if re.search(rf"^{re.escape(cand)}{suffix}:", cs or "", re.M):
                return ("checksum", cand + suffix)
    return (None, None)


def role_default(src, tag, var):
    """A `var:` literal defined in some role's defaults at `tag` -> (version, path)."""
    out = subprocess.run(["git", "-C", src, "grep", "-n", f"^{var}:", tag, "--", "roles"],
                         capture_output=True, text=True).stdout
    for ln in out.splitlines():
        m = re.match(rf"^[^:]+:(\S+):\d+:{re.escape(var)}:\s*(.+?)\s*$", ln)
        if m and "{{" not in m.group(2):
            return CV.clean_ver(m.group(2)), m.group(1)
    return None, None


def lookup(src, component, tags):
    rows = []
    for tag in tags:
        dl, cs = CV.download_yml(src, tag), CV.checksums_yml(src, tag)
        if not dl:
            rows.append((tag, None, "source not available (fetch the tag)", None))
            continue
        kind, name = target_for(component, dl, cs)
        if kind is None:
            # not in the shared download machinery — a role may still pin it
            var = component if component.endswith("_version") else \
                f"{component.replace('-', '_')}_version"
            value, where = role_default(src, tag, var)
            rows.append((tag, value, f"static pin in {where}" if value
                         else "not defined at this tag", var if value else None))
            continue
        if kind == "perk8s":
            per = CV.resolve_perk8s(src, tag).get(CV.norm(component), {})
            value = ", ".join(f"k8s {k} → {v}" for k, v in sorted(per.items())) or None
            rows.append((tag, value, HOW["computed-per-k8s"], name))
            continue
        actual, how = CV.resolve(src, tag, kind, name, dl, cs)
        if actual is None and how == "var-absent":
            # some components pin their version in their own role, not in download.yml
            actual, where = role_default(src, tag, name)
            if actual:
                rows.append((tag, actual, f"static pin in {where}", name))
                continue
        rows.append((tag, actual, HOW.get(how, how), name))
    return rows


def main():
    ap = argparse.ArgumentParser(description="Per-tag component version lookup")
    ap.add_argument("component", nargs="?", help="component or variable, e.g. cilium, runc, runc_version")
    ap.add_argument("--src", default=os.path.join(ROOT, "kubespray-src"),
                    help="path to a kubespray git checkout (default: ./kubespray-src)")
    ap.add_argument("--tags", help="comma-separated tags (default: every tag the KB covers)")
    ap.add_argument("--list", action="store_true", help="list the components with a known mapping")
    args = ap.parse_args()

    if args.list:
        print("known components (others are guessed as <name>_version / <name>_checksums):")
        for k, (kind, name) in sorted(CV.RESOLVE.items()):
            print(f"  {k:14} {kind:9} {name or '-'}")
        return 0
    if not args.component:
        ap.error("component is required (or use --list)")

    if not os.path.isdir(os.path.join(args.src, ".git")):
        print(f"kubespray source not found at {args.src} — this lookup needs a git checkout.")
        return 1

    tags = [t.strip() for t in args.tags.split(",")] if args.tags else kb_tags()
    rows = lookup(args.src, args.component, tags)

    print(f"{args.component} — per Kubespray tag (source: {args.src})")
    print("-" * 78)
    print(f"{'tag':10} {'version':22} {'defined as':32} KB")
    for tag, value, how, name in rows:
        claimed = kb_claim(tag, args.component)
        if claimed is None:
            agree = "-"
        elif value and re.search(r"[0-9]+\.[0-9]+[0-9.]*", claimed or "") \
                and re.search(r"[0-9]+\.[0-9]+[0-9.]*", claimed).group(0) == value:
            agree = "ok"
        else:
            agree = f"claims {claimed}"
        print(f"{tag:10} {(value or '—'):22} {how:32} {agree}")
    print("-" * 78)
    names = {n for _, _, _, n in rows if n}
    if names:
        print("source variable/table: " + ", ".join(sorted(names)))
    print("read from roles/kubespray[-_]defaults/defaults/main/download.yml and "
          "vars|defaults/main/checksums.yml at each tag.")
    return 0 if any(v for _, v, _, _ in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
