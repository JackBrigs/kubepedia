---
id: VARIABLE-CERTIFICATES_KEY_SIZE
type: variable
title: certificates_key_size
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - certificates_key_size
tags:
  - certificates
  - security
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "certificates_key_size: 2048 (default, unchanged v2.29.0-v2.31.0)"
relations: []
---

# certificates_key_size

## Summary

`certificates_key_size` sets the RSA key size (in bits) used when Kubespray
generates cluster certificates. The default is `2048` across `v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` as
`certificates_key_size: 2048`. The literal value `2048` is unchanged across all
four tags; only the line number shifts (713 in v2.29.0/v2.29.1, 716 in v2.30.0,
735 in v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: default `2048`.
- Applies to generated cluster certificate key material.

## References

- `roles/kubespray_defaults/defaults/main/main.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
