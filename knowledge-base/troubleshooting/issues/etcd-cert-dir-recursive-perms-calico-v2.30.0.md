---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12908
retrieved_at: 2026-07-14
topics:
  - etcd
  - certificates
  - calico
affected_versions:
  - v2.29.1
fixed_versions:
  - v2.30.0
reliability: confirmed
---

# etcd: рекурсивные права 0700 на каталоге сертификатов ломали Calico в режиме etcd datastore (исправлено в v2.30.0)

> Примечание: сценарий затрагивает Calico (CNI вне детального охвата базы — индексируется только Cilium), но корневое изменение относится к etcd и объясняет удаление переменной `etcd_cert_dir_mode` в v2.30.0.

## Симптом

Кластеры с Calico в режиме **etcd datastore** и выделенными etcd-узлами падали при обновлении / ротации control-plane: `calico-kube-controllers` не мог прочитать сертификаты для доступа к etcd.

## Корневая причина

Права `0700` применялись **рекурсивно** к каталогу `/etc/ssl/etcd/ssl`, снимая групповые права с файлов сертификатов, от которых зависит Calico.

## Решение (breaking change v2.30.0)

PR [#12908](https://github.com/kubernetes-sigs/kubespray/pull/12908) (merged 2026-01-27): удалена переменная `etcd_cert_dir_mode` (режим каталога всегда `0700`), права на каталог применяются **нерекурсивно**. Бэкпорты в release-2.27/2.28/2.29.

## Проверка по коду тега v2.30.0

Переменная `etcd_cert_dir_mode` в коде тега **отсутствует** (grep по `roles/` пуст) — подтверждает удаление. Это breaking change для тех, кто её переопределял.

## Версии

- **Затронуто:** ≤ v2.29.1 (рекурсивное применение прав).
- **Исправлено:** v2.30.0 (+ бэкпорты 2.27–2.29).

## Связанное

[[versions/v2.30.0/variables/etcd|Переменные etcd]] · [[versions/v2.30.0/release-notes|Release notes v2.30.0 (удаление etcd_cert_dir_mode)]]
