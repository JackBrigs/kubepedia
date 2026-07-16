---
id: CONCEPT-K8S_CONTROL_PLANE_VERSIONS
type: concept
title: Control-plane component versions (all track kube_version)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - control plane versions
  - kube-apiserver version
  - kube-controller-manager version
  - kube-scheduler version
tags:
  - kubernetes
  - control-plane
  - kubeadm
  - versions
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "control plane deployed via kubeadm (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "kube_image_repo=registry.k8s.io; binaries pinned to v{kube_version}"
relations:
  - type: see_also
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
---

# Control-plane component versions (all track kube_version)

## Summary

There is **one Kubernetes version knob** for the control plane: `kube_version`. The
core control-plane components — **kube-apiserver, kube-controller-manager,
kube-scheduler, kube-proxy** — are all deployed by **kubeadm** and run at exactly
`kube_version`. There are no separate per-component version variables to bump; you
change the Kubernetes version in one place and every control-plane component follows.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (Kubernetes `1.31`–`1.35`).
- Kubespray installs the control plane through **kubeadm**
  (`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`); the `kubeadm` and
  `kubelet` binaries are downloaded pinned to `v{{ kube_version }}` from the
  Kubernetes download site, and the static-pod images come from
  `kube_image_repo` (default **`registry.k8s.io`**) tagged with the same version.
- `kube_version` itself defaults to the newest entry in Kubespray's bundled
  `kubelet_checksums` map (i.e. the release's default Kubernetes version) — see
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]] for the per-Kubespray-version window.

**Implication for the upgrade report:** you do **not** track apiserver /
controller-manager / scheduler / kube-proxy versions independently — they are all
equal to `kube_version`. Only components **outside** the kubeadm control plane
(etcd, container runtime, CNI, CoreDNS, add-ons) have their own version variables and
must be tracked separately.

- kube-proxy is the one control-plane component with a Kubespray image variable
  (`kube_proxy_image_repo = {{ kube_image_repo }}/kube-proxy`), but its tag still
  tracks the Kubernetes version — it is a kubeadm-managed DaemonSet, not an
  independently versioned add-on.
- Node components (kubelet, kube-proxy) run the same `kube_version`; kubelet
  behaviour is configured separately — see [[CONFIG-KUBELET_CONFIGURATION]].

## References

- kubeadm setup + download defaults at tag `v2.31.0` (see sources).
- Version window per Kubespray release: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]];
  the `kube_version` variable: [[VARIABLE-KUBE_VERSION]].
