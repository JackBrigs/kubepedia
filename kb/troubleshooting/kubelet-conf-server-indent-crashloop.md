---
id: TROUBLE-KUBELET_CONF_SERVER_INDENT_CRASHLOOP
type: troubleshooting
title: "kubelet crash-loop после апгрейда: неверный отступ server: в kubelet.conf"
status: active
kubespray_version: "v2.31.0"
kubernetes_version: ">=v1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubelet-conf-server-indent
tags:
  - kubelet
  - kubeadm
  - upgrade
sources:
  - type: github_issue
    url: https://github.com/kubernetes-sigs/kubespray/issues/13277
    note: "Issue с подтверждённой корневой причиной; предложенный PR #13284 открыт, не влит"
relations:
  - type: see_also
    target: CONCEPT-KUBEADM_CONFIG
---

# kubelet crash-loop после апгрейда: неверный отступ server: в kubelet.conf

## Summary
После апгрейда на Kubernetes 1.35+ воркеры уходят в NotReady, kubelet в crash-loop с ошибкой `invalid configuration: no server found for cluster 'default-cluster'`. Причина — жёстко заданный отступ строки `server:` в `kubelet.conf`, из-за которого поле выпадает из блока `cluster:`. На момент составления записи исправляющий PR #13284 открыт и не влит.

## Problem
Задача `lineinfile` в `roles/kubernetes/kubeadm/tasks/main.yml` записывает строку `server:` с жёстко заданным отступом в 4 пробела, из-за чего поле оказывается вне вложенного блока `cluster:` в `kubelet.conf` (kubeadm-стиль требует 8 пробелов для вложенных полей). kubelet не находит server для кластера. Проявляется при включённом локальном балансировщике apiserver (localhost LB).

## Context
- Затронуто: v2.31.0 (прямая связь с дефолтным Kubernetes 1.35 и localhost LB).
- Исправлено: пока нет (PR #13284 открыт). Держать на контроле.
- Условие срабатывания: апгрейд на Kubernetes 1.35+ при включённом localhost LB.

## Diagnostics
На затронутых воркерах kubelet в crash-loop с сообщением `invalid configuration: no server found for cluster 'default-cluster'`, узлы в статусе NotReady. Проверить файл `{{ kube_config_dir }}/kubelet.conf`: строка `server:` записана с отступом 4 пробела вместо 8 и оказывается вне блока `cluster:`. По коду тега v2.31.0 `roles/kubernetes/kubeadm/tasks/main.yml` (строки 104–107):

```yaml
lineinfile:
  dest: "{{ kube_config_dir }}/kubelet.conf"
  regexp: 'server:'
  line: '    server: {{ kube_apiserver_endpoint }}'   # <- 4 пробела отступа
```

## Known Issues
Корневая причина: задача `lineinfile` жёстко задаёт отступ 4 пробела для строки `server:`, что выводит поле за пределы вложенного блока `cluster:`. Предложенный фикс — PR [#13284](https://github.com/kubernetes-sigs/kubespray/pull/13284) (использует `backrefs: true` с сохранением исходного отступа). PR открыт, не влит — исправления в релизе пока нет. Issue [#13277](https://github.com/kubernetes-sigs/kubespray/issues/13277).

Обходной путь на v2.31.0: после апгрейда проверить `{{ kube_config_dir }}/kubelet.conf` на затронутых воркерах и вручную исправить отступ строки `server:` (8 пробелов, внутри блока `cluster:`), затем перезапустить kubelet.

## References
- https://github.com/kubernetes-sigs/kubespray/issues/13277
- https://github.com/kubernetes-sigs/kubespray/pull/13284
- Migrated from Kubepedia 0.1.0 cache: kubelet-conf-server-indent-crashloop-v2.31.0.md
