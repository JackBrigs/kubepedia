---
id: VARIABLE-ETCD_DEPLOYMENT_TYPE
type: variable
title: etcd_deployment_type
status: active
kubespray_version: v2.29.0
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
    note: "etcd_deployment_type: host"
  - type: code
    path: roles/etcd/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0/roles/etcd/tasks
    note: "Guards etcd_deployment_type in ['host', 'docker', 'kubeadm'] select install method."
relations:
  - type: part_of
    target: COMPONENT-ETCD
---

# etcd_deployment_type

## Summary

`etcd_deployment_type` selects how Kubespray installs and runs the etcd cluster
in Kubespray `v2.29.0`. It is defined in the `kubespray_defaults` role and read by
the `etcd` role to choose the installation method. The default is `host`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml:424`:

```yaml
etcd_deployment_type: host
```

The `etcd` role validates the value against a fixed set and branches on it:

```
etcd_deployment_type in ['host', 'docker', 'kubeadm']
```

Accepted values in `v2.29.0`:

- `host` (default) — etcd is installed as a static binary on the host and run as a
  systemd service. In this mode Kubespray downloads the etcd binary and verifies
  it against `etcd_binary_checksums`.
- `docker` — etcd runs as a container managed by the Docker engine. Selecting this
  value also forces `deploy_container_engine` for the etcd nodes
  (`roles/kubespray_defaults/defaults/main/main.yml:322`).
- `kubeadm` — etcd runs as a kubeadm-managed static pod on the control plane. This
  changes certificate paths and cluster-setup logic in the `etcd` role.

The value does not change the etcd version, which is derived independently (see
[[COMPONENT-ETCD]]).

## Compatibility

- Kubespray: `v2.29.0` (this document).
- Kubernetes: not applicable — the value governs Kubespray's deployment method,
  not a Kubernetes API.
- The `docker` mode requires a Docker container engine on the etcd nodes; `host`
  and `kubeadm` do not.

## References

- `roles/kubespray_defaults/defaults/main/main.yml:424` — default value.
- `roles/etcd/tasks/` — value validation and per-mode installation branches
  (tag `v2.29.0`, commit `9991412`).
