---
id: VARIABLE-REMOVE_ANONYMOUS_ACCESS
type: variable
title: remove_anonymous_access
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - remove_anonymous_access
tags:
  - security
  - hardening
  - authentication
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "79 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "remove_anonymous_access: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_TOKEN_AUTH
---

# remove_anonymous_access

## Summary

`remove_anonymous_access` controls whether Kubespray removes the permissive
anonymous-access RBAC bindings it would otherwise create for bootstrap. The
default is `false` across `v2.29.0`–`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`false`, unchanged
across all four tags). When `true`, Kubespray removes the anonymous-access
ClusterRoleBindings after bootstrap, tightening who can reach the API
unauthenticated.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- A hardening control; verify bootstrap and health-check flows still work before
  enabling it cluster-wide. Related auth control: [[VARIABLE-KUBE_TOKEN_AUTH]].

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L79 in v2.31.0;
  shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
