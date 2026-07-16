---
id: PRACTICE-UPGRADE_PREFLIGHT
type: best_practice
title: Pre-upgrade checklist (Kubespray)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - pre-upgrade checklist
  - upgrade readiness
tags:
  - operations
  - upgrade
  - diagnostics
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "upgrade procedure; checklist is derived operational practice"
relations:
  - type: see_also
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: PRACTICE-ETCD_BACKUP_RESTORE
---

# Pre-upgrade checklist (Kubespray)

## Summary

A short readiness checklist to run before a Kubespray upgrade, so the graceful
per-node upgrade ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]) does not stall or lose data.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Upgrade **one Kubespray minor at a
  time** (patch releases may be skipped).

## Diagnostics

Before upgrading, confirm:

```bash
# 1. cluster is healthy NOW (do not upgrade a broken cluster)
kubectl get nodes; kubectl get pods -A | grep -vE 'Running|Completed'

# 2. etcd is healthy and BACKED UP  (see PRACTICE-ETCD_BACKUP_RESTORE)
etcdctl endpoint health; etcdctl snapshot save /var/backups/pre-upgrade.db

# 3. certificates are not about to expire
kubeadm certs check-expiration

# 4. you are moving exactly one Kubespray minor (check out the next tag)
git -C kubespray describe --tags
```

## Implementation

Checklist:
- ✅ **One minor at a time** — no skipping Kubespray minors.
- ✅ **etcd snapshot** taken and stored off-node.
- ✅ **Cluster healthy** — all nodes Ready, no crashlooping system pods.
- ✅ **Certs valid** for the upgrade window.
- ✅ **Spare capacity** to drain nodes (graceful upgrade cordons/drains).
- ✅ **Review breaking changes** for the target release
  ([[RELEASE-V2_31_0]] etc.) and any **API removals**
  ([[CONCEPT-K8S_API_REMOVALS]]) / removed **feature gates**
  ([[CONCEPT-K8S_FEATURE_GATES]]) that your manifests/flags use.
- ✅ **`serial`** set appropriately (default 20%; `serial=1` for the most
  cautious rollout).
- ✅ **Inventory `kube_version`** either unset (uses the tag default) or updated
  to the target.

## References

- `docs/operations/upgrades.md`; [[UPGRADE-KUBESPRAY_SEQUENTIAL]].
