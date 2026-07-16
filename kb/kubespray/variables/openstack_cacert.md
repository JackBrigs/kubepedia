---
id: VARIABLE-OPENSTACK_CACERT
type: variable
title: openstack_cacert
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - openstack_cacert
tags:
  - openstack
  - tls
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "CA certificate for OpenStack API; default read from the OS_CACERT environment variable."
relations: []
---

# openstack_cacert

## Summary
Provides the CA certificate used to verify the OpenStack API endpoint for the cloud provider integration. By default the value is read from the `OS_CACERT` environment variable of the host running Ansible.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed default:

```yaml
openstack_cacert: "{{ lookup('env', 'OS_CACERT') }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number drifts from 493 in v2.29.0 to 501 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the OpenStack cloud provider integration. Related variables: `openstack_blockstorage_ignore_volume_az`, `openstack_lbaas_enabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
