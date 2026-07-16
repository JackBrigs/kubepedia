---
id: VARIABLE-KUBE_SCHEDULER_CLIENT_CONN_EXTRA_OPTS
type: variable
title: kube_scheduler_client_conn_extra_opts
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_scheduler_client_conn_extra_opts
tags:
  - control-plane
  - kube-scheduler
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Defines the default empty dict {} for scheduler clientConnection options"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_scheduler_client_conn_extra_opts

## Summary
Extra `clientConnection` options (e.g. `burst`, `qps`) for the KubeSchedulerConfiguration, beyond those derived from the kubeconfig. The default is an empty dict `{}`, so no extra client-connection settings are emitted.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml:10` as:

```yaml
kube_scheduler_client_conn_extra_opts: {}
```

Consumed in `roles/kubernetes/control-plane/templates/kubescheduler-config.yaml.j2` via `{% for key in kube_scheduler_client_conn_extra_opts %}`, which renders each key/value under the scheduler's `clientConnection` section. The default value `{}` and the path are unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related to `kube_scheduler_config_extra_opts` and other kube-scheduler options in the same defaults file; rendered into `kubescheduler-config.yaml.j2`.

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- roles/kubernetes/control-plane/templates/kubescheduler-config.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
