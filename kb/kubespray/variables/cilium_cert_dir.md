---
id: VARIABLE-CILIUM_CERT_DIR
type: variable
title: cilium_cert_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_cert_dir
tags:
  - cilium
  - cni
  - certificates
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Filesystem directory for Cilium certificates; default /etc/cilium/certs"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_cert_dir

## Summary
Sets the filesystem directory where Cilium certificates are stored. Defaults to `/etc/cilium/certs`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_cert_dir: /etc/cilium/certs
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 35 in v2.29.0/v2.29.1, 33 in v2.30.0, 18 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
