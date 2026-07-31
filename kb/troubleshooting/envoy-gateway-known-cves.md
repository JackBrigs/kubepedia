---
id: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
type: troubleshooting
title: "Envoy Gateway: known CVEs across all releases"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <=1.8.3"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway cve
  - envoy gateway security
  - envoy gateway lua rce
  - envoy gateway admin interface exposed
  - gateway api controller vulnerabilities
tags:
  - security
  - cve
  - envoy
  - gateway-api
sources:
  - type: code
    path: envoyproxy/gateway release-notes/*.yaml — "security updates" sections of all 62 releases
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "upstream structured notes; authoritative for which patch carries which fix, per maintenance branch"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_1_6_KNOWN_ISSUES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Envoy Gateway: known CVEs across all releases

## Summary

Twelve advisories are named across the project's history, in **64 security updates** spanning 62
releases. They land in three different places, and that distinction decides how exposed a cluster
actually is:

- **the controller's own code** — Lua execution, admin-interface exposure, log injection, ext_proc
  handling;
- **the Envoy proxy image** the controller deploys — data-plane exposure, reachable from client
  traffic;
- **Go dependencies and the toolchain** compiled into the controller.

Upstream backports across maintenance branches, so the same CVE appears with a different fix version
per line: `CVE-2026-22771` is fixed in **1.5.7** and **1.6.2**, `CVE-2026-33186` in **1.6.7** and
**1.7.3**.

## Problem

Each row is the version that first carries the fix on that branch. A cluster below that version on
the same line is affected.

## Context

| CVE | What it is | Fixed in |
|---|---|---|
| **CVE-2025-24030** | Envoy **admin interface exposed** through the Prometheus stats endpoint | 1.2.6 |
| **CVE-2025-25294** | **log injection** via the default access log | 1.2.7, 1.3.1 |
| **CVE-2025-30157** | local replies incorrectly sent to the **ext_proc** server | 1.2.8 |
| **CVE-2025-58058** | Go module `xz` | 1.4.4 |
| **CVE-2025-64527** | Envoy proxy (data plane), bundled 1.36.3 | 1.5.6, 1.6.1 |
| **CVE-2025-66220** | Envoy proxy (data plane), bundled 1.36.3 | 1.5.6, 1.6.1 |
| **CVE-2025-64763** | Envoy proxy (data plane), bundled 1.36.3 | 1.5.6, 1.6.1 |
| **CVE-2026-22771** | **arbitrary code execution through `EnvoyExtensionPolicy` Lua scripts** | 1.5.7, 1.6.2 |
| **CVE-2025-0913** | Envoy proxy (data plane), bundled 1.36.4 | 1.6.3 |
| **CVE-2026-33186** | **Critical — gRPC-Go authorization bypass via a non-canonical HTTP/2 `:path` header** | 1.6.7, 1.7.3 |
| **CVE-2026-24051** | High — OpenTelemetry Go SDK path hijacking, **macOS/Darwin only** (no exposure on Linux nodes) | 1.6.7, 1.7.3 |
| **CVE-2026-47774** | Envoy proxy (data plane), bundled 1.37.3 | 1.7.4 |

Unnumbered security work is frequent on top of this: Go toolchain bumps (1.25.6 / 1.25.7 / 1.25.8
for `go` and `crypto/tls`), Envoy proxy bumps (1.36.3 → 1.36.4 → 1.36.5 → 1.37.3) and rate-limit
image bumps. Staying on the newest patch of a line picks these up without a minor upgrade.

## Diagnostics

```bash
# control plane version
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'

# data plane — carries the Envoy CVEs and is upgraded by rolling the proxy Deployments
kubectl -n <eg-ns> get pods -l app.kubernetes.io/name=envoy \
  -o jsonpath='{range .items[*]}{.spec.containers[*].image}{"\n"}{end}' | sort -u

# is the Lua execution path in use at all?
kubectl get envoyextensionpolicy -A
```

## Known Issues

**Two images, one release.** The controller and the proxy ship together, but a proxy pod keeps its
old image until its Deployment is rolled. After upgrading the controller, confirm the proxies
actually restarted — otherwise the data-plane advisories stay open while the reported version says
they are closed.

**Patch, don't jump.** Every advisory here is closed within a maintenance line, so the cheap and
low-risk remediation is the newest patch of the line already in use — the Gateway API CRD contract
does not shift the way it does on a minor upgrade. Read
[[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] first: patch releases 1.6.4, 1.6.6, 1.8.1, 1.8.2 and
1.8.3 each carry a behaviour change despite being patches.

## References

- Upstream `release-notes/*.yaml`, `security updates` sections of all 62 releases, read at
  `origin/main` on 2026-07-31.
- Defects on the 1.6 line: [[TROUBLE-ENVOY_GATEWAY_1_6_KNOWN_ISSUES]]; behaviour changes:
  [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]]; add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
