---
id: VARIABLE-KUBERNETES_AUDIT
type: variable
title: kubernetes_audit
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kubernetes_audit
tags:
  - security
  - hardening
  - audit
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    lines: "54 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kubernetes_audit: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: TAG-CONTROL_PLANE
---

# kubernetes_audit

## Summary

`kubernetes_audit` enables API-server audit logging. The default is `false`
across `v2.29.0`–`v2.31.0`; enabling it configures an audit policy and log
backend on the control plane.

## Implementation

Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (`false`,
unchanged across all four tags). When `true`, Kubespray wires the API server's
`--audit-policy-file` / `--audit-log-*` flags (with related `audit_*` variables
controlling policy and retention).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- A hardening control; enabling it adds audit-log volume and disk usage on the
  control plane.

## References

- `roles/kubernetes/control-plane/defaults/main/main.yml` — default (L51 in
  v2.29.0, L54 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
