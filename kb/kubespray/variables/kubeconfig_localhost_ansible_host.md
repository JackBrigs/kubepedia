---
id: VARIABLE-KUBECONFIG_LOCALHOST_ANSIBLE_HOST
type: variable
title: kubeconfig_localhost_ansible_host
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubeconfig_localhost_ansible_host
tags:
  - kubernetes
  - client
  - variable
sources:
  - type: code
    path: roles/kubernetes/client/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/client/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# kubeconfig_localhost_ansible_host

## Summary

Kubespray variable `kubeconfig_localhost_ansible_host` — default `false`. Defined in `roles/kubernetes/client/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/client/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kubeconfig_localhost_ansible_host: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/client/defaults/main.yml` (Kubespray `v2.31.0`).
