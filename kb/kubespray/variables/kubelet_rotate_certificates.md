---
id: VARIABLE-KUBELET_ROTATE_CERTIFICATES
type: variable
title: kubelet_rotate_certificates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kubelet_rotate_certificates
tags:
  - security
  - kubelet
  - certificates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "606 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kubelet_rotate_certificates: true (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES
---

# kubelet_rotate_certificates

## Summary

`kubelet_rotate_certificates` enables automatic rotation of the kubelet **client**
certificate. The default is `true` across `v2.29.0`–`v2.31.0`, so kubelets renew
their client certs before expiry without manual intervention.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`true`, unchanged
across all four tags). It sets the kubelet's `rotateCertificates` option; the
kubelet requests a new client cert from the API server as expiry approaches.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `true`.
- Keep it enabled to avoid client-cert expiry outages. Server-cert rotation is a
  separate setting: [[VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES]].

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L606 in v2.31.0;
  shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
