---
id: VARIABLE-DOCKER_LOG_OPTS
type: variable
title: docker_log_opts
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_log_opts
tags:
  - docker
  - logging
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Log-driver options passed to the Docker daemon; default max-size=50m, max-file=5"
relations: []
---

# docker_log_opts

## Summary
Log-driver options passed to the Docker daemon to bound log growth. Default caps each log file at 50 MB and keeps at most 5 files.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
docker_log_opts: "--log-opt max-size=50m --log-opt max-file=5"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies when Docker is the selected container engine.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
