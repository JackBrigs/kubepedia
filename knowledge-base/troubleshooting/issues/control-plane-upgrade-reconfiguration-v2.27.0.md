---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12015
retrieved_at: 2026-07-15
topics:
  - upgrade
  - control-plane
  - kubeadm
affected_versions:
  - v2.27.0
fixed_versions:
  - v2.27.1
  - v2.28.0
reliability: confirmed
---

# Обновление control plane: не поддерживалась реконфигурация и корректный upgrade вторичных узлов (исправлено в v2.27.1)

## Симптом

При обновлении кластера control plane обновлялся некорректно: отсутствовала поддержка
реконфигурации control plane через `kubeadm` во время апгрейда, а вторичные (не первые)
control-plane-узлы обновлялись не через штатный механизм `kubeadm upgrade node`. Изменения
конфигурации, вносимые между версиями, при обновлении не применялись к control plane.

## Корневая причина

Роль `roles/kubernetes/control-plane` не использовала `UpgradeConfiguration` из kubeadm
v1beta4 и не вызывала `kubeadm upgrade node` для вторичных control-plane-узлов. Логика
апгрейда была построена без раздельной обработки реконфигурации и обновления версии.

## Проверка по коду тега v2.27.0

В v2.27.0 отсутствует шаблон `kubeadm-config.v1beta4.yaml.j2` и логика реконфигурации в
`roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml`. PR добавляет эти файлы:

- `roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2` (новый);
- изменения в `roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml`, `kubeadm-setup.yml`, `check-api.yml`;
- новые поля в `roles/kubernetes/control-plane/defaults/main/main.yml`.

## Решение

PR [#12015](https://github.com/kubernetes-sigs/kubespray/pull/12015) «Refactor control plane
upgrades with reconfiguration support» (master, commit `b551fe083`): добавлена поддержка
`kubeadm-config` v1beta4 `UpgradeConfiguration.apply` / `UpgradeConfiguration.node` и
использование `kubeadm upgrade node` при обновлении вторичных control-plane-узлов.

Бэкпорт в ветку release-2.27 — PR #12103 (commit `bf68231a5`), вошёл в тег v2.27.1.

## Версии

- **Затронуто:** v2.27.0.
- **Исправлено:** v2.27.1 (бэкпорт #12103) и v2.28.0 (мастер-фикс #12015). В v2.28.x/v2.29.x проблема отсутствует.

## Связанное

[[versions/v2.27.0/docs/upgrades|Дайджест: обновление кластера]] · [[versions/v2.27.0/docs/nodes|Дайджест: узлы]] · [[versions/v2.27.1/release-notes|release-notes v2.27.1]]
