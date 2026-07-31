#!/usr/bin/env python3
"""kubepedia cve-matrix — матрица CVE по версиям, которые везёт Kubespray.

Заметки к релизам говорят «здесь починили», но не говорят «ваша версия затронута».
Ответ на второй вопрос даёт osv.dev: он фильтрует по версии, а не по тексту. Поэтому
матрицы строятся отсюда, а не из changelog — так же, как это уже сделано для
containerd, etcd, Calico и остальных.

Скрипт спрашивает osv.dev по каждой версии из конверта тегов Kubespray и пишет
документ KDS. Дальше его подхватывает периодический пере-свип (`cve_sweep.py`),
который сверяет матрицу с текущим состоянием osv.dev и сообщает о расхождениях.

Пакет задаётся явно: угадывать путь модуля нельзя. Неверный путь тихо вернёт
пустой ответ, и компонент будет выглядеть безопасным.

    kubepedia cve-matrix --component ingress-nginx --package k8s.io/ingress-nginx
    kubepedia cve-matrix --all
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "kb", "troubleshooting")
OSV = "https://api.osv.dev/v1/query"

# Проверено запросом к osv.dev: эти пакеты он знает и умеет фильтровать по версии.
# Остальные компоненты периметра в его индексе отсутствуют — матрицу по ним строить
# не из чего, и выдумывать её нельзя.
KNOWN = {
    "ingress-nginx": ("k8s.io/ingress-nginx", "COMPONENT-INGRESS_NGINX"),
    "flannel": ("github.com/flannel-io/flannel", "COMPONENT-FLANNEL"),
    "local-path-provisioner": ("github.com/rancher/local-path-provisioner",
                               "COMPONENT-LOCAL_PATH_PROVISIONER"),
    "kube-router": ("github.com/cloudnativelabs/kube-router", "COMPONENT-KUBE_ROUTER"),
    "kata-containers": ("github.com/kata-containers/kata-containers", "COMPONENT-KATA_CONTAINERS"),
}


def shipped_versions(comp):
    """Версия компонента на каждом теге Kubespray — из штатного лукапа базы."""
    out = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "versions_lookup.py"), comp],
                         capture_output=True, text=True).stdout
    rows = []
    for line in out.split("\n"):
        m = re.match(r"^(v\d+\.\d+\.\d+)\s+(\S+)", line)
        if m and m.group(2) != "—":
            rows.append((m.group(1), m.group(2)))
    return rows


def osv_query(pkg, version, cache):
    key = (pkg, version)
    if key in cache:
        return cache[key]
    body = json.dumps({"package": {"name": pkg, "ecosystem": "Go"}, "version": version}).encode()
    req = urllib.request.Request(OSV, data=body, headers={
        "Content-Type": "application/json", "User-Agent": "kubepedia-cve-matrix"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            vulns = json.load(r).get("vulns", [])
    except Exception as exc:                            # noqa: BLE001 — сеть не должна ронять прогон
        print(f"  ! osv.dev не ответил по {pkg}@{version}: {exc}", file=sys.stderr)
        return None
    cache[key] = vulns
    time.sleep(0.2)
    return vulns


def version_resolvable(v):
    """Умеет ли запись osv отвечать на вопрос «затронута ли конкретная версия».

    Часть записей описывает затронутый диапазон только коммитами (тип GIT). Такая
    запись совпадает с любой версией, и в матрице она выглядит так, будто уязвимость
    есть даже там, где её давно починили. Проверено на ingress-nginx: 1.13.3 получал
    CVE, исправленную в 1.12.1. Такие записи в версионную таблицу не идут.
    """
    for aff in v.get("affected", []):
        for rng in aff.get("ranges", []):
            if rng.get("type") in ("SEMVER", "ECOSYSTEM"):
                return True
    return False


def vt(x):
    return tuple(int(n) for n in re.findall(r"\d+", x)[:3])


def affected_with_fixes(cid, version, fixes_by_cve):
    """Затронута ли версия с учётом фиксов, собранных по всем записям этого CVE."""
    fixes = sorted(fixes_by_cve.get(cid) or [], key=vt)
    if not fixes:
        return True
    same_line = [f for f in fixes if vt(f)[:2] == vt(version)[:2]]
    threshold = max(same_line or fixes, key=vt)
    return vt(version) < vt(threshold)


def still_affected(v, version):
    """Затронута ли версия на самом деле, с поправкой на неполные записи osv.

    Часть записей Go-базы описывает диапазон как «introduced: 0» без события
    «исправлено» — формально это «затронуты все версии», и по такой записи любая
    версия выглядит уязвимой. При этом сведения об исправлении есть в парной записи
    того же CVE (GHSA). Проверено на ingress-nginx: 1.13.3 выходил после фиксов,
    но по Go-записи получал все десять CVE.

    Поэтому: если у записи вообще есть версия исправления — сравниваем с ней, отдавая
    предпочтение фиксу на той же линии поддержки. Нет фикса нигде — уязвимость
    действительно открыта, и версия затронута.
    """
    fixes = fixed_in(v)
    if not fixes:
        return True
    same_line = [f for f in fixes if vt(f)[:2] == vt(version)[:2]]
    threshold = max(same_line or fixes, key=vt)
    return vt(version) < vt(threshold)


def cve_id(v):
    for a in v.get("aliases", []):
        if a.startswith("CVE-"):
            return a
    return v.get("id")


def fixed_in(v):
    out = []
    for aff in v.get("affected", []):
        for rng in aff.get("ranges", []):
            for ev in rng.get("events", []):
                if ev.get("fixed"):
                    out.append(ev["fixed"])
    return sorted(set(out))


def build(comp, pkg, comp_id, today):
    rows = shipped_versions(comp)
    if not rows:
        return None
    cache, table, details = {}, [], {}
    # Один и тот же CVE приходит несколькими записями (GO и GHSA), и сведения об
    # исправлении есть не в каждой. Собираем версии фиксов по всем записям сразу,
    # иначе неполная запись объявит уязвимой версию, где всё давно починено.
    raw = {}
    for tag, ver in rows:
        vulns = osv_query(pkg, ver, cache)
        if vulns is None:
            return None
        raw[ver] = [v for v in vulns if version_resolvable(v)]
    fixes_by_cve = {}
    for vulns in raw.values():
        for v in vulns:
            fixes_by_cve.setdefault(cve_id(v), set()).update(fixed_in(v))

    for tag, ver in rows:
        ids = sorted({cve_id(v) for v in raw[ver]
                      if affected_with_fixes(cve_id(v), ver, fixes_by_cve)})
        table.append((tag, ver, ids))
        for v in raw[ver]:
            cid = cve_id(v)
            if cid in ids and (cid not in details or not fixed_in(details[cid])):
                details[cid] = v
    if not details:
        return {"empty": True, "comp": comp, "rows": table}

    body = ["| Kubespray | Component version | # CVEs | CVEs |", "|---|---|---:|---|"]
    for tag, ver, ids in table:
        body.append(f"| {tag} | {ver} | {len(ids)} | {', '.join(ids) if ids else '—'} |")
    known = ["", "CVEs (id — summary — fixed in):", ""]
    for cid, v in sorted(details.items()):
        summary = re.sub(r"\s+", " ", v.get("summary") or v.get("details", "")[:160]).strip()
        fx = ", ".join(sorted(fixes_by_cve.get(cid) or [], key=vt)) or "no fix released"
        known.append(f"- **{cid}** — {summary} — fixed in: `{fx}`")
    worst = max(table, key=lambda r: len(r[2]))
    newest = table[-1]
    return {
        "comp": comp, "pkg": pkg, "comp_id": comp_id, "today": today,
        "first_v": table[0][1], "last_v": newest[1],
        "n_cve": len(details), "n_newest": len(newest[2]), "newest_tag": newest[0],
        "worst_tag": worst[0], "worst_n": len(worst[2]),
        "table": "\n".join(body), "known": "\n".join(known),
    }


DOC = """---
id: TROUBLE-{sid}_KNOWN_CVES
type: troubleshooting
title: "{comp}: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">={first_v} <={last_v}"
verified_at: "{today}"
confidence: verified
aliases:
  - {comp} cve
  - {comp} security
  - is {comp} vulnerable
tags:
  - security
  - cve
  - {comp}
sources:
  - type: docs
    path: osv.dev API ({pkg})
    url: https://osv.dev/list?q={pkg}
    note: "version-filtered vulnerability data, queried per shipped version"
relations:
  - type: see_also
    target: {comp_id}
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# {comp}: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **{n_cve} distinct CVEs** affecting the {comp} versions Kubespray ships across
v2.27.0–v2.31.0. The newest shipped version ({last_v}, {newest_tag}) is affected by **{n_newest}**;
the worst tag is {worst_tag} with {worst_n}.

Counts are distinct advisories. osv.dev returns one record per database (GHSA *and* GO) for the same
CVE, so a raw record count roughly doubles it.

## Problem

Each shipped version carries the CVEs below. osv.dev returns only vulnerabilities that affect the
queried version, so this is authoritative affectedness rather than a guess from release notes.

## Context

{table}

## Diagnostics

```bash
kubectl get pods -A -o jsonpath='{{range .items[*]}}{{range .spec.containers[*]}}{{.image}}{{"\\n"}}{{end}}{{end}}' \\
  | grep -i {comp} | sort -u
```

## Known Issues

{known}

**Recommendation:** compare the version in use against the "fixed in" column. When Kubespray pins a
version below the fix, the remedy is an explicit pin in inventory plus the matching checksum — the
same pattern as for the container runtime; see [[CONCEPT-SECURITY_INDEX]].

## References

- osv.dev queried per shipped version for `{pkg}` — verified {today}.
- Component: [[{comp_id}]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
"""


def main():
    ap = argparse.ArgumentParser(description="Матрица CVE по версиям из конверта Kubespray")
    ap.add_argument("--component", action="append")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--today", default="2026-07-31")
    args = ap.parse_args()
    comps = args.component or (sorted(KNOWN) if args.all else [])
    if not comps:
        ap.error("нужен --component или --all")

    for comp in comps:
        if comp not in KNOWN:
            print(f"[--] {comp}: пакет osv.dev не подтверждён, матрицу строить не из чего")
            continue
        pkg, comp_id = KNOWN[comp]
        d = build(comp, pkg, comp_id, args.today)
        if d is None:
            print(f"[--] {comp}: нет версий или osv.dev недоступен")
            continue
        if d.get("empty"):
            print(f"[ok] {comp}: уязвимостей по версиям из конверта не найдено — документ не нужен")
            continue
        d["sid"] = re.sub(r"[^A-Z0-9]+", "_", comp.upper()).strip("_")
        path = os.path.join(KB, f"{comp}-known-cves.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(DOC.format(**d))
        print(f"[ok] {comp:24} CVE {d['n_cve']:3}, на новейшей версии {d['n_newest']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
