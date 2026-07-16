---
id: VARIABLE-KUBELET_ADDRESS
type: variable
title: kubelet_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_address
tags:
  - kubelet
  - networking
  - node
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kubelet_address as joined main_ips"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_address

## Summary
Advertised host IP(s) for the kubelet; affects network plugin configuration. Defaults to the node's `main_ips` joined by commas (`{{ main_ips | join(',') }}`). For dualstack, IPv6 may need to be added manually because IPv4 has priority in `main_ip`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as:

```yaml
kubelet_address: "{{ main_ips | join(',') }}"
```

The definition is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 4 in all four tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `main_ips`, `main_ip`, `kubelet_bind_address`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
