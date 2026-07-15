---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
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
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1
retrieved_at: 2026-07-14
topics:
  - inventory
  - cloud-providers
reliability: authoritative
---

# Облачные провайдеры в sample-inventory (v2.29.1)

Заметка описывает файлы `inventory/sample/group_vars/all/<cloud>.yml` тега **v2.29.1** (commit `0c6a295`). Источник истины — [[versions/v2.29.1/inventory/cloud-providers|cloud-providers.yaml]]; здесь дан человекочитаемый обзор.

> [!important] Все переменные закомментированы
> Во **всех девяти** файлах провайдеров каждая переменная закомментирована — это примеры-заготовки, которые пользователь раскомментирует и заполняет под своё окружение. Поэтому у всех записей в YAML стоит `is_set: false`. Значения по умолчанию, которые реально применяются при развёртывании, находятся в `roles/*/defaults/`, а не в этих файлах.

## Поддержанные провайдеры

В sample-inventory v2.29.1 присутствуют заготовки для 9 облачных провайдеров:

| Провайдер | Файл | Что настраивается | Ключевые переменные |
|---|---|---|---|
| AWS | `all/aws.yml` | AWS EBS CSI Driver (тома EBS) | `aws_ebs_csi_enabled`, `aws_ebs_csi_controller_replicas`, `aws_ebs_csi_extra_volume_tags` |
| Azure | `all/azure.yml` | Azure cloud provider + Azure Disk CSI | `azure_tenant_id`, `azure_subscription_id`, `azure_vmtype`, `azure_csi_enabled` |
| GCP | `all/gcp.yml` | GCP Persistent Disk CSI Driver | `gcp_pd_csi_enabled`, `gcp_pd_csi_sa_cred_file`, `gcp_pd_csi_driver_image_tag` |
| Hetzner (hcloud) | `all/hcloud.yml` | Внешний Hetzner Cloud Controller Manager | `external_hcloud_cloud` (словарь: `hcloud_api_token`, `with_networks`, `load_balancers_*`) |
| Huawei Cloud | `all/huaweicloud.yml` | Внешний Huawei Cloud Controller (LBaaS, Keystone) | `external_huaweicloud_auth_url`, `external_huaweicloud_access_key`, `external_huawei_cloud_controller_image_tag` |
| Oracle (OCI) | `all/oci.yml` | Внешний OCI CCM + устаревший in-tree провайдер | `external_oracle_auth_*`, `external_oracle_cloud_controller_image_tag`, `oci_*` |
| OpenStack | `all/openstack.yml` | LBaaS (in-tree и внешний CCM) + Cinder CSI | `external_openstack_lbaas_enabled`, `cinder_csi_enabled`, `storage_classes` |
| UpCloud | `all/upcloud.yml` | UpCloud CSI Driver | `upcloud_csi_enabled`, `upcloud_csi_controller_replicas`, `storage_classes` |
| vSphere | `all/vsphere.yml` | Внешний vSphere Cloud Provider + vSphere CSI | `external_vsphere_vcenter_ip`, `external_vsphere_user`, `vsphere_csi_enabled` |

## Назначение по провайдерам

### AWS (`aws.yml`)
Только настройки AWS EBS CSI Driver для провижининга томов: включение (`aws_ebs_csi_enabled`), опции планирования/снапшотов/ресайза томов, число реплик контроллера, тег образа и дополнительные теги для создаваемых томов EBS.

### Azure (`azure.yml`)
Две группы переменных: (1) параметры Azure cloud provider (`azure_tenant_id`, `azure_subscription_id`, `azure_resource_group`, `azure_vnet_name`, `azure_vmtype` — `standard` или `vmss` и т. д.); (2) отдельный набор `azure_csi_*` для Azure Disk CSI, включая включение (`azure_csi_enabled`) и креденшелы. Подробности — в `docs/azure.md` и `docs/azure-csi.md`.

### GCP (`gcp.yml`)
Настройки GCP Persistent Disk CSI Driver: путь к файлу креденшелов сервис-аккаунта (`gcp_pd_csi_sa_cred_file`), включение драйвера, число реплик, тег образа.

### Hetzner (`hcloud.yml`)
Единый словарь `external_hcloud_cloud` с вложенными ключами для внешнего Hetzner Cloud Controller Manager: API-токен, поддержка networks, имя сети, аргументы контроллера и группа настроек балансировщиков (`load_balancers_location`, `load_balancers_network_zone`, `load_balancers_use_private_ip` и др.).

### Huawei Cloud (`huaweicloud.yml`)
Внешний Huawei Cloud Controller: ID подсети/сети для LBaaS VIP и креденшелы Keystone (по умолчанию читаются из переменных окружения `OS_*`), а также репозиторий и тег образа контроллера.

### Oracle Cloud (`oci.yml`)
Самый крупный файл. Содержит: (1) параметры внешнего OCI Cloud Controller Manager (`external_oracle_auth_*`, балансировщики, rate limiter, образ CCM); (2) устаревший in-tree OCI провайдер (`oci_*`: креденшелы, подсети, security lists, instance principals, rate limits, зеркало образов).

### OpenStack (`openstack.yml`)
Три блока: (1) встроенный (in-tree) LBaaSv2 — `openstack_lbaas_*`; (2) внешний OpenStack Cloud Controller — `external_openstack_lbaas_*` и `external_openstack_network_*`, а также application credentials для Keystone; (3) Cinder CSI — теги образов сопутствующих контейнеров (`cinder_csi_*_image_tag`), включение и пример `storage_classes`.

### UpCloud (`upcloud.yml`)
UpCloud CSI Driver: включение (нужны `UPCLOUD_USERNAME`/`UPCLOUD_PASSWORD`), число реплик, теги образов компонентов CSI, tolerations и пример списка `storage_classes` (`standard`, `hdd`).

### vSphere (`vsphere.yml`)
Внешний vSphere Cloud Provider: адрес и порт vCenter, флаг небезопасного подключения, пользователь и пароль (можно задать через `VSPHERE_USER`/`VSPHERE_PASSWORD`), датацентр, идентификатор кластера. Плюс включение vSphere CSI и число реплик его контроллера.

## Проверка расхождений с defaults ролей

Поскольку все переменные закомментированы, они не переопределяют значения ролей. Раскомментированных переменных, конфликтующих по значению с `roles/*/defaults`, **не обнаружено** — расхождений нет.

## Связанные заметки

- [[versions/v2.29.1/README|Срез v2.29.1]]
