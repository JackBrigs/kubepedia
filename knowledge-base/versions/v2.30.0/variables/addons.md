---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: code
source_path: versions/v2.30.0/variables/addons.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - addons
  - kubernetes-apps
reliability: authoritative
---

# Переменные аддонов (kubernetes-apps) — Kubespray v2.30.0

Справочник переменных дополнительных компонентов кластера из `roles/kubernetes-apps/*/defaults`. Источник истины — парный `addons.yaml` (380 переменных, покрытие defaults полное). Из охвата исключены детально: сетевые плагины (кроме Cilium — отдельный справочник), `container_engine_accelerator`/`nvidia_gpu`, `container_runtimes`.

- **Всего переменных:** 380
- **Разобрано групп аддонов:** 37

## Флаги включения аддонов

Переменные вида `*_enabled`, управляющие развёртыванием аддона (значения по умолчанию — дословно из кода):

| Переменная | Значение по умолчанию |
|---|---|
| `argocd_enabled` | `false` |
| `aws_ebs_csi_enabled` | `false` |
| `azure_csi_enabled` | `false` |
| `cert_manager_enabled` | `false` |
| `cinder_csi_enabled` | `false` |
| `csi_snapshot_controller_enabled` | `false` |
| `dashboard_enabled` | `false` |
| `gateway_api_enabled` | `false` |
| `gcp_pd_csi_enabled` | `false` |
| `gcp_pd_regional_replication_enabled` | `false` |
| `helm_enabled` | `false` |
| `ingress_alb_enabled` | `false` |
| `ingress_nginx_enabled` | `false` |
| `ingress_nginx_opentelemetry_enabled` | `false` |
| `ingress_nginx_webhook_enabled` | `false` |
| `kubelet_csr_approver_enabled` | `{{ kubelet_rotate_server_certificates }}` |
| `local_path_provisioner_enabled` | `false` |
| `local_volume_provisioner_enabled` | `false` |
| `metallb_enabled` | `false` |
| `metallb_speaker_enabled` | `{{ metallb_enabled }}` |
| `metrics_server_enabled` | `false` |
| `node_feature_discovery_enabled` | `false` |
| `nvidia_accelerator_enabled` | `false` |
| `persistent_volumes_enabled` | `false` |
| `registry_enabled` | `false` |
| `scheduler_plugins_enabled` | `false` |
| `upcloud_csi_enabled` | `false` |
| `vsphere_csi_enabled` | `false` |

## Переменные по аддонам

Полный перечень — в `addons.yaml`. Ниже — состав по группам (число переменных):

| Аддон / группа | Переменных |
|---|---|
| `ansible/defaults` | 63 |
| `csi_driver/vsphere` | 33 |
| `csi_driver/cinder` | 26 |
| `ingress_controller/ingress_nginx` | 25 |
| `external_cloud_controller/oci` | 19 |
| `external_cloud_controller/openstack` | 17 |
| `registry` | 17 |
| `флаги включения (kubespray_defaults)` | 15 |
| `node_feature_discovery` | 15 |
| `csi_driver/upcloud` | 15 |
| `container_engine_accelerator` | 13 |
| `metrics_server` | 13 |
| `ingress_controller/cert_manager` | 12 |
| `metallb` | 11 |
| `external_provisioner/local_path_provisioner` | 9 |
| `external_cloud_controller/huaweicloud` | 9 |
| `scheduler_plugins` | 8 |
| `kubelet-csr-approver` | 7 |
| `policy_controller/calico` | 7 |
| `external_cloud_controller/vsphere` | 6 |
| `external_provisioner/local_volume_provisioner` | 6 |
| `csi_driver/aws_ebs` | 5 |
| `csi_driver/azuredisk` | 5 |
| `persistent_volumes/gcp-pd-csi` | 4 |
| `argocd` | 3 |
| `ingress_controller/alb_ingress_controller` | 3 |
| `common_crds/gateway_api` | 2 |
| `persistent_volumes/aws-ebs-csi` | 2 |
| `snapshots/snapshot-controller` | 2 |
| `helm` | 1 |
| `csi_driver/gcp_pd` | 1 |
| `external_cloud_controller/hcloud` | 1 |
| `persistent_volumes/azuredisk-csi` | 1 |
| `persistent_volumes/cinder-csi` | 1 |
| `persistent_volumes/upcloud-csi` | 1 |
| `snapshots/cinder-csi` | 1 |
| `utils` | 1 |

## Примечания

- Источник истины — `addons.yaml`; эта заметка — презентация (правило 17.4).
- Полнота сверена с кодом: реальных top-level ключей в defaults `kubernetes-apps` — 365, извлечено 380 (включая флаги включения из `kubespray_defaults`).
- Непроиндексированные детально: сетевые плагины (см. [[versions/v2.30.0/variables/cni|cni]]), `container_engine_accelerator`, `container_runtimes`.

Назад: [[versions/v2.30.0/README|Срез v2.30.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
