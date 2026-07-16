---
id: VARIABLE-PING_ACCESS_IP
type: variable
title: ping_access_ip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ping_access_ip
tags:
  - network
  - preinstall
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines ping_access_ip: true (whether to ping the access IP during preinstall checks)"
relations: []
---

# ping_access_ip

## Summary
Controls whether Kubespray verifies reachability of the API access IP (a ping check) during the preinstall stage. Default is `true`, meaning the access IP is expected to respond to ICMP.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 10):

```yaml
ping_access_ip: true
```

The sample inventory ships it commented out at `inventory/sample/group_vars/all/all.yml:113` (`# ping_access_ip: true`), so the role default applies unless overridden. The value `true` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged). Set to `false` for environments where the access IP does not answer ICMP (e.g. behind a load balancer that blocks ping).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/all/all.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
