---
id: TROUBLE-KYVERNO_REPORTS_ETCD_SCALE
type: troubleshooting
title: "Kyverno: reports/UpdateRequests flood etcd (read-only / OOM)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.10.0 <=1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kyverno reports controller oom
  - kyverno admission reports etcd full
  - kyverno updaterequests flood
  - kyverno policyreport scale
tags:
  - troubleshooting
  - kyverno
  - etcd
  - scale
  - policy
sources:
  - type: docs
    path: kyverno issue #8974 (admission reports → etcd read-only)
    url: https://github.com/kyverno/kyverno/issues/8974
    note: "~1.6M reports, ~9.4GB etcd, quota breached"
  - type: docs
    path: kyverno issue #10049 (UpdateRequests flood, etcd OOM)
    url: https://github.com/kyverno/kyverno/issues/10049
    note: "background controller OOM crashloop → UR pileup"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: TROUBLE-ETCD_DB_SPACE_EXCEEDED
---

# Kyverno: reports/UpdateRequests flood etcd (read-only / OOM)

## Summary

At scale, Kyverno's **reports-controller** and **background-controller** can generate huge
numbers of PolicyReport / admission-report / UpdateRequest objects, overloading the API server
and **etcd** — up to flipping etcd **read-only** (quota breach) or OOM-crashing it.

## Problem

- reports-controller floods the apiserver with expensive `List` calls; heavy etcd load
  (worse with many namespaces).
- etcd hits its quota and goes read-only (writes fail cluster-wide).
- Background controller OOM-crashloops; `UpdateRequest` count explodes.

## Context

- Applies to Kyverno **1.10–1.18** at scale ([[CONCEPT-ADDON_KYVERNO]]). etcd-full generic
  handling: [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]].

## Diagnostics

- **Count the objects:** `kubectl get policyreports,clusterpolicyreports -A | wc -l`,
  `kubectl get updaterequests -n kyverno | wc -l`, and admission/ephemeral reports. Millions
  of them is the tell.
- **etcd read-only from admission reports:** ~1.6M report objects consumed ~9.4 GB etcd and
  breached an 8 GB quota (issue #8974). Kyverno **1.10+** ships cron jobs to auto-delete
  reports past a threshold — ensure they run; manually purge the backlog; then compact/defrag
  etcd and disarm the alarm ([[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]).
- **UpdateRequest flood:** a background-controller OOM crashloop stops deleting URs while
  admission keeps creating them (700k+ observed) → etcd OOM (issue #10049). **Give the
  background controller enough memory**, purge the URs (fixed by PR #10793 in **1.13**).
- **Expensive Lists:** the reports-controller historically omitted `ResourceVersion: "0"`,
  forcing direct etcd reads instead of the watch cache (issue #8005, fixed toward 1.11) —
  upgrade if on an affected version.
- **GlobalContextEntry memory:** caching large resource sets (e.g. all nodes) OOMs the
  admission controller — narrow what it caches, raise limits (issue #11693).

## Known Issues

- **1.12.0 specifically** has ephemeralreports/etcd-growth bugs — upgrade straight to
  **1.12.4+**.

## References

- kyverno issues #8974/#10049/#8005/#11693 (above); etcd space:
  [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]; addon: [[CONCEPT-ADDON_KYVERNO]].
