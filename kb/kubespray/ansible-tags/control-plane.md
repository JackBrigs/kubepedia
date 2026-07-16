---
id: TAG-CONTROL_PLANE
type: ansible_tag
title: control-plane (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - control-plane
  - --tags control-plane
  - master
tags:
  - ansible-tag
  - control-plane
  - kubeadm
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "34-41"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "hosts: kube_control_plane; role kubernetes/control-plane tagged control-plane"
  - type: code
    path: playbooks/upgrade_cluster.yml
    lines: "58"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/playbooks/upgrade_cluster.yml
    note: "v2.29.0/v2.29.1: same role tagged master (legacy); renamed to control-plane by v2.30.0"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# control-plane (Ansible run-tag)

## Summary

`control-plane` is the run-tag that deploys and configures the Kubernetes control
plane: it runs the `kubernetes/control-plane` role on `kube_control_plane` hosts —
rendering the kubeadm configuration and invoking kubeadm to bring up
`kube-apiserver`, `kube-controller-manager`, and `kube-scheduler` (see
[[CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS]]).

## Context

- **Playbooks:** `cluster.yml` (the "Install the control plane" play) and
  `upgrade-cluster.yml`.
- **Affected host group:** `kube_control_plane`.
- **Related roles under the same tag:** `win_nodes/kubernetes_patch` is tagged
  `["control-plane", "win_nodes"]` for Windows-node patching.
- Uses the kubeadm config format from
  [[CONFIG-KUBEADM_CONFIG_API_VERSION]] (`v1beta4`).

## Implementation

In `playbooks/cluster.yml` the control-plane play runs on `kube_control_plane`:

```yaml
- name: Install the control plane
  hosts: kube_control_plane
  roles:
    - { role: kubespray_defaults }
    - { role: kubernetes/control-plane, tags: control-plane }
```

The `kubernetes/control-plane` role generates the kubeadm ClusterConfiguration
(`kubeadm-config.v1beta4.yaml.j2`) and runs `kubeadm init`/`join` for control-plane
nodes, plus certificate, kubeconfig, and static-pod setup.

**Naming history (`master` → `control-plane`):** in `cluster.yml` the tag is
`control-plane` throughout `v2.29.0`–`v2.31.0`. In `upgrade_cluster.yml` the same
role kept the **legacy `master` tag** in `v2.29.0` and `v2.29.1`
(`{ role: kubernetes/control-plane, tags: master, upgrade_cluster_setup: true }`);
it was renamed to `control-plane` by `v2.30.0`. The `master` alias is retained here
for discoverability.

| Kubespray | tag in cluster.yml | tag in upgrade_cluster.yml |
|-----------|--------------------|----------------------------|
| v2.29.0   | control-plane      | master (legacy)            |
| v2.29.1   | control-plane      | master (legacy)            |
| v2.30.0   | control-plane      | control-plane              |
| v2.31.0   | control-plane      | control-plane              |

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `--tags control-plane` runs the
  `kubernetes/control-plane` role on `kube_control_plane`.
- For upgrades on `v2.29.0`/`v2.29.1`, the equivalent step in
  `upgrade-cluster.yml` responds to `--tags master`.
- **Standalone-run safety: risky.** Requires gathered facts, a reachable etcd, and
  downloaded artifacts; it drives kubeadm and can restart control-plane static
  pods. Not a no-op.

## References

- `playbooks/cluster.yml:34-41` — control-plane play and tag.
- `playbooks/upgrade_cluster.yml:58` — legacy `master` tag (v2.29.0 `9991412`,
  v2.29.1 `0c6a295`), renamed by v2.30.0 `f4ccdb5`.
- `roles/kubernetes/control-plane/` — role body (kubeadm config + init/join).
- Verified on tags v2.29.0, v2.29.1, v2.30.0, v2.31.0 `1c9add4`.
