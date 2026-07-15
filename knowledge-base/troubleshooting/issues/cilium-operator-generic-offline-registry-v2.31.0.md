---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13270
retrieved_at: 2026-07-14
topics:
  - cilium
  - offline
  - registry
affected_versions:
  - v2.30.0
  - v2.31.0
fixed_versions: []
reliability: confirmed
---

# Cilium: неверный образ оператора в offline-реестре (`operator` vs `operator-generic`) — затрагивает v2.31.0

## Симптом

При развёртывании из offline-реестра под `cilium-operator` уходит в CrashLoopBackOff с ошибкой `exec: "cilium-operator-generic": executable file not found in $PATH`.

## Корневая причина

Kubespray синхронизирует в offline-реестр образ `quay.io/cilium/operator`, но Helm-чарт Cilium для не-облачных инсталляций автоматически добавляет суффикс `-generic` и запрашивает `cilium/operator-generic`, которого в реестре нет.

## Проверка по коду тега v2.31.0

`roles/kubespray_defaults/defaults/main/download.yml:237`:

```yaml
cilium_operator_image_repo: "{{ quay_image_repo }}/cilium/operator"
```

Значение оканчивается на `cilium/operator` (без `-generic`) — при offline-реестре чарт добавит `-generic`, и образ не найдётся. Баг присутствует.

## Решение

PR [#13270](https://github.com/kubernetes-sigs/kubespray/pull/13270) (merged 2026-06-22, **после** тега v2.31.0) меняет `cilium_operator_image_repo` на `cilium/operator-generic` и добавляет `operator.image.override` в Helm values, чтобы чарт не добавлял суффикс повторно. Issue [#13252](https://github.com/kubernetes-sigs/kubespray/issues/13252).

**Обходной путь на v2.31.0:** вручную положить образ `cilium/operator-generic` в offline-реестр (в дополнение к `cilium/operator`), либо переопределить `cilium_operator_image_repo`.

## Версии

- **Затронуто:** v2.30.0, **v2.31.0** (дефолт `cilium/operator` в теге не изменён).
- **Исправлено:** фикс влит в master после тега v2.31.0 — войдёт в будущий релиз (v2.31.1 / v2.32.0). В v2.31.0 не исправлено.

## Связанное

[[versions/v2.31.0/docs/offline|Дайджест: offline]] · [[versions/v2.31.0/variables/cni|Переменные CNI (cilium_operator_image_repo)]]
