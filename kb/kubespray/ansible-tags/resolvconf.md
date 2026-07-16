---
id: TAG-RESOLVCONF
type: ansible_tag
title: resolvconf (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - resolvconf
  - --tags resolvconf
tags:
  - ansible-tag
  - dns
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "96"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "kubernetes/preinstall re-run tagged resolvconf, dns_late: true; when dns_mode != none and resolvconf_mode == host_resolvconf"
relations:
  - type: see_also
    target: TAG-PREINSTALL
  - type: see_also
    target: COMPONENT-COREDNS
---

# resolvconf (Ansible run-tag)

## Summary

`resolvconf` runs a late pass of the `kubernetes/preinstall` role (`dns_late:
true`) that applies host `resolv.conf` changes **after** cluster DNS is up, so
nodes resolve names through the in-cluster DNS (see [[COMPONENT-COREDNS]]).

## Context

- **Playbook:** `cluster.yml` (the final "Apply resolv.conf changes now that
  cluster DNS is up" play).
- **Hosts:** `k8s_cluster`.
- **Condition:** runs only when `dns_mode != 'none'` and `resolvconf_mode ==
  'host_resolvconf'`.
- It is the deferred counterpart of the early resolv.conf work done under
  [[TAG-PREINSTALL]].

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: kubernetes/preinstall, when: "dns_mode != 'none' and resolvconf_mode == 'host_resolvconf'", tags: resolvconf, dns_late: true }
```

The same `kubernetes/preinstall` role runs with `dns_late: true`, executing only
the resolv.conf/DNS tasks appropriate for the post-DNS phase.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `resolvconf` tags the late `kubernetes/preinstall`
  pass in `cluster.yml`.
- **Standalone-run safety: risky.** Rewrites host DNS configuration; only
  meaningful once cluster DNS exists.

## References

- `playbooks/cluster.yml:96` — late `resolvconf` pass.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
