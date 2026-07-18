---
id: VARIABLE-NETCHECK_AGENT_IMAGE_REPO
type: variable
title: netcheck_agent_image_repo
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - netcheck_agent_image_repo
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: {{ docker_image_repo }}/mirantis/k8s-netchecker-agent"
relations: []
---
<!-- generated: variable-stub -->

# netcheck_agent_image_repo

## Summary

Kubespray variable `netcheck_agent_image_repo` — default `{{ docker_image_repo }}/mirantis/k8s-netchecker-agent`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.30.0`):

```yaml
netcheck_agent_image_repo: {{ docker_image_repo }}/mirantis/k8s-netchecker-agent
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.30.0`).
