---
id: TAG-ETCDCTL
type: ansible_tag
title: etcdctl (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - etcdctl
  - --tags etcdctl
tags:
  - ansible-tag
  - etcd
sources:
  - type: code
    path: roles/etcdctl_etcdutl/tasks/main.yml
    lines: "8,37"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcdctl_etcdutl/tasks/main.yml
    note: "tasks tagged etcdctl; install etcdctl and etcdutl binaries"
  - type: code
    path: roles/etcd/tasks/main.yml
    lines: "64"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/tasks/main.yml
    note: "etcd role includes the etcdctl_etcdutl role"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TAG-ETCD
---

# etcdctl (Ansible run-tag)

## Summary

`etcdctl` installs the `etcdctl` and `etcdutl` client binaries onto the target
hosts (copied from the etcd image, matching [[COMPONENT-ETCD]]). It is provided by
the `etcdctl_etcdutl` role, which is included by the `etcd` role and by the
control-plane kubeadm-etcd path.

## Context

- **Included by:** the `etcd` role (`roles/etcd/tasks/main.yml`) and
  `kubernetes/control-plane` (`kubeadm-etcd.yml`), so it runs on etcd /
  control-plane hosts.
- **Purpose:** make `etcdctl`/`etcdutl` available for operations and diagnostics
  at the etcd version the cluster runs.

## Implementation

`roles/etcdctl_etcdutl/tasks/main.yml` copies the binaries out of the etcd
container image (`{{ etcd_image_repo }}:{{ etcd_image_tag }}`) into `bin_dir`:

```yaml
with_items:
  - etcdctl
  - etcdutl
  tags:
    - etcdctl
```

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: the `etcdctl` tag installs the client binaries
  via the `etcdctl_etcdutl` role.
- **Standalone-run safety: safe.** Places client binaries; does not change the
  running etcd cluster. Useful to (re)install the tools in isolation.

## References

- `roles/etcdctl_etcdutl/tasks/main.yml:8,37` — `etcdctl` tag and binary install.
- `roles/etcd/tasks/main.yml:64` — inclusion of the role.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
