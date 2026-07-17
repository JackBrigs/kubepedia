---
id: TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK
type: troubleshooting
title: "kubeadm upgrade: health-check fails (static control plane won't come up)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - upgrade health FATAL
  - waiting for the kubelet to boot up the control plane
  - kubeadm upgrade static pod hash
  - kubespray upgrade stuck check api healthz
  - control plane not healthy after upgrade
tags:
  - troubleshooting
  - kubeadm
  - upgrade
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    note: "kubeadm upgrade apply runs kubeadm's health check"
  - type: docs
    path: kubeadm upgrade troubleshooting
    url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/
    note: "static-pod manifest swap + health"
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: TROUBLE-KUBEADM_UPGRADE_APPLY
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
---

# kubeadm upgrade: health-check fails (static control plane won't come up)

## Summary

A Kubespray upgrade hangs or fails "in the middle of Ansible", but the real error is
**kubeadm's health check**: after swapping a control-plane static-pod manifest, kubeadm waits
for the component to come back healthy and aborts if it doesn't. This is a **kubeadm** failure
surfaced by Ansible (see [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]).

## Problem

- kubeadm: `[upgrade/health] FATAL`, or `[upgrade/staticpods] Waiting for the kubelet to boot up
  the control plane as static Pods …` that never completes; `context deadline exceeded`.
- Kubespray's own `check-api.yml` then times out: `/healthz` never returns 200 (60×5 s).
- `kubeadm upgrade apply` returns non-zero and Ansible reports the wrapped stderr.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. kubeadm upgrades a CP
  component by writing a new manifest to `/etc/kubernetes/manifests`, waiting for the kubelet to
  restart the static pod, then health-checking it.

## Diagnostics

1. **Which component?** kubeadm names it (apiserver/controller-manager/scheduler/etcd). Check
   that static pod: `crictl ps`, `crictl logs`, and the kubelet log — a crash-looping static pod
   is the usual cause (bad flag/feature-gate, cert, or image pull).
2. **kubelet must pick up the new manifest:** if the static pod doesn't restart, the kubelet is
   wedged (PLEG — [[TROUBLE-KUBELET_PLEG_NOT_HEALTHY]]) or the manifest hash didn't change;
   restart the kubelet.
3. **etcd health:** kubeadm upgrades etcd too — an unhealthy/quorum-less etcd fails the health
   check ([[TROUBLE-ETCD_QUORUM_LOSS]]).
4. **Removed flag/feature-gate after a version jump:** the new component version may reject a
   flag/gate present in the old config → static pod crashloops → health check fails. Cross-check
   the target version's removals ([[TROUBLE-KUBEADM_UPGRADE_APPLY]]).
5. **Resume:** Kubespray re-runs are idempotent; fix the failing static pod, then re-run the
   upgrade play — `check-api.yml` will pass once `/healthz` is 200.

## Known Issues

- Kubespray tolerates `field is immutable` on `kubeadm upgrade` (`failed_when: rc != 0 and
  "field is immutable" not in stderr`) — that specific message is **not** the health-check
  failure; a genuine health failure has a different stderr.

## References

- `kubeadm-upgrade.yml` (v2.31.0) + kubeadm upgrade docs (above); seam:
  [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; apply failures: [[TROUBLE-KUBEADM_UPGRADE_APPLY]]; etcd:
  [[TROUBLE-ETCD_QUORUM_LOSS]].
