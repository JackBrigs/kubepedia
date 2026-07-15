---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_paths:
  - roles/kubespray_defaults/defaults/main/download.yml
  - roles/kubespray_defaults/defaults/main/main.yml
  - roles/kubespray_defaults/vars/main/main.yml
  - roles/kubespray_defaults/vars/main/checksums.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - components
  - versions
reliability: authoritative
---

# Компоненты и версии по умолчанию в v2.31.0

Срез: [[versions/v2.31.0/README|Срез v2.31.0]]

Источник истины — YAML-справочник [[versions/v2.31.0/components|components.yaml]].
Ниже — человекочитаемая таблица. Версии, зависящие от Kubernetes, разрешены для
`kube_major_version = 1.35`.

## Цепочка разрешения версии Kubernetes

`kube_version` берётся как первый ключ таблицы `kubelet_checksums['amd64']`
(самая новая поддерживаемая версия):

- `kube_version` = **1.35.4**
- `kube_major_version` = **1.35**
- `kube_major_next_version` = **1.36**

От `kube_major_version` зависят версии etcd, coredns, pause (pod_infra),
snapshot_controller и scheduler_plugins; от `kube_major_next_version` — выбор
crictl и cri-o (наибольшая версия строго ниже 1.36).

## Основные компоненты

| Компонент | Переменная | Версия |
|---|---|---|
| Kubernetes | `kube_version` | 1.35.4 |
| etcd | `etcd_version` | 3.6.10 |
| containerd | `containerd_version` | 2.2.3 |
| runc | `runc_version` | 1.4.2 |
| crictl | `crictl_version` | 1.35.0 |
| nerdctl | `nerdctl_version` | 2.2.2 |
| cni-plugins | `cni_version` | 1.9.1 |
| CoreDNS | `coredns_version` | 1.12.4 |
| nodelocaldns | `nodelocaldns_version` | 1.25.0 |
| pause (pod_infra) | `pod_infra_version` | 3.10.1 |
| Helm | `helm_version` | 3.18.4 |

## Container runtime / низкоуровневые рантаймы

| Компонент | Переменная | Версия | Примечание |
|---|---|---|---|
| cri-o | `crio_version` | 1.35.0 | при `container_manager=crio` |
| cri-dockerd | `cri_dockerd_version` | 0.3.24 | при `container_manager=docker` |
| docker containerd | `docker_containerd_version` | 1.6.32 | при `container_manager=docker` |
| skopeo | `skopeo_version` | 1.16.1 | при crio |
| crun | `crun_version` | 1.17 | |
| youki | `youki_version` | 0.5.7 | |
| gVisor | `gvisor_version` | 20260323.0 | версия — дата; только amd64 |
| Kata Containers | `kata_containers_version` | 3.7.0 | |

## Сеть (CNI)

| Компонент | Переменная | Версия | Примечание |
|---|---|---|---|
| Calico | `calico_version` | 3.31.5 | ctl/cni/policy/typha/apiserver наследуют |
| Cilium | `cilium_version` | 1.19.3 | жёстко задано |
| Cilium CLI | `cilium_cli_version` | 0.18.9 | |
| Flannel | `flannel_version` | 0.28.4 | cni: 1.7.1-flannel1 |
| kube-ovn | `kube_ovn_version` | 1.12.21 | |
| kube-router | `kube_router_version` | 2.1.1 | |
| Multus | `multus_version` | 4.2.2 | |

## Приложения и дополнения

| Компонент | Переменная | Версия |
|---|---|---|
| kube-vip | `kube_vip_version` | 1.0.3 |
| Gateway API | `gateway_api_version` | 1.5.1 |
| metrics-server | `metrics_server_version` | 0.8.1 |
| cert-manager | `cert_manager_version` | 1.15.3 |
| Argo CD | `argocd_version` | 2.14.21 |
| MetalLB | `metallb_version` | 0.13.9 |
| local-path-provisioner | `local_path_provisioner_version` | 0.0.32 |
| local-volume-provisioner | `local_volume_provisioner_version` | 2.5.0 |
| registry | `registry_version` | 2.8.1 |
| dns-autoscaler | `dnsautoscaler_version` | 1.8.8 |
| node-feature-discovery | `node_feature_discovery_version` | 0.16.4 |
| prometheus-operator CRDs | `prometheus_operator_crds_version` | 0.88.1 |
| yq | `yq_version` | 4.42.1 |

## Разрешение Jinja-выражений

Для многих компонентов версия задаётся выражением вида
`{{ (X_checksums['amd64'] | dict2items)[0].key }}` — это первый ключ
соответствующего словаря в `roles/kubespray_defaults/vars/main/checksums.yml`.
Ключи там упорядочены по убыванию версии, поэтому первый ключ = самая новая
поддерживаемая версия. Точные выражения и их разрешённые значения — в
[[versions/v2.31.0/components|components.yaml]].

## Удалённые компоненты (относительно предыдущих версий)

- **ingress_nginx** (nginx ingress controller) — роль удалена. В
  `roles/kubernetes-apps/ingress_controller/` остался только
  `alb_ingress_controller`; переменных `ingress_nginx_*` в `download.yml` нет.
- **kubernetes-dashboard** — отсутствует в v2.31.0 (ссылок на dashboard в
  `kubespray_defaults` нет).

## Изменения версий относительно v2.30.0

| Компонент | v2.30.0 | v2.31.0 |
|---|---|---|
| Kubernetes | 1.34.3 | 1.35.4 |
| containerd | 2.2.1 | 2.2.3 |
| Cilium | 1.18.6 | 1.19.3 |
| Gateway API | 1.4.1 | 1.5.1 |
