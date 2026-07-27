---
id: TROUBLE-CONTAINERD_KNOWN_CVES
type: troubleshooting
title: "containerd: known CVEs by shipped version (osv.dev)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.7.24 <=2.2.3"
verified_at: "2026-07-27"
confidence: verified
aliases:
  - containerd cve
  - containerd security
tags:
  - security
  - cve
  - containerd
sources:
  - type: docs
    path: osv.dev API (github.com/containerd/containerd)
    url: https://osv.dev/list?q=github.com/containerd/containerd
    note: "authoritative, version-filtered vulnerability data (queried per shipped version) — 1.7.x line"
  - type: docs
    path: osv.dev API (github.com/containerd/containerd/v2)
    url: https://osv.dev/list?q=github.com/containerd/containerd/v2
    note: "the 2.x module path; the unsuffixed path under-reports for 2.x versions"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# containerd: known CVEs by shipped version (osv.dev)

## Summary

osv.dev reports **9 unique CVEs** affecting the containerd versions Kubespray ships (see [COMPONENT-CONTAINERD]). Exposure does **not** drop much with newer releases: the newest indexed version **2.2.3** (Kubespray v2.31.0) is still affected by **6**, including `CVE-2026-53488` — host-root command execution triggered by pulling a crafted image. Upstream fixes exist (2.2.5 / 2.1.9 / 2.3.2); no Kubespray release ships them yet, so a pin is the only remediation today.

Counts here are **distinct advisories**. osv.dev returns one record per database (GHSA *and* GO) for the same CVE, so a raw record count is roughly double; do not read it as the number of vulnerabilities.

## Problem

Each shipped containerd version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness).

**Query the right module path.** containerd 2.x lives at the Go module `github.com/containerd/containerd/v2`; the unsuffixed `github.com/containerd/containerd` path answers only for the 1.x line. Querying the unsuffixed path for a 2.x version returns a *subset* without any error — that is exactly how this matrix previously recorded 3 CVEs for v2.28.0–v2.31.0 where there are 6–8. `scripts/cve_sweep.py` now derives the `/vN` suffix from the queried version.

## Context

| Component version | Kubespray | # CVEs | CVEs |
|---|---|---|---|
| 1.7.24 | v2.27.0 | 8 | CVE-2024-25621, CVE-2024-40635, CVE-2025-64329, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492 |
| 1.7.27 | v2.27.1 | 8 | CVE-2024-25621, CVE-2025-64329, CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492 |
| 2.0.5 | v2.28.0 | 5 | CVE-2024-25621, CVE-2025-64329, CVE-2026-46680, CVE-2026-47262, CVE-2026-53488 |
| 2.0.6 | v2.28.1 | 5 | CVE-2024-25621, CVE-2025-64329, CVE-2026-46680, CVE-2026-47262, CVE-2026-53488 |
| 2.1.4 | v2.29.0 | 8 | CVE-2024-25621, CVE-2025-64329, CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492 |
| 2.1.5 | v2.29.1 | 6 | CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492 |
| 2.2.1 | v2.30.0 | 6 | CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492 |
| 2.2.3 | v2.31.0 | 6 | CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492 |

The 1.7.x rows are queried against `github.com/containerd/containerd`, the 2.x rows against `github.com/containerd/containerd/v2`. The checkpoint trio (`CVE-2026-50195` / `CVE-2026-53489` / `CVE-2026-53492`) is recorded as introduced at 2.1.0 on the 2.x branch, so 2.0.5 / 2.0.6 are clear of it; on the 1.x branch osv records it as introduced at 0 with **no fix released**, so 1.7.24 / 1.7.27 carry it permanently.

## Diagnostics

```bash
containerd --version ; crictl version
```

## Known Issues

CVEs (id — summary — fixed in):

- **CVE-2024-25621** [CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H] — local privilege escalation via wide permissions on the CRI directory — fixed in: `1.7.29, 2.0.7, 2.1.5, 2.2.0`
- **CVE-2024-40635** [CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:L/I:L/A:N] — integer overflow in User ID handling — fixed in: `1.6.38, 1.7.27, 2.0.4`
- **CVE-2025-64329** [CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N] — CRI server: host memory exhaustion through an Attach goroutine leak — fixed in: `1.7.29, 2.0.7, 2.1.5, 2.2.0`
- **CVE-2026-46680** [CVSS:4.0/AV:L/AC:L/AT:P/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N] — user ID handling bypass allows `runAsNonRoot` evasion — fixed in: `1.7.32, 2.0.9, 2.2.4, 2.3.1` (**no 2.1.x fix** — the 2.1 line stays affected)
- **CVE-2026-47262** [CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N] — image-triggered runtime DoS via unbounded group parsing — fixed in: `1.7.33, 2.0.10, 2.1.9, 2.2.5, 2.3.2`
- **CVE-2026-50195** [CVSS:4.0/AV:N/AC:L/AT:P/PR:L/UI:N/VC:N/VI:L/VA:N/SC:H/SI:H/SA:L] — CRI checkpoint import allows local image tag poisoning — fixed in: `2.1.9, 2.2.5, 2.3.2` (1.x: unfixed)
- **CVE-2026-53488** [CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H] — an image-config `LABEL` reaches the restart-monitor `binary://` logger: **host-root command execution from an image pull** — fixed in: `1.7.33, 2.0.10, 2.1.9, 2.2.5, 2.3.2`
- **CVE-2026-53489** [CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:N/VC:H/VI:N/VA:N/SC:H/SI:N/SA:N] — arbitrary host CRI log file read via symlink following in CRI checkpoint restore — fixed in: `2.1.9, 2.2.5, 2.3.2` (1.x: unfixed)
- **CVE-2026-53492** [CVSS:4.0/AV:N/AC:L/AT:N/PR:L/UI:N/VC:N/VI:H/VA:N/SC:H/SI:H/SA:N] — CRI checkpoint restore CDI annotation smuggling — fixed in: `2.1.9, 2.2.5, 2.3.2` (1.x: unfixed)

**Recommendation:** moving to the newest Kubespray release (v2.31.0, containerd 2.2.3) does **not** clear the runtime — 6 CVEs remain, `CVE-2026-53488` among them. Containerd **2.2.5** (released 2026-06-18) fixes all six on the 2.2 line, so the remediation is to stay on Kubespray v2.31.0 and pin `containerd_version: 2.2.5` (see [[VARIABLE-CONTAINERD_VERSION]] — the default is *computed* from the newest checksum key, so it must be pinned explicitly).

That pin needs a checksum: `containerd_archive_checksums` at v2.31.0 tops out at **2.2.3** (`roles/kubespray_defaults/vars/main/checksums.yml`), so add the amd64/arm64 sha256 for 2.2.5 in your inventory before the run — otherwise the download task fails on the missing key. Then re-run the `container-engine` scope and confirm with `containerd --version` on every node. Reduce blast radius with PRACTICE-HARDENING.

## References

- osv.dev (queried per version) for `github.com/containerd/containerd` (1.7.x) and `github.com/containerd/containerd/v2` (2.x) — verified 2026-07-27.
- Component: [[COMPONENT-CONTAINERD]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].