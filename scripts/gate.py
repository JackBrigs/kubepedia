#!/usr/bin/env python3
"""kubepedia gate — CI gate for a Kubespray upgrade. Exits non-zero on blocking issues
so it can fail a pull request / pipeline.

  FAIL (exit 1): the inventory still sets variables that are REMOVED in the target tag
                 (they'd be silently ignored — a real misconfiguration).
  WARN         : the inventory PINS a component `*_version` that differs from the target
                 tag's default — that component won't move on upgrade (the "Cilium stuck"
                 class). Informational unless --strict (then it also fails).

    kubepedia gate --from v2.28.1 --to v2.31.0 \
        --inventory shared-defaults --inventory prod-cluster [--strict]

Reuses the `plan` (upgrade_diff) machinery: variable diff from the tagged Kubespray
source, inventory resolved via ansible-inventory.
"""
import argparse
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load(script):
    spec = importlib.util.spec_from_file_location("_" + script, os.path.join(HERE, script))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ud = _load("upgrade_diff.py")

# `*_version` vars that are the operator's legitimate choice, not a component pin to gate
VERSION_PIN_ALLOW = {"kube_version"}


def default_token_at(src, tag, var):
    """Version token of `var`'s default at a tag (None if absent/non-version)."""
    out = subprocess.run(["git", "-C", src, "grep", "-hE", f"^{re.escape(var)}:", tag,
                          "--", "roles/"], capture_output=True, text=True).stdout
    for ln in out.splitlines():
        val = ln.split(":", 1)[1].strip() if ":" in ln else ""
        m = re.search(r"[0-9]+\.[0-9]+[0-9.]*", val)
        if m:
            return m.group(0)
    return None


def token(s):
    m = re.search(r"[0-9]+\.[0-9]+[0-9.]*", str(s))
    return m.group(0) if m else None


def main():
    ap = argparse.ArgumentParser(description="Kubespray upgrade CI gate")
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--to", dest="to", required=True)
    ap.add_argument("--inventory", action="append", default=[], required=True,
                    help="inventory dir/file (repeat for composite)")
    ap.add_argument("--src", default=os.path.join(ROOT, "kubespray-src"))
    ap.add_argument("--strict", action="store_true", help="also fail on warnings")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru")
    args = ap.parse_args()
    ru = args.lang == "ru"

    frm = args.frm if args.frm.startswith("v") else "v" + args.frm
    to = args.to if args.to.startswith("v") else "v" + args.to
    if not os.path.isdir(os.path.join(args.src, ".git")):
        raise SystemExit(f"Kubespray checkout not found at {args.src} (need it for the diff)")

    fvars = ud.tag_var_names(args.src, frm)
    tvars = ud.tag_var_names(args.src, to)
    if not fvars or not tvars:
        raise SystemExit(f"could not read default vars for {frm}/{to} — are the tags fetched?")
    removed = fvars - tvars
    values, _prof, _how = ud.resolve_inventory(args.inventory)
    setvars = set(values)

    must_remove = sorted(setvars & removed)
    pins = []
    for v in sorted(setvars):
        if v.endswith("_version") and v not in VERSION_PIN_ALLOW:
            pt, dt = token(values.get(v)), default_token_at(args.src, to, v)
            if pt and dt and pt != dt:
                pins.append((v, pt, dt))

    out = [f"# {'CI-гейт апгрейда' if ru else 'Upgrade CI gate'}: {frm} → {to}\n"]
    if must_remove:
        out.append("❌ " + ("**БЛОК** — инвентарь задаёт переменные, удалённые в "
                            f"`{to}` (будут молча проигнорированы):" if ru else
                            f"**BLOCK** — inventory sets variables removed in `{to}` "
                            "(silently ignored):"))
        out += [f"  - `{v}`" for v in must_remove]
    if pins:
        out.append(("⚠ Запиненные версии компонентов, которые НЕ поедут с тегом "
                    "(в скобках — целевой дефолт):" if ru else
                    "⚠ Pinned component versions that won't move with the tag "
                    "(target default in parens):"))
        out += [f"  - `{v} = {pt}`  ({'цель' if ru else 'target'}: `{dt}`)" for v, pt, dt in pins]
    if not must_remove and not pins:
        out.append("✅ " + ("блокирующих проблем не найдено." if ru else "no blocking issues."))

    fail = bool(must_remove) or (bool(pins) and args.strict)
    verdict = ("❌ FAIL" if fail else "✅ PASS")
    note = ""
    if pins and not args.strict and not must_remove:
        note = ("  (пины — предупреждение; --strict сделает их блокирующими)" if ru
                else "  (pins are warnings; --strict makes them blocking)")
    out.append(f"\n{'Вердикт' if ru else 'Verdict'}: {verdict}{note}")
    sys.stdout.write("\n".join(out) + "\n")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
