---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12401
retrieved_at: 2026-07-15
topics:
  - coredns
  - dns
  - addons
affected_versions:
  - v2.28.0
  - v2.28.1
fixed_versions:
  - v2.29.0
reliability: confirmed
---

# CoreDNS/nodelocaldns: поды не перезапускались при изменении конфигурации (исправлено в v2.29.0)

## Симптом

После изменения конфигурации CoreDNS или nodelocaldns (ConfigMap) поды не переразворачивались и
продолжали работать со старым конфигом — изменения DNS не применялись до ручного рестарта.

## Корневая причина

В шаблонах деплойментов/демонсетов отсутствовала аннотация с контрольной суммой конфигурации, по
которой Kubernetes триггерит rollout при изменении ConfigMap. Без `checksum/config` под-темплейт
не менялся, и rollout не запускался.

## Проверка по коду тега v2.28.1

В `roles/kubernetes-apps/ansible/templates/coredns-deployment.yml.j2`,
`nodelocaldns-daemonset.yml.j2` и `nodelocaldns-second-daemonset.yml.j2` (v2.28.1) в блоке
`annotations` нет `checksum/config`. Аннотация добавляется только в v2.29.0.

## Решение

PR [#12401](https://github.com/kubernetes-sigs/kubespray/pull/12401) «fix: redeploy coredns and
nodelocaldns when its config changed» (master, commit `66cab1549`, вошёл в v2.29.0) добавляет в
аннотации подов контрольную сумму конфигурации:

```jinja
checksum/config: "{{ lookup('template', 'coredns-config.yml.j2') | checksum }}"
```

и аналогично для nodelocaldns — при изменении конфига меняется аннотация и запускается rollout.

**Бэкпорта в release-2.28 нет.**

## Версии

- **Затронуто:** v2.28.0, v2.28.1.
- **Исправлено:** v2.29.0 (#12401).

## Связанное

[[versions/v2.28.1/variables/addons|Переменные addons (CoreDNS/nodelocaldns)]] · [[versions/v2.28.1/docs/installation|Дайджест: установка]]
