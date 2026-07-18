---
id: VARIABLE-SSH_BASTION_CONFIG_NAME
type: variable
title: ssh_bastion_config_name
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ssh_bastion_config_name
tags:
  - bastion-ssh-config
  - variable
sources:
  - type: code
    path: roles/bastion-ssh-config/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bastion-ssh-config/defaults/main.yml
    note: "default: ssh-bastion.conf"
relations: []
---
<!-- generated: variable-stub -->

# ssh_bastion_config_name

## Summary

Kubespray variable `ssh_bastion_config_name` — default `ssh-bastion.conf`. Defined in `roles/bastion-ssh-config/defaults/main.yml`. Present in Kubespray
`v2.31.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/bastion-ssh-config/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
ssh_bastion_config_name: ssh-bastion.conf
```

## Compatibility

Present in the Kubespray tags `v2.31.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/bastion-ssh-config/defaults/main.yml` (Kubespray `v2.31.0`).
