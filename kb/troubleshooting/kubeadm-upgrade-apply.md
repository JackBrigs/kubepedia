---
id: TROUBLE-KUBEADM_UPGRADE_APPLY
type: troubleshooting
title: "kubeadm upgrade apply/node fails (config, etcd, addons, certs)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubeadm upgrade apply failed
  - kubeadm upgrade node failed
  - error execution phase addon
  - kubeadm config migrate
  - field is immutable kubeadm upgrade
tags:
  - troubleshooting
  - kubeadm
  - upgrade
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    note: "upgrade apply/node + init phase upload-config/kube-proxy/etcd/control-plane"
  - type: docs
    path: kubeadm upgrade guide
    url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK
  - type: see_also
    target: CONCEPT-K8S_API_REMOVALS
---

# kubeadm upgrade apply/node fails (config, etcd, addons, certs)

## Summary

`kubeadm upgrade apply` (primary CP) or `kubeadm upgrade node` (secondaries) fails before the
health check — on **config migration**, an **unsupported version jump**, **etcd**, an **addon
re-apply**, or **cert renewal**. Kubespray then re-applies phases (`init phase
upload-config/kube-proxy/etcd/control-plane`).

## Problem

- `kubeadm upgrade apply` returns non-zero; `error execution phase …`; config/addon errors.
- `kube-proxy`/`coredns`/etcd re-apply step fails; certs not renewed.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray's
  `kubeadm-upgrade.yml` runs `upgrade apply/node`, then `kubeadm init phase upload-config all`,
  `addon kube-proxy`, `etcd local`, `control-plane all` (some with retries).

## Diagnostics

- **Config migration / immutable fields:** kubeadm may need the ClusterConfiguration migrated to
  the target's API version ([[CONCEPT-KUBEADM_CONFIG]]). Kubespray **tolerates** `field is
  immutable` (`failed_when: rc != 0 and "field is immutable" not in stderr`) — that specific
  error is expected on re-render; other config errors are real.
- **Unsupported version jump:** kubeadm refuses to skip a minor — [[TROUBLE-KUBEADM_VERSION_SKEW]].
- **Removed API/flag/feature-gate at the target version:** e.g. a component-config field or
  feature gate removed in the target minor makes the phase fail — cross-check
  [[CONCEPT-K8S_API_REMOVALS]] and the per-version changes docs.
- **etcd phase:** `init phase etcd local` re-renders the etcd static pod; a failure here is an
  etcd/manifest problem ([[TROUBLE-ETCD_QUORUM_LOSS]]).
- **Addon phase (kube-proxy/coredns):** the `addon` phase re-applies the addon manifests; RBAC
  or an existing customized addon can conflict — Kubespray retries these (`retries: 3/6`).
- **Certs:** kubeadm renews control-plane certs on upgrade by default; a cert/CA problem fails
  the apply — check `/etc/kubernetes/pki` and `kubeadm certs check-expiration`.

## Known Issues

- If `upgrade apply` succeeds but the component then won't come healthy, that's the **health
  check** class, not the apply — [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]].

## References

- `kubeadm-upgrade.yml` (v2.31.0) + kubeadm upgrade guide (above); seam:
  [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; health: [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]; removals:
  [[CONCEPT-K8S_API_REMOVALS]].
