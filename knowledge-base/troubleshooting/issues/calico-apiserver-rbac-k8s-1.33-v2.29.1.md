---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12695
retrieved_at: 2026-07-14
topics:
  - calico
  - rbac
  - kubernetes-1-33
affected_versions:
  - v2.29.0
fixed_versions:
  - v2.29.1
reliability: confirmed
---

# Calico apiserver: нехватка RBAC на Kubernetes 1.33+ (исправлено в v2.29.1)

> Примечание: Calico — CNI вне детального охвата базы знаний (индексируется только Cilium). Запись приведена для полноты, так как исправление входит в v2.29.1 и относится к дефолтной версии Kubernetes 1.33.7.

## Симптом

На Kubernetes 1.33+ Calico apiserver работал некорректно и засорял логи ошибками из-за отсутствующих прав RBAC.

## Корневая причина

Kubernetes 1.33 ввёл ресурсы `ValidatingAdmissionPolicy` (KEP-3488), для доступа к которым требуются явные права RBAC. В роли Calico они отсутствовали.

## Решение

PR [#12695](https://github.com/kubernetes-sigs/kubespray/pull/12695) (cherry-pick #12654, commit `e5a1f68a2`) добавил в роль `calico-webhook-reader` два ресурса:

- `validatingadmissionpolicies`
- `validatingadmissionpolicybindings`

## Проверка по коду тега v2.29.1

`roles/network_plugin/calico/templates/calico-apiserver.yml.j2:238-239`:

```yaml
  - validatingadmissionpolicies        # Required for Kubernetes 1.33+
  - validatingadmissionpolicybindings  # Required for Kubernetes 1.33+
```

Коммит `e5a1f68a2` входит в диапазон `v2.29.0..v2.29.1`.

## Версии

- **Затронуто:** v2.29.0 с Kubernetes 1.33+ (в v2.29.1 Kubernetes по умолчанию — 1.33.7).
- **Исправлено:** v2.29.1.

## Связанное

[[versions/v2.29.1/components|Компоненты (Kubernetes 1.33.7)]] · [[versions/v2.29.1/release-notes|Release notes v2.29.1]]
