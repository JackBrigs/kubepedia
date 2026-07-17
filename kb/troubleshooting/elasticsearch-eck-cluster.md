---
id: TROUBLE-ELASTICSEARCH_ECK_CLUSTER
type: troubleshooting
title: "ECK/Elasticsearch: stuck ApplyingChanges, watermark, OOM, master election"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.33"
component_version: ">=3.0.0 <=3.4.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - elasticsearch applyingchanges stuck
  - es flood stage watermark read-only
  - elasticsearch master not discovered
  - es oomkilled exit 137
  - eck pvc expansion stuck
tags:
  - troubleshooting
  - elasticsearch
  - eck
  - data
sources:
  - type: docs
    path: ECK common problems
    url: https://www.elastic.co/docs/troubleshoot/deployments/cloud-on-k8s/common-problems
    note: "rolling upgrade, PVC expansion, operator OOM"
  - type: docs
    path: Elasticsearch fix watermark errors
    url: https://www.elastic.co/docs/troubleshoot/elasticsearch/fix-watermark-errors
    note: "flood-stage disk watermark read-only block"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ECK_OPERATOR
---

# ECK/Elasticsearch: stuck ApplyingChanges, watermark, OOM, master election

## Summary

Real-world ECK failure modes (community-sourced): the cluster gets stuck in
**`ApplyingChanges`**, indices go read-only on a **disk watermark**, ES pods **OOMKill**, or a
**master-election** deadlock blocks recovery. ECK deliberately refuses to progress a rolling
change while the ES cluster is unhealthy — fix ES health first.

## Problem

- `Elasticsearch` phase stuck `ApplyingChanges`; pods never roll.
- Writes fail with `index has read-only-allow-delete block` / `TOO_MANY_REQUESTS/12`.
- ES pods `OOMKilled` (exit 137); or the **operator itself** OOMKills on large clusters.
- `master not discovered or elected yet`.

## Context

- Applies to ECK **3.0–3.4** managing Elasticsearch 8.x/9.x (owner runs 3.1.0 —
  [[CONCEPT-ADDON_ECK_OPERATOR]]).

## Diagnostics

- **Stuck `ApplyingChanges`:** the cluster is unhealthy (unassigned/relocating shards) so the
  operator won't delete more pods, or nodes lack memory (`0/3 nodes... Insufficient memory`).
  Check `_cluster/health` / `_cat/shards`, restore shard allocation, add capacity, wait for
  recovery (issue #2087).
- **PVC expansion wedge:** `only dynamically provisioned pvc can be resized` — set
  `allowVolumeExpansion: true` on the StorageClass; for an incompatible size, **rename the
  `nodeSet`** so ECK builds a fresh StatefulSet and migrates data (issues #7260/#4467).
- **Flood-stage watermark (read-only):** a node crossed ~95% disk. Free disk / expand PVC
  below the high watermark; modern ES auto-releases, else
  `PUT _all/_settings {"index.blocks.read_only_allow_delete": null}`.
- **Master election deadlock:** ≥half the master-eligible nodes stopped → no quorum → even the
  voting-config-exclusions API returns 503. Restore enough master-eligible nodes first
  (issue #3399).
- **OOMKilled:** default 2 GiB limit ⇒ ~1 GiB heap. Always set **explicit memory limits
  (limit == request)** in `podTemplate`; setting requests **without** limits makes the JVM
  size heap off full node memory. **Operator OOM:** raise the operator StatefulSet limit to
  2 Gi (controller-runtime caches all resources at startup).

## Known Issues

- **Upgrade ordering:** ES Stack 9.0.0 needs ECK ≥3.0.0 and must pass through 8.18
  (validation-enforced); downgrades blocked (recover via
  `eck.k8s.elastic.co/disable-downgrade-validation=true`).
- Expired **custom transport CA** causes an endless cert-rotation loop (`x509: certificate has
  expired`) — update the CA secret (issue #8952).
- Elasticsearch 8.x/9.x carry their own ESA advisories (Tika XXE ESA-2025-14, PKI-realm
  ESA-2025-27, etc.) — patch the Stack version, not just the operator.

## References

- ECK common problems + ES watermark docs (above); issues #2087/#7260/#4467/#3399/#8952.
- Addon: [[CONCEPT-ADDON_ECK_OPERATOR]].
