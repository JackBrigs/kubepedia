#!/usr/bin/env python3
"""Self-improvement collector — mine the project for improvement suggestions.

A feedback loop (NOT ML "self-learning"): it scans the KB + git history (and,
opt-in, your session transcripts) for the exact classes of weakness this project
has hit, and emits a ranked backlog to reports/IMPROVEMENTS.md.

Signals encode the lessons already paid for:
  * operational docs (runbook/upgrade) with NO explicit service-impact/disruption
    statement  -> the "didn't state downtime" miss;
  * over-optimistic language ("non-disruptive/seamless/no downtime") in ops docs
    -> verify against the real Kubespray playbook/role;
  * ops docs whose mechanism isn't backed by a Kubespray *code* source
    -> the invented-variable / unverified-mechanism miss;
  * stale verified_at; thin non-stub docs;
  * recently-corrected git topics -> check sibling docs for the same class.

Usage:
    .venv/bin/python scripts/learn.py                       # in-repo signals -> reports/IMPROVEMENTS.md
    .venv/bin/python scripts/learn.py --transcripts <dir>   # + theme frequencies from session .jsonl (aggregate only)
    .venv/bin/python scripts/learn.py --stale-days 180
"""
import argparse
import json
import glob
import os
import re
import subprocess
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = "2026-07-20"  # Date.now() unavailable in some runners; caller may override

OPS_TYPES = {"best_practice", "upgrade"}
IMPACT_HINTS = ("impact", "disrupt", "downtime", "outage", "влияни", "простой",
                "backout", "rollback", "maintenance window", "service-affecting")
OPTIMISTIC = ("non-disruptive", "no downtime", "zero downtime", "seamless",
              "without disruption", "no disruption", "no interruption",
              "pods keep running", "datapath survives")
KUBESPRAY_CODE = ("kubernetes-sigs/kubespray",)
# a doc is a *mutating* operation (needs an explicit impact statement) only if it runs something
# a doc *claims a Kubespray mechanism* when it names a playbook, a job tag, a role path or a
# Kubespray variable — those are the claims that must be backed by tagged source code.
MECHANISM = re.compile(
    r"\b\w*\.yml\b"                       # cluster.yml, scale.yml, upgrade_cluster.yml …
    r"|--tags|--skip-tags|job tag"        # tag-scoped runs (AWX or CLI)
    r"|\broles/[\w.\-/]+"                 # a role/task path
    r"|\b[a-z][a-z0-9]*(?:_[a-z0-9]+)*_(?:version|enabled|owner|mode|dir|repo|image)\b",
    re.I,
)
MUTATING = ("cluster.yml", "upgrade-cluster.yml", "scale.yml", "reset.yml", "remove-node.yml",
            "remove_node.yml", "recover-control-plane.yml", "ansible-playbook", "converge",
            "helm upgrade", "helm install", "kubectl apply", "kubectl delete", "kubectl drain",
            "cilium upgrade", "cilium install")


def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta, body = m.group(1), m.group(2)
    d = {}
    for k in ("id", "type", "verified_at"):
        km = re.search(rf"^{k}:\s*(.+)$", meta, re.M)
        if km:
            d[k] = km.group(1).strip().strip('"')
    d["_meta"] = meta
    d["_stub"] = "generated: variable-stub" in body
    return d, body


def days_since(date):
    try:
        from datetime import date as D
        y1, m1, d1 = map(int, date.split("-"))
        y2, m2, d2 = map(int, TODAY.split("-"))
        return (D(y2, m2, d2) - D(y1, m1, d1)).days
    except Exception:
        return None


def git_corrections(n=60):
    try:
        out = subprocess.run(["git", "-C", ROOT, "log", f"-{n}", "--pretty=%h %s"],
                             capture_output=True, text=True).stdout
    except Exception:
        return []
    pat = re.compile(r"исправ|промах|неверн|по факту|аудит|\bfix\b|correct|revert", re.I)
    return [ln for ln in out.splitlines() if pat.search(ln)]


def scan():
    impact_missing, optimistic, no_code_src, stale, thin = [], [], [], [], []
    for f in glob.glob(os.path.join(ROOT, "kb", "**", "*.md"), recursive=True):
        d, body = fm(open(f).read())
        _id, typ = d.get("id"), d.get("type")
        if not _id:
            continue
        rel = os.path.relpath(f, ROOT)
        low = body.lower()
        if typ in OPS_TYPES and not d["_stub"]:
            if any(m in low for m in MUTATING) and not any(h in low for h in IMPACT_HINTS):
                impact_missing.append((_id, rel))
            # optimistic ONLY when the doc never also discusses impact (else it's a corrected/qualified use)
            hit = [w for w in OPTIMISTIC if w in low]
            if hit and not any(h in low for h in IMPACT_HINTS):
                optimistic.append((_id, rel, hit[0]))
            # mechanism claim not backed by a kubespray code source?
            # Only when the doc actually *names a mechanism* — a playbook, a tag, a role path
            # or a Kubespray variable. Merely mentioning "kubespray"/"cilium" is a topic, not
            # a claim (generic best practices were flagged falsely before this).
            if MECHANISM.search(body) and not any(c in d["_meta"] for c in KUBESPRAY_CODE):
                no_code_src.append((_id, rel))
        va = d.get("verified_at")
        if va and not d["_stub"]:
            ds = days_since(va)
            if ds and ds > STALE_DAYS:
                stale.append((ds, _id, rel))
        if not d["_stub"] and typ in OPS_TYPES | {"troubleshooting", "concept", "component"} and len(body) < 900:
            thin.append((len(body), _id, rel))
    return impact_missing, optimistic, no_code_src, stale, thin


def transcript_themes(d):
    words = Counter()
    qcount = 0
    for jf in glob.glob(os.path.join(d, "*.jsonl")):
        for ln in open(jf, errors="ignore"):
            try:
                o = json.loads(ln)
            except Exception:
                continue
            msg = o.get("message", o)
            if isinstance(msg, dict) and msg.get("role") == "user":
                c = msg.get("content", "")
                text = c if isinstance(c, str) else " ".join(
                    b.get("text", "") for b in c if isinstance(b, dict))
                t = text.strip()
                # skip non-questions: empty, tags, tool/system content, and pasted blobs/summaries
                if (not t or t.startswith("<") or "system-reminder" in t or "tool_result" in t
                        or t.lower().startswith(("analysis:", "summary:")) or len(t) > 1500):
                    continue
                qcount += 1
                for w in re.findall(r"[a-zA-Zа-яА-Я][a-zA-Zа-яА-Я_-]{3,}", t.lower()):
                    words[w] += 1
    STOP = set(("надо нужно давай если что-то этот тебе мне для как это про там ещё быть или git the "
                "and for you can что чтобы можешь может from user claude with docs summary fixed main "
                "tags потом пока продолжай version versions это все всё этого также так что-то есть "
                "there this that have will your").split())
    return qcount, [(w, c) for w, c in words.most_common(60) if w not in STOP and len(w) > 3][:20]


def main():
    global STALE_DAYS
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcripts", help="dir with session .jsonl (aggregate themes only; not committed content)")
    ap.add_argument("--stale-days", type=int, default=180)
    args = ap.parse_args()
    STALE_DAYS = args.stale_days

    impact_missing, optimistic, no_code_src, stale, thin = scan()
    corr = git_corrections()

    L = ["# Improvement backlog (сгенерировано `scripts/learn.py`)",
         f"_Дата: {TODAY}. Петля обратной связи: сигналы из базы + git. Перегенерируется; правьте не файл, а базу._\n",
         "## P0 — риски корректности (уроки этой сессии, автоматизированы)\n"]

    L.append(f"### Операционные доки БЕЗ явного impact/простоя ({len(optimistic)+len(impact_missing)} сигналов)")
    if optimistic:
        L.append("**Оптимистичные формулировки — сверить с playbook/ролью Kubespray и указать реальный простой:**")
        for _id, rel, w in optimistic[:15]:
            L.append(f"- `{_id}` — «{w}» → `{rel}`")
    if impact_missing:
        L.append("\n**Нет раздела impact/disruption (runbook/upgrade):**")
        for _id, rel in impact_missing[:20]:
            L.append(f"- `{_id}` → `{rel}`")
    L.append(f"\n### Механизм не подкреплён исходником Kubespray ({len(no_code_src)})")
    L.append("_Док описывает cluster.yml/scale.yml/cilium/kubespray, но в `sources` нет `type: code` на роль/плейбук → риск выдуманной переменной/механизма (как `cilium_upgrade_compatibility`)._")
    for _id, rel in no_code_src[:20]:
        L.append(f"- `{_id}` → `{rel}`")

    L.append(f"\n## P1 — свежесть и полнота\n### Протухший verified_at (>{STALE_DAYS}д): {len(stale)}")
    for ds, _id, rel in sorted(stale, reverse=True)[:15]:
        L.append(f"- {ds}д `{_id}` → `{rel}`")
    L.append(f"\n### Тонкие доки (<900 симв.): {len(thin)}")
    for n, _id, rel in sorted(thin)[:15]:
        L.append(f"- {n}c `{_id}` → `{rel}`")

    L.append(f"\n## P2 — недавно исправленное (проверить соседей на тот же класс ошибки): {len(corr)}")
    L.append("_После правки одного дока тот же промах часто есть в соседних (Cilium→add-nodes)._")
    for ln in corr[:12]:
        L.append(f"- {ln}")

    if args.transcripts and os.path.isdir(args.transcripts):
        qn, themes = transcript_themes(args.transcripts)
        L.append(f"\n## Темы твоих вопросов ({qn} реплик; агрегат, без сырого текста)")
        L.append("_Частые темы = где база активнее всего проверяется/дёргается — кандидаты на углубление._")
        L.append(", ".join(f"`{w}`×{c}" for w, c in themes))

    out = os.path.join(ROOT, "reports", "IMPROVEMENTS.md")
    open(out, "w").write("\n".join(L) + "\n")
    print(f"[learn] impact-risks={len(optimistic)+len(impact_missing)} no-code-src={len(no_code_src)} "
          f"stale={len(stale)} thin={len(thin)} corrections={len(corr)} -> {os.path.relpath(out, ROOT)}")


if __name__ == "__main__":
    main()
