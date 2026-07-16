---
id: VARIABLE-KUBELET_STATUS_UPDATE_FREQUENCY
type: variable
title: kubelet_status_update_frequency
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_status_update_frequency
tags:
  - kubelet
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "How often kubelet posts node status to the API server; default 10s"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_status_update_frequency

## Summary
Specifies how frequently kubelet reports node status to the API server (kubelet `nodeStatusUpdateFrequency`). Default is `10s`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_status_update_frequency: 10s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 61 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. No dependencies on other variables.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
