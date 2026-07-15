---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13019
retrieved_at: 2026-07-14
topics:
  - kubeadm
  - control-plane
affected_versions:
  - v2.29.0
  - v2.29.1
  - v2.30.0
fixed_versions:
  - v2.31.0
reliability: confirmed
---

# kubeadm: устаревшие `kubeadm_patches` не удаляются при изменении inventory (затрагивает v2.30.0)

## Симптом

При изменении переменной `kubeadm_patches` (удаление или изменение патча) старые файлы патчей остаются на узлах control-plane и продолжают применяться kubeadm — удалённые настройки «залипают» (конфиг-дрейф), в том числе при обновлении кластера.

## Корневая причина

Роль записи патчей только создаёт каталог и копирует патчи из текущего `kubeadm_patches`, но **не удаляет** с файловой системы патчи, отсутствующие в текущем значении переменной.

## Проверка по коду тега v2.30.0

`roles/kubernetes/kubeadm_common/tasks/main.yml` содержит только две задачи — создание каталога (`file: state: directory`) и копирование патчей (`copy ... loop: kubeadm_patches`). Задачи очистки (`state: absent` / `find` устаревших файлов) отсутствуют. Баг присутствует.

## Решение

PR [#13019](https://github.com/kubernetes-sigs/kubespray/pull/13019) (master → v2.31.0), бэкпорт в release-2.30 — PR [#13020](https://github.com/kubernetes-sigs/kubespray/pull/13020). Логика фикса: удаляет с узлов файлы патчей, которых нет в текущем `kubeadm_patches`.

**Обходной путь на v2.30.0:** вручную удалять устаревшие файлы патчей из каталога `kubeadm_patches_dir` на control-plane узлах.

## Версии

- **Затронуто:** v2.29.0, v2.29.1, **v2.30.0** (уязвимый код одинаков во всех).
- **Исправлено:** v2.31.0 (master). Бэкпорт в release-2.30 (будущий v2.30.1, тег не выпущен). Для линии release-2.29 также существует бэкпорт (#13021).

## Связанное

[[versions/v2.30.0/variables/k8s-cluster|Переменные ядра (kubeadm_patches)]] · [[versions/v2.30.0/ansible-tags|Ansible-теги (kubeadm)]]
