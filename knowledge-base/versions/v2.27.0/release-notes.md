---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.27.0
retrieved_at: 2026-07-15
topics:
  - release
  - versions
  - changelog
  - breaking-changes
reliability: authoritative
---

# GitHub Release Kubespray v2.27.0

- **Тег:** `v2.27.0` (commit `9ec9b3a`)
- **Дата тега:** 2 января 2025 (commit `9ec9b3a`, subject «[ingress-nginx] upgrade to 1.12.0 (#11846)»)
- **Дата публикации релиза:** 6 января 2025 (по странице GitHub Release)
- **Тип:** минорный релиз (feature release) с обновлением компонентов и рядом breaking changes относительно v2.26.x.
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.27.0

## Версии компонентов (по релизу)

Официально указанные в релизе версии. **Сверены с разрешёнными из кода тега** ([[versions/v2.27.0/components|components]]) — расхождений нет.

| Компонент | Версия | В `components.yaml` |
|---|---|---|
| Kubernetes | 1.31.4 | ✓ совпадает |
| etcd | 3.5.16 | ✓ совпадает |
| containerd | 1.7.24 | ✓ совпадает |
| runc | 1.2.3 | ✓ совпадает |
| CoreDNS | 1.11.3 | ✓ совпадает |
| Cilium | 1.15.9 | ✓ совпадает |
| Calico | 3.29.1 | ✓ совпадает |
| Helm | 3.16.4 | ✓ совпадает |
| CRI-O | 1.31.0 | ✓ совпадает |
| ingress-nginx | 1.12.0 | ✓ совпадает |

Минимально поддерживаемая версия Kubernetes в этом теге — **1.29.x** (`kube_version_min_required = v1.29.0`); минимальная CRI-O — 1.29.x.

## Ключевые изменения

- Поддержка Fedora 39/40; прекращена поддержка Fedora 37/38.
- Добавлен CI для openEuler 24.03.
- Поддержка выбора рантайма по умолчанию для CRI-O (в т.ч. `crun`).
- Настройка admission-плагина `ResourceQuota`.
- Частичная поддержка Cilium 1.16+ с функциями BGP Control Plane.
- Поддержка нескольких cloud controller manager-ов (добавлен Oracle OCI).
- Введена поддержка `ntpsec`.
- Сетевая изоляция в конфигурации Multus.
- ingress-nginx обновлён до 1.12.0 (коммит тега `9ec9b3a`, PR #11846).

## Breaking changes / предупреждения об обновлении

Релиз v2.27.0 содержит несколько обязательных изменений конфигурации при обновлении:

1. **Формат `kubeadm_patches`** изменён: вместо patch-файлов теперь используется массив inline-патчей. Существующие конфигурации нужно переписать.
2. **Статические токены**: удалена генерация статических токенов для каждого узла кластера при `kube_token_auth: true`.
3. **Конфигурация kubelet**: node-специфичные флаги объявлены устаревшими — использовать унифицированные переменные в `group_vars`.
4. **Группа `k8s_cluster`** теперь генерируется автоматически; ручное определение в inventory больше не требуется.
5. **Preflight-ошибки kubeadm**: новая переменная `kubeadm_ignore_preflight_errors` заменяет прежнее поведение `all`.
6. **`--limit` без кэшированных фактов** больше не поддерживается: запуск Kubespray с `--limit` без предварительно собранных фактов не работает.

## Устаревшие функции и удаления

- In-tree cloud-провайдеры объявлены устаревшими — требуется переход на внешние реализации.
- Удалены скрипты `inventory_builder` и `contrib/dind`.
- Драйверы vSphere CSI/CPI теперь берутся из `registry.k8s.io` вместо `gcr.io`.

## Примечания

- Дата тега по git (2 января 2025) и дата публикации Release на GitHub (6 января 2025) различаются — это нормально: тег создаётся раньше публикации заметок релиза. В метаданных среза (`meta.yaml`) зафиксирована дата тега.
- Детальное сравнение кода с предыдущей проиндексированной версией (отчёт в `diffs/`, раздел 7) будет выполнено при наличии в базе смежной версии; на момент составления среза сравнение «по коду» не проводилось.

---

Связанные срезы: [[versions/v2.27.0/components|Компоненты и версии]] · [[versions/v2.27.0/meta|meta.yaml]]

Назад: [[versions/v2.27.0/README|Срез v2.27.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
