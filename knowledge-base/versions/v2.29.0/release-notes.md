---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.29.0
retrieved_at: 2026-07-14
topics:
  - release
  - versions
  - changelog
reliability: authoritative
---

# GitHub Release Kubespray v2.29.0

- **Тег:** `v2.29.0` (commit `9991412`)
- **Дата релиза:** 14 октября 2025
- **Тип:** **минорный релиз** линии Kubernetes 1.33; следующий за линией v2.28.
- **Предыдущая проиндексированная версия:** v2.28.1.
- **Следующий (патч) релиз:** v2.29.1.
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.29.0

## Urgent Upgrade Notes (breaking changes)

Релиз содержит раздел «Urgent Upgrade Notes (No, really, you MUST read this before you upgrade)».
Действия, требующие внимания при обновлении:

- **`/etc/hosts` больше не заполняется списком всех узлов кластера.** Если ваши сценарии
  или приложения полагались на разрешение имён узлов через `/etc/hosts`, потребуется
  альтернатива (DNS/собственная конфигурация).
- **Удалена node-affinity у деплоймента CoreDNS; добавлена переменная `coredns_affinity`.**
  По умолчанию поды CoreDNS больше не назначаются на control-plane-узлы. Прежнее поведение
  задаётся явной настройкой `coredns_affinity`.
- **Удалена поддержка сетевого плагина Weave** (`weave`). Кластеры на Weave нужно
  мигрировать на поддерживаемый CNI до обновления.
- **Ansible-тег `master` удалён и заменён на `control-plane`.** Все запуски с
  `--tags master` / `--skip-tags master` необходимо перевести на `control-plane`.
- **Переменная `conntrack_modules` удалена**; список загружаемых conntrack-модулей теперь
  зашит в коде (hardcoded).
- **Прекращена поддержка CRI-O на Ubuntu 20.04** (`cri-o` + ubuntu20).

## Категории изменений релиза

На странице релиза присутствуют разделы:

- **Urgent Upgrade Notes** (см. выше);
- **Changes by Kind**: Feature, Design, Bug or Regression, Other (Cleanup or Flake);
- **Components**;
- **Contributors**.

## Версии компонентов

Версии ниже **разрешены из кода тега** (`roles/kubespray_defaults/...`, источник истины —
[[versions/v2.29.0/components|components]]) в соответствии с правилом раздела 5.1 CLAUDE.md
(при расхождениях приоритет за кодом).

| Компонент | Версия (из кода тега) |
|---|---|
| Kubernetes | 1.33.5 |
| etcd | 3.5.23 |
| containerd | 2.1.4 |
| CRI-O | 1.33.5 |
| cri-dockerd | 0.3.20 |
| runc | 1.3.2 |
| cni-plugins | 1.8.0 |
| Calico | 3.30.3 |
| Cilium | 1.18.2 |
| Flannel | 0.27.3 |
| kube-ovn | 1.12.21 |
| kube-router | 2.1.1 |
| Multus | 4.2.2 |
| CoreDNS | 1.12.0 |
| Helm | 3.18.4 |
| cert-manager | 1.15.3 |
| Ingress-NGINX | 1.13.3 |
| MetalLB | 0.13.9 |
| Argo CD | 2.14.20 |

Из CNI-плагинов проект детально индексирует только Cilium; Calico/Flannel/kube-ovn/
kube-router/Multus приведены для полноты (их версии заданы в том же
`roles/kubespray_defaults/defaults/main/download.yml`).

## Примечания

- Детальное сравнение кода с предыдущей проиндексированной версией (v2.28.1) выполняется
  отдельным отчётом `diffs/` (раздел 7 CLAUDE.md).
- Патч-релиз v2.29.1 (11 декабря 2025) поверх v2.29.0 обновляет ряд версий
  (Kubernetes 1.33.5→1.33.7, etcd 3.5.23→3.5.25, containerd 2.1.4→2.1.5,
  Cilium 1.18.2→1.18.4, Calico 3.30.3→3.30.5, CRI-O 1.33.5→1.33.7 и др.) и
  консолидирует переменную `unsafe_show_logs`; см. срез v2.29.1.

---

Связанные срезы: [[versions/v2.29.0/components|Компоненты и версии]] · [[versions/v2.29.0/variables/cni|Переменные CNI]] · [[versions/v2.29.0/docs/nodes|Дайджест: узлы]]

Назад: [[versions/v2.29.0/README|Срез v2.29.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
