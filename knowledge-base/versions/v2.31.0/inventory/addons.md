---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: inventory
source_path: inventory/sample/group_vars/k8s_cluster/addons.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - addons
  - inventory
reliability: authoritative
---

# Sample inventory: addons (v2.31.0)

Разбор файла дополнений (addons) sample-инвентаря тега `v2.31.0` (commit `1c9add4`):
`inventory/sample/group_vars/k8s_cluster/addons.yml`. Источник истины — YAML-файл
[[versions/v2.31.0/inventory/addons|addons.yaml]]; данная заметка — человекочитаемое представление.
Полный справочник значений по умолчанию — в [[versions/v2.31.0/variables/addons|variables/addons.yaml]].

Обозначения: **задана** — переменная раскомментирована (`is_set: true`); **пример** —
закомментированный образец (`is_set: false`).

## Важное изменение в v2.31.0

В `addons.yml` **удалены** переменные:

- **Kubernetes Dashboard** (`dashboard_enabled` и связанные) — роль убрана из Kubespray;
- **ingress_nginx** (`ingress_nginx_enabled` и связанные) — роль убрана из Kubespray.

В sample-файле этих переменных больше нет.

## Флаги включения дополнений (заданы, все `false`)

| Переменная | Значение | Назначение |
|---|---|---|
| `helm_enabled` | `false` | Установка клиента Helm |
| `registry_enabled` | `false` | Внутрикластерный registry |
| `metrics_server_enabled` | `false` | metrics-server |
| `local_path_provisioner_enabled` | `false` | Rancher Local Path Provisioner |
| `local_volume_provisioner_enabled` | `false` | Local Volume Provisioner |
| `gateway_api_enabled` | `false` | CRD Gateway API |
| `ingress_alb_enabled` | `false` | AWS ALB Ingress Controller |
| `cert_manager_enabled` | `false` | cert-manager |
| `metallb_enabled` | `false` | MetalLB |
| `argocd_enabled` | `false` | Argo CD |
| `kube_vip_enabled` | `false` | kube-vip (виртуальный IP API-сервера) |
| `node_feature_discovery_enabled` | `false` | Node Feature Discovery |

## Заданные (не-флаговые) переменные

| Переменная | Значение |
|---|---|
| `metallb_speaker_enabled` | `{{ metallb_enabled }}` |
| `metallb_namespace` | `metallb-system` |

## Закомментированные примеры (по компонентам)

- **Registry**: `registry_namespace`, `registry_storage_class`, `registry_disk_size`.
- **Metrics Server**: `metrics_server_container_port` (`10250`), `metrics_server_kubelet_insecure_tls` (`true`), `metrics_server_metric_resolution` (`15s`), `metrics_server_kubelet_preferred_address_types`, `metrics_server_host_network`, `metrics_server_replicas`.
- **Local Path Provisioner**: `local_path_provisioner_namespace`, `_storage_class`, `_reclaim_policy` (`Delete`), `_claim_root`, `_debug`, `_image_repo`, `_helper_image_repo` (`busybox`), `_helper_image_tag` (`latest`).
- **Local Volume Provisioner**: `local_volume_provisioner_namespace` (`kube-system`), `_nodelabels`, `_storage_classes` (пример с `local-storage` и `fast-disks`), `_tolerations`.
- **CSI Snapshot Controller**: `csi_snapshot_controller_enabled`, `snapshot_controller_namespace`.
- **ALB Ingress**: `alb_ingress_aws_region` (`us-east-1`), `alb_ingress_restrict_scheme`, `alb_ingress_aws_debug`.
- **cert-manager**: `cert_manager_namespace` (`cert-manager`), `_tolerations`, `_affinity`, `_nodeselector`, `_trusted_internal_ca`, `_leader_election_namespace`, `_dns_policy`, `_dns_config`, `_controller_extra_args`.
- **MetalLB**: `metallb_protocol` (`layer2`), `metallb_port` (`7472`), `metallb_memberlist_port` (`7946`), `metallb_config` (развёрнутый пример: speaker/controller, address_pools, layer2/layer3, communities, peers).
- **Argo CD**: `argocd_namespace` (`argocd`), `argocd_admin_password`.
- **kube-vip**: `kube_vip_arp_enabled`, `kube_vip_controlplane_enabled`, `kube_vip_address`, `loadbalancer_apiserver`, `kube_vip_interface` (`eth0`), `kube_vip_services_enabled`, `kube_vip_dns_mode` (`first`), `kube_vip_cp_detect`, `kube_vip_leasename` (`plndr-cp-lock`), `kube_vip_enable_node_labeling`, `kube_vip_lb_fwdmethod` (`local`), `kube_vip_bgp_sourceip`, `kube_vip_bgp_sourceif`.
- **Node Feature Discovery**: `node_feature_discovery_gc_sa_name`, `_gc_sa_create`, `_worker_sa_name`, `_worker_sa_create`, `node_feature_discovery_master_config`.

## Проверка расхождений с defaults

Все раскомментированные (`is_set: true`) переменные, присутствующие в `roles/*/defaults`,
сверены со значениями `default` из [[versions/v2.31.0/variables/addons|variables/addons.yaml]]
(и `roles/kubespray_defaults` для флагов включения). **Расхождений не обнаружено**.

## Навигация

- [[versions/v2.31.0/inventory/k8s-cluster|Sample inventory: k8s-cluster]]
- [[versions/v2.31.0/inventory/inventory-ini|Sample inventory.ini]]
- [[versions/v2.31.0/README|Срез v2.31.0]]
