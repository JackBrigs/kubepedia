---
id: TAG-POLICY_CONTROLLER
type: ansible_tag
title: policy-controller (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - policy-controller
  - --tags policy-controller
tags:
  - ansible-tag
  - network-policy
  - addons
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "84"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes-apps/policy_controller tagged policy-controller; hosts kube_control_plane"
relations:
  - type: see_also
    target: TAG-NETWORK
---

# policy-controller (Ansible run-tag)

## Summary

`policy-controller` runs the `kubernetes-apps/policy_controller` role, which
deploys the network-policy controller add-on when enabled (for CNIs that need a
separate policy controller). It complements the CNI installed under
[[TAG-NETWORK]].

## Context

- **Playbook:** `cluster.yml` (the "Install Kubernetes apps" play).
- **Hosts:** `kube_control_plane`.

## Implementation

```yaml
# playbooks/cluster.yml
- { role: kubernetes-apps/policy_controller, tags: policy-controller }
```

The role applies the policy-controller manifests via the API server when the
corresponding feature is enabled in inventory.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `policy-controller` tags the
  `kubernetes-apps/policy_controller` role in `cluster.yml`.
- **Standalone-run safety: risky.** Applies manifests to a running cluster;
  requires a reachable API server.

## References

- `playbooks/cluster.yml:84` — `policy-controller` tag.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
