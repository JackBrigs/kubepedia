---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
git_commit_full: 63cdf87915421dda5955281f38401fd1b55b230b
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.28.0
retrieved_at: 2026-07-15
topics:
  - release
  - versions
  - changelog
reliability: authoritative
---

# GitHub Release Kubespray v2.28.0

- **Тег:** `v2.28.0` (commit `63cdf87`, полный `63cdf87915421dda5955281f38401fd1b55b230b`)
- **Дата тега:** 20 мая 2025.
- **Тип:** минорный релиз (feature release) — новые возможности, breaking changes и удаление устаревших функций относительно v2.27.x.
- **Субъект коммита тега:** `Removed equinix provider (#12229)`.
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.28.0

## Версии компонентов (по релизу)

Официально указанные в релизе версии. **Сверены с разрешёнными из кода тега** ([[versions/v2.28.0/components|components]]).

| Компонент | Версия (релиз) | В `components.yaml` |
|---|---|---|
| Kubernetes | 1.32.5 | ✓ совпадает |
| etcd | 3.5.16 | ✓ совпадает |
| containerd | 2.0.5 | ✓ совпадает |
| Docker | 28.0 | движок Docker (не индексируется отдельно) |
| CRI-O | 1.32.0 | ✓ совпадает |
| Calico | 3.29.3 | ✓ совпадает |
| Cilium | 1.17.3 | ✓ совпадает |
| Flannel | 0.22.0 | ✓ совпадает |
| kube-ovn | 1.12.21 | ✓ совпадает |
| kube-router | 2.1.1 | ✓ совпадает |
| CoreDNS | 1.11.3 | ✓ совпадает |
| Helm | 3.16.4 | ✓ совпадает |
| Ingress-NGINX | 1.12.1 | ✓ совпадает |
| Argo CD | 2.14.5 | ✓ совпадает |
| cert-manager | 1.15.3 | ✓ совпадает |

## Breaking changes / требуются действия при обновлении

- **#11890** — необходимо убрать ведущую `v` из всех явно заданных версий компонентов в inventory (переменные `*_version` теперь задаются без префикса `v`). Это изменение согласуется с логикой `download.yml`, где префикс `v` подставляется в URL шаблонами.
- **#11901** — удалён (ранее deprecated) параметр `etcd_kubeadm_enabled`; его нужно убрать из inventory.
- **#11824** — удалена поддержка установки **Krew**.
- **#12229** — удалён провайдер **Equinix Metal** (Packet); субъект коммита тега. Соответствующая инфраструктура и переменные провайдера более недоступны.

## Устаревшие функции (deprecations)

- **#11763** — `gateway_api_experimental_channel` объявлен устаревшим; следует использовать `gateway_api_channel`.
- **#11872** — **последняя** версия Kubespray с поддержкой **RHEL 8**.
- Анонсировано предстоящее удаление CNI **Weave** в следующем релизе (в v2.28.0 Weave 2.8.7 ещё присутствует).

## Удалённые функции (removed)

- Поддержка установки Krew (#11824).
- Провайдер Equinix Metal (#12229).
- Playbook **Heketi** (#12091).
- `contrib/kvm-setup` и `contrib/mitogen` (#12093).
- Документация Cephfs-provisioner и rbd-provisioner (#12113, #12114).

## Заметные новые возможности

- **#12218** — новый параметр `deploy_coredns` (bool, по умолчанию `true`): позволяет управлять развёртыванием CoreDNS силами Kubespray.
- **#11852** — поддержка структурированных файлов `AuthorizationConfiguration` (см. `kube_apiserver_use_authorization_config_file` в defaults).
- **#12060** — поддержка режима **nftables** для kube-proxy.
- **#12101** — установка Cilium переведена с Jinja-шаблонов на **Cilium CLI**.
- **#11883** — `external_cloud_provider` получил опцию `manual`.
- **#12189** — CRD Gateway API разворачиваются до установки CNI.

## Примечания

- Полный сравнительный changelog `v2.27.x...v2.28.0` на странице релиза приведён списком PR; детальное сравнение кода с предыдущей проиндексированной версией (v2.29.1) выполняется отдельным отчётом в `diffs/` при построении цепочки версий.
- Номера PR и версии выше извлечены со страницы GitHub Release и подтверждены субъектом коммита тега (`#12229`); reliability: authoritative.

---

Связанные срезы: [[versions/v2.28.0/components|Компоненты и версии]]

Назад: [[versions/v2.28.0/README|Срез v2.28.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
