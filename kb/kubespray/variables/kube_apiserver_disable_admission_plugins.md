---
id: VARIABLE-KUBE_APISERVER_DISABLE_ADMISSION_PLUGINS
type: variable
title: kube_apiserver_disable_admission_plugins
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_disable_admission_plugins
tags:
  - apiserver
  - admission
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_apiserver_disable_admission_plugins definition"
relations: []
---

# kube_apiserver_disable_admission_plugins

## Summary
Список admission-плагинов, отключаемых у kube-apiserver (флаг `--disable-admission-plugins`). По умолчанию пустой список (`[]`).

## Implementation
Определена в `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_apiserver_disable_admission_plugins: []
```

Комментарий в коде: «1.10+ list of disabled admission plugins». Значение не менялось между тегами v2.29.0–v2.31.0 (строка 137 в v2.29.0/v2.29.1, 140 в v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Дополняет `kube_apiserver_enable_admission_plugins`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
