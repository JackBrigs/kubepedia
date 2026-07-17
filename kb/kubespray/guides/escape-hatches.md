---
id: CONCEPT-ESCAPE_HATCHES
type: concept
title: "Escape hatches — how to set an option Kubespray doesn't expose"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - escape hatch
  - escape hatches
  - how to set a flag not exposed by kubespray
  - custom flags kubespray
  - extra args kubespray
  - passthrough config
  - set arbitrary kubeletconfiguration field
  - runtime-request-timeout kubespray
  - kubelet_config_extra_args
  - kubelet_node_config_extra_args
  - kube_kubeadm_apiserver_extra_args
  - kubeadm_patches
tags:
  - kubespray
  - configuration
  - customization
  - index
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "kubelet_config_extra_args {}, kubelet_custom_flags []"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_kubeadm_{apiserver,controller,scheduler}_extra_args, kubeadm_patches"
relations:
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
  - type: see_also
    target: CONCEPT-KUBEADM_CONFIG
  - type: see_also
    target: CONFIG-FEATURE_GATES_AND_FLAGS
---

# Escape hatches — how to set an option Kubespray doesn't expose

## Summary

Kubespray exposes **named variables** for common settings, but for anything it *doesn't* wrap
there are generic **escape hatches** — passthrough variables that inject your value verbatim
into the component's config, CLI flags, or the kubeadm objects. This is the index an operator
needs when the question is **"how do I set flag/field X on component Y?"** and there's no
dedicated variable for it. The knowledge for each hatch lives in the per-component config docs;
this page collects the hatches in one place.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0**. Every variable in the table below was **verified
  present in v2.29.0, v2.30.0, and v2.31.0** (git-grep per tag) — the names are stable across
  the range. (Note: there is **no** per-node `kubelet_node_config_extra_args` variable — per-node
  customization is done by setting the **same** `kubelet_config_extra_args`/`kubelet_custom_flags`
  in a node's **host_vars/group_vars**, which Ansible variable precedence scopes to that node.)
- **Decision order** (prefer the most specific): **① a dedicated named variable** →
  **② a typed `*_extra_args` map** (merged into the component's config) → **③ raw `*_custom_flags`
  / `kubeadm_patches`** (last resort, unvalidated).

## Implementation

**Escape hatches per component:**

| Component | Variable | Mechanism / what it sets |
|-----------|----------|--------------------------|
| **kubelet** | `kubelet_config_extra_args` `{}` | free-form map **merged verbatim** into the generated **KubeletConfiguration** — the hatch for any KubeletConfiguration field with no dedicated var (e.g. `{runtimeRequestTimeout: "15m"}`, `maxPods`, `systemReserved`). |
| kubelet (raw CLI) | `kubelet_custom_flags` `[]` | list of **raw command-line flags** appended to `KUBELET_ARGS` — for kubelet flags **not** in KubeletConfiguration. |
| **kube-apiserver** | `kube_kubeadm_apiserver_extra_args` | map merged into the kubeadm **ClusterConfiguration** `apiServer.extraArgs` → apiserver flags. |
| **kube-controller-manager** | `kube_kubeadm_controller_extra_args` | → `controllerManager.extraArgs`. |
| **kube-scheduler** | `kube_kubeadm_scheduler_extra_args` | → `scheduler.extraArgs`. |
| **any kubeadm object / static pod** | `kubeadm_patches` | kubeadm **patch** files applied to the generated manifests (apiserver/cm/scheduler/etcd static pods, etc.) — the most general hatch when `extraArgs` isn't enough (volumes, resources, arbitrary fields). |
| **etcd** (host role) | `etcd_extra_vars` | extra environment/config for the host etcd ([[CONCEPT-KUBESPRAY_ETCD_OWNERSHIP]]). |
| **containerd** | `containerd_base_runtime_specs`, `containerd_additional_runtimes`, `containerd_base_runtime_spec_rlimit_nofile` | runtime-spec / extra-runtime passthrough for the CRI config. |
| **CoreDNS** | `coredns_external_zones` | inject custom Corefile zones/forwarders not covered by defaults. |
| **cert-manager** | `cert_manager_controller_extra_args` | extra controller flags. |
| **Cilium (addon)** | `cilium_extra_values`, `cilium_config_extra_vars`, `cilium_agent_extra_args`, `cilium_agent_extra_env_vars`, `cilium_install_extra_flags` | Helm-values / agent / install passthrough — the addon-style hatch. |

**Addon Helm-values pattern.** Beyond Cilium, many addons expose a `*_extra_values` / `*_extra_args`
style variable to pass through to their chart/deployment when a setting isn't wrapped — check the
addon's role defaults (`roles/.../defaults/main.yml`) for a `*_extra*` / `*_values` variable
before concluding a setting is unreachable.

## Compatibility

- **`*_extra_args` values are merged, not validated** — a bad flag/field surfaces later (kubelet
  crash-loop, apiserver rejects the flag, or the kubeadm health check fails —
  [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]). Use the exact upstream field/flag name for the
  target version; a flag removed in a newer minor breaks start-up
  ([[CONFIG-FEATURE_GATES_AND_FLAGS]]).
- **Prefer the named variable** when one exists — the escape hatch bypasses Kubespray's own
  consistency handling.
- These are **Kubespray-managed** components; addon **Helm charts** you deploy independently have
  their own values (see the addon docs / [[CONCEPT-ADDON_CATALOG]]).

## References

- Node/defaults + kubespray_defaults main.yml (v2.31.0, above). Per-component detail:
  [[CONFIG-KUBELET_CONFIGURATION]], [[CONCEPT-KUBEADM_CONFIG]],
  [[CONFIG-FEATURE_GATES_AND_FLAGS]]; etcd ownership: [[CONCEPT-KUBESPRAY_ETCD_OWNERSHIP]].
