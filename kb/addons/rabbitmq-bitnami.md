---
id: CONCEPT-ADDON_RABBITMQ_BITNAMI
type: concept
title: "RabbitMQ (Bitnami cluster-operator chart) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "2.4.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rabbitmq bitnami
  - rabbitmq-cluster-operator bitnami
  - rabbitmq chart 3.7.0
tags:
  - addons
  - messaging
  - rabbitmq
sources:
  - type: code
    path: bitnami/rabbitmq-cluster-operator/Chart.yaml
    url: https://raw.githubusercontent.com/bitnami/charts/rabbitmq-cluster-operator/3.7.0/bitnami/rabbitmq-cluster-operator/Chart.yaml
    note: "kubeVersion >=1.19.0-0; appVersion 2.4.0 (operator); broker 3.11.21"
  - type: docs
    path: Bitnami catalog migration
    url: https://github.com/bitnami/charts/issues/35164
    note: "images moved to docker.io/bitnamilegacy (2025-08)"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR
---

# RabbitMQ (Bitnami cluster-operator chart) — addon

## Summary

RabbitMQ via the **Bitnami** `rabbitmq-cluster-operator` chart **3.7.0**. **Two serious
caveats:** (1) chart 3.7.0 is old (2023) and ships operator **2.4.0** + broker **3.11.21**;
(2) since 2025-08 Bitnami moved versioned images to `docker.io/bitnamilegacy` (frozen), so
this chart's pinned images **no longer pull** from the free `docker.io/bitnami` namespace →
`ImagePullBackOff` unless repointed.

## Context

- Class: upstream addon; `rabbitmq` row in [[CONCEPT-ADDON_CATALOG]]. **Distinct** from the
  official RabbitMQ operator [[CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR]] (both confusingly
  called "cluster-operator").

## Implementation

- Chart→app (chart≠app): `rabbitmq-cluster-operator-3.7.0` → operator **2.4.0**, bundles
  broker **3.11.21** (Bitnami downpin), Messaging Topology Operator 1.12.0.
- Chart `kubeVersion`: **`>=1.19.0-0`** (floor only).

## Configuration

- **Repoint images** to `bitnamilegacy/*` (or Bitnami Secure Images) or installs fail with
  `ImagePullBackOff` after the 2025-09 public-catalog deletion.
- Pause reconciliation before operator upgrades — they trigger a rolling update of managed
  RabbitMQ StatefulSets. Moving the broker to 3.12.x requires being on 3.11.18+ first with
  all feature flags enabled.

## Compatibility

- **Kubernetes range:** chart nominally allows 1.29–1.35 (no upper cap) but operator 2.4.0
  (2023-07) **predates 1.29** and was never tested against it (**unverified**).
- **CVE:** bundled broker **3.11.21 is vulnerable to CVE-2023-46118 / GHSA-w6cq-9cf4-gqpg**
  (HTTP API missing body limit → authenticated DoS/OOM; 3.11.0–3.11.23, patched 3.11.24).
  Operator binary itself: none found.
- **Known issues:** `ImagePullBackOff` post-migration; Erlang inter-node/hostname resolution
  on multi-node; broker rolling-restart disruption without pausing reconciliation.

## Upstream issues & upgrade notes (mined 2026-07-19)

**⚠⚠ CRITICAL — Bitnami catalog deprecation (effective 2025-08-28, bitnami/charts #35164):** Bitnami moved most free container images to a frozen **`docker.io/bitnamilegacy`** repo (no further updates), and the paid **Bitnami Secure Images** replaced the public catalog. **RabbitMQ was left out of the secure catalog** — so this chart **breaks when it tries to pull images that no longer exist** at the old paths. Deployments pinned to `docker.io/bitnami/rabbitmq:<tag>` will fail on new pulls.
- **Fix / migrate:** move to the **RabbitMQ Cluster Operator** ([[CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR]]) or a maintained chart, mirror the needed legacy images before they rot, or subscribe to Bitnami Secure Images. Treat this chart as **end-of-free-life**.

## References

- `Chart.yaml`, Bitnami migration issue #35164, RabbitMQ GHSA-w6cq-9cf4-gqpg (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; official operator: [[CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR]].
