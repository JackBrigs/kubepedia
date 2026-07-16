---
id: TAG-BASTION
type: ansible_tag
title: bastion (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - bastion
  - --tags bastion
tags:
  - ansible-tag
  - bastion
  - ssh
sources:
  - type: code
    path: playbooks/boilerplate.yml
    lines: "17-23"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/boilerplate.yml
    note: "role bastion-ssh-config tagged [localhost, bastion]; hosts bastion[0]"
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# bastion (Ansible run-tag)

## Summary

`bastion` runs the `bastion-ssh-config` role, which generates the local SSH
configuration (ProxyCommand/jump-host) needed for Ansible to reach cluster nodes
through a bastion host. It runs early, before the cluster is touched.

## Context

- **Playbook:** `boilerplate.yml` (imported by `cluster.yml`, `upgrade-cluster.yml`,
  `scale.yml`, etc.).
- **Hosts:** `bastion[0]`.
- Also carries the `localhost` tag (the SSH config is written on the control
  machine).
- Only relevant when a `bastion` host group is defined in the inventory.

## Implementation

`playbooks/boilerplate.yml`:

```yaml
- name: Install bastion ssh config
  hosts: bastion[0]
  roles:
    - { role: bastion-ssh-config, tags: ["localhost", "bastion"] }
```

The role writes the SSH client config so subsequent connections to cluster nodes
are proxied through the bastion.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `bastion` tags the `bastion-ssh-config` role in
  `boilerplate.yml`.
- **Standalone-run safety: safe.** Writes local SSH config only; no changes to
  cluster nodes. No-op when no `bastion` group is defined.

## References

- `playbooks/boilerplate.yml:17-23` — `bastion` tag and role.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
