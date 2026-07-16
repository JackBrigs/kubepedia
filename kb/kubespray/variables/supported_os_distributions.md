---
id: VARIABLE-SUPPORTED_OS_DISTRIBUTIONS
type: variable
title: supported_os_distributions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - supported_os_distributions
tags:
  - preinstall
  - os
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "List of OS distributions Kubespray asserts as supported during preinstall"
relations: []
---

# supported_os_distributions

## Summary
List of operating-system distributions that Kubespray considers supported. It is
used in preinstall assertion checks to fail early on an unsupported OS.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` as a list:

```yaml
supported_os_distributions:
  - 'RedHat'
  - 'CentOS'
  - 'Fedora'
  - 'Ubuntu'
  - 'Debian'
  - 'Flatcar'
  - 'Flatcar Container Linux by Kinvolk'
  - 'Suse'
  - 'openSUSE Leap'
  - 'openSUSE Tumbleweed'
  - 'ClearLinux'
  - 'OracleLinux'
  - 'AlmaLinux'
  - 'Rocky'
  - 'Amazon'
```

The list is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Used by the preinstall OS-support assertion;
matched against `ansible_distribution`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
