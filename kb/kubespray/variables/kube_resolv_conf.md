---
id: VARIABLE-KUBE_RESOLV_CONF
type: variable
title: kube_resolv_conf
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_resolv_conf
tags:
  - kubelet
  - dns
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_resolv_conf default /etc/resolv.conf"
relations: []
---

# kube_resolv_conf

## Summary
Path to the resolv.conf file that kubelet uses. Default is `/etc/resolv.conf`, overridden to `/run/systemd/resolve/resolv.conf` on systemd-resolved distributions (Fedora, Ubuntu 18/20/22/24).

## Implementation
Base default in `roles/kubernetes/node/defaults/main.yml` at line 10:

```yaml
kube_resolv_conf: "/etc/resolv.conf"
```

OS-specific overrides in `roles/kubernetes/node/vars/` (fedora.yml, ubuntu-18.yml, ubuntu-20.yml, ubuntu-22.yml, ubuntu-24.yml) set:

```yaml
kube_resolv_conf: "/run/systemd/resolve/resolv.conf"
```

Both the default and the overrides are unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. The applied value depends on the target OS (systemd-resolved distributions override the base default).

## References
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/node/vars/{fedora,ubuntu-18,ubuntu-20,ubuntu-22,ubuntu-24}.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
