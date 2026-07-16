---
id: VARIABLE-ANSIBLE_SSH_COMMON_ARGS
type: variable
title: ansible_ssh_common_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ansible_ssh_common_args
tags:
  - ssh
  - bastion
  - connection
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Sets SSH ProxyCommand args when a bastion host is present"
relations: []
---

# ansible_ssh_common_args

## Summary
Common SSH arguments Ansible passes on every connection. Kubespray computes this to inject a `ProxyCommand` through a bastion host when a `bastion` entry exists in the inventory; otherwise it resolves to an empty string.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 4):
```yaml
ansible_ssh_common_args: "{% if 'bastion' in groups['all'] %} -o ProxyCommand='ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -W %h:%p -p {{ hostvars['bastion']['ansible_port'] | default(22) }} {{ hostvars['bastion']['ansible_user'] }}@{{ hostvars['bastion']['ansible_host'] }} {% if ansible_ssh_private_key_file is defined %}-i {{ ansible_ssh_private_key_file }}{% endif %} ' {% endif %}"
```
This computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. (A separate template `contrib/terraform/openstack/.../ansible_bastion_template.txt` also emits this variable.)

## Compatibility
Kubespray v2.29.0 through v2.31.0. Uses `hostvars['bastion']` (ansible_port/user/host) and optional `ansible_ssh_private_key_file`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
