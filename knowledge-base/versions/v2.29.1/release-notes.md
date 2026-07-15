---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.29.1
retrieved_at: 2026-07-14
topics:
  - release
  - versions
  - changelog
reliability: authoritative
---

# GitHub Release Kubespray v2.29.1

- **Тег:** `v2.29.1` (commit `0c6a295`)
- **Дата релиза:** 11 декабря 2025, 15:21 (UTC)
- **Тип:** патч-релиз с минимальными изменениями — только исправления ошибок относительно v2.29.0.
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.29.1

## Исправления (Bug Fixes)

В патч-релиз вошли четыре исправления (относительно v2.29.0):

| PR | Описание |
|---|---|
| [#12695](https://github.com/kubernetes-sigs/kubespray/pull/12695) | Fix Calico apiserver RBAC permissions for Kubernetes 1.33+ |
| [#12705](https://github.com/kubernetes-sigs/kubespray/pull/12705) | Fix Cilium `loadBalancer.mode` rendering in Kubespray values template |
| [#12644](https://github.com/kubernetes-sigs/kubespray/pull/12644) | Fix(calico): Add missed rbac verb `watch` for hostendpoints |
| [#12685](https://github.com/kubernetes-sigs/kubespray/pull/12685) | Removing external etcd member (not stacked with control plane) should now work |

Замечания:

- **#12705** относится к проиндексированному в базе CNI Cilium: исправлен рендеринг `loadBalancer.mode` в helm-values Cilium. Связано с переменными среза [[versions/v2.29.1/variables/cni|Переменные CNI]].
- **#12685** — исправление удаления внешнего (не stacked) члена etcd; относится к сценарию управления узлами, см. [[versions/v2.29.1/docs/nodes|Дайджест: узлы]].
- **#12695** и **#12644** касаются Calico (CNI вне детального охвата проекта) — приведены для полноты.

## Версии компонентов (по релизу)

Официально указанные в релизе версии. **Все сверены с разрешёнными из кода тега** ([[versions/v2.29.1/components|components]]) — расхождений нет.

| Компонент | Версия | В `components.yaml` |
|---|---|---|
| Kubernetes | 1.33.7 | ✓ совпадает |
| etcd | 3.5.25 | ✓ совпадает |
| containerd | 2.1.5 | ✓ совпадает |
| CRI-O | 1.33.7 | ✓ совпадает |
| cni-plugins | 1.8.0 | ✓ совпадает |
| Cilium | 1.18.4 | ✓ совпадает |
| CoreDNS | 1.12.0 | ✓ совпадает |
| Ingress-NGINX | 1.13.3 | ✓ совпадает |
| cert-manager | 1.15.3 | ✓ совпадает |
| Helm | 3.18.4 | ✓ совпадает |
| MetalLB | 0.13.9 | ✓ совпадает |
| Calico | 3.30.5 | не индексируется (CNI вне охвата) |
| Flannel | 0.27.3 | не индексируется (CNI вне охвата) |

## Breaking changes / предупреждения об обновлении

В заметках релиза v2.29.1 **не задокументировано** breaking changes, устаревших функций или предупреждений об обновлении — это ожидаемо для патч-релиза.

## Примечания

- Полный сравнительный changelog (`v2.29.0...v2.29.1`) на странице релиза в извлечённом виде полностью не отображается; перечень PR выше соответствует разделу Bug Fixes релиза. Детальное сравнение кода с предыдущей проиндексированной версией будет выполнено при добавлении v2.30.0 (раздел 7 — отчёт `diffs/`), поскольку предыдущей версии v2.29.0 в базе нет (стартовая версия проекта — v2.29.1).

---

Связанные срезы: [[versions/v2.29.1/components|Компоненты и версии]] · [[versions/v2.29.1/variables/cni|Переменные CNI]] · [[versions/v2.29.1/docs/nodes|Дайджест: узлы]]

Назад: [[versions/v2.29.1/README|Срез v2.29.1]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
