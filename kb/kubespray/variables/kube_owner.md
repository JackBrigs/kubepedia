---
id: VARIABLE-KUBE_OWNER
type: variable
title: kube_owner
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_owner
tags:
  - security
  - permissions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_owner default kube (system user owning Kubernetes files)"
relations: []
---

# kube_owner

## Summary
Name of the system user that owns Kubernetes configuration and certificate files and directories on the nodes. Default is `kube`. The `adduser` role creates this user, and other roles use it for file ownership.

## Implementation
Defined with the same value `kube` in several places (all unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0):

```yaml
kube_owner: kube
```

- `roles/kubespray_defaults/defaults/main/main.yml`
- `roles/adduser/defaults/main.yml`
- `roles/kubernetes/preinstall/defaults/main.yml`

It is also exposed (uncommented, same value) in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_cert_group`, `kube_config_dir`. Consumed by the `adduser` role to create the user.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/adduser/defaults/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
