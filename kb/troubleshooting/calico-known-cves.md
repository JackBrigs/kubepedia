---
id: TROUBLE-CALICO_KNOWN_CVES
type: troubleshooting
title: "Calico: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=3.29.1 <=3.31.5"
verified_at: "2026-07-27"
confidence: verified
aliases:
  - calico cve
  - calico security
tags:
  - security
  - cve
  - calico
  - cni
sources:
  - type: docs
    path: osv.dev API (github.com/projectcalico/calico)
    url: https://osv.dev/list?q=github.com/projectcalico/calico
    note: "version-filtered vulnerability data, confirmed version-resolvable (3.31.6 drops two of the three)"
relations:
  - type: see_also
    target: COMPONENT-CALICO
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Calico: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **3 distinct advisories** affecting the Calico versions Kubespray ships (see
[COMPONENT-CALICO]). Exposure is **flat across the entire envelope**: every version from 3.29.1
(v2.27.0) to 3.31.5 (v2.31.0) carries all three, because two of them are first fixed in **3.31.6** —
one patch above the newest Kubespray ships — and the third has no fix at all.

Calico is the **default CNI**, so these apply to any cluster that did not explicitly choose another
plugin ([[VARIABLE-KUBE_NETWORK_PLUGIN]]).

Counts are **distinct advisories** (osv.dev returns one record per database for the same CVE).

## Problem

Each shipped Calico version carries the advisories below. Two are log-disclosure issues reachable by
any authenticated low-privilege caller; the third is a privilege-escalation report with no published
fix.

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 3.29.1 | v2.27.0 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |
| 3.29.3 | v2.27.1 / v2.28.0 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |
| 3.29.5 | v2.28.1 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |
| 3.30.3 | v2.29.0 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |
| 3.30.5 | v2.29.1 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |
| 3.30.6 | v2.30.0 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |
| 3.31.5 | v2.31.0 | 3 | CVE-2024-33522, CVE-2026-41184, CVE-2026-41185 |

The version Kubespray installs is **computed**, not pinned: it is the first key of
`calicoctl_binary_checksums` at that tag ([[CONCEPT-COMPONENT_VERSION_SELECTION]]).

## Diagnostics

```bash
kubectl -n kube-system get ds calico-node -o jsonpath='{.spec.template.spec.containers[*].image}'
calicoctl version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2024-33522** — Calico privilege-escalation report — fixed in: `—` (no published fix; osv carries only a commit range for it)
- **CVE-2026-41184** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N] — Calico inserts sensitive information into a log file — fixed in: `3.31.6`
- **CVE-2026-41185** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N] — Calico inserts sensitive information into a log file (second path) — fixed in: `3.31.6`

**Recommendation:** no Kubespray release clears these — **3.31.6 is one patch above the newest
shipped 3.31.5**. Options, in order of preference: wait for the Kubespray tag that picks up 3.31.6+
and treat it as a security upgrade; or, if the log-disclosure class matters for your threat model,
restrict read access to Calico component logs (they are the disclosure channel) and keep the
`calico-node` service account scoped ([[PRACTICE-HARDENING]]). Overriding the Calico version by hand
means adding the checksum for the target version first — the default is computed from the checksum
table, so an unlisted version fails the download task.

## References

- osv.dev (queried per version) for `github.com/projectcalico/calico` — verified 2026-07-27.
- Component: [[COMPONENT-CALICO]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
