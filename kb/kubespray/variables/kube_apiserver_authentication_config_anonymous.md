---
id: VARIABLE-KUBE_APISERVER_AUTHENTICATION_CONFIG_ANONYMOUS
type: variable
title: kube_apiserver_authentication_config_anonymous
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_authentication_config_anonymous
tags:
  - apiserver
  - authentication
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_authentication_config_anonymous definition"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_authentication_config_anonymous

## Summary
Секция `anonymous` структурированной `AuthenticationConfiguration` API-сервера. По умолчанию включает анонимный доступ по значению `kube_api_anonymous_auth` и не задаёт условий. Используется только при `kube_apiserver_use_authentication_config_file: true`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml` (строка 532 в v2.31.0):

```yaml
kube_apiserver_authentication_config_anonymous:
  enabled: "{{ kube_api_anonymous_auth }}"
  conditions: []
```

Переменная появилась только в v2.31.0; в v2.29.0, v2.29.1 и v2.30.0 отсутствует.

## Compatibility
Только Kubespray v2.31.0. Часть структурированной AuthenticationConfiguration (GA в Kubernetes v1.34). Связанные переменные: `kube_apiserver_use_authentication_config_file`, `kube_apiserver_authentication_config_api_version`, `kube_api_anonymous_auth`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
