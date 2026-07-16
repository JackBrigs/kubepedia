---
id: VARIABLE-IS_FEDORA_COREOS
type: variable
title: is_fedora_coreos
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - is_fedora_coreos
tags:
  - os
  - bootstrap
  - coreos
sources:
  - type: code
    path: roles/bootstrap_os/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/defaults/main.yml
    note: "Flag indicating the target host runs Fedora CoreOS, defaults to false"
relations: []
---

# is_fedora_coreos

## Summary
Boolean flag indicating whether the target host is running Fedora CoreOS, which drives OS-specific bootstrap behavior. It defaults to `false` and is set to `true` only when Fedora CoreOS is detected.

## Implementation
Defined with default `false` in both `roles/bootstrap_os/defaults/main.yml` and `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
is_fedora_coreos: false
```

It is overridden to `true` in `roles/bootstrap_os/vars/fedora-coreos.yml`:

```yaml
is_fedora_coreos: true
```

Values are unchanged across v2.29.0–v2.31.0 (bootstrap_os defaults line 37 in v2.29.0–v2.30.0, line 45 in v2.31.0; kubespray_defaults line 18 in all tags; vars/fedora-coreos.yml line 2 in all tags).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed by the `bootstrap_os` role and OS-conditional tasks.

## References
- roles/bootstrap_os/defaults/main.yml
- roles/bootstrap_os/vars/fedora-coreos.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
