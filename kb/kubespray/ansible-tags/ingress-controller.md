---
id: TAG-INGRESS_CONTROLLER
type: ansible_tag
title: ingress-controller (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - ingress-controller
  - --tags ingress-controller
tags:
  - ansible-tag
  - ingress
  - addons
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "85"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes-apps/ingress_controller tagged ingress-controller; hosts kube_control_plane"
relations:
  - type: see_also
    target: TAG-APPS
---

# ingress-controller (Ansible run-tag)

## Summary

`ingress-controller` runs the `kubernetes-apps/ingress_controller` role, which
deploys the enabled ingress controller add-on(s) (e.g. ingress-nginx, ALB) to the
cluster. It runs only for the add-ons enabled in inventory.

## Context

- **Playbook:** `cluster.yml` (the "Install Kubernetes apps" play).
- **Hosts:** `kube_control_plane`.
- One of the dedicated add-on tags alongside [[TAG-APPS]].

## Implementation

```yaml
# playbooks/cluster.yml
- { role: kubernetes-apps/ingress_controller, tags: ingress-controller }
```

The role applies the ingress-controller manifests via the API server when the
corresponding `*_enabled` flags are set.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `ingress-controller` tags the
  `kubernetes-apps/ingress_controller` role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies manifests to a running cluster;
  requires a reachable API server.

## References

- `playbooks/cluster.yml:85` — `ingress-controller` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
