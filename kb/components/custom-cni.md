---
id: CONCEPT-CUSTOM_CNI
type: concept
title: "custom_cni — bring-your-own CNI via manifests or a Helm chart"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - custom_cni
  - kube_network_plugin custom_cni
  - bring your own cni kubespray
  - custom_cni_manifests
  - custom_cni_chart
tags:
  - kubespray
  - cni
  - networking
sources:
  - type: code
    path: roles/network_plugin/custom_cni/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/custom_cni/defaults/main.yml
    note: "custom_cni_manifests [] and custom_cni_chart_* (namespace/release/repo/ref/version/values)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: ROLE-NETWORK_PLUGIN
  - type: see_also
    target: PRACTICE-CNI_GENERIC_PLUGIN
---

# custom_cni — bring-your-own CNI via manifests or a Helm chart

## Summary

`kube_network_plugin: custom_cni` tells Kubespray to install a CNI **you supply** — either a list of
**raw manifests** (`custom_cni_manifests`) or a **Helm chart** (`custom_cni_chart_*`) — instead of a
Kubespray-managed CNI. Unlike the generic `cni` option ([[PRACTICE-CNI_GENERIC_PLUGIN]], which only
unpacks the binaries and leaves you to wire everything), `custom_cni` actually **applies your CNI's
deployment** for you. Use it to run a CNI Kubespray doesn't natively manage (e.g. a specific Cilium/
Calico chart version, or a niche plugin) while still letting Kubespray drive the cluster.

## Context

- Selected via [[VARIABLE-KUBE_NETWORK_PLUGIN]] `= custom_cni`; applied by the
  `network_plugin/custom_cni` role ([[ROLE-NETWORK_PLUGIN]]). Stable across **v2.27.0–v2.31.0**.
- **Two mutually-usable delivery modes:**
  - **Manifests:** `custom_cni_manifests: [<path/URL>, …]` — Kubespray applies each manifest into the
    cluster (kubectl apply). You own their content and versioning.
  - **Helm chart:** `custom_cni_chart_repository_name` / `_repository_url` / `_ref` / `_version` /
    `_release_name` / `_namespace` (default `kube-system`) / `_values` `{}` — Kubespray installs the
    chart. This is the clean path to pin an **exact upstream CNI chart version** outside Kubespray's
    pinned CNI versions.
- **You own compatibility:** Kubespray does not validate your CNI against the cluster's pod CIDR, MTU,
  kube-proxy-replacement, or Kubernetes version — that is entirely on you. Ensure the CNI's chart/
  manifests match `kube_pods_subnet` and the cluster networking model.

## Implementation notes

- Because you supply the deployment, **upgrades of the CNI are your responsibility** — bump
  `custom_cni_chart_version` (or your manifests) and re-run; Kubespray won't move it for you.
- Good fit for: running a newer CNI version than Kubespray pins, a CNI with a custom values overlay, or
  an in-house/forked plugin. For a truly unmanaged binaries-only setup, contrast the generic `cni`
  option ([[PRACTICE-CNI_GENERIC_PLUGIN]]).

## References

- `roles/network_plugin/custom_cni/defaults/main.yml` (tag v2.31.0). Selector
  [[VARIABLE-KUBE_NETWORK_PLUGIN]]; role [[ROLE-NETWORK_PLUGIN]]; generic binaries-only option
  [[PRACTICE-CNI_GENERIC_PLUGIN]].
