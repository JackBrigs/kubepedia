---
id: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
type: concept
title: Control plane component versions in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31.0 <=1.35.4"
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - control plane versions
  - kube-apiserver version
  - kube-scheduler version
  - kube-controller-manager version
tags:
  - control-plane
  - kubeadm
  - version
sources:
  - type: code
    path: roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    lines: "118,125"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    note: "kubernetesVersion: v{{ kube_version }}; imageRepository: {{ kubeadm_image_repo }}"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "92,216"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "kube_image_repo=registry.k8s.io; kubeadm_image_repo={{ kube_image_repo }}; kube_proxy_image_repo"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
---

# Control plane component versions in Kubespray

## Summary

The core control plane components — `kube-apiserver`, `kube-controller-manager`,
`kube-scheduler`, and `kube-proxy` — are deployed by kubeadm and all run at
exactly [[VARIABLE-KUBE_VERSION]]. Kubespray does not version them independently.
Their images come from `registry.k8s.io`. This is unchanged across
`v2.29.0`–`v2.31.0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- These components are managed by kubeadm, configured through the generated
  kubeadm ClusterConfiguration (see [[CONFIG-KUBEADM_CONFIG_API_VERSION]]).
- The installed Kubernetes version is [[VARIABLE-KUBE_VERSION]]; supported ranges
  are in [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].

## Implementation

kubeadm pins the control plane version and image source from the generated
config (`roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2`):

```yaml
kubernetesVersion: v{{ kube_version }}     # line 118
imageRepository: {{ kubeadm_image_repo }}  # line 125
```

with (`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
kube_image_repo: "registry.k8s.io"
kubeadm_image_repo: "{{ kube_image_repo }}"
```

So kubeadm pulls, for `kube_version` X.Y.Z:

- `registry.k8s.io/kube-apiserver:vX.Y.Z`
- `registry.k8s.io/kube-controller-manager:vX.Y.Z`
- `registry.k8s.io/kube-scheduler:vX.Y.Z`

`kube-proxy` is deployed by kubeadm as a DaemonSet from
`kube_proxy_image_repo: "{{ kube_image_repo }}/kube-proxy"` at the same
`kube_version`; its proxy backend is set by [[VARIABLE-KUBE_PROXY_MODE]].

Per-tag concrete version (the default `kube_version`):

| Kubespray | Control plane version (default) |
|-----------|---------------------------------|
| v2.29.0   | 1.33.5                          |
| v2.29.1   | 1.33.7                          |
| v2.30.0   | 1.34.3                          |
| v2.31.0   | 1.35.4                          |

Any `kube_version` within the tag's supported range moves all four components
together.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: control plane images from `registry.k8s.io`,
  version equal to `kube_version`.
- No independent override of individual control plane component versions is
  provided; they follow `kube_version` via kubeadm.

## References

- `roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2:118,125`
- `roles/kubespray_defaults/defaults/main/download.yml` (`kube_image_repo`,
  `kubeadm_image_repo`, `kube_proxy_image_repo`)
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
