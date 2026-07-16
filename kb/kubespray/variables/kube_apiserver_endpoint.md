---
id: VARIABLE-KUBE_APISERVER_ENDPOINT
type: variable
title: kube_apiserver_endpoint
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_endpoint
tags:
  - apiserver
  - networking
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_endpoint definition"
relations: []
---

# kube_apiserver_endpoint

## Summary
Вычисляемый URL для обращения к kube-apiserver. Выбирается по контексту: внешний балансировщик (`loadbalancer_apiserver`), localhost-балансировщик на не-control-plane узлах, локальный адрес на control-plane, иначе адрес первого control-plane узла. Порт по умолчанию — `kube_apiserver_port`.

## Implementation
Определена в `roles/kubespray_defaults/defaults/main/main.yml` как многострочный Jinja-шаблон (строка 652 в v2.29.0/v2.29.1, 655 в v2.30.0, 674 в v2.31.0).

Выражение изменилось между тегами в ветке внешнего балансировщика:

| Теги | Строка домена балансировщика |
|------|------------------------------|
| v2.29.0, v2.29.1 | `https://{{ apiserver_loadbalancer_domain_name }}:{{ ... }}` |
| v2.30.0, v2.31.0 | `https://{{ apiserver_loadbalancer_domain_name \| ansible.utils.ipwrap }}:{{ ... }}` |

Начиная с v2.30.0 к домену балансировщика применяется фильтр `ansible.utils.ipwrap` (корректная обёртка IPv6-адресов в квадратные скобки). Остальные ветки шаблона (localhost, control-plane с заменой `::` на `127.0.0.1`, первый control-plane) идентичны во всех четырёх тегах.

## Compatibility
Kubespray v2.29.0–v2.31.0. Зависит от `loadbalancer_apiserver`, `apiserver_loadbalancer_domain_name`, `loadbalancer_apiserver_localhost`, `kube_apiserver_bind_address`, `kube_apiserver_port`, `first_kube_control_plane_address`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
