---
id: TAG-EXTERNAL_CLOUD_CONTROLLER
type: ansible_tag
title: external-cloud-controller (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - external-cloud-controller
  - --tags external-cloud-controller
tags:
  - ansible-tag
  - cloud-provider
  - addons
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "83"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes-apps/external_cloud_controller tagged external-cloud-controller; hosts kube_control_plane"
relations:
  - type: see_also
    target: TAG-APPS
---

# external-cloud-controller (Ansible run-tag)

## Summary

`external-cloud-controller` runs the `kubernetes-apps/external_cloud_controller`
role, which deploys the external cloud-controller-manager add-on for the
configured cloud provider (e.g. OpenStack, vSphere, AWS) when enabled.

## Context

- **Playbook:** `cluster.yml` (the "Install Kubernetes apps" play).
- **Hosts:** `kube_control_plane`.
- Relevant only when an external cloud provider is configured.

## Implementation

```yaml
# playbooks/cluster.yml
- { role: kubernetes-apps/external_cloud_controller, tags: external-cloud-controller }
```

The role applies the cloud-controller-manager manifests via the API server when
the corresponding cloud provider is enabled in inventory.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `external-cloud-controller` tags the
  `kubernetes-apps/external_cloud_controller` role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies manifests to a running cluster;
  requires a reachable API server.

## References

- `playbooks/cluster.yml:83` — `external-cloud-controller` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
