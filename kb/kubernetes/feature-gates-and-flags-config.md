---
id: CONFIG-FEATURE_GATES_AND_FLAGS
type: configuration
title: "Enabling feature gates and custom flags in Kubespray"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable feature gate kubespray
  - kube_feature_gates
  - kube_apiserver_feature_gates
  - custom apiserver flags
  - kubelet_custom_flags
  - extra args
tags:
  - kubernetes
  - feature-gates
  - configuration
  - apiserver
  - kubelet
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_feature_gates + per-component *_feature_gates defaults (tag v2.31.0)"
  - type: code
    path: roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    lines: "84-89"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    note: "kubelet featureGates rendered from kubelet_feature_gates|kube_feature_gates (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
  - type: see_also
    target: VARIABLE-KUBE_FEATURE_GATES
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
---

# Enabling feature gates and custom flags in Kubespray

## Summary

To turn a Kubernetes feature gate on/off, or pass a flag Kubespray doesn't expose as a
dedicated variable, use the **`*_feature_gates`** lists and the **`*_extra_args`** escape
hatches. `kube_feature_gates` sets a gate for **all** components at once; per-component
lists override it for a single component. This is the "how"; which gates exist and their
per-version state is [[CONCEPT-K8S_FEATURE_GATES]].

## Configuration

**Feature gates** (all default `[]`, format `Name=true` / `Name=false`):

| Variable | Scope |
|----------|-------|
| `kube_feature_gates` | **all** components (global default) |
| `kube_apiserver_feature_gates` | kube-apiserver |
| `kube_controller_feature_gates` | kube-controller-manager |
| `kube_scheduler_feature_gates` | kube-scheduler |
| `kube_proxy_feature_gates` | kube-proxy |
| `kubelet_feature_gates` | kubelet |

- Each per-component list **falls back to `kube_feature_gates`** when unset — so set the
  global for cluster-wide gates, a per-component list only when one component differs.
- Example: `kube_feature_gates: ["SomeGate=true"]`.

**Custom flags / config (escape hatches):**

- `kube_kubeadm_apiserver_extra_args: {}` — extra kube-apiserver flags via kubeadm.
- `kubelet_custom_flags: []` — extra kubelet **command-line** flags.
- `kubelet_config_extra_args: {}` — extra **KubeletConfiguration** fields not exposed as a
  variable ([[CONFIG-KUBELET_CONFIGURATION]]).

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **Don't reference a removed gate.** A gate that Kubernetes has removed makes the
  component fail to start if passed — drop it after its removal
  ([[CONCEPT-K8S_FEATURE_GATES]]). Setting a **GA-locked** gate is a no-op (it can't be
  changed) and only risks a future removal error.
- Feature-gate **values move with the K8s version** — a gate that's Alpha in one minor may
  be Beta/GA (and eventually removed) in another; re-check `*_feature_gates` entries at
  each upgrade.
- Prefer a **dedicated variable** when one exists (e.g. `kubelet_seccomp_default`) over a
  raw flag — dedicated vars are validated and survive template changes; extra-args are
  unchecked passthrough.

## References

- `*_feature_gates` defaults and kubelet featureGates template at tag `v2.31.0`. Which
  gates / per-version state: [[CONCEPT-K8S_FEATURE_GATES]]; kubelet config:
  [[CONFIG-KUBELET_CONFIGURATION]].
