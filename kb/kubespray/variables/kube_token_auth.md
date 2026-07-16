---
id: VARIABLE-KUBE_TOKEN_AUTH
type: variable
title: kube_token_auth
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_token_auth
tags:
  - security
  - hardening
  - authentication
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    lines: "146 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_token_auth: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-REMOVE_ANONYMOUS_ACCESS
---

# kube_token_auth

## Summary

`kube_token_auth` enables static token-file authentication on the API server. The
default is `false` across `v2.29.0`–`v2.31.0` — the hardened setting, since static
tokens are long-lived and hard to rotate.

## Implementation

Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (`false`,
unchanged across all four tags). When `true`, Kubespray generates a token file and
sets the API server's `--token-auth-file`. Leaving it `false` keeps
authentication on certificates/bootstrap tokens.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Keep it disabled for hardening; prefer certificate or OIDC auth. Related:
  [[VARIABLE-REMOVE_ANONYMOUS_ACCESS]].

## References

- `roles/kubernetes/control-plane/defaults/main/main.yml` — default (L143 in
  v2.29.0, L146 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
