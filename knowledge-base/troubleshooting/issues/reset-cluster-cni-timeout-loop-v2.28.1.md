---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12300
retrieved_at: 2026-07-15
topics:
  - reset
  - cni
  - etcd
affected_versions:
  - v2.28.0
  - v2.28.1
fixed_versions:
  - v2.29.0
reliability: confirmed
---

# reset: зацикливание/таймауты при удалении кластера (порядок остановки сервисов и очистки CNI) (исправлено в v2.29.0)

## Симптом

При полном удалении кластера (`reset.yml`) выполнение зависало в цикле таймаутов на этапе очистки
CNI (в частности Calico). Проявлялось как «looping timeout» при попытке остановить/удалить сервисы
и контейнеры в неверном порядке.

## Корневая причина

В `roles/reset/tasks/main.yml` порядок остановки сервисов и удаления контейнеров был некорректен:
сервисы etcd и containerd останавливались/удалялись раздельными блоками так, что очистка сетевого
плагина упиралась в таймауты (сеть/рантайм ещё активны или уже частично снесены). Требовалась
консолидация остановки containerd и etcd и корректная последовательность.

## Проверка по коду тега v2.28.1

`roles/reset/tasks/main.yml` (v2.28.1) содержит раздельные блоки: `etcd.service` /
`etcd-events.service` в списках остановки/удаления и отдельный блок «Reset | remove containerd».
Реструктуризация («Reset | stop containerd and etcd services») присутствует только начиная с v2.29.0.

## Решение

PR [#12300](https://github.com/kubernetes-sigs/kubespray/pull/12300) «Fix calico CNI timeouts in
reset role» (master, commit `b04ceba89`, вошёл в v2.29.0) переупорядочивает остановку сервисов
containerd/etcd и очистку, устраняя зацикливание таймаутов при reset. В заметках релиза v2.29.0
это отражено как «Fixed a looping timeout bug when deleting an entire cluster».

**Бэкпорта в release-2.28 нет.**

## Версии

- **Затронуто:** v2.28.0, v2.28.1.
- **Исправлено:** v2.29.0 (#12300).

## Связанное

[[versions/v2.28.1/docs/nodes|Дайджест: узлы/сброс]] · [[versions/v2.28.1/ansible-tags|Ansible-теги (reset)]]
