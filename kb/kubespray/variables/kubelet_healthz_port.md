---
id: VARIABLE-KUBELET_HEALTHZ_PORT
type: variable
title: kubelet_healthz_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_healthz_port
tags:
  - kubelet
  - healthz
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Port for the kubelet healthz endpoint; defaults to 10248"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_healthz_port

## Summary
The port on which kubelet serves its healthz endpoint. Defaults to `10248`, the standard kubelet health-check port.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_healthz_port: 10248
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 142 in v2.29.0, line 141 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `kubelet_healthz_bind_address`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
