---
id: VARIABLE-CILIUM_DEPLOY_ADDITIONALLY
type: variable
title: cilium_deploy_additionally
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_deploy_additionally
tags:
  - cilium
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "cilium_deploy_additionally: false (default, unchanged v2.29.0-v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_deploy_additionally

## Summary

`cilium_deploy_additionally` controls whether Cilium is deployed as an additional
CNI alongside the primary network plugin. The default is `false` across
`v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` as
`cilium_deploy_additionally: false`. The literal `false` is unchanged across all
four tags; only the line number shifts (221 in v2.29.0/v2.29.1, 222 in v2.30.0,
219 in v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: default `false`.
- Related: `kube_network_plugin`, the Cilium network plugin role.

## References

- `roles/kubespray_defaults/defaults/main/main.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
