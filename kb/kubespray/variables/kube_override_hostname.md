---
id: VARIABLE-KUBE_OVERRIDE_HOSTNAME
type: variable
title: kube_override_hostname
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_override_hostname
tags:
  - kubelet
  - hostname
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_override_hostname default to inventory_hostname"
relations: []
---

# kube_override_hostname

## Summary
The hostname registered for a node in Kubernetes (kubelet `--hostname-override`). Defaults to the Ansible `inventory_hostname`, so each node's Kubernetes node name matches its inventory name unless overridden.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_override_hostname: "{{ inventory_hostname }}"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is exposed as a commented example `# kube_override_hostname: {{ inventory_hostname }}` in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on the Ansible fact `inventory_hostname`. Sets the kubelet hostname override used as the node's Kubernetes name.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
