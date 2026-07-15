---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: versions/v2.31.0/variables/addons.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - addons
reliability: authoritative
---

# Переменные аддонов (kubernetes-apps) в v2.31.0

Заметка описывает переменные роли `roles/kubernetes-apps` для тега **v2.31.0** (commit `1c9add4`). Источником истины является машиночитаемый справочник [[versions/v2.31.0/variables/addons|addons.yaml]]; данная заметка — его человекочитаемое представление.

## Обзор

- Проанализированы **все 35 файлов** `roles/kubernetes-apps/*/defaults/main.yml` тега v2.31.0.
- Суммарно извлечено **306 top-level переменных** из этих файлов — это полный набор ключей `kubernetes-apps` в данной версии.
- Дополнительно вынесены **13 флагов включения** аддонов, объявленных в `roles/kubespray_defaults/defaults/main/main.yml` (`registry_enabled`, `metrics_server_enabled`, `cinder_csi_enabled` и т. д.), — итого **319 записей** в `addons.yaml`.
- Значения по умолчанию приведены дословно, включая Jinja-выражения.

Не разбираются детально (упомянуты только флаги включения):

- `container_engine_accelerator/nvidia_gpu` — флаг `nvidia_accelerator_enabled`;
- container runtimes и сетевые CNI-плагины — их переменные вынесены в отдельные срезы (`container-runtime`, `cni`).

## Удалённые аддоны относительно v2.30.0

В v2.30.0 роли **Ingress NGINX** и **Kubernetes Dashboard** были помечены как последние поддерживаемые. В **v2.31.0 они удалены**:

- **Ingress NGINX** — каталог `roles/kubernetes-apps/ingress_controller/ingress_nginx/` удалён целиком (в v2.30.0 его `defaults/main.yml` содержал 25 top-level ключей). Флаг `ingress_nginx_enabled` из `kubespray_defaults` также удалён.
- **Kubernetes Dashboard** — удалён из роли `roles/kubernetes-apps/ansible` (число ключей роли `ansible` упало 63 → 28; убрано 13 ключей `dashboard*` и связанные с ними). Флаг `dashboard_enabled` из `kubespray_defaults` также удалён.

Итог по количеству ключей `kubernetes-apps`: **365 (v2.30.0) → 306 (v2.31.0)**, то есть на 59 ключей меньше. Новых defaults-файлов в `kubernetes-apps` в v2.31.0 не добавлено.

Проверка выполнена сравнением тегов через `git ls-tree`/`git show` между `v2.30.0` и `v2.31.0`.

## Таблица флагов включения аддонов

| Аддон | Флаг включения | Default | Где объявлен |
|---|---|---|---|
| Helm (клиент) | `helm_enabled` | `false` | `helm/defaults/main.yml` |
| Docker registry | `registry_enabled` | `false` | `kubespray_defaults` |
| metrics-server | `metrics_server_enabled` | `false` | `kubespray_defaults` |
| Local Path Provisioner | `local_path_provisioner_enabled` | `false` | `external_provisioner/local_path_provisioner` |
| Local Volume Provisioner | `local_volume_provisioner_enabled` | `false` | `kubespray_defaults` |
| Cinder CSI | `cinder_csi_enabled` | `false` | `kubespray_defaults` |
| AWS EBS CSI | `aws_ebs_csi_enabled` | `false` | `kubespray_defaults` |
| Azure Disk CSI | `azure_csi_enabled` | `false` | `kubespray_defaults` |
| GCP PD CSI | `gcp_pd_csi_enabled` | `false` | `kubespray_defaults` |
| vSphere CSI | `vsphere_csi_enabled` | `false` | `kubespray_defaults` |
| UpCloud CSI | `upcloud_csi_enabled` | `false` | `kubespray_defaults` |
| CSI snapshot-controller | `csi_snapshot_controller_enabled` | `false` | `kubespray_defaults` |
| PersistentVolumes | `persistent_volumes_enabled` | `false` | `kubespray_defaults` |
| AWS ALB Ingress | `ingress_alb_enabled` | `false` | `kubespray_defaults` |
| cert-manager | `cert_manager_enabled` | `false` | `kubespray_defaults` |
| MetalLB | `metallb_enabled` | `false` | `metallb/defaults/main.yml` |
| MetalLB speaker | `metallb_speaker_enabled` | `{{ metallb_enabled }}` | `metallb/defaults/main.yml` |
| Argo CD | `argocd_enabled` | `false` | `argocd/defaults/main.yml` |
| Gateway API (CRD) | `gateway_api_enabled` | `false` | `common_crds/gateway_api` |
| Node Feature Discovery | `node_feature_discovery_enabled` | `false` | `node_feature_discovery` |
| scheduler-plugins | `scheduler_plugins_enabled` | `false` | `scheduler_plugins/defaults/main.yml` |
| kubelet-csr-approver | `kubelet_csr_approver_enabled` | `{{ kubelet_rotate_server_certificates }}` | `kubelet-csr-approver` |
| NVIDIA GPU device plugin | `nvidia_accelerator_enabled` | `false` | `container_engine_accelerator/nvidia_gpu` |

Все аддоны по умолчанию выключены. Флаг `metallb_speaker_enabled` наследует значение `metallb_enabled`, а `kubelet_csr_approver_enabled` — значение `kubelet_rotate_server_certificates`.

## Разбивка по компонентам (число top-level переменных)

- CoreDNS / nodelocaldns / dns-autoscaler (`ansible`) — 28
- Argo CD — 3
- Gateway API — 2
- NVIDIA GPU (`nvidia_gpu`) — 13
- CSI-драйверы: `aws_ebs` 5, `azuredisk` 5, `cinder` 26, `gcp_pd` 1, `upcloud` 15, `vsphere` 33
- External cloud controllers: `hcloud` 1, `huaweicloud` 9, `oci` 19, `openstack` 17, `vsphere` 6
- Провизионеры: `local_path_provisioner` 10, `local_volume_provisioner` 6
- Helm — 1
- Ingress: `alb_ingress_controller` 3, `cert_manager` 12
- kubelet-csr-approver — 7
- MetalLB — 11
- metrics-server — 13
- Node Feature Discovery — 15
- persistent_volumes: `aws-ebs-csi` 2, `azuredisk-csi` 1, `cinder-csi` 1, `gcp-pd-csi` 4, `upcloud-csi` 1
- policy_controller `calico` — 7
- registry — 17
- scheduler_plugins — 8
- snapshots: `cinder-csi` 1, `snapshot-controller` 2
- utils — 1

**Итого: 306.**

## Примечания к достоверности

Часть переменных Node Feature Discovery (`node_feature_discovery_master_crd_controller`, `..._master_instance`, `..._master_config`, `..._worker_config`, `..._worker_tolerations`) имеют значение `null` и передаются в чарт NFD как есть; точная семантика зависит от версии чарта, поэтому в `addons.yaml` они помечены `reliability: unconfirmed`.

## Ссылки

- [[versions/v2.31.0/variables/addons|addons.yaml — машиночитаемый справочник]]
- [[versions/v2.31.0/README|Срез v2.31.0]]
