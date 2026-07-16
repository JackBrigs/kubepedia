---
id: VARIABLE-DOCKER_CLI_VERSION
type: variable
title: docker_cli_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - docker_cli_version
tags:
  - docker
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/docker/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/defaults/main.yml
    note: "Defines docker_cli_version, default '{{ docker_version }}'"
relations:
  - type: see_also
    target: VARIABLE-CONTAINER_MANAGER
---

# docker_cli_version

## Summary
Version of the docker-ce-cli package to install. The default follows the Docker engine version: `{{ docker_version }}`. Distribution-specific vars files override it on some OSes.

## Implementation
Defined in `roles/container-engine/docker/defaults/main.yml` (line 3 in all four tags):

```yaml
docker_cli_version: "{{ docker_version }}"
```

OS-specific overrides also present in all four tags:

| source_path | value |
| --- | --- |
| roles/container-engine/docker/defaults/main.yml | `{{ docker_version }}` |
| roles/container-engine/docker/vars/kylin.yml | `{{ docker_version }}` |
| roles/container-engine/docker/vars/uniontech.yml | `19.03` |

All three values are unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Only relevant when `container_manager` is `docker`; derives from `docker_version` unless overridden by a distribution vars file.

## References
- roles/container-engine/docker/defaults/main.yml
- roles/container-engine/docker/vars/kylin.yml
- roles/container-engine/docker/vars/uniontech.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
