---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12644
retrieved_at: 2026-07-14
topics:
  - calico
  - rbac
affected_versions:
  - v2.29.0
fixed_versions:
  - v2.29.1
reliability: confirmed
---

# Calico: отсутствовал RBAC-verb `watch` для `hostendpoints` (исправлено в v2.29.1)

> Примечание: Calico — CNI вне детального охвата базы знаний (индексируется только Cilium). Запись приведена для полноты, так как исправление входит в v2.29.1.

## Симптом

Calico не мог отслеживать (`watch`) изменения ресурсов `hostendpoints` — контроллер не получал события об их изменениях.

## Корневая причина

В правилах RBAC Calico для ресурса `hostendpoints` отсутствовал verb `watch`, что ограничивало наблюдение за изменениями этих объектов.

## Решение

PR [#12644](https://github.com/kubernetes-sigs/kubespray/pull/12644) (cherry-pick #12641, commit `9a9e33dc9`) добавил verb `watch` в RBAC-правила Calico для `hostendpoints`.

## Проверка по коду тега v2.29.1

Ресурс `hostendpoints` присутствует в RBAC-шаблонах Calico тега:
- `roles/network_plugin/calico/templates/calico-apiserver.yml.j2:165`
- `roles/network_plugin/calico/templates/calico-cr.yml.j2:132`

Коммит `9a9e33dc9` («fix(calico): Add missed rbac verb for hostendpoints (#12644)») входит в диапазон `v2.29.0..v2.29.1`.

## Версии

- **Затронуто:** v2.29.0.
- **Исправлено:** v2.29.1.

## Связанное

[[versions/v2.29.1/release-notes|Release notes v2.29.1]]
