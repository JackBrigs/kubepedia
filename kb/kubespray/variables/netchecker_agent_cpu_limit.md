---
id: VARIABLE-NETCHECKER_AGENT_CPU_LIMIT
type: variable
title: netchecker_agent_cpu_limit
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - netchecker_agent_cpu_limit
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: 30m"
relations: []
---
<!-- generated: variable-stub -->

# netchecker_agent_cpu_limit

## Summary

Kubespray variable `netchecker_agent_cpu_limit` — default `30m`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
netchecker_agent_cpu_limit: 30m
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.30.0`).
