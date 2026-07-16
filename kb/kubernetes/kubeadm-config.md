---
id: CONCEPT-KUBEADM_CONFIG
type: concept
title: "How Kubespray generates the kubeadm configuration"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm config
  - ClusterConfiguration
  - kubeadm-config.yaml
  - kubeadm_patches
  - kube_kubeadm_apiserver_extra_args
  - kubeadm init phases skip
tags:
  - kubernetes
  - kubeadm
  - control-plane
  - configuration
sources:
  - type: code
    path: roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    note: "generated ClusterConfiguration/InitConfiguration (v1beta4) (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_kubeadm_*_extra_args, kubeadm_init_phases_skip (tag v2.31.0)"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
  - type: see_also
    target: CONFIG-FEATURE_GATES_AND_FLAGS
  - type: see_also
    target: TROUBLE-APISERVER_CERT_SAN
---

# How Kubespray generates the kubeadm configuration

## Summary

Kubespray drives the control plane through **kubeadm**, rendering a `kubeadm-config`
(`ClusterConfiguration` + `InitConfiguration`) from a template and feeding it to
`kubeadm init`/`join`/`upgrade`. Most control-plane settings you tune end up in this file.
Knowing what it contains — and the escape hatches for anything not exposed — is the key to
customizing the control plane.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. The template is
  `kubeadm-config.v1beta4.yaml.j2` — the config **API is `v1beta4`** (the older
  `kubeadm_config_api_version` selector and `v1beta3` fallback were **removed** in
  `v2.31.0` — [[CONFIG-KUBEADM_CONFIG_API_VERSION]]).
- kube-apiserver / controller-manager / scheduler / kube-proxy versions all follow
  `kube_version` (kubeadm-managed — [[CONCEPT-K8S_CONTROL_PLANE_VERSIONS]]).

## Implementation

**What the generated config carries:**

- **certSANs** — from `apiserver_sans` (nodes, LB, `supplementary_addresses_in_ssl_keys`)
  ([[TROUBLE-APISERVER_CERT_SAN]]).
- **Component flags** via `extraArgs` — controller-manager/scheduler bind addresses,
  timeouts, feature gates, etc.
- **etcd** endpoints/mode, networking (pod/service CIDRs, dns_domain), image repo.

**Escape hatches for anything not exposed as a variable:**

- `kube_kubeadm_apiserver_extra_args: {}` / `kube_kubeadm_controller_extra_args: {}` /
  `kube_kubeadm_scheduler_extra_args: {}` — inject extra flags into the respective
  component's `extraArgs`.
- **`kubeadm_patches`** — kubeadm's native patch mechanism: drop-in patch files that modify
  the generated static-pod manifests / config after templating, for fields Kubespray
  doesn't template. (Stale patches aren't auto-removed on inventory change —
  [[TROUBLE-KUBEADM_PATCHES_NOT_REMOVED]].)
- **`kubeadm_init_phases_skip`** — skip specific kubeadm init phases; notably
  `addon/kube-proxy` is added here for kube-proxy-free CNIs ([[CONCEPT-KUBE_PROXY]]).

## Compatibility

- **v1beta4 only** in `v2.31.0` — don't carry `v1beta3`-specific config; the fallback is
  gone ([[CONFIG-KUBEADM_CONFIG_API_VERSION]]).
- **Prefer a dedicated variable** over `*_extra_args`/patches when one exists — dedicated
  vars are validated and survive template changes; extra-args/patches are unchecked
  passthrough that can silently break across kubeadm versions.
- kubeadm patches are powerful but fragile across upgrades — re-verify them when moving
  Kubernetes minors.
- Feature gates go through the `*_feature_gates` lists, not raw extraArgs, where possible
  ([[CONFIG-FEATURE_GATES_AND_FLAGS]]).

## References

- `kubeadm-config.v1beta4.yaml.j2` and `kube_kubeadm_*_extra_args` / `kubeadm_init_phases_skip`
  at tag `v2.31.0`. API version: [[CONFIG-KUBEADM_CONFIG_API_VERSION]]; SANs:
  [[TROUBLE-APISERVER_CERT_SAN]].
