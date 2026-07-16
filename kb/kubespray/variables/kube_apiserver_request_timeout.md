---
id: VARIABLE-KUBE_APISERVER_REQUEST_TIMEOUT
type: variable
title: kube_apiserver_request_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_request_timeout
tags:
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Default \"1m0s\" — kube-apiserver --request-timeout"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_request_timeout

## Summary
Default duration a kube-apiserver request may run before it times out, passed to the `--request-timeout` flag. Default is `"1m0s"`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_apiserver_request_timeout: "1m0s"`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Applies to the control-plane (kube-apiserver) role.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
