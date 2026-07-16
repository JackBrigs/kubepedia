---
id: VARIABLE-KUBEADM_INIT_PHASES_SKIP
type: variable
title: kubeadm_init_phases_skip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_init_phases_skip
tags:
  - kubeadm
  - init
  - kube-proxy
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed list of kubeadm init phases to skip"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_init_phases_skip

## Summary
List of kubeadm init phases to skip. Starts from `kubeadm_init_phases_skip_default` (`[ "addon/coredns" ]`) and additionally appends `addon/kube-proxy` for certain network configurations (kube-router service proxy, Cilium kube-proxy replacement, Calico BPF, or `kube_proxy_remove`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block expression:

```yaml
kubeadm_init_phases_skip_default: [ "addon/coredns" ]
kubeadm_init_phases_skip: >-
  {%- if kube_network_plugin == 'kube-router' and (kube_router_run_service_proxy is defined and kube_router_run_service_proxy) -%}
  {{ kubeadm_init_phases_skip_default + ["addon/kube-proxy"] }}
  {%- elif kube_network_plugin == 'cilium' and (cilium_kube_proxy_replacement is defined and (cilium_kube_proxy_replacement == 'strict' or (cilium_kube_proxy_replacement | bool) or (cilium_kube_proxy_replacement | string | lower == 'true') )) -%}
  {{ kubeadm_init_phases_skip_default + ["addon/kube-proxy"] }}
  {%- elif kube_network_plugin == 'calico' and (calico_bpf_enabled is defined and calico_bpf_enabled) -%}
  {{ kubeadm_init_phases_skip_default + ["addon/kube-proxy"] }}
  {%- elif kube_proxy_remove is defined and kube_proxy_remove -%}
  {{ kubeadm_init_phases_skip_default + ["addon/kube-proxy"] }}
  {%- else -%}
  {{ kubeadm_init_phases_skip_default }}
  {%- endif -%}
```

The expression is byte-identical across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 51 in v2.29.0-v2.30.0, line 50 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `kubeadm_init_phases_skip_default`, `kubeadm_upgrade_node_phases_skip`, `kube_network_plugin`, `kube_proxy_remove`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
