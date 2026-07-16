---
id: VARIABLE-PROXY_ENV_DEFAULTS
type: variable
title: proxy_env_defaults
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - proxy_env_defaults
tags:
  - proxy
  - environment
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Base proxy environment dict built from http_proxy/https_proxy/no_proxy"
relations: []
---

# proxy_env_defaults

## Summary
Base dictionary of proxy environment variables, defining both lowercase and uppercase forms of `http_proxy`, `https_proxy`, and `no_proxy`. Each entry defaults to an empty string when the corresponding `*_proxy` variable is not set. It is the foundation from which `proxy_env` is computed.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
proxy_env_defaults:
  http_proxy: "{{ http_proxy | default('') }}"
  HTTP_PROXY: "{{ http_proxy | default('') }}"
  https_proxy: "{{ https_proxy | default('') }}"
  HTTPS_PROXY: "{{ https_proxy | default('') }}"
  no_proxy: "{{ no_proxy | default('') }}"
  NO_PROXY: "{{ no_proxy | default('') }}"
```

Unchanged across v2.29.0-v2.31.0 (defined at line 750 in v2.29.0/v2.29.1, 753 in v2.30.0, 772 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Consumed by `proxy_env`; reads user-set `http_proxy`, `https_proxy`, `no_proxy`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
