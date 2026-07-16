---
id: TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025
type: troubleshooting
title: "runc container escape (CVE-2025-31133 et al.) affects Kubespray v2.29.0"
status: active
kubespray_version: v2.29.0
kubernetes_version: null
component_version: "1.3.2"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - CVE-2025-31133
  - CVE-2025-52565
  - CVE-2025-52881
  - runc container escape
tags:
  - security
  - cve
  - runc
sources:
  - type: docs
    path: NVD CVE-2025-31133
    url: https://nvd.nist.gov/vuln/detail/CVE-2025-31133
    note: "affected <1.2.8, >=1.3.0-rc.1 <1.3.3, 1.4.0-rc.1/2; fixed 1.2.8/1.3.3/1.4.0-rc.3; CVSS 7.8 HIGH"
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Kubespray v2.29.0 ships runc 1.3.2 (verified from tag)"
relations:
  - type: see_also
    target: COMPONENT-RUNC
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# runc container escape (CVE-2025-31133 et al.) affects Kubespray v2.29.0

## Summary

The November 2025 runc advisories — **CVE-2025-31133** (verified, CVSS 7.8 HIGH),
and the coordinated **CVE-2025-52565** / **CVE-2025-52881** — allow container
escape via mount races (masked-path / `/dev/console` / procfs write redirects).
They are fixed in runc **1.2.8, 1.3.3, and 1.4.0-rc.3**. **Kubespray `v2.29.0`
ships runc `1.3.2`, which is affected.** Later indexed releases are not.

## Problem

A malicious container image/config can exploit runc mount handling to escape to
the host. runc `1.3.2` falls in the affected range `>=1.3.0-rc.1 <1.3.3`.

## Context

- **Affected:** Kubespray `v2.29.0` (runc `1.3.2`).
- **Not affected:** `v2.29.1` / `v2.30.0` (runc `1.3.4` ≥ 1.3.3) and `v2.31.0`
  (runc `1.4.2`). See [[COMPONENT-RUNC]].
- CVE-2025-31133 verified against NVD; the two coordinated CVEs were fixed in the
  same runc releases.

## Diagnostics

```bash
# on each node, check the installed runc version
runc --version            # runc version 1.3.2 -> AFFECTED; >=1.3.3 or 1.4.x -> fixed
crictl info | grep -i runc
```

## Known Issues

- Root cause: runc mount-race gadgets (masked paths, `/dev/console`, procfs write
  redirects). Fixed in runc `1.2.8` / `1.3.3` / `1.4.0-rc.3`.
- **Fix / mitigation:** upgrade runc to `≥1.3.3`. On Kubespray this means moving
  off `v2.29.0` (→ `v2.29.1`+, runc `1.3.4`), or pinning `runc_version` to a fixed
  release and re-running the `container-engine` role. As always, only run trusted
  images and enforce least-privilege (drop CAPs, no privileged pods) to reduce
  blast radius.

## References

- NVD CVE-2025-31133 (https://nvd.nist.gov/vuln/detail/CVE-2025-31133) — verified.
- Coordinated: CVE-2025-52565, CVE-2025-52881 (same fix releases).
- Kubespray runc mapping: [[COMPONENT-RUNC]] (v2.29.0 → 1.3.2, v2.29.1 → 1.3.4,
  v2.31.0 → 1.4.2).
