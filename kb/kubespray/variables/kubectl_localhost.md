---
id: VARIABLE-KUBECTL_LOCALHOST
type: variable
title: kubectl_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubectl_localhost
tags:
  - kubectl
  - client
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for downloading the kubectl binary to the localhost/deploy machine"
relations: []
---

# kubectl_localhost

## Summary
Boolean toggle controlling whether the `kubectl` binary is copied to the
Ansible controller (localhost) so the operator can use it locally. Default:
`false`.

## Implementation
Defined as `kubectl_localhost: false` in two places, both with the same default:
`roles/kubespray_defaults/defaults/main/main.yml` (the global default) and
`roles/kubernetes/client/defaults/main.yml` (the consuming role). The value is
`false` and unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Line in
kubespray_defaults: 430 (v2.29.0/v2.29.1), 431 (v2.30.0), 443 (v2.31.0); the
kubernetes/client default is at line 4 in all four tags.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to the `kubernetes/client` role and
`kubeconfig_localhost`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes/client/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
