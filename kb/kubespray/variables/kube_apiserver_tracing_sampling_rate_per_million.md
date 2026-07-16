---
id: VARIABLE-KUBE_APISERVER_TRACING_SAMPLING_RATE_PER_MILLION
type: variable
title: kube_apiserver_tracing_sampling_rate_per_million
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_tracing_sampling_rate_per_million
tags:
  - apiserver
  - tracing
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines the apiserver tracing sampling rate per million; default 100"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_tracing_sampling_rate_per_million

## Summary
Controls the number of samples collected per million spans for kube-apiserver distributed tracing. Default is `100`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_apiserver_tracing_sampling_rate_per_million: 100
```

The value `100` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related to apiserver tracing configuration.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
