---
id: VARIABLE-PREINSTALL_SELINUX_STATE
type: variable
title: preinstall_selinux_state
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - preinstall_selinux_state
tags:
  - preinstall
  - security
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Target SELinux state set during preinstall (default: permissive)"
relations: []
---

# preinstall_selinux_state

## Summary
The SELinux mode Kubespray configures on nodes during the preinstall stage. Default is `permissive`, so SELinux logs but does not enforce.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 7):

```yaml
preinstall_selinux_state: permissive
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged). Relevant on SELinux-enabled distributions (RHEL-family). Accepted SELinux states include `enforcing`, `permissive`, and `disabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
