---
id: VARIABLE-KUBE_APISERVER_CLIENT_KEY
type: variable
title: kube_apiserver_client_key
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_client_key
tags:
  - apiserver
  - certificates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_client_key definition"
relations: []
---

# kube_apiserver_client_key

## Summary
Путь к приватному ключу CA, используемому при обращении к kube-apiserver. По умолчанию `{{ kube_cert_dir }}/ca.key`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_client_key: "{{ kube_cert_dir }}/ca.key"
```

Выражение не менялось между тегами v2.29.0–v2.31.0 (строка 663 в v2.29.0/v2.29.1, 666 в v2.30.0, 685 в v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Зависит от `kube_cert_dir`. Обычно используется в паре с `kube_apiserver_client_cert`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
