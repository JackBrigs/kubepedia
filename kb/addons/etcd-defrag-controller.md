---
id: CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER
type: concept
title: "etcd-defrag-controller — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.0.7"
verified_at: "2026-07-17"
confidence: probable
aliases:
  - etcd-defrag-controller
  - etcd defrag
tags:
  - addons
  - etcd
  - maintenance
sources:
  - type: code
    path: helm/charts/etcd-defrag-controller/Chart.yaml
    url: https://raw.githubusercontent.com/kaasops/etcd-defrag-controller/v0.0.7/helm/charts/etcd-defrag-controller/Chart.yaml
    note: "kaasops project; chart==app v0.0.7; no kubeVersion"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd-defrag-controller — addon

## Summary

`etcd-defrag-controller` (**kaasops/etcd-defrag-controller**, chart/app **v0.0.7**) automates
etcd defragmentation, which reclaims space after compaction. It is a small,
effectively-undocumented project — most engineering detail is `unverified`.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Relates to cluster etcd
  ([[COMPONENT-ETCD]]).
- Upstream is `kaasops/etcd-defrag-controller` (not the unrelated `ahrtr/etcd-defrag` CLI nor
  the `christianhuth` CronJob chart).

## Implementation

- Chart==app **v0.0.7**, image `kaasops/etcd-defrag-controller`. Chart `kubeVersion`:
  **none**. `go.mod` targets Go 1.18.

## Configuration

- Defragmentation locks the etcd member briefly — schedule it to run one member at a time,
  off-peak, to avoid latency spikes / quorum risk ([[TROUBLE-ETCD_QUORUM_LOSS]]).

## Compatibility

- **Kubernetes range:** **unverified** — empty README, no release notes, no compat statement.
  Assumed workable across 1.29–1.35 (it talks to etcd, not the K8s API server) but not
  declared — hence `confidence: probable`.
- **CVEs:** none found (not in OSV, no GHSA).

## References

- kaasops/etcd-defrag-controller `Chart.yaml` (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; etcd: [[COMPONENT-ETCD]].
