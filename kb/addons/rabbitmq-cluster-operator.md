---
id: CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR
type: concept
title: "RabbitMQ Cluster Operator (official) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.32"
component_version: "4.1.3"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rabbitmq-cluster-operator
  - rabbitmq official operator
  - rabbitmq operator v2.19.2
tags:
  - addons
  - messaging
  - rabbitmq
sources:
  - type: docs
    path: RabbitMQ operator install (supported K8s)
    url: https://www.rabbitmq.com/kubernetes/operator/install-operator
    note: "tested K8s v1.29–v1.32, minimum 1.31"
  - type: docs
    path: cluster-operator v2.19.2 README/release
    url: https://github.com/rabbitmq/cluster-operator/releases/tag/v2.19.2
    note: "deploys RabbitMQ 4.1.3; startup probe added; Go 1.25.8"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_RABBITMQ_BITNAMI
---

# RabbitMQ Cluster Operator (official) — addon

## Summary

The official RabbitMQ **cluster-operator** **v2.19.2** (kustomize install), which deploys
**RabbitMQ 4.1.3** by default. Officially tested on Kubernetes **v1.29–v1.32** with a
**minimum of 1.31**. Distinct from the Bitnami chart of a similar name
([[CONCEPT-ADDON_RABBITMQ_BITNAMI]]).

## Context

- Class: upstream addon; `rabbitmq-cluster-operator` row in [[CONCEPT-ADDON_CATALOG]].
  Installed via kustomize, not Helm.

## Implementation

- Operator **v2.19.2** → default broker **RabbitMQ 4.1.3**. Rebuilt with Go 1.25.8 to
  resolve stdlib CVEs; a new RabbitMQ startup probe was added (changes startup/readiness).

## Configuration

- Pause reconciliation before operator upgrades (rolling StatefulSet update).
- The default broker is **4.x** — clusters not pinning `spec.image` move onto 4.x, which has
  its own 3.x→4.x constraints (feature-flag / classic-mirrored-queue removal). Pin
  `spec.image` to control this.
- **Do not naively scale down** — the operator has no `forget_cluster_node`, so removing
  nodes can strand quorum.

## Compatibility

- **Kubernetes range:** tested **v1.29–v1.32**, minimum **1.31**. Within 1.29–1.35: only
  **1.31–1.32** are inside the tested+supported window; 1.29–1.30 are below the minimum;
  1.33–1.35 are **untested**.
- **CVEs:** operator itself none found. Default broker **4.1.3**: CVE-2026-44839 (mgmt-UI XSS)
  was fixed in 4.1.2 → **not** affected; **CVE-2026-57211** (Windows-only SSRF/UNC via mgmt
  static handler, fixed 4.1.11) → **4.1.3 affected on Windows nodes** (bump image ≥4.1.11).
- **Known issues:** unsafe scale-down (#223); PVC ownership/permission-denied on the mnesia
  dir (#1363); NodePort churn with custom port overrides (#826).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond the pinned operator (from upstream releases):
- **⚠ 2.22.0 breaking:** introduces an **HTTP startup probe that requires RabbitMQ 4.2.4+ / 4.3.0+**. For older RabbitMQ, set the annotation **`rabbitmq.com/legacy-startup-probe: "true"`** or the pods fail their startup probe.
- **Every operator upgrade triggers a rolling update of the underlying StatefulSets** — **pause cluster reconciliation** before upgrading the operator, then resume, to control the roll.
- 2.22.1 fixes a metrics-certificate secret collision; 2.21.x improves imagePullSecrets handling.

## References

- Install/supported-K8s doc, v2.19.2 release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Bitnami variant: [[CONCEPT-ADDON_RABBITMQ_BITNAMI]].
