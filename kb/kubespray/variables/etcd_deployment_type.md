---
id: VARIABLE-ETCD_DEPLOYMENT_TYPE
type: variable
title: etcd_deployment_type
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - etcd_deployment_type
tags:
  - etcd
  - deployment
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "424"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "v2.29.0: etcd_deployment_type: host (line 424)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "425"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "v2.30.0: etcd_deployment_type: host (line 425)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "437"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "v2.31.0: etcd_deployment_type: host (line 437)"
  - type: code
    path: roles/etcd/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/etcd/tasks
    note: "etcd_deployment_type in ['host', 'docker', 'kubeadm'] selects install method (all tags)"
relations:
  - type: part_of
    target: COMPONENT-ETCD
---

# etcd_deployment_type

## Summary

`etcd_deployment_type` selects how Kubespray installs and runs the etcd cluster.
It is defined in the `kubespray_defaults` role and read by the `etcd` role to
choose the installation method. The default is `host` and the accepted set is
unchanged across `v2.29.0`–`v2.31.0`.

## Implementation

Default in `roles/kubespray_defaults/defaults/main/main.yml` (`host`):

| Kubespray | Line | Default |
|-----------|------|---------|
| v2.29.0   | 424  | host    |
| v2.29.1   | 424  | host    |
| v2.30.0   | 425  | host    |
| v2.31.0   | 437  | host    |

The `etcd` role validates the value against a fixed set and branches on it:

```
etcd_deployment_type in ['host', 'docker', 'kubeadm']
```

Accepted values (all tags):

- `host` (default) — etcd is installed as a static binary run as a systemd
  service; the binary is downloaded and verified against `etcd_binary_checksums`.
- `docker` — etcd runs as a container managed by the Docker engine; this also
  forces `deploy_container_engine` on the etcd nodes.
- `kubeadm` — etcd runs as a kubeadm-managed static pod on the control plane,
  changing certificate paths and cluster-setup logic.

The value does not change the etcd version, which is derived independently (see
[[COMPONENT-ETCD]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `host`; accepted `host` | `docker` |
  `kubeadm` (unchanged).
- Kubernetes: not applicable — the value governs Kubespray's deployment method,
  not a Kubernetes API.
- `docker` mode requires a Docker container engine on the etcd nodes; `host` and
  `kubeadm` do not.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (`v2.29.0:424`,
  `v2.30.0:425`, `v2.31.0:437`).
- `roles/etcd/tasks/` — value validation and per-mode install branches.
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
