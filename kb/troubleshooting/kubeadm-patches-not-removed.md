---
id: TROUBLE-KUBEADM_PATCHES_NOT_REMOVED
type: troubleshooting
title: "kubeadm: устаревшие kubeadm_patches не удаляются при изменении inventory"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubeadm-patches-stale
tags:
  - kubeadm
  - control-plane
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13019
    note: "PR исправления (master -> v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-KUBEADM_CONFIG
---

# kubeadm: устаревшие kubeadm_patches не удаляются при изменении inventory

## Summary
При изменении переменной `kubeadm_patches` (удаление или изменение патча) старые файлы патчей остаются на узлах control-plane и продолжают применяться kubeadm. Удалённые настройки «залипают» (конфиг-дрейф), в том числе при обновлении кластера. Исправлено в v2.31.0 (PR #13019).

## Problem
Роль записи патчей только создаёт каталог и копирует патчи из текущего `kubeadm_patches`, но не удаляет с файловой системы патчи, отсутствующие в текущем значении переменной. В результате удалённые или изменённые патчи продолжают действовать.

## Context
- Затронуто: v2.29.0, v2.29.1, v2.30.0 (уязвимый код одинаков во всех).
- Исправлено: v2.31.0 (master). Бэкпорт в release-2.30 — PR #13020 (будущий v2.30.1, тег не выпущен). Для линии release-2.29 также существует бэкпорт (#13021).
- Условие срабатывания: изменение или удаление патчей в `kubeadm_patches` без ручной очистки каталога `kubeadm_patches_dir`.

## Diagnostics
Проверить на control-plane узлах содержимое каталога `kubeadm_patches_dir` и сравнить с текущим значением переменной `kubeadm_patches`. Файлы патчей, отсутствующие в текущем inventory, указывают на проблему. По коду тега v2.30.0: `roles/kubernetes/kubeadm_common/tasks/main.yml` содержит только две задачи — создание каталога (`file: state: directory`) и копирование патчей (`copy ... loop: kubeadm_patches`); задачи очистки (`state: absent` / `find` устаревших файлов) отсутствуют.

## Known Issues
Корневая причина: роль не удаляет устаревшие файлы патчей с узлов. Исправление — PR [#13019](https://github.com/kubernetes-sigs/kubespray/pull/13019) (master -> v2.31.0), бэкпорт в release-2.30 — PR #13020: логика фикса удаляет с узлов файлы патчей, которых нет в текущем `kubeadm_patches`.

Обходной путь на v2.30.0: вручную удалять устаревшие файлы патчей из каталога `kubeadm_patches_dir` на control-plane узлах.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13019
- Migrated from Kubepedia 0.1.0 cache: kubeadm-patches-not-removed-v2.30.0.md
