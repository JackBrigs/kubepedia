---
id: VARIABLE-KUBE_APISERVER_ADMISSION_CONTROL_CONFIG_FILE
type: variable
title: kube_apiserver_admission_control_config_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_admission_control_config_file
tags:
  - apiserver
  - admission
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Toggles generating/using an apiserver admission control config file; default false"
relations: []
---

# kube_apiserver_admission_control_config_file

## Summary
Boolean toggle that controls whether kube-apiserver is configured with an admission control configuration file (`--admission-control-config-file`). Disabled by default.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_apiserver_admission_control_config_file: false
```

Unchanged across v2.29.0-v2.31.0 (line 101 in v2.29.0/v2.29.1, line 104 in v2.30.0/v2.31.0). The hardening test file `tests/files/ubuntu24-calico-all-in-one-hardening.yml` sets it to `true` as an example, but this is a test override, not the default.

## Compatibility
Kubespray v2.29.0 through v2.31.0. When enabled, it works together with admission settings such as `kube_apiserver_admission_event_rate_limits`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- tests/files/ubuntu24-calico-all-in-one-hardening.yml (test override)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
