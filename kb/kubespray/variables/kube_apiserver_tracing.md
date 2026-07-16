---
id: VARIABLE-KUBE_APISERVER_TRACING
type: variable
title: kube_apiserver_tracing
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_tracing
tags:
  - apiserver
  - tracing
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Default false — enable kube-apiserver distributed tracing"
relations: []
---

# kube_apiserver_tracing

## Summary
Toggles OpenTelemetry distributed tracing for the kube-apiserver via its tracing configuration. Default is `false` (disabled).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_apiserver_tracing: false`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Related: `kube_apiserver_tracing_endpoint`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
