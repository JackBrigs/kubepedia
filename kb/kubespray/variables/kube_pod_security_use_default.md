---
id: VARIABLE-KUBE_POD_SECURITY_USE_DEFAULT
type: variable
title: kube_pod_security_use_default
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_pod_security_use_default
tags:
  - security
  - hardening
  - pod-security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    lines: "117 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_pod_security_use_default: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_APISERVER_ENABLE_ADMISSION_PLUGINS
---

# kube_pod_security_use_default

## Summary

`kube_pod_security_use_default` enables a cluster-wide default Pod Security
admission configuration. The default is `false` across `v2.29.0`–`v2.31.0`, so no
default Pod Security level is enforced unless the operator opts in.

## Implementation

Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (`false`,
unchanged across all four tags). When `true`, Kubespray configures the
`PodSecurity` admission plugin with default levels (`kube_pod_security_default_*`
variables set enforce/audit/warn profiles). Works together with
[[VARIABLE-KUBE_APISERVER_ENABLE_ADMISSION_PLUGINS]].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- A hardening control; enabling a `restricted` default may reject non-compliant
  workloads, so roll it out with audit/warn first.

## References

- `roles/kubernetes/control-plane/defaults/main/main.yml` — default (L114 in
  v2.29.0, L117 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
