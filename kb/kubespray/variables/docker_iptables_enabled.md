---
id: VARIABLE-DOCKER_IPTABLES_ENABLED
type: variable
title: docker_iptables_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_iptables_enabled
tags:
  - docker
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Whether the Docker daemon manages iptables rules; default \"false\""
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_iptables_enabled

## Summary
Controls whether the Docker daemon is allowed to add/manage iptables rules. Defaults to the string `"false"`, so Docker does not manipulate iptables (Kubernetes/CNI manage networking).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
docker_iptables_enabled: "false"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when Docker is the selected container engine.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
