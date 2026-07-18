---
id: VARIABLE-CALICO_BAREMETAL_NODENAME
type: variable
title: calico_baremetal_nodename
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calico_baremetal_nodename
tags:
  - network-plugin
  - calico
  - variable
sources:
  - type: code
    path: roles/network_plugin/calico/rr/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico/rr/defaults/main.yml
    note: "default: {{ kube_override_hostname | default(inventory_hostname) }}"
relations: []
---
<!-- generated: variable-stub -->

# calico_baremetal_nodename

## Summary

Kubespray variable `calico_baremetal_nodename` — default `{{ kube_override_hostname | default(inventory_hostname) }}`. Defined in `roles/network_plugin/calico/rr/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/calico/rr/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
calico_baremetal_nodename: {{ kube_override_hostname | default(inventory_hostname) }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/calico/rr/defaults/main.yml` (Kubespray `v2.31.0`).
