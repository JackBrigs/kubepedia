---
id: VARIABLE-KUBE_APISERVER_ADDRESS
type: variable
title: kube_apiserver_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_address
tags:
  - apiserver
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Bind/local address of the apiserver on a node, from that host's main_ip"
relations: []
---

# kube_apiserver_address

## Summary
The local address of the kube-apiserver on a given node. Derived from that host's `main_ip`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_address: "{{ hostvars[inventory_hostname]['main_ip'] }}"
```

Unchanged across v2.29.0-v2.31.0 (line 637 in v2.29.0/v2.29.1, line 640 in v2.30.0, line 659 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `kube_apiserver_access_address` (which uses `main_access_ip` for the externally reachable address).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
