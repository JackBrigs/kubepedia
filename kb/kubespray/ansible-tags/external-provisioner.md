---
id: TAG-EXTERNAL_PROVISIONER
type: ansible_tag
title: external-provisioner (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - external-provisioner
  - --tags external-provisioner
tags:
  - ansible-tag
  - storage
  - addons
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "86"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes-apps/external_provisioner tagged external-provisioner; hosts kube_control_plane"
relations:
  - type: see_also
    target: TAG-APPS
---

# external-provisioner (Ansible run-tag)

## Summary

`external-provisioner` runs the `kubernetes-apps/external_provisioner` role, which
deploys the enabled storage provisioner add-on(s) (e.g. local-path / local-volume
provisioner) to the cluster.

## Context

- **Playbook:** `cluster.yml` (the "Install Kubernetes apps" play).
- **Hosts:** `kube_control_plane`.

## Implementation

```yaml
# playbooks/cluster.yml
- { role: kubernetes-apps/external_provisioner, tags: external-provisioner }
```

The role applies the storage-provisioner manifests via the API server when the
corresponding `*_enabled` flags are set.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `external-provisioner` tags the
  `kubernetes-apps/external_provisioner` role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies manifests to a running cluster;
  requires a reachable API server.

## References

- `playbooks/cluster.yml:86` — `external-provisioner` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
