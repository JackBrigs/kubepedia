---
id: VARIABLE-SYSTEMD_RESOLVED_DISABLE_STUB_LISTENER
type: variable
title: systemd_resolved_disable_stub_listener
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - systemd_resolved_disable_stub_listener
tags:
  - dns
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Whether to disable the systemd-resolved DNSStubListener; computed from OS family"
relations: []
---

# systemd_resolved_disable_stub_listener

## Summary
Controls whether the systemd-resolved `DNSStubListener` is disabled during preinstall. Default is computed to `true` only on Flatcar hosts, otherwise `false`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` as `systemd_resolved_disable_stub_listener: "{{ ansible_os_family in ['Flatcar', 'Flatcar Container Linux by Kinvolk'] }}"`. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (all at line 107).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Value depends on the detected `ansible_os_family`; evaluates to `true` for Flatcar / Flatcar Container Linux by Kinvolk and `false` elsewhere.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
