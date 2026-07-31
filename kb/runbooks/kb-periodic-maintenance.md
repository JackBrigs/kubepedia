---
id: PRACTICE-RUNBOOK_KB_MAINTENANCE
type: best_practice
title: "Runbook: periodic maintenance of the knowledge base itself"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kb periodic maintenance
  - keep the knowledge base fresh
  - nightly kb checks
  - what to run weekly on the knowledge base
tags:
  - runbook
  - maintenance
  - security
sources:
  - type: code
    path: scripts/kubepedia.py — subcommands feed, cve, issues, breaking, defects, cve-matrix
    note: "the loop is the tooling; this document records cadence, order and what each answer means"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Runbook: periodic maintenance of the knowledge base itself

## Summary

The knowledge base ages in three independent ways, and each has its own guard. Upstream releases new
tags, so the version envelope falls behind. Vulnerability databases add records, so security
matrices become wrong without anything in the base changing. Projects publish defects and behaviour
changes, so the problem layer thins out.

Nothing here needs a cluster. All of it is read-only against upstream sources.

## Context

The loop below is the tooling in `scripts/kubepedia.py`; this document records the cadence, the
order and what each answer means. Nothing here touches a cluster — every step is read-only against
upstream sources.

### Prerequisites

- a GitHub token for the release sweep — unauthenticated API allows 60 requests an hour, which is
  not enough for the component map (`gh auth login`, or `GITHUB_TOKEN` in the environment);
- network access to `api.osv.dev` and `raw.githubusercontent.com`.

## Implementation

**Weekly — freshness and drift.**

```bash
kubepedia feed --upstream --journal      # new upstream tags, merged PRs, ageing verified_at
kubepedia cve                            # re-sweep every CVE matrix against osv.dev
kubepedia verify                         # component versions in the KB vs the tagged source
```

`feed --journal` appends to `reports/UPSTREAM-WATCH.md`, and the date of the last entry becomes the
starting point for the next run — the loop keeps its own place.

`cve` reports three kinds of drift: new CVEs against a version already recorded, CVEs that
disappeared, and count mismatches. Any of them means a matrix needs re-verification, not a blind
update.

**Monthly — the upstream problem layer.**

```bash
kubepedia issues --all                   # mine release notes: CVE / breaking / defects
kubepedia breaking --all                 # regenerate behaviour-change documents
kubepedia defects --all                  # regenerate defect indexes per support line
kubepedia index && kubepedia validate    # rebuild the derived index, then check
```

**When a component's version envelope moves** (a new Kubespray tag enters the base):

```bash
kubepedia cve-matrix --all               # rebuild version-filtered CVE matrices
```

### Verification

```bash
kubepedia validate                       # must end in [PASS], zero warnings
kubepedia verify                         # zero mismatches
python3 scripts/bench_search.py          # retrieval quality did not regress
```

The benchmark matters after any bulk generation: adding a large machine-generated layer can crowd
out analysed documents, and the number is the only way to notice.

### Rollback

Everything is generated into git. A bad sweep is reverted with `git revert`; no cluster state is
touched at any point.

## Known Issues

**Machine-generated layers do not replace analysis.** The defect indexes answer "was this already
fixed"; they do not explain a symptom. When a defect turns out to matter, it earns its own document
with sources, diagnostics and a remedy.

**Do not trust an unchanged answer.** A CVE matrix identical across every shipped version, or a
component reporting zero vulnerabilities, is far more likely to be a broken query than good news —
see [[CONCEPT-OSV_RECORD_PITFALLS]].

**The sweep is only as good as its component map.** `scripts/upstream_issues.py` keeps repository
paths by hand on purpose: a wrong path silently returns another project's notes.

## References

- Tooling: `scripts/kubepedia.py` and the scripts it dispatches to.
- Ageing of the envelope: [[CONCEPT-UPGRADE_HORIZON]]; security tracking:
  [[CONCEPT-SECURITY_ADVISORIES]].
