---
id: VARIABLE-KUBE_APISERVER_BIND_ADDRESS
type: variable
title: kube_apiserver_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_bind_address
tags:
  - apiserver
  - networking
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_apiserver_bind_address definition"
relations: []
---

# kube_apiserver_bind_address

## Summary
IP-адрес, на котором слушает kube-apiserver (флаг `--bind-address`). По умолчанию `::` — прослушивание всех интерфейсов (dual-stack).

## Implementation
Определена (с идентичным значением) в двух местах:

- `roles/kubernetes/control-plane/defaults/main/main.yml`
- `roles/kubespray_defaults/defaults/main/main.yml`

```yaml
kube_apiserver_bind_address: "::"
```

Значение `::` не менялось между тегами v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0–v2.31.0. Используется, в частности, при вычислении `kube_apiserver_endpoint` (там `::` заменяется на `127.0.0.1`). Определена дважды с одинаковым значением, поэтому расхождения нет.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
