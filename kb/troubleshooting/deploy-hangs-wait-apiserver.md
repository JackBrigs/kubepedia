---
id: TROUBLE-DEPLOY_HANGS_WAIT_APISERVER
type: troubleshooting
title: "Kubespray deploy hangs waiting for the API server (init)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubespray hangs check api is up
  - waiting for apiserver healthz init
  - control plane static pods not up deploy
  - kubeadm init hangs kubelet
tags:
  - troubleshooting
  - kubespray
  - control-plane
  - deploy
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/check-api.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/check-api.yml
    note: "GET /healthz==200, 60x5s"
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK
  - type: see_also
    target: TROUBLE-CGROUP_DRIVER_MISMATCH
---

# Kubespray deploy hangs waiting for the API server (init)

## Summary

A fresh `cluster.yml` run stalls on Kubespray's **`check-api.yml`** — `GET https://<ip>:6443
/healthz` never returns 200 (60×5 s = 5 min), then fails. The API server static pod isn't coming
up; this is the **init-time** twin of the upgrade health check
([[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]).

## Problem

- Ansible stuck on `Kubeadm | Check api is up` then `FAILED (retries exhausted)`.
- `kubeadm init` completed (or is stuck) but `/healthz` never healthy.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0**. After `kubeadm init` writes the control-plane
  static-pod manifests, the **kubelet** must start them; `check-api.yml` waits for the API to be
  healthy.

## Diagnostics

1. **Is the kubelet running & healthy?** `systemctl status kubelet`, `journalctl -u kubelet` on
   the first CP node — a kubelet that won't start (bad config, **cgroup-driver mismatch**
   [[TROUBLE-CGROUP_DRIVER_MISMATCH]]) never launches the static pods.
2. **Are the static pods there?** `crictl ps` / `crictl logs` for kube-apiserver — a
   crash-looping apiserver (bad flag/feature-gate, cert, etcd unreachable) fails `/healthz`.
3. **etcd reachable?** apiserver won't be healthy without etcd — check the etcd service/pod
   ([[TROUBLE-ETCD_QUORUM_LOSS]]); with host etcd, the etcd role must have come up first.
4. **Container runtime up?** no CRI → no static pods; check containerd/CRI-O.
5. **Manifests present?** `ls /etc/kubernetes/manifests` — empty means `kubeadm init` didn't
   complete (see its output — [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]).
6. **Resume:** fix the failing component and re-run — the play is idempotent.

## Known Issues

- This is almost always a **kubelet / static-pod / etcd** problem, not Ansible — the Ansible
  timeout is just the messenger.

## References

- `check-api.yml` (v2.31.0, above); seam: [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; upgrade twin:
  [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]; cgroup: [[TROUBLE-CGROUP_DRIVER_MISMATCH]].
