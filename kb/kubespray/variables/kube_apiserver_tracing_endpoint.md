---
id: VARIABLE-KUBE_APISERVER_TRACING_ENDPOINT
type: variable
title: kube_apiserver_tracing_endpoint
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_tracing_endpoint
tags:
  - apiserver
  - tracing
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Default \"[::]:4317\" — OTLP collector endpoint for apiserver tracing"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_tracing_endpoint

## Summary
Endpoint of the OpenTelemetry collector to which the kube-apiserver sends traces when tracing is enabled. Default is `"[::]:4317"`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_apiserver_tracing_endpoint: "[::]:4317"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Effective only when `kube_apiserver_tracing` is `true`.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Related: `kube_apiserver_tracing`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
