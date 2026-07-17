---
id: CONFIG-NTP
type: configuration
title: "Time synchronization (NTP) in Kubespray"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp
  - time sync
  - ntp_enabled
  - ntp_servers
  - chrony
  - clock synchronization
tags:
  - operations
  - ntp
  - time
  - configuration
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "ntp_manage_config / ntp_servers / ntp_timezone / ntp_tinker_panic defaults (tag v2.31.0)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "ntp_enabled / ntp_package defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-CLOCK_SKEW_TLS
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# Time synchronization (NTP) in Kubespray

## Summary

Kubernetes needs the clocks on all nodes closely in sync — TLS handshakes, certificate
validity, etcd leases, and token expiry all depend on it. Kubespray can install and
manage an NTP client (chrony/ntp), but it is **off by default** (`ntp_enabled: false`) —
so if your image/provider doesn't already sync time, enable it.

## Configuration

Defaults:

| Variable | Default | Purpose |
|----------|---------|---------|
| `ntp_enabled` | `false` | install/enable the NTP client |
| `ntp_package` | OS-appropriate (chrony/ntp) | override the package — e.g. `ntpsec` on Ubuntu 24.04 or distros that already ship `systemd-timesyncd` |
| `ntp_manage_config` | `false` | let Kubespray write the NTP config (servers/pools) |
| `ntp_servers` | (list) | upstream NTP servers/pools (used when `ntp_manage_config`) |
| `ntp_timezone` | `""` | set the system timezone (empty = leave as-is) |
| `ntp_tinker_panic` | `false` | keep syncing despite large offsets (`true` avoids the daemon bailing on big jumps — useful for VMs that pause/resume) |
| `ntp_force_sync_immediately` | `false` | step the clock at once instead of slewing |

- Enable with `ntp_enabled: true`; to also push your own servers set
  `ntp_manage_config: true` and `ntp_servers: [...]`.
- On air-gapped networks point `ntp_servers` at an internal time source (external pools
  are unreachable).

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **If you rely on the host image/cloud to sync time**, you can leave `ntp_enabled: false`
  — but verify time actually syncs; unsynced clocks cause the classic
  `x509: certificate has expired or is not yet valid` and auth failures
  ([[TROUBLE-CLOCK_SKEW_TLS]]).
- `ntp_tinker_panic: true` is worth it for VMs that snapshot/suspend (the clock can jump
  far enough that a default NTP daemon refuses to correct it).
- Setting `ntp_timezone` under SELinux has a known pitfall — see the timezone-under-SELinux
  troubleshooting entry.

## References

- `ntp_*` defaults at tag `v2.31.0`. Clock-skew symptoms: [[TROUBLE-CLOCK_SKEW_TLS]];
  where to set: [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]].
