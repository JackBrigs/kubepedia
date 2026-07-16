---
id: VARIABLE-ETCD_CERT_ALT_IPS
type: variable
title: etcd_cert_alt_ips
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_cert_alt_ips
tags:
  - etcd
  - certificates
  - tls
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Extra IP SANs added to the etcd certificate; default empty list"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_cert_alt_ips

## Summary
List of additional IP addresses added as Subject Alternative Names (SANs) to the etcd certificate. Default is an empty list `[]`. It does not create DNS/IP entries, only adds them to the certificate.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_cert_alt_ips: []` (line 30 in v2.29.0/v2.29.1, line 29 in v2.30.0/v2.31.0). Also mirrored in `roles/kubernetes/control-plane/defaults/main/etcd.yml:12` as `etcd_cert_alt_ips: []`. The default `[]` is **unchanged across v2.29.0-v2.31.0**.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `etcd_cert_alt_names` (DNS SANs), `etcd_cert_dir`.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubernetes/control-plane/defaults/main/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
