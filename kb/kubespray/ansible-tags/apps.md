---
id: TAG-APPS
type: ansible_tag
title: apps (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - apps
  - --tags apps
tags:
  - ansible-tag
  - addons
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "83-87"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "kubernetes-apps role tagged apps; sibling addon roles have their own tags"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
---

# apps (Ansible run-tag)

## Summary

`apps` runs the `kubernetes-apps` role, which deploys the cluster add-ons managed
by Kubespray (DNS/CoreDNS, metrics-server, and other enabled add-ons). It is the
umbrella tag for the "Install Kubernetes apps" play; individual add-on families
also have their own tags.

## Context

- **Playbook:** `cluster.yml` (the "Install Kubernetes apps" play).
- **Hosts:** `kube_control_plane`.
- Sibling roles in the same play carry dedicated tags: `external-cloud-controller`,
  `policy-controller`, `ingress-controller`, `external-provisioner`.

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes-apps/external_cloud_controller, tags: external-cloud-controller }
- { role: kubernetes-apps/policy_controller, tags: policy-controller }
- { role: kubernetes-apps/ingress_controller, tags: ingress-controller }
- { role: kubernetes-apps/external_provisioner, tags: external-provisioner }
- { role: kubernetes-apps, tags: apps }
```

The `kubernetes-apps` role applies the enabled add-on manifests to the cluster via
the control-plane node. CoreDNS (see [[COMPONENT-COREDNS]]) is deployed here.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `apps` tags the `kubernetes-apps` role in
  `cluster.yml`.
- **Standalone-run safety: risky.** Re-applies add-on manifests to a running
  cluster; requires a reachable API server (control plane and CNI up).

## References

- `playbooks/cluster.yml:83-87` — add-on roles and the `apps` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
