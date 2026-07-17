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

etcd/coredns are computed **per Kubernetes minor** (not a simple first-key), so
they are reported as "computed-per-k8s (not checked)" rather than guessed.

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
#   ("perk8s", None)   : computed per Kubernetes minor -> skip comparison
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
    cm = re.search(r"\(\s*(\w+)\s*\[", val)  # {{ (X_checksums['amd64'] ...) }}
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
        for comp, claimed in comps.items():
            if comp not in RESOLVE:
                continue
            kind, name = RESOLVE[comp]
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
