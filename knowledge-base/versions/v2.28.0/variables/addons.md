---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: code
source_path: versions/v2.28.0/variables/addons.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - addons
  - kubernetes-apps
reliability: authoritative
---

# Переменные аддонов (kubernetes-apps) в Kubespray v2.28.0

Справочник переменных дополнительных компонентов, разворачиваемых ролями `roles/kubernetes-apps/*` на теге `v2.28.0` (коммит `63cdf87`).

**Источник истины** — машиночитаемый справочник [[versions/v2.28.0/variables/addons|addons.yaml]] (368 переменных). Эта заметка — человекочитаемое изложение.

Назад к срезу: [[versions/v2.28.0/README|Срез v2.28.0]]

## Обзор

В v2.28.0 через `kubernetes-apps` доступны следующие аддоны:

- **DNS-стек** (роль `kubernetes-apps/ansible`): CoreDNS, dns-autoscaler, nodelocaldns — разворачивается всегда (при `deploy_coredns: true`);
- **Netchecker** — проверка сетевой связности;
- **Kubernetes Dashboard**;
- **Helm** (установка CLI на control plane);
- **Внутрикластерный registry**;
- **metrics-server**;
- **Ingress-контроллеры**: ingress-nginx, AWS ALB Ingress Controller;
- **cert-manager**;
- **MetalLB**;
- **Argo CD**;
- **CRD Gateway API** (роль `gateway_api` — в v2.28.0 расположена в `roles/kubernetes-apps/gateway_api/`, в v2.29.1 перенесена в `common_crds/gateway_api`);
- **Провижионеры хранилища**: Local Path Provisioner, local-volume-provisioner;
- **CSI-драйверы**: AWS EBS, Azure Disk, OpenStack Cinder, GCP PD, UpCloud, vSphere (+ роль `csi_driver/csi_crd` без собственных defaults);
- **Внешние cloud controller manager**: Hetzner (hcloud), Huawei Cloud, Oracle (OCI), OpenStack, vSphere;
- **persistent_volumes** — создание StorageClass для облачных CSI;
- **snapshots** — snapshot-controller и VolumeSnapshotClass для Cinder;
- **kubelet-csr-approver** — автоодобрение CSR kubelet (ставится Helm-чартом);
- **Node Feature Discovery (NFD)**;
- **scheduler-plugins** — второй планировщик;
- **policy_controller/calico** — calico-kube-controllers (разворачивается при `kube_network_plugin: calico` и включённых network policy);
- **cluster_roles** — базовые RBAC-объекты кластера (собственных переменных в defaults не имеет).

Не проиндексированы в этом справочнике (сознательно):

- сетевые плагины (CNI) — отдельный справочник `variables/cni.yaml`;
- `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu` (NVIDIA GPU) — 13 ключей, относится к отдельной теме GPU, здесь не индексируется (см. раздел «Сверка полноты»);
- `roles/kubernetes-apps/container_runtimes` (kata containers и др.) — относится к справочнику container runtime, не проиндексировано здесь.

Роль `roles/helm-apps` каталога `defaults/` не имеет — её параметры (`helm_update`, `helm_defaults`, `helm_repository_defaults`) лежат в `roles/helm-apps/vars/main.yml` и в справочник defaults не включены.

## Отличия v2.28.0 от v2.29.1 (структурные)

- **Gateway API**: в v2.28.0 роль расположена в `roles/kubernetes-apps/gateway_api/`; в v2.29.1 перенесена в `roles/kubernetes-apps/common_crds/gateway_api/`.
- **Нет Prometheus Operator CRD**: роль `common_crds/prometheus_operator_crds` и флаг `prometheus_operator_crds_enabled` в v2.28.0 отсутствуют (появились в v2.29.1).
- **Общий namespace-ключ**: в `roles/kubernetes-apps/defaults/main.yml` переменная называется `namespace` (в v2.29.1 переименована в `k8s_namespace`).
- **argocd**: в v2.28.0 defaults роли содержат `argocd_install_url` (URL манифеста установки).
- **container_engine_accelerator/nvidia_gpu**: в v2.28.0 у роли есть `defaults/main.yml` (13 ключей); в справочник не включён (как и в v2.29.1).

## Переменные включения аддонов

Все флаги ниже по умолчанию выключены (значение `false`), кроме особо отмеченных. Часть флагов определена одновременно в `roles/kubespray_defaults/defaults/main/main.yml` и в defaults самой роли (отмечено «оба места»).

| Аддон | Переменная включения | Значение по умолчанию | Где определена |
|---|---|---|---|
| CoreDNS | `deploy_coredns` | `true` | `roles/kubernetes-apps/ansible/defaults/main.yml` |
| Netchecker | `deploy_netchecker` | `false` | оба места |
| Kubernetes Dashboard | `dashboard_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| Helm | `helm_enabled` | `false` | оба места |
| Registry | `registry_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| metrics-server | `metrics_server_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| ingress-nginx | `ingress_nginx_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| ALB Ingress | `ingress_alb_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| cert-manager | `cert_manager_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| MetalLB | `metallb_enabled` | `false` | оба места |
| MetalLB speaker | `metallb_speaker_enabled` | `{{ metallb_enabled }}` | оба места |
| Argo CD | `argocd_enabled` | `false` | оба места |
| Gateway API CRD | `gateway_api_enabled` | `false` | оба места |
| Local Path Provisioner | `local_path_provisioner_enabled` | `false` | оба места |
| local-volume-provisioner | `local_volume_provisioner_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| Cinder CSI | `cinder_csi_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| AWS EBS CSI | `aws_ebs_csi_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| Azure Disk CSI | `azure_csi_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| GCP PD CSI | `gcp_pd_csi_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| vSphere CSI | `vsphere_csi_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| UpCloud CSI | `upcloud_csi_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| snapshot-controller | `csi_snapshot_controller_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| StorageClass облаков | `persistent_volumes_enabled` | `false` | `roles/kubespray_defaults/defaults/main/main.yml` |
| kubelet-csr-approver | `kubelet_csr_approver_enabled` | `{{ kubelet_rotate_server_certificates }}` | `roles/kubernetes-apps/kubelet-csr-approver/defaults/main.yml` |
| Node Feature Discovery | `node_feature_discovery_enabled` | `false` | `roles/kubernetes-apps/node_feature_discovery/defaults/main.yml` |
| scheduler-plugins | `scheduler_plugins_enabled` | `false` | оба места |

Внешние cloud controller manager включаются не флагом `*_enabled`, а связкой `cloud_provider: "external"` + `external_cloud_provider: <имя>` (обе переменные — в `roles/kubespray_defaults/defaults/main/main.yml`, по умолчанию пустые).

## Ключевые настройки основных аддонов

### CoreDNS / dns-autoscaler / nodelocaldns

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `dns_min_replicas` | `{{ [2, groups['k8s_cluster'] \| length] \| min }}` | минимум реплик CoreDNS для автоскейлера |
| `dns_nodes_per_replica` | `16` | узлов на реплику CoreDNS |
| `dns_cores_per_replica` | `256` | ядер на реплику CoreDNS |
| `enable_coredns_reverse_dns_lookups` | `true` | обратные PTR-запросы |
| `coredns_pod_disruption_budget` | `false` | PDB для CoreDNS |
| `coredns_default_zone_cache_block` | `cache 30` | блок cache в Corefile |
| `nodelocaldns_prometheus_port` | `9253` | порт метрик nodelocaldns |
| `old_dns_domains` | `[]` | прежние домены кластера после смены `dns_domain` |

Отдельного ключа `coredns_replicas` в defaults роли `ansible` в v2.28.0 нет (число реплик при выключенном автоскейлере задаётся в другом месте); сам флаг `enable_nodelocaldns` относится к справочнику k8s-cluster (kubespray_defaults).

### metrics-server

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `metrics_server_kubelet_insecure_tls` | `true` | не проверять TLS kubelet |
| `metrics_server_metric_resolution` | `15s` | интервал сбора метрик |
| `metrics_server_kubelet_preferred_address_types` | `"InternalIP,ExternalIP,Hostname"` | приоритет адресов kubelet |
| `metrics_server_replicas` | `1` | число реплик |
| `metrics_server_host_network` | `false` | hostNetwork |

### ingress-nginx

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `ingress_nginx_namespace` | `"ingress-nginx"` | namespace |
| `ingress_nginx_service_type` | `LoadBalancer` | тип сервиса |
| `ingress_nginx_class` | `nginx` | имя IngressClass |
| `ingress_nginx_without_class` | `true` | обрабатывать Ingress без класса |
| `ingress_nginx_default` | `false` | IngressClass по умолчанию |
| `ingress_nginx_insecure_port` / `ingress_nginx_secure_port` | `80` / `443` | порты HTTP/HTTPS |
| `ingress_nginx_webhook_enabled` | `false` | admission webhook |

### MetalLB

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `metallb_log_level` | `info` | уровень логов |
| `metallb_port` | `"7472"` | порт метрик |
| `metallb_memberlist_port` | `"7946"` | порт memberlist |
| `metallb_speaker_enabled` | `{{ metallb_enabled }}` | DaemonSet speaker |
| `metallb_speaker_tolerations` | toleration на control plane (`NoSchedule`) | tolerations speaker |
| `metallb_loadbalancer_class` | `""` | обслуживаемый loadBalancerClass |

Пулы адресов (IPAddressPool, L2/BGP-advertisement) в defaults роли v2.28.0 не задаются — настраиваются пользователем через инвентарь.

### cert-manager

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `cert_manager_namespace` | `"cert-manager"` | namespace |
| `cert_manager_user` | `1001` | UID подов |
| `cert_manager_leader_election_namespace` | `kube-system` | namespace leader election |
| `cert_manager_http_proxy` / `https_proxy` / `no_proxy` | `{{ http_proxy \| default('') }}` и т.п. | проксирование |

### Argo CD

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `argocd_version` | `2.14.5` | версия Argo CD |
| `argocd_namespace` | `argocd` | namespace |
| `argocd_install_url` | URL манифеста install.yaml (по `argocd_version`) | источник манифеста |
| `argocd_admin_password` | не задана (закомментирована) | пароль admin |

### Gateway API

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `gateway_api_version` | `1.2.1` | версия CRD Gateway API |
| `gateway_api_channel` | `"standard"` | канал: standard / experimental |

Роль в v2.28.0 — `roles/kubernetes-apps/gateway_api/` (не `common_crds/`).

### Local Path Provisioner

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `local_path_provisioner_namespace` | `"local-path-storage"` | namespace |
| `local_path_provisioner_storage_class` | `"local-path"` | имя StorageClass |
| `local_path_provisioner_is_default_storageclass` | `"true"` | класс по умолчанию |
| `local_path_provisioner_claim_root` | `/opt/local-path-provisioner/` | каталог томов на узлах |
| `local_path_provisioner_reclaim_policy` | `Delete` | reclaimPolicy |
| `local_path_provisioner_helper_image_repo` / `_tag` | `busybox` / `latest` | helper-образ |

### kubelet-csr-approver

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `kubelet_csr_approver_enabled` | `{{ kubelet_rotate_server_certificates }}` | включение (следует за ротацией сертификатов kubelet) |
| `kubelet_csr_approver_chart_version` | `1.1.0` | версия Helm-чарта |
| `kubelet_csr_approver_repository_url` | `https://postfinance.github.io/kubelet-csr-approver` | Helm-репозиторий |
| `kubelet_csr_approver_values` | `{}` | переопределение values |

### Node Feature Discovery

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `node_feature_discovery_namespace` | `node-feature-discovery` | namespace |
| `node_feature_discovery_enable_nodefeature_api` | `true` | NodeFeature API (CRD) |
| `node_feature_discovery_master_replicas` | `1` | реплики nfd-master |
| `node_feature_discovery_gc_interval` | `1h` | интервал nfd-gc |

### scheduler-plugins

| Переменная | Значение по умолчанию | Назначение |
|---|---|---|
| `scheduler_plugins_namespace` | `scheduler-plugins` | namespace |
| `scheduler_plugins_scheduler_leader_elect` | `{{ ((groups['kube_control_plane'] \| length) > 1) }}` | leader election |
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
| OpenStack | `v1.32.0` | креды из окружения `OS_*` |
| vSphere | `v1.31.0` | переменные `external_vsphere_vcenter_port`, `external_vsphere_insecure`, `external_vsphere_user`, `external_vsphere_password` продублированы в defaults ролей CSI и CCM |

## Замечания и особенности

- Переменная `storage_classes` определена **дважды** с разными значениями по умолчанию: в `roles/kubernetes-apps/persistent_volumes/cinder-csi/defaults/main.yml` и в `roles/kubernetes-apps/persistent_volumes/upcloud-csi/defaults/main.yml`. Конфликта нет, так как роли применяются для разных облаков, но при переопределении в инвентаре это одна и та же переменная. В YAML внесены обе записи.
- Переменные `external_vsphere_vcenter_port`, `external_vsphere_insecure`, `external_vsphere_user`, `external_vsphere_password` определены **дважды**: в `roles/kubernetes-apps/csi_driver/vsphere/defaults/main.yml` и в `roles/kubernetes-apps/external_cloud_controller/vsphere/defaults/main.yml`. В YAML внесены обе записи (каждая со своим `source_path`).
- `upcloud_cacert` читается из переменной окружения `OS_CACERT` (а не `UPCLOUD_*`) — вероятно, унаследовано из кода Cinder; помечено `reliability: unconfirmed` в YAML.
- Ряд флагов включения дублируется в `roles/kubespray_defaults/defaults/main/main.yml` и в defaults самой роли с одинаковыми значениями (см. таблицу выше).
- Закомментированные (не имеющие значения по умолчанию) переменные — `dns_cpu_limit` и др. в `ansible/defaults`, а также `argocd_admin_password` — в YAML-справочник не включены (нет значения по умолчанию).
- Роли без собственных `defaults/`: `cluster_roles`, `csi_driver/csi_crd`, `helm-apps` (переменные в `vars/`).

## Сверка полноты

Согласно критической проверке (`find roles/kubernetes-apps roles/helm-apps -path '*/defaults/main.yml'`):

- **Файлов defaults найдено**: 36 (`roles/helm-apps` каталога `defaults/` не имеет — только `vars/`).
- **Суммарное число ключей верхнего уровня** (`grep -cE '^[a-z_][a-z0-9_]*:'` по каждому файлу): **364**.
- **Исключён**: `roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu/defaults/main.yml` — **13 ключей** (тема NVIDIA GPU, отдельный справочник; как и в v2.29.1). Ключи: `nvidia_accelerator_enabled`, `nvidia_driver_version`, `nvidia_gpu_tesla_base_url`, `nvidia_gpu_gtx_base_url`, `nvidia_gpu_flavor`, `nvidia_url_end`, `nvidia_driver_install_container`, `nvidia_driver_install_centos_container`, `nvidia_driver_install_ubuntu_container`, `nvidia_driver_install_supported`, `nvidia_gpu_device_plugin_container`, `nvidia_gpu_nodes`, `nvidia_gpu_device_plugin_memory`.
- **Извлечено из defaults ролей kubernetes-apps**: 364 − 13 = **351** (совпадает с целевым числом за вычетом исключённого файла).
- **Дополнительно добавлено**: **17** флагов включения аддонов, определённых только в `roles/kubespray_defaults/defaults/main/main.yml` (не дублируются в defaults ролей).
- **Итого переменных в `addons.yaml`**: 351 + 17 = **368**.

Результат сверки: **совпадает** — все 351 ключа из 35 индексируемых defaults-файлов извлечены (13 ключей `nvidia_gpu` осознанно исключены и перечислены выше).
