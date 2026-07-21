#!/usr/bin/env python3
"""Per-tag version consistency check (Kubepedia).

Cross-checks the component versions claimed in the KB's RELEASE-V<tag> docs
against the *actual* Kubespray tagged source, per tag. This is the automated
guard for the version-drift bug class we hit by hand (runc 1.2.5-vs-1.2.6,
flannel 0.27.3-vs-0.28.4, calico 3.30.x-vs-3.31.5): the KB stamps a version, the
source is authority, and this catches disagreements.

It handles the two extraction traps that broke us:
  * a `*_version` can be a **static pin** (`runc_version: v1.2.6`) OR a
    **computed first-checksum-key** (`{{ (runc_checksums['amd64']|dict2items)[0].key }}`);
  * the role path is `kubespray-defaults` (hyphen) pre-v2.28.0 and
    `kubespray_defaults` (underscore) from v2.28.0.

etcd/coredns are computed **per Kubernetes minor**. They ARE now verified: the
resolver reads `etcd_supported_versions` / `coredns_supported_versions` (literal
dict, checksum-filter `select('version',BOUND,'<')[0]`, or the older inline
conditional) and checks that every version the RELEASE doc claims is one the
source actually ships (source-only per-minor versions are an info note, not a
failure). Only the K8s version itself stays a range (not a single-pin) and the
`kubernetes` row is left unchecked.

Usage:
    python scripts/check_versions.py                 # src = ./kubespray-src
    python scripts/check_versions.py --src /path/to/kubespray
Exit code 1 if any mismatch is found (suitable for CI).
"""
import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL_DIR = os.path.join(ROOT, "kb", "kubespray", "releases")

# RELEASE component label (normalized) -> how to resolve the version from source.
#   ("var", name)      : read `name:` from download.yml (literal or first-key)
#   ("checksum", name) : first version key of `name:` in checksums.yml
#   ("perk8s", None)   : per Kubernetes minor -> etcd/coredns resolved & set-checked
#                        via resolve_perk8s(); `kubernetes` (a range) stays skipped
RESOLVE = {
    "runc": ("var", "runc_version"),
    "containerd": ("var", "containerd_version"),
    "flannel": ("var", "flannel_version"),
    "cilium": ("var", "cilium_version"),
    "metallb": ("var", "metallb_version"),
    "kube-vip": ("var", "kube_vip_version"),
    "nerdctl": ("var", "nerdctl_version"),
    "cni-plugins": ("checksum", "cni_binary_checksums"),
    "calico": ("checksum", "calicoctl_binary_checksums"),
    "etcd": ("perk8s", None),
    "coredns": ("perk8s", None),
    "kubernetes": ("perk8s", None),
}


def norm(name):
    return re.sub(r"\(.*?\)", "", name).strip().lower()


def clean_ver(s):
    return s.strip().strip('"').strip("'").lstrip("v")


def git_show(src, tag, path):
    p = subprocess.run(["git", "-C", src, "show", f"{tag}:{path}"],
                       capture_output=True, text=True)
    return p.stdout if p.returncode == 0 else ""


def file_at(src, tag, sub):
    for role in ("kubespray_defaults", "kubespray-defaults"):
        c = git_show(src, tag, f"roles/{role}/{sub}")
        if c:
            return c
    return ""


def download_yml(src, tag):
    return file_at(src, tag, "defaults/main/download.yml")


def checksums_yml(src, tag):
    # checksums moved from defaults/main/ (<=v2.27.x) to vars/main/ (v2.28.0+)
    return (file_at(src, tag, "vars/main/checksums.yml")
            or file_at(src, tag, "defaults/main/checksums.yml"))


def first_checksum_key(cs_text, name):
    """First version-like key under `name:` in the checksums YAML text."""
    lines = cs_text.splitlines()
    grab = False
    for ln in lines:
        if re.match(rf"^{re.escape(name)}:\s*$", ln):
            grab = True
            continue
        if grab:
            if re.match(r"^\S", ln):  # next top-level key
                break
            # keys carry a leading 'v' pre-v2.28.0 (v3.29.1:), none after (3.29.3:)
            m = re.match(r"^\s+v?([0-9]+\.[0-9]+[0-9.]*):", ln)
            if m:
                return m.group(1)
    return None


def vtuple(s):
    return tuple(int(x) for x in re.findall(r"\d+", s))


def etcd_checksum_keys(cs_text):
    """Ordered version keys under etcd_binary_checksums: amd64: (file order = desc)."""
    lines = cs_text.splitlines()
    top = arch = False
    keys = []
    for ln in lines:
        if re.match(r"^etcd_binary_checksums:\s*$", ln):
            top = True
            continue
        if top:
            if re.match(r"^\S", ln):  # left the block
                break
            if re.match(r"^\s{2}amd64:\s*$", ln):
                arch = True
                continue
            if arch:
                if re.match(r"^\s{2}\S", ln):  # next arch key
                    arch = False
                    continue
                m = re.match(r"^\s+v?([0-9]+\.[0-9]+\.[0-9]+):", ln)
                if m:
                    keys.append(m.group(1))
    return keys


def _supported_block(text, name):
    """Lines of a `name:` mapping block (until the next top-level key)."""
    out, grab = [], False
    for ln in text.splitlines():
        if re.match(rf"^{re.escape(name)}:\s*$", ln):
            grab = True
            continue
        if grab:
            if re.match(r"^\S", ln):
                break
            out.append(ln)
    return out


def resolve_supported(text, name, etcd_keys):
    """Parse a *_supported_versions dict -> {minor: 'x.y.z'} resolving both the
    literal form (v1.31: v3.5.16) and the checksum-filter form
    (select('version','3.6','<')[0] over etcd_binary_checksums)."""
    result = {}
    for ln in _supported_block(text, name):
        m = re.match(r"^\s+'?v?([0-9]+\.[0-9]+)'?:\s*(.+?)\s*$", ln)
        if not m:
            continue
        minor, val = m.group(1), m.group(2)
        if "{{" not in val:  # literal
            vm = re.search(r"[0-9]+\.[0-9]+\.[0-9]+", val)
            if vm:
                result[minor] = vm.group(0)
            continue
        # checksum-filter: (etcd_binary_checksums['amd64'].keys() | select('version','BOUND','<'))[0]
        fm = re.search(r"select\(\s*['\"]version['\"]\s*,\s*['\"]([0-9.]+)['\"]\s*,\s*['\"](<=?)['\"]", val)
        if fm and etcd_keys:
            bound, op = fm.group(1), fm.group(2)
            bt = vtuple(bound)
            for k in etcd_keys:  # file order (descending); [0] == first match
                kt = vtuple(k)
                if (kt < bt) if op == "<" else (kt <= bt):
                    result[minor] = k
                    break
    return result


def flat_conditional_versions(text, varname):
    """Literal x.y.z tokens on a `varname: "{{ ... }}"` line — handles the older
    inline-conditional form (coredns_version: {{ '1.11.3' if ... else '1.11.1' }})."""
    m = re.search(rf"^{re.escape(varname)}:\s*(.+)$", text, re.M)
    if not m or "{{" not in m.group(1):
        return {}
    # drop the guard versions inside version('X','op') so only the component
    # versions of the conditional's branches remain
    expr = re.sub(r"version\([^)]*\)", "", m.group(1))
    toks = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+", expr)
    return {str(i): v for i, v in enumerate(toks)}


def resolve_perk8s(src, tag):
    """{'etcd': {minor: ver}, 'coredns': {minor: ver}} from tagged source."""
    vars_main = file_at(src, tag, "vars/main/main.yml")
    dl = download_yml(src, tag)
    cs = checksums_yml(src, tag)
    etcd_keys = etcd_checksum_keys(cs)
    both = vars_main + "\n" + dl
    out = {
        "etcd": resolve_supported(both, "etcd_supported_versions", etcd_keys),
        "coredns": resolve_supported(both, "coredns_supported_versions", etcd_keys),
    }
    # fallback for the older inline-conditional form (no *_supported_versions dict)
    if not out["coredns"]:
        out["coredns"] = flat_conditional_versions(both, "coredns_version")
    if not out["etcd"]:
        out["etcd"] = flat_conditional_versions(both, "etcd_version")
    return out


def resolve(src, tag, kind, name, dl, cs):
    if kind == "perk8s":
        return None, "computed-per-k8s"
    if kind == "checksum":
        v = first_checksum_key(cs, name)
        return (v, "checksum-first-key") if v else (None, "checksum-absent")
    # kind == var
    m = re.search(rf"^{re.escape(name)}:\s*(.+?)\s*$", dl, re.M)
    if not m:
        return None, "var-absent"
    val = m.group(1)
    if "{{" not in val:
        return clean_ver(val), "literal-pin"
    # {{ (X_checksums['amd64'] ...) }} or {{ (X_checksums.no_arch | ...) }}
    cm = re.search(r"\(\s*(\w+)\s*[\[.]", val)
    if cm:
        v = first_checksum_key(cs, cm.group(1))
        if v:
            return v, "computed-first-key"
    return None, "computed-unresolved"


def parse_release(path):
    """(tag, {normalized_component: version}) from a RELEASE-V doc table."""
    text = open(path).read()
    m = re.search(r'^id:\s*RELEASE-V([0-9_]+)', text, re.M)
    if not m:
        return None, {}
    tag = "v" + m.group(1).replace("_", ".")
    impl = text.split("## Implementation", 1)[-1].split("\n## ", 1)[0]
    comps = {}
    for ln in impl.splitlines():
        cm = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", ln)
        if not cm:
            continue
        nm, ver = cm.group(1).strip(), cm.group(2).strip()
        if nm.lower() == "component" or set(nm) <= set("-| "):
            continue
        comps[norm(nm)] = ver
    return tag, comps


def main():
    ap = argparse.ArgumentParser(description="Kubepedia per-tag version consistency check")
    ap.add_argument("--src", default=os.path.join(ROOT, "kubespray-src"),
                    help="path to a kubespray git checkout (default: ./kubespray-src)")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(os.path.join(args.src, ".git")):
        print(f"kubespray source not found at {args.src} — skipping "
              f"(this check needs a kubespray git checkout).")
        return 0

    mismatches, checked, skipped = [], 0, 0
    for fn in sorted(os.listdir(REL_DIR)):
        if not fn.endswith(".md"):
            continue
        tag, comps = parse_release(os.path.join(REL_DIR, fn))
        if not tag or not comps:
            continue
        dl, cs = download_yml(args.src, tag), checksums_yml(args.src, tag)
        if not dl:
            print(f"  ! {tag}: source not available (fetch the tag) — skipped")
            continue
        perk8s = resolve_perk8s(args.src, tag)
        for comp, claimed in comps.items():
            if comp not in RESOLVE:
                continue
            kind, name = RESOLVE[comp]
            # etcd/coredns are per-K8s-minor: compare the SET of versions the doc
            # claims against the set the source resolves (doc must not claim a
            # version source doesn't ship; source-only versions are an info note).
            if comp in ("etcd", "coredns"):
                src_vers = set(perk8s.get(comp, {}).values())
                doc_vers = set(re.findall(r"\d+\.\d+\.\d+", claimed))
                if not src_vers or not doc_vers:
                    skipped += 1
                    if args.verbose:
                        print(f"  ~ {tag} {comp}: perk8s unresolved "
                              f"(claimed '{claimed}') — not checked")
                    continue
                missing = doc_vers - src_vers
                if missing:
                    mismatches.append((tag, comp, ",".join(sorted(doc_vers)),
                                       ",".join(sorted(src_vers)), "perk8s"))
                else:
                    checked += 1
                    omitted = src_vers - doc_vers
                    if args.verbose:
                        note = f" (source also has {','.join(sorted(omitted))})" if omitted else ""
                        print(f"  ok {tag} {comp}: {','.join(sorted(doc_vers))} (perk8s){note}")
                continue
            actual, how = resolve(args.src, tag, kind, name, dl, cs)
            if actual is None:
                skipped += 1
                if args.verbose:
                    print(f"  ~ {tag} {comp}: {how} (claimed '{claimed}') — not checked")
                continue
            checked += 1
            # claimed may carry markdown/qualifiers; compare on the version token
            cm = re.search(r"[0-9]+\.[0-9]+[0-9.]*", claimed)
            claim_v = cm.group(0) if cm else claimed
            if claim_v != actual:
                mismatches.append((tag, comp, claim_v, actual, how))
            elif args.verbose:
                print(f"  ok {tag} {comp}: {actual} ({how})")

    print("-" * 60)
    if mismatches:
        print(f"MISMATCHES ({len(mismatches)}) — RELEASE doc vs kubespray source:")
        for tag, comp, claimed, actual, how in mismatches:
            print(f"  [{tag}] {comp}: doc says '{claimed}', source has '{actual}' ({how})")
        print(f"\nchecked: {checked}   skipped: {skipped}   mismatches: {len(mismatches)}")
        return 1
    print(f"[PASS] version consistency: checked {checked}, skipped {skipped} "
          f"(computed-per-k8s/unresolved), 0 mismatches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
