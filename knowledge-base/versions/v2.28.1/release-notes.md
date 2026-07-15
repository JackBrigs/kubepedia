---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
git_commit_full: a20891ab67136f8c92ccad3fad9ad11fc71363d0
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.28.1
retrieved_at: 2026-07-15
topics:
  - release
  - versions
  - changelog
reliability: authoritative
---

# GitHub Release Kubespray v2.28.1

- **Тег:** `v2.28.1` (commit `a20891a`, полный `a20891ab67136f8c92ccad3fad9ad11fc71363d0`)
- **Дата релиза/тега:** 26 августа 2025.
- **Тип:** **патч-релиз** над v2.28.0 — только исправления ошибок и регрессий, обновление патч-версий компонентов. **Новых breaking changes нет.**
- **Субъект коммита тега:** `Fix SAN address collection from ansible_default_ipv{4,6} (#12505)`.
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.28.1

## Версии компонентов (по релизу)

Официально указанные в релизе версии. **Сверены с разрешёнными из кода тега** ([[versions/v2.28.1/components|components]]). В скобках — значение в v2.28.0 (что изменилось патчем).

| Компонент | Версия (релиз) | В `components.yaml` |
|---|---|---|
| Kubernetes | 1.32.8 (было 1.32.5) | ✓ совпадает |
| etcd | 3.5.22 (было 3.5.16) | ✓ совпадает |
| containerd | 2.0.6 (было 2.0.5) | ✓ совпадает |
| CRI-O | 1.32.0 | ✓ совпадает |
| cri-dockerd | 0.3.18 (было 0.3.17) | ✓ совпадает |
| Calico | 3.29.5 (было 3.29.3) | ✓ совпадает |
| Cilium | 1.17.7 (было 1.17.3) | ✓ совпадает |
| cilium-cli | 0.18.6 (было 0.18.3) | ✓ совпадает |
| youki | 0.5.5 (было 0.5.3) | ✓ совпадает |
| gVisor | 20250820.0 (было 20250512.0) | ✓ совпадает |
| Flannel | 0.22.0 | ✓ совпадает |
| kube-ovn | 1.12.21 | ✓ совпадает |
| kube-router | 2.1.1 | ✓ совпадает |
| CoreDNS | 1.11.3 | ✓ совпадает |
| Helm | 3.16.4 | ✓ совпадает |
| Ingress-NGINX | 1.12.1 | ✓ совпадает |
| Argo CD | 2.14.5 | ✓ совпадает |
| cert-manager | 1.15.3 | ✓ совпадает |

Патчем поднялись только версии компонентов, вычисляемые из `checksums.yml` по «первому ключу» (kube, containerd, calico, cilium-cli, cri-dockerd, youki, gVisor), а также `cilium_version` (литерал 1.17.3 → 1.17.7) и `etcd_version` (переведён на выражение «наибольшая версия < 3.6», резолвится в 3.5.22). Версия Argo CD (2.14.5) не изменилась, но механизм её установки переработан (см. ниже).

## Breaking changes

**Отсутствуют.** Это патч-релиз; breaking changes и удаления функций (Krew, Equinix Metal, `etcd_kubeadm_enabled`, снятие ведущей `v` у версий и пр.) относятся к минорному релизу v2.28.0 и в v2.28.1 не добавлялись.

## Исправления ошибок и регрессий (What's Changed)

Полный список PR патча:

- **#12467** — добавлен `argocd_install_checksum` для проверки контрольной суммы `argocd_install_url` (ArgoCD теперь ставится по checksum через `downloads.argocd_install`).
- **#12505** — добавлены недостающие адреса (`ansible_default_ipv4/ipv6`) в SAN сертификата kube-apiserver (субъект коммита тега).
- **#12283** — исправлены ошибки установки Cilium из-за синтаксиса шаблонов при включении нестандартных возможностей (шифрование и т.п.).
- **#12374** — исправлено обнаружение peer у Hubble-Relay в кластерах с нестандартным именем: корректная настройка `clusterDomain` в helm-values Cilium (переменная `cilium_hubble_peer_service_cluster_domain`).
- **#12338** — Cilium-роль теперь рендерит `cilium_config_extra_vars` в helm-values.
- **#12478** — исправлена некорректная конфигурация PodSecurity admission при `kube_pod_security_use_default: false`.
- **#12324** — исправлено падение при апгрейде кластера Cilium с 2.27 на 2.28 (введена миграционная задача `remove_old_resources` и переменная `cilium_remove_old_resources`); исправлено сообщение о повторном использовании helm-release.
- **#12352** — исправлен сбой добавления узла etcd из-за неверного `ETCD_INITIAL_CLUSTER`.
- **#12354** — kubeadm: флаг `--skip-phases` добавляется условно для Kubernetes v1.32.0+ (переменные `kubeadm_upgrade_node_phases_skip*`).
- **#12316** — исправлено получение `image_id` в `manage-offline-container-images.sh register` при использовании Podman.
- **#12432** — исправлена конфигурация `cilium_enable_bgp_control_plane`.
- **#12394** — исправлена синтаксическая ошибка, из-за которой `_bgp_config` становился `AnsibleUnsafeText` вместо `dict` и ломал шаг «Calico | Process BGP Configuration».

## Влияние на срез знаний (что изменилось относительно v2.28.0)

- **Cilium:** версия 1.17.3 → 1.17.7; добавлены переменные `cilium_remove_old_resources` (миграция, #12324) и `cilium_hubble_peer_service_cluster_domain` (#12374); в sample добавлена закомментированная `cilium_hubble_peer_service_cluster_domain`.
- **ArgoCD (#12467):** `argocd_version` резолвится из `argocd_install_checksums.no_arch`; добавлены `argocd_install_url` и `argocd_install_checksum` в `download.yml`; установка через `downloads.argocd_install` по контрольной сумме. Из defaults роли argocd убран `argocd_install_url`.
- **kubeadm (#12354):** добавлены `kubeadm_upgrade_node_phases_skip_default` и `kubeadm_upgrade_node_phases_skip` (main.yml).
- **etcd:** `etcd_supported_versions` переведены с литерала 3.5.16 на выражение (наибольшая версия < 3.6) → 3.5.22.

## Примечания

- Детальное сравнение кода с соседней версией (v2.28.0 → v2.28.1) выполняется отдельным отчётом в `diffs/` при построении цепочки версий.
- Номера PR и версии извлечены со страницы GitHub Release и подтверждены субъектом коммита тега (`#12505`) и разбором кода тега; reliability: authoritative.

---

Связанные срезы: [[versions/v2.28.1/components|Компоненты и версии]]

Назад: [[versions/v2.28.1/README|Срез v2.28.1]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
