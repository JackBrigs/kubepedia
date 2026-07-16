---
id: VARIABLE-PROXY_DISABLE_ENV
type: variable
title: proxy_disable_env
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - proxy_disable_env
tags:
  - proxy
  - network
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Dict of proxy env vars set empty to disable proxying for a command/context"
relations: []
---

# proxy_disable_env

## Summary
A dictionary of proxy-related environment variables all set to empty strings, used to explicitly disable HTTP(S)/FTP/ALL proxying in contexts where a configured proxy must be bypassed. Covers both upper- and lower-case variants.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 762 in v2.29.0/v2.29.1, 765 in v2.30.0, 784 in v2.31.0):

```yaml
proxy_disable_env:
  ALL_PROXY: ''
  FTP_PROXY: ''
  HTTPS_PROXY: ''
  HTTP_PROXY: ''
  NO_PROXY: ''
  all_proxy: ''
  ftp_proxy: ''
  http_proxy: ''
  https_proxy: ''
  no_proxy: ''
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts).

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged). Applied as an `environment:` override on tasks that must run without proxying. Related: `http_proxy`, `https_proxy`, `no_proxy`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
