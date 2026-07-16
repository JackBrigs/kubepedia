---
id: VARIABLE-KUBE_APISERVER_ADMISSION_PLUGINS_PODNODESELECTOR_DEFAULT_NODE_SELECTOR
type: variable
title: kube_apiserver_admission_plugins_podnodeselector_default_node_selector
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_admission_plugins_podnodeselector_default_node_selector
tags:
  - apiserver
  - admission
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_apiserver_admission_plugins_podnodeselector_default_node_selector definition"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_admission_plugins_podnodeselector_default_node_selector

## Summary
Задаёт кластерный `clusterDefaultNodeSelector` для admission-плагина `PodNodeSelector` API-сервера. По умолчанию пустая строка (`""`), то есть селектор по умолчанию не применяется.

## Implementation
Определена в `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_apiserver_admission_plugins_podnodeselector_default_node_selector: ""
```

Значение не менялось между тегами v2.29.0–v2.31.0 (строка 159 в v2.29.0/v2.29.1, строка 162 в v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Значение используется при формировании конфигурации admission-плагина `PodNodeSelector`; действует только если этот плагин включён.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
