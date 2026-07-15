---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: inventory
source_paths:
  - inventory/sample/group_vars/all/aws.yml
  - inventory/sample/group_vars/all/azure.yml
  - inventory/sample/group_vars/all/gcp.yml
  - inventory/sample/group_vars/all/hcloud.yml
  - inventory/sample/group_vars/all/huaweicloud.yml
  - inventory/sample/group_vars/all/oci.yml
  - inventory/sample/group_vars/all/openstack.yml
  - inventory/sample/group_vars/all/upcloud.yml
  - inventory/sample/group_vars/all/vsphere.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - cloud-providers
reliability: authoritative
---

# Облачные провайдеры в sample-инвентаре v2.30.0

Заметка описывает файлы `inventory/sample/group_vars/all/*.yml`, отвечающие за интеграцию Kubespray с облачными провайдерами (внешние Cloud Controller Manager и CSI-драйверы) на теге **v2.30.0** (commit `f4ccdb5`).

Относится к срезу: [[versions/v2.30.0/README|Срез v2.30.0]].

> Источник истины — машиночитаемый файл `cloud-providers.yaml` в этой же директории. Данная заметка — только человекочитаемое представление.

## Обзор

Проанализировано 9 файлов, 143 переменные. **Все переменные во всех файлах закомментированы** — это шаблон (`is_set: false`), поэтому они не переопределяют значения из `roles/*/defaults`. Пользователь раскомментирует и заполняет нужные значения под свою облачную среду.

| Провайдер | Файл | Переменных | Назначение |
| --- | --- | --- | --- |
| aws | `all/aws.yml` | 7 | Драйвер AWS EBS CSI |
| azure | `all/azure.yml` | 30 | Учётные данные Azure и Azure Disk CSI |
| gcp | `all/gcp.yml` | 4 | Драйвер GCP Persistent Disk CSI |
| hcloud | `all/hcloud.yml` | 1 | Внешний Hetzner Cloud Controller (словарь) |
| huaweicloud | `all/huaweicloud.yml` | 10 | Внешний Huawei Cloud Controller |
| oci | `all/oci.yml` | 34 | Внешний OCI CCM и настройки OCI |
| openstack | `all/openstack.yml` | 39 | LBaaS, внешний OpenStack CCM, Cinder CSI |
| upcloud | `all/upcloud.yml` | 9 | Драйвер UpCloud CSI |
| vsphere | `all/vsphere.yml` | 9 | Внешний vSphere-провайдер и vSphere CSI |

## AWS (`aws.yml`)

Настройка драйвера AWS EBS CSI для динамического выделения томов.

| Переменная | Пример значения |
| --- | --- |
| `aws_ebs_csi_enabled` | `true` |
| `aws_ebs_csi_enable_volume_scheduling` | `true` |
| `aws_ebs_csi_enable_volume_snapshot` | `false` |
| `aws_ebs_csi_enable_volume_resizing` | `false` |
| `aws_ebs_csi_controller_replicas` | `1` |
| `aws_ebs_csi_plugin_image_tag` | `latest` |
| `aws_ebs_csi_extra_volume_tags` | `Owner=owner,Team=team,Environment=environment'` |

Примечание: в примере `aws_ebs_csi_extra_volume_tags` присутствует опечатка — незакрытая кавычка (дословно из исходника).

## Azure (`azure.yml`)

Две группы: учётные данные и параметры облака Azure (tenant, subscription, сервисный принципал, сеть, NSG, таблица маршрутизации, тип ВМ) и отдельный блок Azure Disk CSI (`azure_csi_*`).

Ключевые переменные: `azure_cloud`, `azure_tenant_id`, `azure_subscription_id`, `azure_aad_client_id`, `azure_aad_client_secret`, `azure_resource_group`, `azure_location`, `azure_vmtype` (`standard` или `vmss`). Для CSI: `azure_csi_enabled`, `azure_csi_controller_replicas` (`1`), `azure_csi_plugin_image_tag` (`latest`), плюс собственный набор учётных данных `azure_csi_*`. Значение `azure_csi_tags` в примере также содержит незакрытую кавычку.

## GCP (`gcp.yml`)

Драйвер GCP Persistent Disk CSI.

| Переменная | Пример значения |
| --- | --- |
| `gcp_pd_csi_sa_cred_file` | `/my/safe/credentials/directory/cloud-sa.json` |
| `gcp_pd_csi_enabled` | `true` |
| `gcp_pd_csi_controller_replicas` | `1` |
| `gcp_pd_csi_driver_image_tag` | `v0.7.0-gke.0` |

## Hetzner Cloud (`hcloud.yml`)

Единственная переменная-словарь `external_hcloud_cloud` описывает внешний Hetzner Cloud Controller Manager. Вложенные ключи: `hcloud_api_token` (`""`), `token_secret_name` (`hcloud`), `with_networks` (`false`), `network_name`, `service_account_name` (`cloud-controller-manager`), `controller_image_tag` (`latest`), `controller_extra_args` (`{}`), а также группа параметров балансировщиков (`load_balancers_location`, `load_balancers_network_zone`, `load_balancers_disable_private_ingress`, `load_balancers_use_private_ip`, `load_balancers_enabled`) и `network_routes_enabled`.

## Huawei Cloud (`huaweicloud.yml`)

Внешний Huawei Cloud Controller. Параметры LBaaS (`external_huaweicloud_lbaas_subnet_id`, `external_huaweicloud_lbaas_network_id`), учётные данные Keystone, по умолчанию считываемые из переменных окружения (`external_huaweicloud_auth_url`, `external_huaweicloud_access_key`, `external_huaweicloud_secret_key`, `external_huaweicloud_region`, `external_huaweicloud_project_id`, `external_huaweicloud_cloud`), а также образ контроллера: `external_huawei_cloud_controller_image_repo` (`swr.ap-southeast-1.myhuaweicloud.com`) и `external_huawei_cloud_controller_image_tag` (`v0.26.8`).

## Oracle Cloud (`oci.yml`)

Самый крупный блок: внешний OCI Cloud Controller Manager (`external_oracle_*`) и устаревшие встроенные настройки OCI (`oci_*`).

Внешний CCM: аутентификация (`external_oracle_auth_region/tenancy/user/key/passphrase/fingerprint`, `external_oracle_auth_use_instance_principals` = `false`), балансировщик (`external_oracle_load_balancer_subnet1/subnet2`, `..._security_list_management_mode` = `All`), rate limiter (`external_oracle_ratelimiter_qps_read/write` = `20.0`, `..._bucket_read/write` = `5`) и образ (`external_oracle_cloud_controller_image_repo` = `ghcr.io/oracle/cloud-provider-oci`, `..._image_tag` = `v1.29.0`).

Встроенные OCI: `oci_private_key`, `oci_region_id`, `oci_tenancy_id`, `oci_user_id`, `oci_user_fingerprint`, `oci_compartment_id`, `oci_vnc_id`, `oci_subnet1_id`, `oci_subnet2_id`, `oci_security_list_management` (`All`), `oci_security_lists`, `oci_use_instance_principals` (`false`), `oci_rate_limit`, `oci_cloud_controller_pull_source`, `oci_cloud_controller_pull_secret`.

## OpenStack (`openstack.yml`)

Три группы: устаревший встроенный LBaaSv2 (`openstack_lbaas_*`), внешний OpenStack Cloud Controller (`external_openstack_*`) и Cinder CSI (`cinder_csi_*`).

Встроенный LBaaS: `openstack_lbaas_enabled` (`True`), `openstack_lbaas_use_octavia` (`False`), `openstack_lbaas_method` (`ROUND_ROBIN`), `openstack_lbaas_provider` (`haproxy`), параметры health-монитора.

Внешний CCM: `external_openstack_lbaas_enabled` (`true`), `external_openstack_lbaas_provider` (`amphora`), сети/подсети для floating IP и VIP, `external_openstack_metadata_search_order` (`configDrive,metadataService`), application credentials для Keystone.

Cinder CSI: `cinder_csi_enabled`, `cinder_csi_controller_replicas` (`1`), теги образов sig-storage (`cinder_csi_attacher_image_tag` = `v4.4.2`, `cinder_csi_provisioner_image_tag` = `v3.6.2`, `cinder_csi_snapshotter_image_tag` = `v6.3.2`, `cinder_csi_resizer_image_tag` = `v1.9.2`, `cinder_csi_livenessprobe_image_tag` = `v2.11.0`) и `storage_classes` (пример StorageClass `cinder-csi`).

## UpCloud (`upcloud.yml`)

Драйвер UpCloud CSI. Требует переменные окружения `UPCLOUD_USERNAME` и `UPCLOUD_PASSWORD`.

| Переменная | Пример значения |
| --- | --- |
| `upcloud_csi_enabled` | `true` |
| `upcloud_csi_controller_replicas` | `1` |
| `upcloud_csi_provisioner_image_tag` | `v3.1.0` |
| `upcloud_csi_attacher_image_tag` | `v3.4.0` |
| `upcloud_csi_resizer_image_tag` | `v1.4.0` |
| `upcloud_csi_plugin_image_tag` | `v0.3.3` |
| `upcloud_csi_node_image_tag` | `v2.5.0` |
| `upcloud_tolerations` | `[]` |
| `storage_classes` | список (`standard` tier `maxiops`, `hdd` tier `hdd`) |

## vSphere (`vsphere.yml`)

Внешний vSphere Cloud Provider и vSphere CSI.

| Переменная | Пример значения |
| --- | --- |
| `external_vsphere_vcenter_ip` | `myvcenter.domain.com` |
| `external_vsphere_vcenter_port` | `443` |
| `external_vsphere_insecure` | `true` |
| `external_vsphere_user` | `administrator@vsphere.local` |
| `external_vsphere_password` | `K8s_admin` |
| `external_vsphere_datacenter` | `DATACENTER_name` |
| `external_vsphere_kubernetes_cluster_id` | `kubernetes-cluster-id` |
| `vsphere_csi_enabled` | `true` |
| `vsphere_csi_controller_replicas` | `1` |

`external_vsphere_user` и `external_vsphere_password` можно задать через переменные окружения `VSPHERE_USER` и `VSPHERE_PASSWORD`.

## Расхождения с defaults

Не выявлены. Все 143 переменные во всех облачных файлах sample-инвентаря закомментированы, поэтому не переопределяют значения из `roles/*/defaults`. В `cloud-providers.yaml` поле `discrepancies: []`.
