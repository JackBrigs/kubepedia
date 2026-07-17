---
id: CONCEPT-KUBESPRAY_ETCD_OWNERSHIP
type: concept
title: "Who owns etcd in Kubespray — host role vs kubeadm-managed"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - etcd_deployment_type host
  - etcd_kubeadm_enabled
  - kubespray etcd not kubeadm
  - stacked vs external etcd kubespray
  - who upgrades etcd kubespray
tags:
  - kubespray
  - etcd
  - kubeadm
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "etcd_deployment_type: host (default)"
  - type: code
    path: roles/etcd/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/etcd/tasks
    note: "Kubespray's own etcd role (host binaries / systemd)"
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
---

# Who owns etcd in Kubespray — host role vs kubeadm-managed

## Summary

A common misconception: "kubeadm manages etcd". In **Kubespray, by default it does not**. The
default **`etcd_deployment_type: host`** means Kubespray runs etcd as its **own** role — host
binaries under systemd, with its own certs/config and its own upgrade path — **not** as a
kubeadm-stacked static pod. kubeadm only owns etcd when you opt into `etcd_kubeadm_enabled`. This
changes which docs/commands apply for etcd upgrade, backup, and restore.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Clarifies the seam
  ([[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]): most of the control plane is kubeadm's, but **etcd is
  usually Kubespray's**.

## Implementation

**Default — `etcd_deployment_type: host` (Kubespray owns etcd):**

- etcd runs as a **systemd service** from host binaries (the `etcd` role), typically on the
  `etcd` inventory group (can be co-located with control-plane nodes).
- **Kubespray** generates the etcd PKI, config, and peer/client setup; **Kubespray** upgrades
  etcd (the `etcd` role installs the new binary), and backup/restore uses `etcdctl snapshot` /
  the Kubespray recovery tooling — **not** `kubeadm upgrade`.
- kubeadm's `kubeadm-config.yaml` points at this etcd as **external** endpoints.

**Opt-in — `etcd_kubeadm_enabled: true` (kubeadm-managed, stacked):**

- etcd runs as a **kubeadm static pod**; then `kubeadm upgrade` (`init phase etcd local`) does
  own the etcd upgrade, and etcd shares the control-plane node lifecycle.

**Other `etcd_deployment_type` values** (e.g. `kubeadm`, `docker`) select the same
host-vs-static distinction — confirm the value in your inventory before assuming who upgrades
etcd.

## Compatibility

- **Practical impact:** for the default host etcd, **don't** expect `kubeadm upgrade apply` to
  bump etcd — Kubespray's etcd role does it. Backup/restore, defrag, and quorum recovery are all
  operated against the **host etcd** ([[TROUBLE-ETCD_QUORUM_LOSS]],
  [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]).
- The `kubeadm init phase etcd local` step in `kubeadm-upgrade.yml` only meaningfully applies
  when etcd is kubeadm-managed.

## References

- `etcd_deployment_type` default + `etcd` role (v2.31.0, above); seam:
  [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; component: [[COMPONENT-ETCD]]; quorum:
  [[TROUBLE-ETCD_QUORUM_LOSS]].
