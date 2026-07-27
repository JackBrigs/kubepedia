#!/usr/bin/env python3
"""Kubepedia periodic osv.dev CVE re-sweep.

Re-queries osv.dev for every component version listed in the KB's CVE matrices
(`kb/troubleshooting/*known-cves.md`) and diffs the live answer against what the
document records. CVE data is date-sensitive: a matrix that was correct when it
was written silently rots as new advisories land against already-shipped
versions. This script makes that drift visible and cheap to re-check.

It never edits knowledge — it reports. Updating a matrix stays a normal KDS
change (body + `verified_at` + validation).

Usage:
    python3 scripts/cve_sweep.py                  # sweep every matrix, RU report
    python3 scripts/cve_sweep.py --lang en
    python3 scripts/cve_sweep.py cilium containerd
    python3 scripts/cve_sweep.py --json
    python3 scripts/cve_sweep.py --offline        # parse only, no network
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

KB = Path(__file__).resolve().parent.parent / "kb"
MATRIX_GLOB = "troubleshooting/*known-cves.md"
OSV_API = "https://api.osv.dev/v1/query"
OSV_PKG_RE = re.compile(r"path:\s*osv\.dev API \((?P<pkg>[^)]+)\)")
ID_RE = re.compile(r"\b(?:CVE-\d{4}-\d{4,}|GHSA-[\w-]{14,}|GO-\d{4}-\d+)\b")


class Matrix:
    """One `*-known-cves.md` document: its package, and version -> recorded CVE ids."""

    def __init__(self, path: Path, text: str):
        self.path = path
        self.name = path.stem.replace("-known-cves", "")
        fm = text.split("---", 2)[1] if text.startswith("---") else ""
        self.doc_id = _fm_value(fm, "id")
        self.verified_at = _fm_value(fm, "verified_at").strip('"')
        # A component can span several Go modules (etcd: go.etcd.io/etcd/v3 +
        # .../server/v3). Every osv.dev source is queried and the results unioned,
        # so a matrix can never under-report because one module path was missed.
        self.packages = OSV_PKG_RE.findall(fm)
        self.package = self.packages[0] if self.packages else None
        self.rows = _parse_rows(text)

    @property
    def usable(self) -> bool:
        return bool(self.packages and self.rows)


def _fm_value(fm: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
    return m.group(1).strip() if m else ""


def _parse_rows(text: str) -> list[dict]:
    """Rows of the `| Component version | Kubespray | # CVEs | CVEs |` table.

    A cell that carries no advisory id (e.g. "1.7.x line — larger set") means the
    document deliberately did not enumerate that version: recorded is left None so
    the sweep reports the live count without claiming drift.
    """
    rows = []
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        version = cells[0]
        if not re.match(r"^v?\d+\.\d+", version):
            continue
        ids = set(ID_RE.findall(cells[3]))
        rows.append(
            {
                "version": version.lstrip("v"),
                "kubespray": cells[1],
                "recorded": ids or None,
                "recorded_count": cells[2],
            }
        )
    return rows


def load_matrices(kb: Path, only: list[str]) -> list[Matrix]:
    out = []
    for path in sorted(kb.glob(MATRIX_GLOB)):
        m = Matrix(path, path.read_text(encoding="utf-8"))
        if only and m.name not in only:
            continue
        out.append(m)
    return out


def packages_for(packages: list[str], version: str) -> list[str]:
    """The declared module paths that can legitimately answer for `version`.

    A `/vN` suffix pins a module to major N, and the two failure modes are
    symmetric — both were observed on containerd:

    * querying `.../containerd/v2` with 1.7.27 compares an out-of-module version
      against the v2 ranges and returns advisories that do not apply;
    * querying the **unsuffixed** `.../containerd` with 2.0.5 matches the v1
      entries of the checkpoint advisories (`introduced: 0`, never fixed on 1.x)
      and over-reports 8 where there are 5.

    So: when the document declares a `/vN` path matching the version's major, that
    path is authoritative and the unsuffixed one is dropped. Otherwise every
    non-conflicting declared path is used (Calico 3.x legitimately lives on an
    unsuffixed module).
    """
    major = version.split(".")[0]
    exact = [
        p for p in packages
        if (m := re.search(r"/v(\d+)$", p)) and m.group(1) == major
    ]
    if exact:
        return exact
    return [p for p in packages if not re.search(r"/v\d+$", p)]


def osv_query(package: str, version: str, cache: dict) -> list[dict] | None:
    """Vulns affecting `version` of `package`, or None when osv.dev is unreachable.

    The package is queried **exactly as the document declares it**. Deriving a `/vN`
    suffix from the version looks helpful and is a guess: containerd 2.x really does
    live at `.../containerd/v2`, while Calico 3.x stays on the unsuffixed path. A
    matrix that needs two module paths lists both in its `sources` and they are
    unioned.
    """
    key = (package, version)
    if key in cache:
        return cache[key]
    body = json.dumps(
        {"version": version, "package": {"name": package, "ecosystem": "Go"}}
    ).encode()
    req = urllib.request.Request(
        OSV_API, data=body, headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            vulns = json.load(resp).get("vulns", [])
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"  ! osv.dev query failed for {package}@{version}: {exc}", file=sys.stderr)
        cache[key] = None
        return None
    cache[key] = vulns
    return vulns


def version_resolvable(vuln: dict) -> bool:
    """Can this advisory's affectedness be decided from a version number?

    An osv record whose only ranges are GIT commit ranges cannot: osv.dev then
    answers a version query by matching the *package*, not the version, and hands
    back the same set for 1.11.0, 1.13.3 and 999.0.0 alike (k8s.io/ingress-nginx is
    the live example). Rows built on such records look precise and are not.
    """
    for a in vuln.get("affected", []):
        for r in a.get("ranges", []):
            if r.get("type") in ("SEMVER", "ECOSYSTEM"):
                return True
    return False


def canonical_ids(vulns: list[dict]) -> dict[str, dict]:
    """Map an advisory to the id form the KB uses: CVE alias when osv has one."""
    out = {}
    for v in vulns:
        cve = next((a for a in v.get("aliases", []) if a.startswith("CVE-")), None)
        key = cve or v["id"]
        # The same advisory is filed in several databases; keep the record that can
        # actually be reasoned about by version (the GO/GHSA one) over a git-only CVE
        # record, so both the fix data and the version-resolvable guard are accurate.
        if key not in out or (
            version_resolvable(v) and not version_resolvable(out[key])
        ):
            out[key] = v
    return out


def summarize(vuln: dict) -> str:
    text = vuln.get("summary") or vuln.get("details", "").split("\n")[0]
    return " ".join(text.split())[:140]


def sweep(matrices: list[Matrix], offline: bool) -> list[dict]:
    cache: dict = {}
    results = []
    for m in matrices:
        entry = {
            "component": m.name,
            "doc": str(m.path.relative_to(KB.parent)),
            "id": m.doc_id,
            "package": ", ".join(m.packages),
            "verified_at": m.verified_at,
            "rows": [],
            "usable": m.usable,
        }
        if m.usable and offline:
            entry["rows"] = [
                {
                    "version": r["version"],
                    "kubespray": r["kubespray"],
                    "recorded": sorted(r["recorded"]) if r["recorded"] else None,
                    "skipped": True,
                }
                for r in m.rows
            ]
        elif m.usable:
            for row in m.rows:
                vulns, failed = [], False
                for pkg in packages_for(m.packages, row["version"]):
                    got = osv_query(pkg, row["version"], cache)
                    if got is None:
                        failed = True
                    else:
                        vulns.extend(got)
                if failed and not vulns:
                    entry["rows"].append({**row, "error": True})
                    continue
                live = canonical_ids(vulns)
                recorded = row["recorded"]
                # osv ids, CVE and GHSA aliases all appear in the KB; one advisory
                # is "already recorded" if the doc names it under any of them.
                live_all = set(live) | {v["id"] for v in vulns}
                for v in vulns:
                    live_all.update(v.get("aliases", []))
                new = sorted(
                    cid
                    for cid, v in live.items()
                    if recorded is not None
                    and not ({cid, v["id"], *v.get("aliases", [])} & recorded)
                )
                gone = sorted(recorded - live_all) if recorded is not None else []
                # A row may state a count without listing the ids ("8 | superset —
                # query osv.dev"). The count still has to hold, so check it.
                stated = row["recorded_count"].strip()
                count_drift = (
                    int(stated) != len(live) if stated.isdigit() else None
                )
                entry["rows"].append(
                    {
                        "version": row["version"],
                        "kubespray": row["kubespray"],
                        "recorded": sorted(recorded) if recorded else None,
                        "recorded_count": stated,
                        "count_drift": count_drift,
                        "live_count": len(live),
                        "live": sorted(live),
                        "new": new,
                        "gone": gone,
                        "details": {k: summarize(v) for k, v in live.items() if k in new},
                        "git_only": sorted(
                            cid for cid, v in live.items() if not version_resolvable(v)
                        ),
                    }
                )
        results.append(entry)
    return results


T = {
    "ru": {
        "title": "Пере-свип CVE по osv.dev",
        "no_pkg": "не разобран (нет пакета osv.dev или таблицы версий)",
        "clean": "✅ расхождений нет — матрицы совпадают с osv.dev",
        "drift": "⚠️ расхождения: матрицы устарели, нужен апдейт",
        "new": "новые",
        "gone": "больше не затрагивают",
        "verified": "проверено",
        "count": "счётчик разошёлся",
        "doc_says": "в доке",
        "git_only": "affectedness не проверяется по версии (в osv только git-диапазоны)",
        "unenumerated": "не перечислялись в доке; сейчас на osv.dev",
        "errors": "запросов не удалось",
        "verdict": "Вердикт",
        "components": "компонентов",
        "versions": "версий",
    },
    "en": {
        "title": "osv.dev CVE re-sweep",
        "no_pkg": "unparsed (no osv.dev package or version table)",
        "clean": "✅ no drift — matrices match osv.dev",
        "drift": "⚠️ drift found: matrices are stale and need an update",
        "new": "new",
        "gone": "no longer affecting",
        "verified": "verified",
        "count": "count drift",
        "doc_says": "doc says",
        "git_only": "affectedness not version-resolvable (osv has git ranges only)",
        "unenumerated": "not enumerated in the doc; osv.dev now reports",
        "errors": "failed queries",
        "verdict": "Verdict",
        "components": "components",
        "versions": "versions",
    },
}


def render(results: list[dict], lang: str, today: str) -> str:
    t = T[lang]
    out = [f"# {t['title']} — {today}", ""]
    drift = errors = versions = 0
    for entry in results:
        if not entry["usable"]:
            out.append(f"## {entry['component']} — {t['no_pkg']}")
            out.append("")
            continue
        lines = []
        for row in entry["rows"]:
            versions += 1
            if row.get("error"):
                errors += 1
                continue
            if row.get("skipped"):
                continue
            tag = f"{row['version']} ({row['kubespray']})"
            if row["count_drift"]:
                drift += 1
                lines.append(
                    f"- `{tag}` — {t['count']}: {t['doc_says']} {row['recorded_count']}, "
                    f"osv.dev — **{row['live_count']}** ({', '.join(row['live']) or '—'})"
                )
                continue
            if row["recorded"] is None:
                lines.append(
                    f"- `{tag}` — {t['unenumerated']}: **{row['live_count']}** — "
                    + (", ".join(row["live"]) or "—")
                )
                continue
            if row["new"]:
                drift += 1
                lines.append(f"- `{tag}` — {t['new']}: **{', '.join(row['new'])}**")
                for cid in row["new"]:
                    lines.append(f"    - {cid} — {row['details'].get(cid, '')}")
            if row["gone"]:
                drift += 1
                lines.append(f"- `{tag}` — {t['gone']}: {', '.join(row['gone'])}")
            if row.get("git_only"):
                lines.append(
                    f"- `{tag}` — {t['git_only']}: {', '.join(row['git_only'])}"
                )
        head = f"## {entry['component']} (`{entry['package']}`, {t['verified']} {entry['verified_at']})"
        out.append(head)
        out.extend(lines or [f"- ✅ {len(entry['rows'])} {t['versions']} — ok"])
        out.append("")
    out.append(f"## {t['verdict']}")
    out.append("")
    counted = sum(1 for e in results if e["usable"])
    out.append(f"{counted} {t['components']}, {versions} {t['versions']}.")
    if errors:
        out.append(f"{t['errors']}: {errors}.")
    out.append(t["drift"] if drift else t["clean"])
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description="Kubepedia osv.dev CVE re-sweep")
    ap.add_argument("components", nargs="*", help="limit to these matrices (e.g. cilium runc)")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--offline", action="store_true", help="parse matrices, skip osv.dev")
    ap.add_argument("--today", default=None, help="report date YYYY-MM-DD")
    args = ap.parse_args()

    matrices = load_matrices(KB, args.components)
    if not matrices:
        print("no CVE matrices matched", file=sys.stderr)
        return 2
    results = sweep(matrices, args.offline)
    if args.json:
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0
    today = args.today or __import__("datetime").date.today().isoformat()
    print(render(results, args.lang, today))
    return 0


if __name__ == "__main__":
    sys.exit(main())
