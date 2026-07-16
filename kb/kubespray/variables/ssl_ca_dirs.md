---
id: VARIABLE-SSL_CA_DIRS
type: variable
title: ssl_ca_dirs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ssl_ca_dirs
tags:
  - certificates
  - security
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "OS-family dependent list of CA certificate directories mounted into components"
relations: []
---

# ssl_ca_dirs

## Summary
An OS-family dependent list of host directories that contain CA certificates.
It is used to expose the host trust store to Kubernetes components. The value is
a Jinja-rendered list whose contents depend on `ansible_os_family`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a templated
block scalar:

```yaml
ssl_ca_dirs: |-
  [
  {% if ansible_os_family in ['Flatcar', 'Flatcar Container Linux by Kinvolk'] -%}
  '/usr/share/ca-certificates',
  {% elif ansible_os_family == 'RedHat' -%}
  '/etc/pki/tls',
  '/etc/pki/ca-trust',
  {% elif ansible_os_family == 'Debian' -%}
  '/usr/share/ca-certificates',
  {% endif -%}
  ]
```

The definition is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Resolves per `ansible_os_family`
(Flatcar, RedHat, Debian handled explicitly; other families yield an empty
list).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
