---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12718
retrieved_at: 2026-07-14
topics:
  - cilium
  - hubble
affected_versions:
  - v2.29.0
fixed_versions:
  - v2.29.1
reliability: confirmed
---

# Cilium/Hubble: настройки flow export не применялись после смены схемы в Cilium 1.18 (исправлено в v2.29.1)

## Симптом

При включённом Hubble flow export статические настройки экспортёра (ротация/размер файлов) не применялись, потому что Cilium 1.18 перенёс их в helm-values под ключ `hubble.export.static`, а Kubespray генерировал значения по старой схеме.

## Корневая причина

Kubespray формировал helm-values Hubble export по устаревшей схеме (до Cilium 1.18). Связано с изменением схемы в upstream (cilium/cilium#36974). В v2.29.1 версия Cilium по умолчанию — 1.18.4, поэтому актуальна новая схема.

## Решение

PR [#12665](https://github.com/kubernetes-sigs/kubespray/pull/12665) (master) привёл значения к новой схеме `hubble.export.static`. Бэкпорт в release-2.29 — PR [#12718](https://github.com/kubernetes-sigs/kubespray/pull/12718), commit `a04592de1`.

## Проверка по коду тега v2.29.1

`roles/network_plugin/cilium/templates/values.yaml.j2` содержит новую схему:

```yaml
  export:
    static:
      fileMaxBackups: {{ cilium_hubble_export_file_max_backups }}
      fileMaxSizeMb: {{ cilium_hubble_export_file_max_size_mb }}
```

Коммит `a04592de1` («Adjust hubble export values for cilium 1.18 schema change (#12718)») входит в диапазон `v2.29.0..v2.29.1`.

## Версии

- **Затронуто:** v2.29.0 (Cilium 1.18 с Hubble export).
- **Исправлено:** v2.29.1.

## Связанное

[[versions/v2.29.1/variables/cni|Переменные CNI (cilium_hubble_*)]] · [[versions/v2.29.1/components|Компоненты (Cilium 1.18.4)]]
