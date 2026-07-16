---
id: VARIABLE-KUBE_READ_ONLY_PORT
type: variable
title: kube_read_only_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_read_only_port
tags:
  - security
  - hardening
  - kubelet
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    lines: "138 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_read_only_port: 0 (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: TAG-NODE
---

# kube_read_only_port

## Summary

`kube_read_only_port` sets the kubelet read-only port. The default is `0`
(disabled) across `v2.29.0`–`v2.31.0` — the hardened setting, since the read-only
port serves unauthenticated node/pod data when open.

## Implementation

Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (`0`, unchanged
across all four tags). `0` disables the kubelet read-only port; the value is
propagated into the kubelet configuration deployed by the node role (see
[[TAG-NODE]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `0` (disabled).
- Keep it `0` for hardening. Some legacy monitoring expects `10255`; prefer the
  authenticated kubelet API instead of re-enabling it.

## References

- `roles/kubernetes/control-plane/defaults/main/main.yml` — default (L139 in
  v2.29.0, L138 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
