---
id: CONCEPT-ADDON_VM_K8S_STACK
type: concept
title: "victoria-metrics-k8s-stack (vm) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.115.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - vm
  - victoria-metrics-k8s-stack
  - victoriametrics stack
  - vm 0.42.0
tags:
  - addons
  - observability
  - metrics
  - victoriametrics
sources:
  - type: code
    path: charts/victoria-metrics-k8s-stack/Chart.yaml
    url: https://raw.githubusercontent.com/VictoriaMetrics/helm-charts/victoria-metrics-k8s-stack-0.42.0/charts/victoria-metrics-k8s-stack/Chart.yaml
    note: "kubeVersion >=1.25.0-0; appVersion v1.115.0"
  - type: docs
    path: vm-k8s-stack changelog
    url: https://docs.victoriametrics.com/helm/victoriametrics-k8s-stack/changelog/
    note: "0.42.0 = VM bump to v1.115.0"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# victoria-metrics-k8s-stack (vm) — addon

## Summary

The VictoriaMetrics Kubernetes monitoring stack, chart **0.42.0** → VM components
**v1.115.0** (vmagent/vmalert/vmsingle etc. via the VM operator). It is the owner's primary
metrics stack; deeper operational guidance is in [[CONCEPT-OBSERVABILITY_STACK]].

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].
- **Inventory-listing caveat:** the sub-versions listed in the inventory (vmalert 0.17.0,
  grafana-operator v5.18.0, oauth2-proxy 8.1.0, helm-exporter 1.2.16) are **not** chart
  0.42.0 dependencies — that chart's dependencies are the VM operator `0.44.*`,
  kube-state-metrics `5.31.*`, prometheus-node-exporter `4.44.*`, grafana `8.9.*`. Those
  extra sub-versions are likely local values/overrides, not shipped by this chart.

## Implementation

- Chart→app: `victoria-metrics-k8s-stack-0.42.0` → VM **v1.115.0** (released 2025-04-07).
- Chart `kubeVersion`: **`>=1.25.0-0`** (floor only; covers 1.29–1.35).
- 0.42.0 is only a VM version bump to v1.115.0 — no documented breaking changes.

## Configuration

- **`helm upgrade` does NOT upgrade CRDs.** VM CRD updates must be applied manually with
  `kubectl` — the recurring cause of CRD drift after a chart bump. Track CRD versions
  separately from the chart.

## Compatibility

- **Kubernetes range:** no explicit upstream matrix (**unverified** upper bound); the only
  machine-readable bound is `>=1.25`. Functions across 1.29–1.35.
- **CVE:** **CVE-2025-65942 / GHSA-66jq-2c23-2xh5** — Snappy decoder DoS/OOM, Low
  (CVSS 2.7), affects VM 1.111.0–<1.122.8 (**includes 1.115.0**), fixed in **1.122.8**.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Open upstream bugs (as of 2026-07-19), VictoriaMetrics ~1.147:**
- **vmstorage background merge has no self memory limit → OOM-killer** under heavy merges (#10203) — size memory / limit ingestion accordingly.
- **vmbackup does not retry S3 `429 TooManyRequests`** — backup fails immediately on rate-limit (#11218).
- multitenant queries with `or` combine tenant + non-tenant filters incorrectly → extra series (#10948).
- unclean shutdown / power loss can corrupt metadata files and block restart (#5012) — ensure clean shutdown / durable storage.

## Older-version CVEs & security history (mined 2026-07-19)

For clusters on an **older** VictoriaMetrics:
- **CVE-2026-61625** (Medium): **path traversal in `vmrestore`** — crafted backup part names escape the restore root; fixed **1.146.0 / 1.136.12 / 1.122.25**.
- **CVE-2025-65942** (Low): Snappy decoder allows malformed blocks to trigger **excessive memory** consumption; fixed **1.129.1 / 1.122.8 / 1.110.23**. Older VM images in the envelope are affected.

## Guides & how-to (official)

- **Docs:** https://docs.victoriametrics.com/helm/victoriametrics-k8s-stack/ ; **VM operator:** https://docs.victoriametrics.com/operator/
- **How to upgrade:** `helm upgrade` the `victoria-metrics-k8s-stack` chart; read the chart's **upgrade notes** (CRD/operator changes between majors); upgrade the VM operator CRDs as directed. Patch off vmrestore/snappy CVEs (see CVE section).
## References

- `Chart.yaml` + upstream changelog (above); advisory GHSA-66jq-2c23-2xh5.
- Observability hub: [[CONCEPT-OBSERVABILITY_STACK]]; catalog: [[CONCEPT-ADDON_CATALOG]].
