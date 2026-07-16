---
id: VARIABLE-KUBECONFIG_LOCALHOST
type: variable
title: kubeconfig_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeconfig_localhost
tags:
  - kubeconfig
  - artifacts
  - client
sources:
  - type: code
    path: roles/kubernetes/client/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/client/defaults/main.yml
    note: "Defines kubeconfig_localhost: false"
relations: []
---

# kubeconfig_localhost

## Summary
When enabled, copies the admin kubeconfig to the Ansible controller (localhost) artifacts directory so the cluster can be accessed locally. Default is `false`.

## Implementation
Defined as `kubeconfig_localhost: false` in two places, both unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0:

- `roles/kubernetes/client/defaults/main.yml` (line 2 in all four tags)
- `roles/kubespray_defaults/defaults/main/main.yml` (line 428 in v2.29.0/v2.29.1, 429 in v2.30.0, 441 in v2.31.0)

Both definitions carry the same default (`false`), so there is no discrepancy between them.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `kubeconfig_localhost_ansible_host`, `kubectl_localhost`, `artifacts_dir`.

## References
- roles/kubernetes/client/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
