---
id: VARIABLE-KUBE_APISERVER_AUTHORIZATION_CONFIG_AUTHORIZERS
type: variable
title: kube_apiserver_authorization_config_authorizers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_authorization_config_authorizers
tags:
  - apiserver
  - authorization
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_authorization_config_authorizers definition"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_authorization_config_authorizers

## Summary
Список авторизаторов структурированного файла `AuthorizationConfiguration` API-сервера. По умолчанию содержит два авторизатора: `Node` (name `node`) и `RBAC` (name `rbac`).

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_authorization_config_authorizers:
- type: Node
  name: node
- type: RBAC
  name: rbac
```

Ниже в файле приведён закомментированный пример добавления авторизатора `Webhook`. Значение не менялось между тегами v2.29.0–v2.31.0 (строка 530 в v2.29.0/v2.29.1, 531 в v2.30.0, 565 в v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Применяется при `kube_apiserver_use_authorization_config_file: true`. Связанные переменные: `kube_apiserver_authorization_config_api_version`, `kube_webhook_authorization`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
