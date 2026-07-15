---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12254
retrieved_at: 2026-07-15
topics:
  - cilium
  - upgrade
  - helm-values
affected_versions:
  - v2.28.0
fixed_versions:
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# Cilium: безусловный `cilium install` ломал обновление кластера с v2.27 на v2.28 (исправлено в v2.28.1)

## Симптом

При обновлении кластера с v2.27 на v2.28 установка Cilium падала. В v2.28.0 задача всегда
выполняла `cilium install`, что эквивалентно `helm install` и завершается ошибкой, если
Helm-release Cilium уже существует (кластер до этого стоял на Cilium из Jinja-манифестов v2.27).

## Корневая причина

`roles/network_plugin/cilium/tasks/apply.yml` в v2.28.0 безусловно вызывал
`cilium install --version ...`. Cilium CLI не переключался на `upgrade`, если релиз уже
установлен, а также оставались старые ресурсы (ServiceAccount, Service и др.) от прежней установки.

## Проверка по коду тега v2.28.0

`roles/network_plugin/cilium/tasks/apply.yml` (v2.28.0), первая задача:

```yaml
- name: Cilium | Install
  command: "{{ bin_dir }}/cilium install --version {{ cilium_version }} -f {{ kube_config_dir }}/cilium-values.yaml"
```

Проверка отсутствия существующего релиза (`cilium_action`) появляется только начиная с v2.28.1
(`git grep cilium_action v2.28.0 -- .../apply.yml` — совпадений нет; в v2.28.1/v2.29.0 — есть).

## Решение

Мастер-фикс — PR [#12254](https://github.com/kubernetes-sigs/kubespray/pull/12254) «Fix: if
cilium release exist, the action will set upgrade» (commit `1f9020f0b`), вошёл в v2.29.0:
через `cilium version` определяется наличие релиза и выбирается `install`/`upgrade`
(`cilium {{ cilium_action }} ...`). Бэкпорт в release-2.28 — PR #12324 (commit `d7c00ce69`),
вошёл в v2.28.1; там же добавлена переменная `cilium_remove_old_resources` (по умолчанию `false`)
для очистки старых ресурсов при миграции.

## Версии

- **Затронуто:** v2.28.0 (при апгрейде с Cilium v2.27).
- **Исправлено:** v2.28.1 (бэкпорт #12324) и v2.29.0 (master #12254).

## Связанное

[[versions/v2.28.0/docs/cni|Дайджест: CNI/Cilium]] · [[versions/v2.28.0/docs/upgrades|Дайджест: обновление кластера]]
