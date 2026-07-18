---
id: VARIABLE-KUBELET_CSR_APPROVER_NAMESPACE
type: variable
title: kubelet_csr_approver_namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubelet_csr_approver_namespace
tags:
  - kubernetes-apps
  - kubelet-csr-approver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml
    note: "default: kube-system"
relations: []
---
<!-- generated: variable-stub -->

# kubelet_csr_approver_namespace

## Summary

Kubespray variable `kubelet_csr_approver_namespace` — default `kube-system`. Defined in `roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kubelet_csr_approver_namespace: kube-system
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml` (Kubespray `v2.31.0`).
