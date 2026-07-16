---
id: VARIABLE-ETCD_CERT_ALT_NAMES
type: variable
title: etcd_cert_alt_names
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_cert_alt_names
tags:
  - etcd
  - certificates
  - tls
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Extra DNS SANs added to the etcd certificate; default etcd.kube-system.* names"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_cert_alt_names

## Summary
List of additional DNS names added as Subject Alternative Names (SANs) to the etcd certificate. A comment in the source notes it does not set up DNS entries, only adds them to the certificate.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` (line 25 in v2.29.0/v2.29.1, line 24 in v2.30.0/v2.31.0). Default value (identical across v2.29.0-v2.31.0):

```yaml
etcd_cert_alt_names:
  - "etcd.kube-system.svc.{{ dns_domain }}"
  - "etcd.kube-system.svc"
  - "etcd.kube-system"
  - "etcd"
```

Also mirrored in `roles/kubernetes/control-plane/defaults/main/etcd.yml:7`. The list is **unchanged across v2.29.0-v2.31.0**; only the line number shifted.

## Compatibility
Kubespray v2.29.0-v2.31.0. Uses `dns_domain`. Related: `etcd_cert_alt_ips` (IP SANs), `etcd_cert_dir`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubernetes/control-plane/defaults/main/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
