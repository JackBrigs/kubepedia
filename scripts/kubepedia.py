#!/usr/bin/env python3
"""kubepedia — one CLI over the Kubepedia tools.

    kubepedia plan   --from v2.28.1 --to v2.31.0 --inventory <dir>   # migration diff (pre)
    kubepedia check  --version v2.31.0 --facts facts.json            # post-upgrade verify
    kubepedia impact etcd                                            # graph impact
    kubepedia versions cilium                                        # version per tag + how it is pinned
    kubepedia report --from v2.28.1 --to v2.31.0                     # KB-narrative report
    kubepedia verify                                                 # KB version consistency
    kubepedia validate                                              # KDS validation
    kubepedia index                                                 # regenerate index/

Each subcommand dispatches to the matching script with the remaining args, so their
own `--help` / flags work unchanged (e.g. `kubepedia plan --help`).
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# subcommand -> (script, one-line description)
CMDS = {
    "plan":     ("upgrade_diff.py",   "inventory migration diff (pre-upgrade): version + variable changes"),
    "gate":     ("gate.py",           "CI gate: fail on removed vars still set / version pins blocking upgrade"),
    "check":    ("post_check.py",     "post-upgrade verification: did every component actually move + health"),
    "impact":   ("impact.py",         "graph impact analysis: what depends on X / what breaks if X changes"),
    "report":   ("upgrade_report.py", "KB-narrative upgrade report (personalized to an inventory)"),
    "verify":   ("check_versions.py", "KB integrity: component versions vs the tagged Kubespray source"),
    "versions": ("versions_lookup.py", "which version of a component ships per tag, and how it is defined"),
    "feed":     ("freshness.py",      "freshness monitor: new upstream tags beyond ceiling + aging verified_at"),
    "validate": ("validate_kds.py",   "KDS validation of the knowledge base"),
    "index":    ("generate_index.py", "regenerate the derived index/ from kb/"),
}


def _load(script):
    path = os.path.join(HERE, script)
    spec = importlib.util.spec_from_file_location("_kp_" + script, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _usage():
    print("kubepedia — one CLI over the Kubepedia tools\n")
    print("usage: kubepedia <command> [args...]\n")
    print("commands:")
    width = max(len(c) for c in CMDS)
    for cmd, (_script, desc) in CMDS.items():
        print(f"  {cmd:<{width}}  {desc}")
    print("\nrun `kubepedia <command> --help` for a command's own options.")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        _usage()
        return 0
    cmd = sys.argv[1]
    if cmd not in CMDS:
        print(f"kubepedia: unknown command '{cmd}'\n", file=sys.stderr)
        _usage()
        return 2
    script, _desc = CMDS[cmd]
    mod = _load(script)
    # hand the rest of argv to the target's own argparse (prog shows as "kubepedia <cmd>")
    sys.argv = [f"kubepedia {cmd}"] + sys.argv[2:]
    return mod.main() or 0


if __name__ == "__main__":
    sys.exit(main())
