---
id: CONCEPT-UBUNTU_24_04_K8S
type: concept
title: "Ubuntu 24.04+ and Kubernetes (Kubespray node OS)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - Ubuntu 24.04
  - Ubuntu 22.04
  - Ubuntu 20.04
  - Ubuntu 26.04
  - Ubuntu 26.04 kubespray support
  - Noble Numbat kubernetes
  - Ubuntu 24.04 kubespray
  - ubuntu cgroup v2
  - ubuntu ntpsec kubernetes
  - ubuntu node os requirements
  - supported ubuntu versions kubespray
tags:
  - os
  - ubuntu
  - nodes
  - kubespray
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "supported_os_distributions includes 'Ubuntu'; ntp_package can be ntpsec (tag v2.31.0)"
  - type: docs
    path: Ubuntu 24.04 LTS (Noble) release notes
    url: https://canonical.com/blog/ubuntu-24-04-lts-noble-numbat-is-here
    note: "24.04 ships kernel 6.8, cgroup v2 unified, systemd-timesyncd, AppArmor (verified)"
relations:
  - type: see_also
    target: CONCEPT-K8S_1_35_CHANGES
  - type: see_also
    target: CONFIG-NTP
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# Ubuntu 24.04+ and Kubernetes (Kubespray node OS)

## Summary

Ubuntu 24.04 LTS ("Noble") is a **supported** Kubespray node OS and a good fit for the
Kubernetes `1.29`–`1.35` range: it ships a recent kernel (6.8), **cgroup v2 by default**,
and modern systemd. A few 24.04 specifics matter for Kubernetes operators — time sync
(`systemd-timesyncd` vs the NTP client), cgroup v2 alignment with K8s 1.35, and
`systemd-resolved` DNS. Across the range Kubespray supports **20.04/22.04/24.04** (20.04
dropped after v2.27.x); **Ubuntu 26.04 is not yet supported by any tag** — see the
future-context note.

## Context

- Applies to Kubespray `v2.27.0`–`v2.31.0`. `Ubuntu` is in
  `supported_os_distributions`, so no `allow_unsupported_distribution_setup` is needed
  ([[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]]).

**Which Ubuntu releases each Kubespray tag claims (from README, verified per tag):**

| Kubespray | Supported Ubuntu LTS |
|-----------|----------------------|
| v2.27.0   | 20.04, 22.04, 24.04 |
| v2.29.0   | 22.04, 24.04 |
| v2.31.0   | 22.04, 24.04 |

- **20.04 (Focal)** was dropped after the v2.27.x line — not listed from v2.29.0 on.
- **26.04 (Noble's successor) is NOT supported by any tag in range** — see the future-context
  note under Compatibility. Only **22.04** and **24.04** are covered by every tag from
  v2.29.0 to the newest (v2.31.0).
- 24.04+ traits relevant here: kernel **6.8** (well above the nftables `5.13` and Cilium
  `4.9.17`/WireGuard `5.6` floors — [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]); **cgroup v2**
  unified hierarchy (default since 22.04); `systemd-timesyncd` for time; `systemd-resolved`
  managing `/etc/resolv.conf`; AppArmor enabled.

## Implementation

**cgroup v2 (a plus for 1.35).** Ubuntu 24.04 already runs cgroup v2, so it satisfies
Kubernetes `1.35`'s `failCgroupV1=true` default (nodes refuse cgroup v1) out of the box —
no migration needed ([[CONCEPT-K8S_1_35_CHANGES]]). The kubelet/containerd `systemd`
cgroup driver (Kubespray default) is the correct pairing.

**Time sync.** 24.04 ships **`systemd-timesyncd`**. If you enable Kubespray NTP
management, set **`ntp_package: ntpsec`** on 24.04 (the distro no longer ships the classic
`ntp` package) — see [[CONFIG-NTP]]. Unsynced clocks cause `x509` cert errors
([[TROUBLE-CLOCK_SKEW_TLS]]).

**DNS / resolv.conf.** `systemd-resolved` points `/etc/resolv.conf` at a stub
(`127.0.0.53`). Kubespray's `resolvconf_mode` (`host_resolvconf` default) handles node
resolver setup; verify the upstream nameservers are real, not just the stub, or pod
upstream DNS can misbehave ([[TROUBLE-DNS_EXTERNAL_RESOLUTION]]).

## Compatibility

- **Kubespray range:** Ubuntu 24.04 works across `v2.29.0`–`v2.31.0`; confirm the exact
  patch OS image against Kubespray CI notes if you hit driver/kernel edge cases.
- **cgroup driver must stay `systemd`** on cgroup v2 — don't switch to `cgroupfs`
  ([[TROUBLE-CGROUP_DRIVER_MISMATCH]]).
- **Newer than 24.04** (e.g. interim releases) may ship kernels/packages ahead of what a
  given Kubespray tag was tested on — prefer the LTS for production nodes.
- **AppArmor** is active; the Kubernetes AppArmor support is GA, so profiles apply
  normally — no special handling for a stock setup.

### Ubuntu 26.04 — future context (NOT yet supported)

`confidence: probable` for everything in this subsection — it is **future context relative
to the covered range**, not a verified claim.

- **No Kubespray tag in range (`v2.27.0`–`v2.31.0`) supports Ubuntu 26.04.** The string
  `26.04` does not appear anywhere in the `v2.31.0` source; the newest tag's README lists
  only **22.04, 24.04**. Running Kubespray on 26.04 today requires
  `allow_unsupported_distribution_setup: true` and is untested — expect preflight and
  package-name surprises ([[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]]).
- **What to expect when support lands** (general reasoning, verify against the tag that
  first lists 26.04): 26.04 continues cgroup v2-only (good for K8s `1.35`
  `failCgroupV1` — [[CONCEPT-K8S_1_35_CHANGES]]), ships a newer kernel (well above every
  networking floor — [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]), keeps `systemd-timesyncd` +
  `ntpsec` (so [[CONFIG-NTP]] guidance holds) and `systemd-resolved`. The likely friction
  points are the same as any new LTS: package/repo names, a Python version bump affecting
  Ansible, and CRI/CNI packages built for the new release.
- **Recommendation:** for production, stay on **24.04 LTS** until a Kubespray release
  explicitly lists 26.04 in `supported_os_distributions` / README. Re-verify this doc when
  that tag ships.

## References

- Kubespray `supported_os_distributions` / `ntp_package` at tag `v2.31.0`; Ubuntu 24.04 LTS
  release notes. Related: [[CONCEPT-K8S_1_35_CHANGES]] (cgroup v1 removal), [[CONFIG-NTP]],
  [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]].
