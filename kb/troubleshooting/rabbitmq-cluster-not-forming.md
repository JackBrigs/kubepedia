---
id: TROUBLE-RABBITMQ_CLUSTER_NOT_FORMING
type: troubleshooting
title: "RabbitMQ operator: cluster not forming / pods not joining"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - rabbitmq pods not clustering
  - rabbitmq erlang cookie mismatch
  - rabbitmq quorum queue
  - rabbitmqcluster not ready
tags:
  - troubleshooting
  - rabbitmq
  - messaging
sources:
  - type: docs
    path: RabbitMQ cluster-operator troubleshooting
    url: https://www.rabbitmq.com/kubernetes/operator/troubleshooting-operator
    note: "clustering, mnesia, quorum queues"
relations:
  - type: see_also
    target: CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR
  - type: see_also
    target: CONCEPT-ADDON_RABBITMQ_BITNAMI
---

# RabbitMQ operator: cluster not forming / pods not joining

## Summary

A `RabbitmqCluster` doesn't become ready or nodes don't cluster. The usual causes are
**PVC/permissions** on the mnesia dir, **peer discovery / Erlang cookie** issues, or an unsafe
scale-down that stranded quorum.

## Problem

- `RabbitmqCluster` stuck not-ready; pods `0/1` or restarting.
- Nodes run standalone instead of clustering; `rabbitmqctl cluster_status` shows one node.
- Quorum queues unavailable after losing nodes.

## Context

- Applies to the official operator ([[CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR]]) and the
  Bitnami-packaged one ([[CONCEPT-ADDON_RABBITMQ_BITNAMI]]).

## Diagnostics

1. `kubectl describe rabbitmqcluster <name>` + pod logs — mnesia/startup errors.
2. **PVC / mnesia dir:** permission-denied on the data dir at startup is a common block — check
   `fsGroup`/security context and that the PVC bound.
3. **Peer discovery / Erlang cookie:** all nodes must share the Erlang cookie (Secret) and use
   the K8s peer-discovery; a headless-service/DNS problem prevents joining.
4. **Quorum after scale-down:** the operator has **no `forget_cluster_node`** — removing nodes
   can strand quorum queues. Restore the removed members or follow the manual forget procedure;
   don't scale down below quorum.
5. **Feature flags on upgrade:** moving the broker to 3.12+/4.x requires the prior version's
   feature flags enabled first.

## Known Issues

- Bitnami chart 3.7.0 images moved to `bitnamilegacy` → `ImagePullBackOff` if not repointed;
  its broker 3.11.21 has CVE-2023-46118. Official operator's default broker 4.x has its own
  3→4 constraints.

## References

- RabbitMQ operator troubleshooting (above); official:
  [[CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR]]; Bitnami: [[CONCEPT-ADDON_RABBITMQ_BITNAMI]].
