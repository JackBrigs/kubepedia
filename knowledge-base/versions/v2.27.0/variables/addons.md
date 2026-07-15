---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: code
source_path: versions/v2.27.0/variables/addons.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - addons
  - kubernetes-apps
reliability: authoritative
---

# Переменные аддонов (kubernetes-apps) в Kubespray v2.27.0

Справочник переменных дополнительных компонентов, разворачиваемых ролями `roles/kubernetes-apps/*` на теге `v2.27.0` (коммит `9ec9b3a`).

**Источник истины** — машиночитаемый справочник [[versions/v2.27.0/variables/addons|addons.yaml]] (409 переменных: 390 из defaults ролей `kubernetes-apps` + 19 флагов-переключателей, определённых только в `roles/kubespray-defaults`). Эта заметка — человекочитаемое изложение.

Назад к срезу: [[versions/v2.27.0/README|Срез v2.27.0]]

## Обзор

В v2.27.0 через `kubernetes-apps` доступны следующие аддоны:

- **DNS-стек** (роль `kubernetes-apps/ansible`): CoreDNS, dns-autoscaler, nodelocaldns;
- **Netchecker** — проверка сетевой связности;
- **Kubernetes Dashboard** (ресурсы разворачивает роль `kubernetes-apps/ansible`);
- **Helm** (установка CLI на control plane) и **krew** (менеджер плагинов kubectl);
- **Внутрикластерный registry**;
- **metrics-server**;
- **Ingress-контроллеры**: ingress-nginx, AWS ALB Ingress Controller;
- **cert-manager**;
- **MetalLB**;
- **Argo CD**;
- **CRD**: Gateway API (роль `kubernetes-apps/gateway_api`);
- **Провижионеры хранилища**: Local Path Provisioner, local-volume-provisioner, CephFS-провижионер, Ceph RBD-провижионер;
- **CSI-драйверы**: AWS EBS, Azure Disk, OpenStack Cinder, GCP PD, UpCloud, vSphere;
- **Внешние cloud controller manager**: Hetzner (hcloud), Huawei Cloud, Oracle (OCI), OpenStack, vSphere;
- **persistent_volumes** — создание StorageClass для облачных CSI;
- **snapshots** — snapshot-controller и VolumeSnapshotClass для Cinder;
- **kubelet-csr-approver** — автоодобрение CSR kubelet (ставится Helm-чартом);
- **Node Feature Discovery (NFD)**;
- **scheduler-plugins** — второй планировщик;
- **container_engine_accelerator/nvidia_gpu** — GPU-ускорители NVIDIA (device plugin и опциональная установка драйверов);
- **policy_controller/calico** — calico-kube-controllers.

## Отличия структуры v2.27.0 от более новых версий

- флаги-переключатели аддонов лежат в `roles/kubespray-defaults` (через **дефис**), а не `roles/kubespray_defaults`;
- Gateway API находится в `roles/kubernetes-apps/gateway_api`, а не в `common_crds/gateway_api`; канал задаётся булевым флагом `gateway_api_experimental_channel` (в более новых версиях — строкой `gateway_api_channel`), а версия по умолчанию — `v1.1.0`;
- присутствуют роли `external_provisioner/cephfs_provisioner` и `external_provisioner/rbd_provisioner` (Ceph-провижионеры) со своими `defaults/`;
- присутствует роль `krew` со своими `defaults/`;
- **container_engine_accelerator/nvidia_gpu ПРОИНДЕКСИРОВАН** в этом справочнике (в отличие от среза v2.29.1, где он был сознательно исключён);
- нет ролей `common_crds/prometheus_operator_crds`, поэтому нет флага `prometheus_operator_crds_enabled`;
- флаги `deploy_coredns`, `enable_dns_autoscaler`, `enable_nodelocaldns` в v2.27.0 отсутствуют в defaults `kubernetes-apps/ansible` — включение DNS-стека управляется переменными k8s-cluster (`enable_dns_autoscaler`/`enable_nodelocaldns` — в `roles/kubespray-defaults`), здесь описаны только ресурсы/настройки подов.

## Что НЕ проиндексировано (сознательно)

- сетевые плагины (CNI) — отдельный справочник `variables/cni.yaml`; каталоги `roles/kubernetes-apps/network_plugin/*` не имеют собственных `defaults/`;
- `roles/kubernetes-apps/container_runtimes/*` (kata_containers, crun, gvisor, youki) — относятся к справочнику container runtime, собственных `defaults/` не имеют;
- роли без собственных `defaults/`: `cluster_roles`, `csi_driver/csi_crd`.

Роль `roles/helm-apps` в v2.27.0 каталога `defaults/` **не имеет** — её параметры (`helm_update`, `helm_defaults`, `helm_repository_defaults`) лежат в `roles/helm-apps/vars/main.yml` и в справочник defaults не включены (в подсчёт полноты не входят).

## Переменные включения аддонов

Все флаги по умолчанию выключены (`false`), кроме особо отмеченных. Часть флагов определена одновременно в `roles/kubespray-defaults/defaults/main/main.yml` и в defaults самой роли (отмечено «оба места»).

| Аддон | Переменная включения | Значение по умолчанию | Где определена |
|---|---|---|---|
| Netchecker | `deploy_netchecker` | `false` | оба места |
| Kubernetes Dashboard | `dashboard_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| Helm | `helm_enabled` | `false` | оба места |
| krew | `krew_enabled` | `false` | оба места |
| Registry | `registry_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| metrics-server | `metrics_server_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| ingress-nginx | `ingress_nginx_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| ALB Ingress | `ingress_alb_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| cert-manager | `cert_manager_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| MetalLB | `metallb_enabled` | `false` | оба места |
| MetalLB speaker | `metallb_speaker_enabled` | `{{ metallb_enabled }}` | оба места |
| Argo CD | `argocd_enabled` | `false` | оба места |
| Gateway API CRD | `gateway_api_enabled` | `false` | `roles/kubernetes-apps/gateway_api/defaults/main.yml` |
| Local Path Provisioner | `local_path_provisioner_enabled` | `false` | оба места |
| local-volume-provisioner | `local_volume_provisioner_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| CephFS-провижионер | `cephfs_provisioner_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| Ceph RBD-провижионер | `rbd_provisioner_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| Cinder CSI | `cinder_csi_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| AWS EBS CSI | `aws_ebs_csi_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| Azure Disk CSI | `azure_csi_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| GCP PD CSI | `gcp_pd_csi_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| vSphere CSI | `vsphere_csi_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| UpCloud CSI | `upcloud_csi_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| snapshot-controller | `csi_snapshot_controller_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| StorageClass облаков | `persistent_volumes_enabled` | `false` | `roles/kubespray-defaults/defaults/main/main.yml` |
| NVIDIA GPU | `nvidia_accelerator_enabled` | `false` | `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml` |
| kubelet-csr-approver | `kubelet_csr_approver_enabled` | `{{ kubelet_rotate_server_certificates }}` | `roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml` |
| Node Feature Discovery | `node_feature_discovery_enabled` | `false` | `roles/kubernetes-apps/node_feature_discovery/defaults/main.yml` |
| scheduler-plugins | `scheduler_plugins_enabled` | `false` | оба места |

Внешние cloud controller manager включаются не флагом `*_enabled`, а связкой `cloud_provider: "external"` + `external_cloud_provider: <имя>` (обе переменные — в `roles/kubespray-defaults/defaults/main/main.yml`).

## Ключевые настройки основных аддонов

### CoreDNS / dns-autoscaler / nodelocaldns

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `dns_min_replicas` | `{{ [2, groups['k8s_cluster'] \| length] \| min }}` | минимум реплик CoreDNS для автоскейлера |
| `dns_nodes_per_replica` | `16` | узлов на реплику CoreDNS |
| `dns_cores_per_replica` | `256` | ядер на реплику CoreDNS |
| `enable_coredns_reverse_dns_lookups` | `true` | обратные PTR-запросы |
| `coredns_pod_disruption_budget` | `false` | PDB для CoreDNS |
| `nodelocaldns_prometheus_port` | `9253` | порт метрик nodelocaldns |
| `old_dns_domains` | `[]` | прежние домены кластера после смены `dns_domain` |

### metrics-server

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `metrics_server_kubelet_insecure_tls` | `true` | не проверять TLS kubelet |
| `metrics_server_metric_resolution` | `15s` | интервал сбора метрик |
| `metrics_server_replicas` | `1` | число реплик |
| `metrics_server_host_network` | `false` | hostNetwork |

### ingress-nginx

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `ingress_nginx_namespace` | `"ingress-nginx"` | namespace |
| `ingress_nginx_service_type` | `LoadBalancer` | тип сервиса |
| `ingress_nginx_class` | `nginx` | имя IngressClass |
| `ingress_nginx_without_class` | `true` | обрабатывать Ingress без класса |
| `ingress_nginx_webhook_enabled` | `false` | admission webhook |

### MetalLB

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `metallb_port` | `"7472"` | порт метрик |
| `metallb_memberlist_port` | `"7946"` | порт memberlist |
| `metallb_speaker_enabled` | `{{ metallb_enabled }}` | DaemonSet speaker |
| `metallb_speaker_tolerations` | toleration на control plane (`NoSchedule`) | tolerations speaker |
| `metallb_loadbalancer_class` | `""` | обслуживаемый loadBalancerClass |

### cert-manager

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `cert_manager_namespace` | `"cert-manager"` | namespace |
| `cert_manager_user` | `1001` | UID подов |
| `cert_manager_leader_election_namespace` | `kube-system` | namespace leader election |

### Argo CD

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `argocd_version` | `v2.11.0` | версия Argo CD |
| `argocd_namespace` | `argocd` | namespace |
| `argocd_install_url` | манифест argoproj для `argocd_version` | URL установки |

### Gateway API

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `gateway_api_version` | `v1.1.0` | версия CRD |
| `gateway_api_experimental_channel` | `false` | экспериментальный канал вместо стандартного |

### Local Path Provisioner

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `local_path_provisioner_namespace` | `"local-path-storage"` | namespace |
| `local_path_provisioner_storage_class` | `"local-path"` | имя StorageClass |
| `local_path_provisioner_is_default_storageclass` | `"true"` | класс по умолчанию |
| `local_path_provisioner_claim_root` | `/opt/local-path-provisioner/` | каталог томов на узлах |

### NVIDIA GPU (container_engine_accelerator)

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `nvidia_driver_version` | `"390.87"` | версия драйвера |
| `nvidia_gpu_flavor` | `tesla` | серия GPU (tesla/gtx) |
| `nvidia_driver_install_container` | `false` | установка драйвера через контейнер |
| `nvidia_gpu_device_plugin_memory` | `30Mi` | память device plugin |

### kubelet-csr-approver

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kubelet_csr_approver_enabled` | `{{ kubelet_rotate_server_certificates }}` | включение (следует за ротацией сертификатов kubelet) |
| `kubelet_csr_approver_chart_version` | `1.1.0` | версия Helm-чарта |
| `kubelet_csr_approver_values` | `{}` | переопределение values |

### Node Feature Discovery

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `node_feature_discovery_namespace` | `node-feature-discovery` | namespace |
| `node_feature_discovery_enable_nodefeature_api` | `true` | NodeFeature API (CRD) |
| `node_feature_discovery_gc_interval` | `1h` | интервал nfd-gc |

### scheduler-plugins

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `scheduler_plugins_namespace` | `scheduler-plugins` | namespace |
| `scheduler_plugins_enabled_plugins` | Coscheduling, CapacityScheduling, NodeResourceTopologyMatch, NodeResourcesAllocatable | включённые плагины |
| `scheduler_plugins_disabled_plugins` | PrioritySort | отключённые плагины |

### CSI-драйверы (сводно)

| Драйвер | Реплики контроллера | Ключевые переменные |
|---|---|---|
| AWS EBS | `aws_ebs_csi_controller_replicas: 1` | `aws_ebs_csi_enable_volume_scheduling: true`, snapshot/resizing: `false`, тег образа `latest` |
| Azure Disk | `azure_csi_controller_replicas: 2` | `azure_csi_use_instance_metadata: true`, тег образа `latest` |
| Cinder | `cinder_csi_controller_replicas: 1` | креды из окружения `OS_*`, теги sidecar-образов v4.4.2/v3.6.2/v6.3.2/v1.9.2/v2.11.0, `cinder_blockstorage_version: "v3"` |
| GCP PD | `gcp_pd_csi_controller_replicas: 1` | единственная переменная в defaults |
| UpCloud | `upcloud_csi_controller_replicas: 1` | креды из `UPCLOUD_*`, снапшоты `upcloud_csi_enable_volume_snapshot: false` |
| vSphere | `vsphere_csi_controller_replicas: 1` | `external_vsphere_*` (vCenter), теги образов v3.3.1 и sidecar-ов, `vsphere_csi_namespace: "kube-system"` |

### Внешние cloud controller manager (сводно)

| Провайдер | Тег образа по умолчанию | Особенности |
|---|---|---|
| Hetzner (hcloud) | `latest` (в словаре `external_hcloud_cloud`) | вся конфигурация — один словарь |
| Huawei Cloud | `v0.26.8` | креды из окружения `OS_*` |
| Oracle (OCI) | `v1.29.0` | все параметры аутентификации пустые, задаются пользователем |
| OpenStack | `v1.30.0` | креды из окружения `OS_*` |
| vSphere | `v1.31.0` | переменные `external_vsphere_vcenter_port`, `external_vsphere_insecure`, `external_vsphere_user`, `external_vsphere_password` продублированы в defaults ролей CSI и CCM |

### Ceph-провижионеры

| Провижионер | Ключевые переменные | Значения по умолчанию |
|---|---|---|
| CephFS | `cephfs_provisioner_storage_class`, `cephfs_provisioner_monitors` | `cephfs`, `~` (задаётся пользователем) |
| Ceph RBD | `rbd_provisioner_storage_class`, `rbd_provisioner_pool`, `rbd_provisioner_replicas` | `rbd`, `kube`, `2` |

## Замечания и особенности

- Переменная `storage_classes` определена **дважды** с разными значениями по умолчанию: в `roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml` и в `roles/kubernetes-apps/persistent_volumes/upcloud-csi/defaults/main.yml`. Конфликта нет, так как роли применяются для разных облаков, но при переопределении в инвентаре это одна и та же переменная.
- Переменные `external_vsphere_vcenter_port`, `external_vsphere_insecure`, `external_vsphere_user`, `external_vsphere_password` продублированы в defaults ролей `csi_driver/vsphere` и `external_cloud_controller/vsphere` (одинаковые значения). В YAML-справочнике каждая приведена дважды — с обоими `source_path`.
- `upcloud_cacert` читается из переменной окружения `OS_CACERT` (а не `UPCLOUD_*`) — вероятно, унаследовано из кода Cinder; помечено `reliability: unconfirmed` в YAML.
- Ряд флагов включения дублируется в `roles/kubespray-defaults/defaults/main/main.yml` и в defaults самой роли с одинаковыми значениями (см. таблицу выше): `deploy_netchecker`, `helm_enabled`, `krew_enabled`, `metallb_enabled`, `metallb_speaker_enabled`, `argocd_enabled`, `local_path_provisioner_enabled`, `scheduler_plugins_enabled`. В YAML эти переменные приведены в разделе своей роли.
- Закомментированные (не имеющие значения по умолчанию) переменные — `dns_cpu_limit`, `dns_extra_tolerations`, `coredns_additional_configs`, `coredns_rewrite_block`, `coredns_additional_error_config`, `coredns_kubernetes_extra_opts`, `dns_upstream_forward_extra_opts`, `nodelocaldns_additional_configs`, `dns_autoscaler_extra_tolerations`, `etcd_metrics_service_labels`, `policy_controller_extra_tolerations`, `argocd_admin_password`, `aws_ebs_csi_annotations`, `cinder_csi_rescan_on_resize` — в YAML-справочник не включены (нет значения по умолчанию), упомянуты здесь для полноты.

## Сверка полноты извлечения

Критическая проверка полноты (главный урок проекта — не пропускать подкаталоги):

- **Число defaults-файлов** под `roles/kubernetes-apps` + `roles/helm-apps`: **39** (все — в `roles/kubernetes-apps`; `roles/helm-apps` каталога `defaults/` не имеет).
- **Суммарное число top-level ключей** в этих файлах (`grep -cE '^[a-z_][a-z0-9_]*:'`, просуммировано): **390**.
- **Число извлечённых переменных из defaults `kubernetes-apps`** в `addons.yaml`: **390**.
- **Результат сверки: 390 = 390 — совпадает.** Ничего не исключено из defaults-файлов ролей.
- Дополнительно в `addons.yaml` включены **19** флагов-переключателей аддонов, определённых только в `roles/kubespray-defaults/defaults/main/main.yml` (эти ключи не входят в defaults `kubernetes-apps` и не учитываются в 390): `dashboard_enabled`, `registry_enabled`, `metrics_server_enabled`, `local_volume_provisioner_enabled`, `local_volume_provisioner_directory_mode`, `cinder_csi_enabled`, `aws_ebs_csi_enabled`, `azure_csi_enabled`, `gcp_pd_csi_enabled`, `vsphere_csi_enabled`, `upcloud_csi_enabled`, `csi_snapshot_controller_enabled`, `persistent_volumes_enabled`, `cephfs_provisioner_enabled`, `rbd_provisioner_enabled`, `ingress_nginx_enabled`, `ingress_alb_enabled`, `cert_manager_enabled`, `expand_persistent_volumes`.
- **Итого в `addons.yaml`: 390 + 19 = 409 записей.**
- Дубли ключей между файлами (`storage_classes` ×2; `external_vsphere_vcenter_port`, `external_vsphere_insecure`, `external_vsphere_user`, `external_vsphere_password` ×2) учтены как отдельные записи с разными `source_path` — поэтому входят в 390 по одному разу на каждый файл.
