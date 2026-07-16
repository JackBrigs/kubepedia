---
id: PRACTICE-NTP
type: best_practice
title: NTP time synchronization in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - NTP sync
tags:
  - ntp
  - time
  - air-gap
sources:
  - type: docs
    path: docs/advanced/ntp.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/ntp.md
    note: "Enabling and customizing NTP/chrony time synchronization"
relations: []
---

# NTP time synchronization in Kubespray

## Summary
Kubespray can manage NTP-based clock synchronization on cluster nodes via `ntpd` or `chrony`. Accurate time sync is important for Kubernetes and etcd correctness. NTP management is opt-in and covers enabling the service, supplying custom servers for air-gapped clusters, setting the timezone, and VM-specific tweaks.

## Context
Applies when you want Kubespray to install and configure time synchronization on nodes. Especially relevant for air-gapped environments (nodes cannot reach public NTP pools) and VM deployments (prone to clock drift). All behavior is driven by `ntp_*` variables; by default NTP is not enabled.

## Implementation
- `ntp_enabled: true` — starts and enables the `ntpd`/`chrony` service at boot; time syncs automatically.
- `ntp_manage_config: true` plus `ntp_servers` — lets Kubespray write the NTP config file with custom servers (needed in air-gap environments):
  ```yaml
  ntp_enabled: true
  ntp_manage_config: true
  ntp_servers:
    - "0.your-ntp-server.org iburst"
    - "1.your-ntp-server.org iburst"
    - "2.your-ntp-server.org iburst"
    - "3.your-ntp-server.org iburst"
  ```
- `ntp_timezone` — sets the node timezone (e.g. `Etc/UTC`, `Asia/Shanghai`). If unset, the timezone is not changed.
- `ntp_tinker_panic: true` — enables `tinker panic`, useful in VMs to avoid clock drift. Only takes effect when `ntp_manage_config` is true.
- `ntp_force_sync_immediately: true` — forces an immediate time sync right after NTP install; useful on freshly installed systems.
- `ntp_package: ntpsec` — use on Ubuntu 24.04 or any distribution that already ships `systemd-timesyncd`.

Caveat: `ntp_tinker_panic` requires `ntp_manage_config: true` to have any effect.

## References
- docs/advanced/ntp.md (tag v2.31.0 1c9add4)
