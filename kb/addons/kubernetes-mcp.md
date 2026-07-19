---
id: CONCEPT-ADDON_KUBERNETES_MCP
type: concept
title: "kubernetes-mcp-server (+ open-webui) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.0.56"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubernetes-mcp
  - kubernetes-mcp-server
  - open-webui
tags:
  - addons
  - ai
  - mcp
  - security
sources:
  - type: code
    path: charts/kubernetes-mcp-server/Chart.yaml
    url: https://raw.githubusercontent.com/containers/kubernetes-mcp-server/main/charts/kubernetes-mcp-server/Chart.yaml
    note: "containers/kubernetes-mcp-server; chart 0.1.0 pins app 0.0.56"
  - type: docs
    path: open-webui CVE-2026-54017
    url: https://osv.dev/vulnerability/PYSEC-2026-2751
    note: "open-webui app 0.9.5 vulnerable, fixed 0.9.6"
relations:
  - type: see_also
    target: TROUBLE-KUBERNETES_MCP
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# kubernetes-mcp-server (+ open-webui) — addon

## Summary

`kubernetes-mcp-server` exposes cluster operations to LLMs via the Model Context Protocol;
paired with **open-webui** (chart 14.6.0) as the chat UI. Chart 0.1.0 → mcp-server app
**0.0.56** (pre-1.0). **Security:** the paired open-webui chart 14.6.0 ships app **0.9.5**,
which is CVE-vulnerable.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Upstream is
  **containers/kubernetes-mcp-server** (maintainer manusa).

## Implementation

- mcp-server chart 0.1.0 → app **0.0.56** (git Chart.yaml `appVersion: latest` is a
  placeholder; the released chart pins 0.0.56; current upstream app 0.0.65). Chart
  `kubeVersion`: **none**. OCI chart needs Helm ≥3.8.
- open-webui chart **14.6.0** → app **0.9.5**; optional subcharts ollama/pipelines/tika/terminals.

## Configuration

- **Pin `image.tag`** — the floating `latest` tag on mcp-server is a reproducibility risk, and
  pre-1.0 tool surface changes across patches.
- The mcp-server grants an LLM cluster access — scope its RBAC tightly and treat it as a
  privileged client.

## Compatibility

- **Kubernetes range:** neither chart declares `kubeVersion` (**unverified**); works across
  1.29–1.35 in practice.
- **open-webui CVE — app 0.9.5 is vulnerable:** **CVE-2026-54017 / PYSEC-2026-2751** (High,
  CVSS 7.7, terminal-server path traversal/SSRF), affects ≤0.9.5, **fixed 0.9.6**; a residual
  GHSA-frvj-c5qp-xj4w affects even 0.9.6. Ship open-webui ≥0.9.6. mcp-server itself: no CVEs
  found.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **0.0.56** — **pre-1.0, breaking changes on nearly every bump** (from upstream releases):
- **0.0.63 breaking:** `PodsExec` now returns **separate stdout/stderr** (parsers expecting combined output break); switched to contextual logging; adds **token pass-through auth mode** and output-schema support.
- 0.0.64/0.0.65: target-specific tool filtering, structured content, NetObserv toolset. Pin exactly and re-test on every upgrade; treat the RBAC of its ServiceAccount as a security boundary ([[TROUBLE-KUBERNETES_MCP]]).

## Older-version CVEs & security history (mined 2026-07-19)

kubernetes-mcp-server is **pre-1.0** with no formal CVE stream, but its security surface is real: it acts as its **ServiceAccount**, so an over-privileged SA on **any** version (old or new) is the dominant risk — treat RBAC as the boundary. Older versions also lack later auth modes (token pass-through) and the PodsExec stdout/stderr split. Pin exactly and minimize SA RBAC.

## References

- kubernetes-mcp-server `Chart.yaml`, open-webui advisory PYSEC-2026-2751 (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
