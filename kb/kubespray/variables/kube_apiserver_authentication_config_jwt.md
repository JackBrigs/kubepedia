---
id: VARIABLE-KUBE_APISERVER_AUTHENTICATION_CONFIG_JWT
type: variable
title: kube_apiserver_authentication_config_jwt
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_authentication_config_jwt
tags:
  - apiserver
  - authentication
  - oidc
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_authentication_config_jwt definition"
relations: []
---

# kube_apiserver_authentication_config_jwt

## Summary
Список JWT-издателей (`jwt`) структурированного файла `AuthenticationConfiguration` API-сервера, заменяющий флаги `--oidc-*`. По умолчанию пустой список (`[]`).

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml` (строка 535 в v2.31.0):

```yaml
kube_apiserver_authentication_config_jwt: []
```

Ниже в файле приведён закомментированный пример структуры (issuer/claimMappings на основе переменных `kube_oidc_*`). Переменная появилась только в v2.31.0; в v2.29.0, v2.29.1 и v2.30.0 отсутствует.

## Compatibility
Только Kubespray v2.31.0. Используется при `kube_apiserver_use_authentication_config_file: true`. Связанные переменные: `kube_apiserver_authentication_config_api_version`, `kube_oidc_*`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
