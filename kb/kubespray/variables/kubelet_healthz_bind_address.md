---
id: VARIABLE-KUBELET_HEALTHZ_BIND_ADDRESS
type: variable
title: kubelet_healthz_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_healthz_bind_address
tags:
  - kubelet
  - healthz
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Bind address for the kubelet healthz endpoint; defaults to 127.0.0.1"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_healthz_bind_address

## Summary
The address on which kubelet serves its healthz endpoint. Defaults to `127.0.0.1`, exposing the health check only on the loopback interface.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_healthz_bind_address: 127.0.0.1
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 145 in v2.29.0, line 144 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `kubelet_healthz_port`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
