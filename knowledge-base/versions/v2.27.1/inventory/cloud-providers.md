---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
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
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - cloud-providers
reliability: authoritative
---

# Облачные провайдеры в sample-inventory (v2.27.1)

Заметка описывает файлы `inventory/sample/group_vars/all/<cloud>.yml` тега
**v2.27.1** (commit `45140b5`). Источник истины —
[[versions/v2.27.1/inventory/cloud-providers|cloud-providers.yaml]]; здесь дан
человекочитаемый обзор.

> [!important] Все переменные закомментированы
> Во **всех девяти** файлах провайдеров каждая переменная закомментирована — это
> примеры-заготовки, которые пользователь раскомментирует и заполняет под своё
> окружение. Поэтому у всех записей в YAML стоит `is_set: false`. Значения по
> умолчанию, реально применяемые при развёртывании, находятся в `roles/*/defaults/`.

## Поддержанные провайдеры

| Провайдер | Файл | Что настраивается |
|---|---|---|
| AWS | `all/aws.yml` | AWS EBS CSI Driver (тома EBS) |
| Azure | `all/azure.yml` | Azure cloud provider + Azure Disk CSI |
| GCP | `all/gcp.yml` | GCP Persistent Disk CSI Driver |
| Hetzner (hcloud) | `all/hcloud.yml` | Внешний Hetzner Cloud Controller Manager |
| Huawei Cloud | `all/huaweicloud.yml` | Внешний Huawei Cloud Controller (LBaaS, Keystone) |
| Oracle (OCI) | `all/oci.yml` | Внешний OCI CCM + устаревший in-tree провайдер |
| OpenStack | `all/openstack.yml` | LBaaS (in-tree и внешний CCM) + Cinder CSI |
| UpCloud | `all/upcloud.yml` | UpCloud CSI Driver |
| vSphere | `all/vsphere.yml` | Внешний vSphere Cloud Provider + vSphere CSI |

## Назначение по провайдерам

- **AWS** — настройки AWS EBS CSI Driver: включение, планирование/снапшоты/ресайз
  томов, число реплик контроллера, теги для создаваемых томов EBS.
- **Azure** — параметры Azure cloud provider (`azure_tenant_id`, `azure_vmtype`
  standard/vmss и др.) и отдельный набор `azure_csi_*` для Azure Disk CSI.
- **GCP** — GCP PD CSI: путь к креденшелам сервис-аккаунта, включение, реплики, тег образа.
- **Hetzner** — единый словарь `external_hcloud_cloud` с ключами внешнего CCM: токен,
  networks, аргументы контроллера, настройки балансировщиков.
- **Huawei Cloud** — внешний Huawei CCM: подсеть/сеть LBaaS VIP и креденшелы Keystone
  (по умолчанию из `OS_*`), репозиторий/тег образа контроллера.
- **Oracle Cloud** — внешний OCI CCM (`external_oracle_*`) и устаревший in-tree
  провайдер (`oci_*`), включая `oci_cloud_controller_version`.
- **OpenStack** — три блока: in-tree LBaaSv2 (`openstack_lbaas_*`, плюс
  `openstack_blockstorage_version`), внешний CCM (`external_openstack_*`) и Cinder CSI.
- **UpCloud** — UpCloud CSI Driver: включение, реплики, теги образов, tolerations,
  пример `storage_classes` (standard, hdd).
- **vSphere** — внешний vSphere Cloud Provider (адрес/порт vCenter, insecure,
  пользователь/пароль, датацентр, cluster id) и полный набор тегов образов
  vSphere CSI, а также включение и реплики контроллера.

> [!note] Отличия v2.27.1 от справочника v2.29.1
> Дополнительно присутствуют закомментированные переменные:
> `openstack_blockstorage_version` (openstack.yml), `oci_cloud_controller_version`
> (oci.yml) и расширенный набор тегов образов vSphere (`external_vsphere_version`,
> `external_vsphere_cloud_controller_image_tag`, `vsphere_syncer_image_tag`,
> `vsphere_csi_attacher_image_tag`, `vsphere_csi_controller`,
> `vsphere_csi_liveness_probe_image_tag`, `vsphere_csi_provisioner_image_tag`,
> `vsphere_csi_resizer_tag`).

## Проверка расхождений с defaults ролей

Поскольку все переменные закомментированы, они не переопределяют значения ролей.
Раскомментированных переменных, конфликтующих по значению с `roles/*/defaults`,
**не обнаружено** — расхождений нет.

## Связанные заметки

- [[versions/v2.27.1/README|Срез v2.27.1]]
