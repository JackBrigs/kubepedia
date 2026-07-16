---
id: VARIABLE-CILIUM_INSTALL_EXTRA_FLAGS
type: variable
title: cilium_install_extra_flags
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_install_extra_flags
tags:
  - cilium
  - install
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Extra flags appended to the cilium install/upgrade CLI command; default empty string"
relations: []
---

# cilium_install_extra_flags

## Summary
Extra command-line flags appended to the `cilium install`/`cilium upgrade` CLI invocation. Default: `""` (empty). Useful for offline installs (e.g. pointing `--repository` at a local Helm mirror).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml`:

```yaml
cilium_install_extra_flags: ""
```

Consumed in `roles/network_plugin/cilium/tasks/apply.yml`, appended verbatim to the command:

```
{{ bin_dir }}/cilium {{ cilium_action }} --version {{ cilium_version }} -f .../cilium-values.yaml -f .../cilium-extra-values.yaml {{ cilium_install_extra_flags }}
```

The default `""` is unchanged across v2.29.0-v2.31.0 (only the line number in `defaults/main.yml` shifts between tags). In v2.31.0 `docs/operations/offline-environment.md` documents an example override `--repository {{ files_repo }}/helm.cilium.io/`, but the code default remains empty.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `cilium_version`, `cilium_action`, `bin_dir`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- roles/network_plugin/cilium/tasks/apply.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
