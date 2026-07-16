---
id: VARIABLE-KUBE_ETCD_KEY_FILE
type: variable
title: kube_etcd_key_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_etcd_key_file
tags:
  - etcd
  - certificates
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Client private key filename used to authenticate to etcd; default node-{{ inventory_hostname }}-key.pem"
relations: []
---

# kube_etcd_key_file

## Summary
Filename of the client TLS private key used by Kubernetes components to authenticate to the etcd cluster. Default: `node-{{ inventory_hostname }}-key.pem`, the per-node etcd node key paired with `kube_etcd_cert_file`.

## Implementation
Defined identically in three roles:
`roles/kubernetes/control-plane/defaults/main/main.yml`, `roles/network_plugin/calico_defaults/defaults/main.yml`, and `roles/network_plugin/cilium/defaults/main.yml`, each as:

```yaml
kube_etcd_key_file: node-{{ inventory_hostname }}-key.pem
```

The value is unchanged across v2.29.0–v2.31.0 (only line numbers shift between tags).

## Compatibility
Kubespray v2.29.0–v2.31.0. Relates to `kube_etcd_cert_file` (the paired certificate). Used where the CNI or control plane connects directly to etcd.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/network_plugin/calico_defaults/defaults/main.yml
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
