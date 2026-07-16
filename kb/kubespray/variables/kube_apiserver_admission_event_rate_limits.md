---
id: VARIABLE-KUBE_APISERVER_ADMISSION_EVENT_RATE_LIMITS
type: variable
title: kube_apiserver_admission_event_rate_limits
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_admission_event_rate_limits
tags:
  - apiserver
  - admission
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Map of EventRateLimit admission plugin limits; default empty map"
relations: []
---

# kube_apiserver_admission_event_rate_limits

## Summary
A map defining EventRateLimit admission plugin limits for the kube-apiserver admission control configuration. Default is an empty map (`{}`).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`, preceded by a commented usage example:

```yaml
# kube_apiserver_admission_event_rate_limits:
kube_apiserver_admission_event_rate_limits: {}
```

Unchanged across v2.29.0-v2.31.0 (value at line 111 in v2.29.0/v2.29.1, line 114 in v2.30.0/v2.31.0). The hardening test file `tests/files/ubuntu24-calico-all-in-one-hardening.yml` populates it as an example.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Effective when `kube_apiserver_admission_control_config_file: true`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- tests/files/ubuntu24-calico-all-in-one-hardening.yml (test override)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
