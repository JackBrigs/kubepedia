---
id: VARIABLE-KUBELET_SYSTEMD_HARDENING
type: variable
title: kubelet_systemd_hardening
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_systemd_hardening
tags:
  - kubelet
  - systemd
  - security
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Toggle for systemd service hardening features on the kubelet unit; default false"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_systemd_hardening

## Summary
Boolean toggle that enables systemd service hardening features for the kubelet service unit. Default is `false`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_systemd_hardening: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 25 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Affects the generated kubelet systemd unit.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
