---
id: VARIABLE-KUBELET_FLEXVOLUMES_PLUGINS_DIR
type: variable
title: kubelet_flexvolumes_plugins_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_flexvolumes_plugins_dir
tags:
  - kubelet
  - flexvolume
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Directory for kubelet FlexVolume driver plugins"
relations: []
---

# kubelet_flexvolumes_plugins_dir

## Summary
Filesystem path where kubelet looks for FlexVolume driver plugins. Defaults to `/usr/libexec/kubernetes/kubelet-plugins/volume/exec`. If that location is not writeable, the preinstall role overrides it to `/var/lib/kubelet/volumeplugins`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 25):

```yaml
kubelet_flexvolumes_plugins_dir: /usr/libexec/kubernetes/kubelet-plugins/volume/exec
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. In `roles/kubernetes/preinstall/tasks/0020-set_facts.yml` it is re-set to `/var/lib/kubelet/volumeplugins` `when: not usr.stat.writeable`.

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- roles/kubernetes/preinstall/tasks/0020-set_facts.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
