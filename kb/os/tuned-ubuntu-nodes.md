---
id: CONCEPT-TUNED_UBUNTU
type: concept
title: "tuned on Ubuntu Kubernetes nodes — what it owns and what already owns the same keys"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - tuned ubuntu
  - tuned-adm
  - tuned profile kubernetes
  - tuned kubernetes node
  - tuned sysctl ubuntu
  - tuned-adm verify
tags:
  - os
  - ubuntu
  - tuned
  - sysctl
  - nodes
sources:
  - type: code
    path: kubespray v2.31.0 — full-tree search for "tuned"
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
    note: "no matches: Kubespray neither installs, configures nor removes tuned at any tag of the envelope"
  - type: docs
    path: Ubuntu procps — /etc/sysctl.d/10-ptrace.conf
    url: https://gemfury.com/dcip/deb:procps/procps-2:3.3.10-4ubuntu2.4-amd64/content/etc/sysctl.d/10-ptrace.conf
    note: "Ubuntu ships kernel.yama.ptrace_scope = 1 as a package-owned file, replaced on package upgrade"
  - type: docs
    path: Ubuntu — restricted unprivileged user namespaces
    url: https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces
    note: "kernel.apparmor_restrict_unprivileged_userns introduced in 23.10, on by default in 24.04"
relations:
  - type: see_also
    target: CONCEPT-UBUNTU_24_04_K8S
  - type: see_also
    target: CONCEPT-TUNED_SYSCTL_OWNERSHIP
  - type: see_also
    target: TROUBLE-TUNED_VERIFY_MISSING_SYSCTL
---

# tuned on Ubuntu Kubernetes nodes — what it owns and what already owns the same keys

## Summary

`tuned` is a profile-driven tuning daemon: a profile declares sysctl values, sysfs writes, kernel
module options and CPU/disk/network knobs, and the daemon applies them and can **verify** that the
running system still matches. On a Kubernetes node it is almost always a *second* owner of settings
that something else already writes — which is where every problem in this layer comes from.

**Kubespray does not manage tuned.** A full-tree search of the tagged source at v2.31.0 returns no
match for `tuned`: it is neither installed, configured nor removed by any role. A tuned profile on a
Kubespray node therefore arrives from the OS image, a separate configuration-management repo, or by
hand, and a Kubespray run will never restore or repair it.

## Context

**Where things live on Ubuntu.** Stock profiles ship in `/usr/lib/tuned/profiles/<name>/tuned.conf`;
administrator profiles go in `/etc/tuned/profiles/<name>/tuned.conf` (older layout:
`/etc/tuned/<name>/tuned.conf`) and win over a stock profile of the same name. A custom profile
normally inherits with `include=`, and everything the parent declares is applied and verified too —
including plugins the node has no hardware for.

Unlike RHEL-family distributions, **tuned is not installed or enabled by default on Ubuntu**; it is
an explicit choice, which is why an Ubuntu fleet often has it on some nodes and not others.

**Ubuntu already owns some of the same keys.** Two collisions matter on this OS:

- **`kernel.yama.ptrace_scope`** — Ubuntu ships `/etc/sysctl.d/10-ptrace.conf` with the value `1`,
  and that file belongs to the **procps package**: it is replaced on package upgrade, so a local
  edit does not survive. A tuned profile that sets `2` wins only until something re-applies
  `sysctl --system` or the boot-time `systemd-sysctl` pass ordering changes.
- **unprivileged user namespaces** — `kernel.unprivileged_userns_clone` is a Debian/Ubuntu-carried,
  all-or-nothing sysctl. From Ubuntu 23.10 the granular
  `kernel.apparmor_restrict_unprivileged_userns` was introduced and is **on by default in 24.04**.
  A profile written for an older release can reference a key the running kernel no longer exposes.
  Do not assume either key exists — read it before writing a profile that depends on it:

```bash
sysctl -a 2>/dev/null | grep -E 'userns|ptrace_scope'
```

**Ordering decides who wins, and it differs by event.** At boot, `systemd-sysctl` applies
`/etc/sysctl.d/*` and then `tuned.service` starts and applies the profile — tuned wins. During
operations that is reversed: an Ansible run that writes a sysctl file and reloads it, or a
`sysctl --system`, lands *after* tuned and wins until the next profile re-apply. Nothing detects the
change; only `tuned-adm verify` notices, and only when it is next run.

**Verification semantics.** `tuned-adm verify` compares every managed setting against the live
system and exits non-zero if a single one differs. It has no notion of "someone else legitimately
owns this key" — a value overwritten by kube-proxy or by an Ansible run is reported exactly like a
misconfiguration. That property makes tuned a useful drift detector and a poor monitoring source
unless the profile contains only settings tuned genuinely owns.

**Practical rule for a Kubernetes node:** a key belongs in a tuned profile only if **no other
component writes it**. Everything kube-proxy configures (conntrack limits and timeouts), everything
Kubespray writes (`net.ipv4.ip_local_reserved_ports`), and everything the distribution ships as a
package-owned sysctl file (`kernel.yama.ptrace_scope` on Ubuntu) should be managed there, not here —
see [[CONCEPT-TUNED_SYSCTL_OWNERSHIP]].

## References

- Kubespray v2.31.0 tree — no `tuned` references (verified 2026-07-28).
- Ubuntu `procps` package file `/etc/sysctl.d/10-ptrace.conf`; Ubuntu 23.10/24.04 unprivileged
  user-namespace restriction notes.
- Node OS baseline: [[CONCEPT-UBUNTU_24_04_K8S]]; ownership map: [[CONCEPT-TUNED_SYSCTL_OWNERSHIP]].
