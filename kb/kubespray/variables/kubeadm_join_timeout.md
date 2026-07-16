---
id: VARIABLE-KUBEADM_JOIN_TIMEOUT
type: variable
title: kubeadm_join_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_join_timeout
tags:
  - kubeadm
  - join
sources:
  - type: code
    path: roles/kubernetes/kubeadm/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/kubeadm/defaults/main.yml
    note: "Timeout for kubeadm join on secondary nodes; default 120s"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_join_timeout

## Summary
Timeout applied when a node runs `kubeadm join`. Default value is `120s`.

## Implementation
Defined in `roles/kubernetes/kubeadm/defaults/main.yml`:

```yaml
kubeadm_join_timeout: 120s
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 5 in every tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the `kubernetes/kubeadm` role that joins worker and secondary control-plane nodes.

## References
- roles/kubernetes/kubeadm/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
