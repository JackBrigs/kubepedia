---
id: VARIABLE-RESOLVCONF_MODE
type: variable
title: resolvconf_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - resolvconf_mode
tags:
  - dns
  - resolvconf
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Mode for configuring host DNS/resolv.conf; default host_resolvconf"
relations: []
---

# resolvconf_mode

## Summary
Selects how Kubespray configures DNS resolution on cluster hosts (`resolv.conf` handling). Defaults to `host_resolvconf`.

## Implementation
Defined as a role default in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
resolvconf_mode: host_resolvconf
```

Also exposed to users in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` with the same value. Both are unchanged across v2.29.0-v2.31.0 (role default at line 150 in all four tags; sample inventory at line 209 in v2.29.0, line 225 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Governs preinstall DNS setup; related to `remove_default_searchdomains` and `resolveconf_cloud_init_conf`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
