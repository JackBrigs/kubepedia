---
id: VARIABLE-KUBE_API_RUNTIME_CONFIG
type: variable
title: kube_api_runtime_config
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_api_runtime_config
tags:
  - apiserver
  - runtime-config
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "List merged into apiserver --runtime-config; default empty list"
relations: []
---

# kube_api_runtime_config

## Summary
A list of API group/version enablement settings passed to the kube-apiserver `--runtime-config` flag (used to enable/disable specific API versions). Default is an empty list.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_api_runtime_config: []
```

Unchanged across v2.29.0-v2.31.0 (line 140 in v2.29.0/v2.29.1, line 143 in v2.30.0/v2.31.0). A commented usage example also appears in `roles/kubernetes/node/defaults/main.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Affects control-plane apiserver flags.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/node/defaults/main.yml (commented example)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
