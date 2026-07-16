---
id: VARIABLE-KUBE_APISERVER_AUTHENTICATION_CONFIG_API_VERSION
type: variable
title: kube_apiserver_authentication_config_api_version
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_authentication_config_api_version
tags:
  - apiserver
  - authentication
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_authentication_config_api_version definition"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_authentication_config_api_version

## Summary
Версия API (`apiVersion`) структурированного файла `AuthenticationConfiguration` API-сервера. Вычисляется по версии Kubernetes: `v1beta1` до 1.34.0, иначе `v1`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml` (строка 531 в v2.31.0):

```yaml
kube_apiserver_authentication_config_api_version: "{{ 'v1beta1' if kube_version is version('1.34.0', '<') else 'v1' }}"
```

Переменная появилась только в v2.31.0; в v2.29.0, v2.29.1 и v2.30.0 отсутствует.

## Compatibility
Только Kubespray v2.31.0. Связанные переменные: `kube_apiserver_use_authentication_config_file`, `kube_apiserver_authentication_config_anonymous`, `kube_apiserver_authentication_config_jwt`, `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
