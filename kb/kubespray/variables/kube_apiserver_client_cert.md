---
id: VARIABLE-KUBE_APISERVER_CLIENT_CERT
type: variable
title: kube_apiserver_client_cert
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_client_cert
tags:
  - apiserver
  - certificates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_client_cert definition"
relations: []
---

# kube_apiserver_client_cert

## Summary
Путь к клиентскому сертификату CA, используемому при обращении к kube-apiserver. По умолчанию `{{ kube_cert_dir }}/ca.crt`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_client_cert: "{{ kube_cert_dir }}/ca.crt"
```

Выражение не менялось между тегами v2.29.0–v2.31.0 (строка 662 в v2.29.0/v2.29.1, 665 в v2.30.0, 684 в v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Зависит от `kube_cert_dir`. Обычно используется в паре с `kube_apiserver_client_key`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
