---
id: VARIABLE-KUBE_SCRIPT_DIR
type: variable
title: kube_script_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_script_dir
tags:
  - paths
  - kubernetes
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_script_dir, default {{ bin_dir }}/kubernetes-scripts"
relations: []
---

# kube_script_dir

## Summary
Directory where Kubespray places Kubernetes helper scripts. Defaults to `{{ bin_dir }}/kubernetes-scripts`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` and mirrored in the sample inventory (`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`, line 8):

```yaml
kube_script_dir: "{{ bin_dir }}/kubernetes-scripts"
```

The computed default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The line number in the role defaults shifts between tags (180 in v2.29.0/v2.29.1, 181 in v2.30.0, 178 in v2.31.0) but the expression is identical.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Depends on `bin_dir`. Related path variables: `kube_config_dir`, `kube_token_dir`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
