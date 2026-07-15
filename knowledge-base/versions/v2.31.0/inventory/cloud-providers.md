---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
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
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/inventory/sample/group_vars/all
retrieved_at: 2026-07-14
topics:
  - inventory
  - cloud-providers
reliability: authoritative
---

# Облачные провайдеры в sample-инвентаре — v2.31.0

Заметка описывает переменные облачных провайдеров из `inventory/sample/group_vars/all/` тега **v2.31.0** (commit `1c9add4`). Источник истины — машиночитаемый справочник [[versions/v2.31.0/inventory/cloud-providers|cloud-providers.yaml]]; данная заметка является его человекочитаемым представлением.

Родительский срез: [[versions/v2.31.0/README|Срез v2.31.0]].

## Важное замечание

В sample-инвентаре **все переменные всех девяти провайдеров закомментированы** (`is_set: false`). Это шаблоны-образцы, а не действующие значения. Приведённые в справочнике `sample_value` взяты дословно из закомментированных строк. Реальные значения по умолчанию определяются кодом ролей (`roles/*/defaults`), а не этими файлами. Поэтому при развёртывании настройки провайдера нужно раскомментировать и заполнить осознанно.

Расхождений между sample-инвентарём и defaults не обнаружено (все строки закомментированы), поэтому в YAML `discrepancies: []`.

## Обзор провайдеров

| Провайдер | Файл | Переменных | Назначение |
|---|---|---|---|
| AWS | `aws.yml` | 7 | Драйвер AWS EBS CSI (провижининг томов EBS) |
| Azure | `azure.yml` | 30 | Учётные данные Azure cloud provider и Azure Disk CSI |
| GCP | `gcp.yml` | 4 | Драйвер GCP Persistent Disk CSI |
| Hetzner Cloud (hcloud) | `hcloud.yml` | 14 | Внешний Hcloud Cloud Controller Manager (словарь `external_hcloud_cloud`) |
| Huawei Cloud | `huaweicloud.yml` | 10 | Внешний Huawei Cloud Controller и LBaaS |
| OCI (Oracle) | `oci.yml` | 34 | Внешний и in-tree OCI Cloud Controller Manager |
| OpenStack | `openstack.yml` | 39 | LBaaS (in-tree и внешний CCM) и Cinder CSI |
| UpCloud | `upcloud.yml` | 9 | Драйвер UpCloud CSI и StorageClass |
| vSphere | `vsphere.yml` | 9 | Внешний vSphere Cloud Provider и vSphere CSI |

Всего: **9 провайдеров, 156 переменных** (все закомментированы).

## AWS (`aws.yml`)

Настройки драйвера AWS EBS CSI. Включение — через `aws_ebs_csi_enabled: true`.

| Переменная | Образец значения | Описание |
|---|---|---|
| `aws_ebs_csi_enabled` | `true` | Включает драйвер EBS CSI |
| `aws_ebs_csi_enable_volume_scheduling` | `true` | Topology-aware планирование томов |
| `aws_ebs_csi_enable_volume_snapshot` | `false` | Поддержка снапшотов |
| `aws_ebs_csi_enable_volume_resizing` | `false` | Изменение размера томов |
| `aws_ebs_csi_controller_replicas` | `1` | Число реплик контроллера |
| `aws_ebs_csi_plugin_image_tag` | `latest` | Тег образа плагина |
| `aws_ebs_csi_extra_volume_tags` | `Owner=owner,Team=team,Environment=environment'` | Доп. теги томов. В образце тега несбалансированная кавычка — приведено дословно |

## Azure (`azure.yml`)

Две группы: параметры Azure cloud provider (`azure_*`, требует `docs/azure.md`) и Azure Disk CSI (`azure_csi_*`, требует `docs/azure-csi.md`). Большинство значений пустые (учётные данные и имена ресурсов заполняются пользователем).

Значимые образцы значений:

| Переменная | Образец значения | Описание |
|---|---|---|
| `azure_vmtype` | `standard` | Тип ВМ: `standard` или `vmss` |
| `azure_csi_tags` | `Owner=owner,Team=team,Environment=environment'` | Теги дисков. В образце несбалансированная кавычка — дословно |
| `azure_csi_enabled` | `true` | Включает Azure Disk CSI |
| `azure_csi_controller_replicas` | `1` | Число реплик контроллера CSI |
| `azure_csi_plugin_image_tag` | `latest` | Тег образа плагина CSI |

Учётные и топологические параметры без образца значения (заполняются пользователем): `azure_cloud`, `azure_tenant_id`, `azure_subscription_id`, `azure_aad_client_id`, `azure_aad_client_secret`, `azure_resource_group`, `azure_location`, `azure_subnet_name`, `azure_security_group_name`, `azure_security_group_resource_group`, `azure_vnet_name`, `azure_vnet_resource_group`, `azure_route_table_name`, `azure_route_table_resource_group`, а также их CSI-аналоги `azure_csi_tenant_id`, `azure_csi_subscription_id`, `azure_csi_aad_client_id`, `azure_csi_aad_client_secret`, `azure_csi_location`, `azure_csi_resource_group`, `azure_csi_vnet_name`, `azure_csi_vnet_resource_group`, `azure_csi_subnet_name`, `azure_csi_security_group_name`, `azure_csi_use_instance_metadata`.

## GCP (`gcp.yml`)

Драйвер GCP Persistent Disk CSI. См. `docs/gcp-pd-csi.md`.

| Переменная | Образец значения | Описание |
|---|---|---|
| `gcp_pd_csi_sa_cred_file` | `/my/safe/credentials/directory/cloud-sa.json` | Путь к файлу учётных данных сервисного аккаунта |
| `gcp_pd_csi_enabled` | `true` | Включает драйвер GCP PD CSI |
| `gcp_pd_csi_controller_replicas` | `1` | Число реплик контроллера |
| `gcp_pd_csi_driver_image_tag` | `v0.7.0-gke.0` | Тег образа драйвера |

## Hetzner Cloud (`hcloud.yml`)

Все параметры вложены в словарь `external_hcloud_cloud` (внешний Hcloud CCM).

| Ключ | Образец значения | Описание |
|---|---|---|
| `hcloud_api_token` | `""` | API-токен Hetzner Cloud |
| `token_secret_name` | `hcloud` | Имя Secret с токеном |
| `with_networks` | `false` | Поддержка сетей в CCM |
| `network_name` | — | Имя/ID приватной сети |
| `service_account_name` | `cloud-controller-manager` | Имя ServiceAccount |
| `controller_image_tag` | `latest` | Тег образа контроллера |
| `controller_extra_args` | `{}` | Доп. аргументы DaemonSet |
| `load_balancers_location` | — | Локация LB (взаимоискл. с network_zone) |
| `load_balancers_network_zone` | — | Сетевая зона LB (взаимоискл. с location) |
| `load_balancers_disable_private_ingress` | — | true при IPVS-плагинах |
| `load_balancers_use_private_ip` | — | true при приватных сетях |
| `load_balancers_enabled` | — | Управление балансировщиками |
| `network_routes_enabled` | — | Управление сетевыми маршрутами |

## Huawei Cloud (`huaweicloud.yml`)

Внешний Huawei Cloud Controller и LBaaS. Учётные данные по умолчанию читаются из переменных окружения (`OS_*`).

| Переменная | Образец значения | Описание |
|---|---|---|
| `external_huaweicloud_lbaas_subnet_id` | `Neutron subnet ID to create LBaaS VIP` | Подсеть Neutron для VIP LBaaS |
| `external_huaweicloud_lbaas_network_id` | `Neutron network ID to create LBaaS VIP` | Сеть Neutron для VIP LBaaS |
| `external_huaweicloud_auth_url` | `{{ lookup('env','OS_AUTH_URL')  }}` | URL Keystone (из OS_AUTH_URL) |
| `external_huaweicloud_access_key` | `{{ lookup('env','OS_ACCESS_KEY')  }}` | Access key (из OS_ACCESS_KEY) |
| `external_huaweicloud_secret_key` | `{{ lookup('env','OS_SECRET_KEY')  }}` | Secret key (из OS_SECRET_KEY) |
| `external_huaweicloud_region` | `{{ lookup('env','OS_REGION_NAME')  }}` | Регион (из OS_REGION_NAME) |
| `external_huaweicloud_project_id` | `{{ lookup('env','OS_TENANT_ID')\| default(lookup('env','OS_PROJECT_ID'),true) }}` | ID проекта (OS_TENANT_ID / OS_PROJECT_ID) |
| `external_huaweicloud_cloud` | `{{ lookup('env','OS_CLOUD') }}` | Имя облака (из OS_CLOUD) |
| `external_huawei_cloud_controller_image_repo` | `swr.ap-southeast-1.myhuaweicloud.com` | Репозиторий образа контроллера |
| `external_huawei_cloud_controller_image_tag` | `v0.26.8` | Тег образа контроллера |

## OCI — Oracle Cloud Infrastructure (`oci.yml`)

Две группы: внешний OCI Cloud Controller Manager (`external_oracle_*`) и in-tree OCI cloud provider (`oci_*`).

Внешний CCM (значимые образцы):

| Переменная | Образец значения | Описание |
|---|---|---|
| `external_oracle_auth_use_instance_principals` | `false` | Использовать instance principals |
| `external_oracle_load_balancer_security_list_management_mode` | `All` | Режим управления security list LB |
| `external_oracle_ratelimiter_qps_read` | `20.0` | Лимит QPS на чтение |
| `external_oracle_ratelimiter_bucket_read` | `5` | Bucket для чтения |
| `external_oracle_ratelimiter_qps_write` | `20.0` | Лимит QPS на запись |
| `external_oracle_ratelimiter_bucket_write` | `5` | Bucket для записи |
| `external_oracle_cloud_controller_image_repo` | `ghcr.io/oracle/cloud-provider-oci` | Репозиторий образа CCM |
| `external_oracle_cloud_controller_image_tag` | `v1.29.0` | Тег образа CCM |

Пустые параметры внешнего CCM (заполняются пользователем): `external_oracle_auth_region`, `external_oracle_auth_tenancy`, `external_oracle_auth_user`, `external_oracle_auth_key`, `external_oracle_auth_passphrase`, `external_oracle_auth_fingerprint`, `external_oracle_compartment`, `external_oracle_vcn`, `external_oracle_load_balancer_subnet1`, `external_oracle_load_balancer_subnet2`, `external_oracle_load_balancer_security_lists` (`{}`).

In-tree провайдер (`oci_*`):

| Переменная | Образец значения | Описание |
|---|---|---|
| `oci_security_list_management` | `All` | Режим управления security list |
| `oci_use_instance_principals` | `false` | Если true, ключи/регион/tenancy не нужны |

Прочие параметры in-tree провайдера без образца значения: `oci_private_key`, `oci_region_id`, `oci_tenancy_id`, `oci_user_id`, `oci_user_fingerprint`, `oci_compartment_id`, `oci_vnc_id`, `oci_subnet1_id`, `oci_subnet2_id`, `oci_security_lists`, `oci_rate_limit` (словарь: `rate_limit_qps_read`, `rate_limit_qps_write`, `rate_limit_bucket_read`, `rate_limit_bucket_write`), `oci_cloud_controller_pull_source` (по умолчанию `iad.ocir.io/oracle/cloud-provider-oci`), `oci_cloud_controller_pull_secret`.

## OpenStack (`openstack.yml`)

Три части: устаревший in-tree LBaaS (`openstack_lbaas_*`), внешний OpenStack CCM (`external_openstack_*`) и Cinder CSI (`cinder_csi_*` + `storage_classes`).

In-tree LBaaS:

| Переменная | Образец значения | Описание |
|---|---|---|
| `openstack_blockstorage_ignore_volume_az` | `yes` | Игнорировать AZ тома Cinder |
| `openstack_lbaas_enabled` | `True` | Включает LBaaSv2 |
| `openstack_lbaas_use_octavia` | `False` | Использовать Octavia |
| `openstack_lbaas_method` | `ROUND_ROBIN` | Алгоритм балансировки |
| `openstack_lbaas_provider` | `haproxy` | Провайдер LBaaS |
| `openstack_lbaas_create_monitor` | `yes` | Создавать монитор |
| `openstack_lbaas_monitor_delay` | `1m` | Интервал проверок |
| `openstack_lbaas_monitor_timeout` | `30s` | Таймаут проверок |
| `openstack_lbaas_monitor_max_retries` | `3` | Число повторов |

Внешний CCM (значимые образцы):

| Переменная | Образец значения | Описание |
|---|---|---|
| `external_openstack_lbaas_enabled` | `true` | Включает LBaaS во внешнем CCM |
| `external_openstack_lbaas_method` | `ROUND_ROBIN` | Алгоритм балансировки |
| `external_openstack_lbaas_provider` | `amphora` | Провайдер LBaaS |
| `external_openstack_lbaas_manage_security_groups` | `false` | Управлять security groups |
| `external_openstack_lbaas_create_monitor` | `false` | Создавать монитор |
| `external_openstack_lbaas_monitor_delay` | `5s` | Интервал проверок |
| `external_openstack_lbaas_monitor_max_retries` | `1` | Число повторов |
| `external_openstack_lbaas_monitor_timeout` | `3s` | Таймаут проверок |
| `external_openstack_lbaas_internal_lb` | `false` | Внутренний LB |
| `external_openstack_network_ipv6_disabled` | `false` | Отключить IPv6 |
| `external_openstack_network_internal_networks` | `[]` | Внутренние сети |
| `external_openstack_network_public_networks` | `[]` | Публичные сети |
| `external_openstack_metadata_search_order` | `configDrive,metadataService` | Порядок поиска метаданных |

Также: `external_openstack_lbaas_floating_network_id`, `external_openstack_lbaas_floating_subnet_id`, `external_openstack_lbaas_subnet_id`, `external_openstack_lbaas_network_id` (образцы — текстовые описания Neutron ID) и application credentials `external_openstack_application_credential_name` / `_id` / `_secret` (пустые, имеют приоритет над username/password).

Cinder CSI:

| Переменная | Образец значения | Описание |
|---|---|---|
| `cinder_csi_attacher_image_tag` | `v4.4.2` | Тег образа csi-attacher |
| `cinder_csi_provisioner_image_tag` | `v3.6.2` | Тег образа csi-provisioner |
| `cinder_csi_snapshotter_image_tag` | `v6.3.2` | Тег образа csi-snapshotter |
| `cinder_csi_resizer_image_tag` | `v1.9.2` | Тег образа csi-resizer |
| `cinder_csi_livenessprobe_image_tag` | `v2.11.0` | Тег образа livenessprobe |
| `cinder_csi_enabled` | `true` | Включает Cinder CSI |
| `cinder_csi_controller_replicas` | `1` | Число реплик контроллера |
| `storage_classes` | список | StorageClass для Cinder (в образце `cinder-csi` / `kubernetes.io/cinder`) |

## UpCloud (`upcloud.yml`)

Драйвер UpCloud CSI. Требуются `UPCLOUD_USERNAME` и `UPCLOUD_PASSWORD`.

| Переменная | Образец значения | Описание |
|---|---|---|
| `upcloud_csi_enabled` | `true` | Включает UpCloud CSI |
| `upcloud_csi_controller_replicas` | `1` | Число реплик контроллера |
| `upcloud_csi_provisioner_image_tag` | `v3.1.0` | Тег образа provisioner |
| `upcloud_csi_attacher_image_tag` | `v3.4.0` | Тег образа attacher |
| `upcloud_csi_resizer_image_tag` | `v1.4.0` | Тег образа resizer |
| `upcloud_csi_plugin_image_tag` | `v0.3.3` | Тег образа плагина |
| `upcloud_csi_node_image_tag` | `v2.5.0` | Тег образа node |
| `upcloud_tolerations` | `[]` | Tolerations подов CSI |
| `storage_classes` | список | StorageClass (в образце `standard` tier maxiops и `hdd` tier hdd) |

## vSphere (`vsphere.yml`)

Внешний vSphere Cloud Provider и vSphere CSI.

| Переменная | Образец значения | Описание |
|---|---|---|
| `external_vsphere_vcenter_ip` | `myvcenter.domain.com` | IP/FQDN vCenter |
| `external_vsphere_vcenter_port` | `443` | Порт vCenter |
| `external_vsphere_insecure` | `true` | Небезопасное подключение (без проверки сертификата) |
| `external_vsphere_user` | `administrator@vsphere.local` | Пользователь vCenter (или `VSPHERE_USER`) |
| `external_vsphere_password` | `K8s_admin` | Пароль vCenter (или `VSPHERE_PASSWORD`) |
| `external_vsphere_datacenter` | `DATACENTER_name` | Имя датацентра |
| `external_vsphere_kubernetes_cluster_id` | `kubernetes-cluster-id` | ID кластера Kubernetes |
| `vsphere_csi_enabled` | `true` | Включает vSphere CSI |
| `vsphere_csi_controller_replicas` | `1` | Число реплик контроллера CSI |
