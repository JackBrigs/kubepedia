---
id: VARIABLE-KUBECTL
type: variable
title: kubectl
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubectl
tags:
  - kubectl
  - kubeconfig
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines the kubectl command string with admin kubeconfig"
relations: []
---

# kubectl

## Summary
Shorthand command string used internally by Kubespray tasks to invoke `kubectl`
against the cluster admin kubeconfig. It is not a boolean/toggle; it is the
pre-composed CLI invocation. Default:
`{{ bin_dir }}/kubectl --kubeconfig {{ kube_config_dir }}/admin.conf`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`kubectl: "{{ bin_dir }}/kubectl --kubeconfig {{ kube_config_dir }}/admin.conf"`.
The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the
line number shifts: 185 in v2.29.0/v2.29.1, 186 in v2.30.0, 183 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `bin_dir` and `kube_config_dir`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
