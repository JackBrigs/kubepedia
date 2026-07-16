---
id: VARIABLE-KUBE_APISERVER_AUTHORIZATION_CONFIG_API_VERSION
type: variable
title: kube_apiserver_authorization_config_api_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_authorization_config_api_version
tags:
  - apiserver
  - authorization
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_authorization_config_api_version definition"
relations: []
---

# kube_apiserver_authorization_config_api_version

## Summary
Версия API (`apiVersion`) структурированного файла `AuthorizationConfiguration` API-сервера. Вычисляется по версии Kubernetes: `v1alpha1` до 1.30.0, `v1beta1` до 1.32.0, иначе `v1`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_authorization_config_api_version: "{{ 'v1alpha1' if kube_version is version('1.30.0', '<') else 'v1beta1' if kube_version is version('1.32.0', '<') else 'v1' }}"
```

Выражение не менялось между тегами v2.29.0–v2.31.0 (строка 529 в v2.29.0/v2.29.1, 530 в v2.30.0, 564 в v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Применяется при `kube_apiserver_use_authorization_config_file: true`. Связанные переменные: `kube_apiserver_authorization_config_authorizers`, `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
