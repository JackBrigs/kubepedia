---
id: TAG-PREINSTALL
type: ansible_tag
title: preinstall (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - preinstall
  - --tags preinstall
tags:
  - ansible-tag
  - preinstall
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "15,96"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role kubernetes/preinstall tagged preinstall; also a late resolvconf pass tagged resolvconf"
  - type: code
    path: roles/kubernetes/preinstall/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes/preinstall/tasks
    note: "swapoff, verify-settings, create_directories, resolvconf, systemd-resolved"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# preinstall (Ansible run-tag)

## Summary

`preinstall` runs the `kubernetes/preinstall` role, which prepares nodes before
Kubernetes is installed: disabling swap, gathering/setting facts, verifying
inventory settings, creating required directories, and configuring host DNS
(`resolv.conf`/`systemd-resolved`).

## Context

- **Playbook:** `cluster.yml` (the "Prepare for etcd install" play).
- **Hosts:** `k8s_cluster:etcd`.
- A separate late pass re-applies resolv.conf under the `resolvconf` tag once
  cluster DNS is up (`dns_late: true`).

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/preinstall, tags: preinstall }
...
- { role: kubernetes/preinstall, when: "dns_mode != 'none' and resolvconf_mode == 'host_resolvconf'", tags: resolvconf, dns_late: true }
```

Task files include `0010-swapoff.yml`, `0040-verify-settings.yml`,
`0050-create_directories.yml`, `0060-resolvconf.yml`, `0061-systemd-resolved.yml`.
The setting checks here complement the inventory-validation assert on
`kube_version` (see [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `preinstall` tags the `kubernetes/preinstall`
  role in `cluster.yml`.
- **Standalone-run safety: risky.** Mostly idempotent host preparation, but it
  changes swap, directories, and DNS configuration on the hosts; it is a
  prerequisite for later roles rather than a read-only step.

## References

- `playbooks/cluster.yml:15,96` — `preinstall` and late `resolvconf` passes.
- `roles/kubernetes/preinstall/tasks/` — host preparation tasks.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
