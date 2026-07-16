---
id: VARIABLE-PROXY_ENV
type: variable
title: proxy_env
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - proxy_env
tags:
  - proxy
  - environment
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Effective proxy environment dict, derived from proxy_env_defaults plus optional SSL_CERT_FILE"
relations: []
---

# proxy_env

## Summary
Computed dictionary of proxy environment variables applied to tasks and services during deployment. It is built from `proxy_env_defaults` and, when `https_proxy_cert_file` is defined, additionally sets `SSL_CERT_FILE` to that path via `combine`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed expression:

```yaml
proxy_env: "{{ proxy_env_defaults | combine({'SSL_CERT_FILE': https_proxy_cert_file}) if https_proxy_cert_file is defined else proxy_env_defaults }}"
```

The `combine` approach avoids injecting an `__omit_place_holder__` value when no cert file is set. The expression is unchanged across v2.29.0-v2.31.0 (only the line number shifts: 760 in v2.29.0/v2.29.1, 763 in v2.30.0, 782 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `proxy_env_defaults` (which reads `http_proxy`, `https_proxy`, `no_proxy`) and on `https_proxy_cert_file`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
