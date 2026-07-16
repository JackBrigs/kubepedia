---
id: VARIABLE-KUBE_KUBEADM_SCHEDULER_EXTRA_ARGS
type: variable
title: kube_kubeadm_scheduler_extra_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_kubeadm_scheduler_extra_args
tags:
  - scheduler
  - kubeadm
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Extra args passed to kube-scheduler via kubeadm; default empty dict"
relations: []
---

# kube_kubeadm_scheduler_extra_args

## Summary
Dictionary of additional command-line flags injected into the kube-scheduler manifest via the kubeadm configuration. Default: `{}` (no extra args).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml` (line 3) as:

```yaml
kube_kubeadm_scheduler_extra_args: {}
```

The default and defining path are unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Companion of `kube_kubeadm_apiserver_extra_args` and `kube_kubeadm_controller_extra_args` for the other control-plane components.

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
