---
id: TAG-CONTAINER_ENGINE
type: ansible_tag
title: container-engine (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - container-engine
  - --tags container-engine
tags:
  - ansible-tag
  - container-runtime
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "16"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role container-engine tagged container-engine; when: deploy_container_engine; hosts k8s_cluster:etcd"
  - type: code
    path: roles/container-engine/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/tasks/main.yml
    note: "dispatches to the containerd/crio/docker sub-roles by container_manager"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# container-engine (Ansible run-tag)

## Summary

`container-engine` runs the `container-engine` role, which installs and configures
the container runtime selected by [[VARIABLE-CONTAINER_MANAGER]] (`containerd` by
default; also `crio` or `docker`) — see [[COMPONENT-CONTAINERD]].

## Context

- **Playbook:** `cluster.yml` (the "Prepare for etcd install" play).
- **Hosts:** `k8s_cluster:etcd`.
- **Condition:** runs only when `deploy_container_engine` is true (which is set
  for cluster nodes and for etcd nodes using `etcd_deployment_type: docker`).

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: "container-engine", tags: "container-engine", when: deploy_container_engine }
```

`roles/container-engine/tasks/main.yml` dispatches to the runtime sub-roles
(`containerd`, `cri-o`, `docker`) based on `container_manager`, installing the
runtime binaries/packages and writing its configuration (e.g.
`/etc/containerd/config.toml`).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `container-engine` tags the `container-engine`
  role in `cluster.yml`, gated on `deploy_container_engine`.
- **Standalone-run safety: risky.** Installing/reconfiguring the runtime can
  restart it; sequence with `download` (artifacts) and before `node`/kubeadm.

## References

- `playbooks/cluster.yml:16` — `container-engine` tag and `deploy_container_engine`
  gate.
- `roles/container-engine/tasks/main.yml` — runtime dispatch.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
