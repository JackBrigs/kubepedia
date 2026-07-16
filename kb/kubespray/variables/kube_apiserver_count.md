---
id: VARIABLE-KUBE_APISERVER_COUNT
type: variable
title: kube_apiserver_count
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_count
tags:
  - apiserver
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_count definition"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_count

## Summary
Количество экземпляров kube-apiserver в кластере. По умолчанию вычисляется как число хостов в группе `kube_control_plane`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_count: "{{ groups['kube_control_plane'] | length }}"
```

Выражение не менялось между тегами v2.29.0–v2.31.0 (строка 636 в v2.29.0/v2.29.1, 639 в v2.30.0, 658 в v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Зависит от состава инвентарной группы `kube_control_plane`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
