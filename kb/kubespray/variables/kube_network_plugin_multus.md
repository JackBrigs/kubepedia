---
id: VARIABLE-KUBE_NETWORK_PLUGIN_MULTUS
type: variable
title: kube_network_plugin_multus
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_network_plugin_multus
tags:
  - networking
  - cni
  - multus
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_network_plugin_multus default false"
relations:
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
---

# kube_network_plugin_multus

## Summary
Toggle that enables the Multus meta-CNI plugin alongside the primary `kube_network_plugin`, allowing pods to attach multiple network interfaces. Default is `false` (Multus disabled).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_network_plugin_multus: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is also exposed (uncommented, same value) in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Used in combination with `kube_network_plugin` as the primary CNI. When set to `true`, Multus is deployed as an additional CNI layer.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
