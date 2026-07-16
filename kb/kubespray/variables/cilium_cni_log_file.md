---
id: VARIABLE-CILIUM_CNI_LOG_FILE
type: variable
title: cilium_cni_log_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_cni_log_file
tags:
  - cilium
  - cni
  - logging
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Path to the Cilium CNI plugin log file; default /var/run/cilium/cilium-cni.log"
relations: []
---

# cilium_cni_log_file

## Summary
Path to the log file used by the Cilium CNI plugin. Default is `/var/run/cilium/cilium-cni.log`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_cni_log_file: "/var/run/cilium/cilium-cni.log"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI. Related: `cilium_cni_exclusive`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
