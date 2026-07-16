---
id: VARIABLE-BIN_DIR
type: variable
title: bin_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - bin_dir
tags:
  - paths
  - install
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Directory where binaries are installed; default /usr/local/bin"
relations: []
---

# bin_dir

## Summary
Directory into which Kubespray installs Kubernetes and related binaries. Default value is `/usr/local/bin`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
bin_dir: /usr/local/bin
```

Also exposed to users in `inventory/sample/group_vars/all/all.yml` with the same value. On Flatcar/CoreOS it is overridden in `roles/bootstrap_os/vars/flatcar.yml` to `/opt/bin`. It is also re-declared as `/usr/local/bin` in `roles/recover_control_plane/control-plane/defaults/main.yml`. The main default `/usr/local/bin` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. Note the Flatcar override to `/opt/bin`; the sample inventory value matches the role default.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/all/all.yml
- roles/bootstrap_os/vars/flatcar.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
