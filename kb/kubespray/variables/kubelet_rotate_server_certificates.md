---
id: VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES
type: variable
title: kubelet_rotate_server_certificates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kubelet_rotate_server_certificates
tags:
  - security
  - kubelet
  - certificates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "608 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kubelet_rotate_server_certificates: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBELET_ROTATE_CERTIFICATES
---

# kubelet_rotate_server_certificates

## Summary

`kubelet_rotate_server_certificates` enables automatic rotation of the kubelet
**serving** certificate. The default is `false` across `v2.29.0`–`v2.31.0`,
because server-cert rotation requires the CSRs to be approved (manually or by an
approver controller).

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`false`, unchanged
across all four tags). When `true`, the kubelet requests serving certificates via
CSR (`serverTLSBootstrap`); those CSRs must be approved — Kubespray offers a
`kubelet-csr-approver` add-on for that.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Enable together with a CSR-approver so kubelet serving certs are signed;
  otherwise the CSRs stay pending. Client-cert rotation is separate:
  [[VARIABLE-KUBELET_ROTATE_CERTIFICATES]].

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L608 in v2.31.0;
  shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
