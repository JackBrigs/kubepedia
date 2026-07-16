---
id: VARIABLE-KUBELET_PREFERRED_ADDRESS_TYPES
type: variable
title: kubelet_preferred_address_types
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_preferred_address_types
tags:
  - kubelet
  - apiserver
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Ordered address types the API server prefers when connecting to the kubelet (kubelet-preferred-address-types)"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_preferred_address_types

## Summary
Ordered list of node address types the API server prefers when connecting to kubelets (maps to the apiserver `--kubelet-preferred-address-types` flag). Default is `InternalDNS,InternalIP,Hostname,ExternalDNS,ExternalIP`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kubelet_preferred_address_types: 'InternalDNS,InternalIP,Hostname,ExternalDNS,ExternalIP'
```

Line number: 177 (v2.29.0/v2.29.1), 180 (v2.30.0/v2.31.0). The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Configured on the control plane; affects how the API server reaches kubelets for logs/exec/proxy.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
