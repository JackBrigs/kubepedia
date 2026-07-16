---
id: VARIABLE-CREDENTIALS_DIR
type: variable
title: credentials_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - credentials_dir
tags:
  - credentials
  - inventory
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory where generated credentials are stored; default {{ inventory_dir }}/credentials"
relations: []
---

# credentials_dir

## Summary
Local directory (on the Ansible control node) where Kubespray stores generated
credentials such as tokens and secrets. Defaults to a `credentials`
subdirectory next to the active inventory.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
credentials_dir: "{{ inventory_dir }}/credentials"
```

The same default is mirrored in the sample inventory at
`inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The value is
unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number
shifts between tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Derived from the Ansible
`inventory_dir` special variable.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
