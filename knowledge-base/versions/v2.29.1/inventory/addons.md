---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/addons.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1
retrieved_at: 2026-07-14
topics:
  - inventory
  - addons
reliability: authoritative
---

# Sample-inventory: addons.yml (v2.29.1)

Разбор `inventory/sample/group_vars/k8s_cluster/addons.yml` (247 строк) — файла включения дополнительных компонентов кластера. Источник истины — [[versions/v2.29.1/inventory/addons|addons.yaml (справочник)]].

Ссылка на срез: [[versions/v2.29.1/README|Срез v2.29.1]].

Всего в справочнике: **92 переменные**, из них реально задано (`is_set: true`) — **16**, закомментированных примеров — **76**.

## Логика файла

По умолчанию **все аддоны выключены**: каждый флаг `*_enabled` в sample либо задан `false`, либо (реже) закомментирован. Под каждым флагом идёт блок закомментированных параметров тонкой настройки — они активируются только при включении соответствующего аддона. Пользователь включает нужный аддон, выставив его флаг в `true`, и при необходимости раскомментирует параметры.

## Флаги включения аддонов (все выключены)

| Аддон | Флаг | Значение в sample | is_set |
|---|---|---|---|
| Dashboard | `dashboard_enabled` | закомментирован (пример `false`) | false |
| Helm CLI | `helm_enabled` | `false` | true |
| Registry | `registry_enabled` | `false` | true |
| Metrics Server | `metrics_server_enabled` | `false` | true |
| Local Path Provisioner | `local_path_provisioner_enabled` | `false` | true |
| Local Volume Provisioner | `local_volume_provisioner_enabled` | `false` | true |
| CSI Snapshot Controller | `csi_snapshot_controller_enabled` | закомментирован (пример `false`) | false |
| Gateway API CRDs | `gateway_api_enabled` | `false` | true |
| Ingress Nginx | `ingress_nginx_enabled` | `false` | true |
| ALB Ingress | `ingress_alb_enabled` | `false` | true |
| Cert Manager | `cert_manager_enabled` | `false` | true |
| MetalLB | `metallb_enabled` | `false` | true |
| Argo CD | `argocd_enabled` | `false` | true |
| Kube VIP | `kube_vip_enabled` | `false` | true |
| Node Feature Discovery | `node_feature_discovery_enabled` | `false` | true |

`dashboard_enabled` и `csi_snapshot_controller_enabled` в sample **закомментированы** (в отличие от остальных флагов, заданных явным `false`).

## Реально заданные переменные, не являющиеся флагами

Помимо флагов `*_enabled`, в sample явно заданы ещё три переменные:

| Переменная | Значение | Комментарий |
|---|---|---|
| `metallb_speaker_enabled` | `{{ metallb_enabled }}` | Наследует значение `metallb_enabled` |
| `metallb_namespace` | `metallb-system` | Namespace MetalLB (в defaults роли отдельной переменной нет) |
| `ingress_publish_status_address` | `""` | Адрес публикации статуса Ingress (пустой) |

## Блоки тонкой настройки (закомментированы)

Под каждым аддоном — закомментированные параметры, среди наиболее объёмных:

- **Local Volume Provisioner**: `local_volume_provisioner_storage_classes` — карта StorageClass'ов (`local-storage`, `fast-disks`) с `host_dir`/`mount_dir`/`volume_mode`/`fs_type` и командами очистки блочных устройств.
- **Ingress Nginx**: множество параметров — тип сервиса, NodePort'ы, ConfigMap'ы TCP/UDP-сервисов, tolerations, класс Ingress, extra args.
- **MetalLB**: `metallb_config` — крупный блок с пулами адресов, layer2/layer3, BGP-пирами (`metallb_peers`) и communities.
- **Kube VIP**: `kube_vip_*` и `loadbalancer_apiserver` — VIP для control plane и сервисов, интерфейс, метод форвардинга.
- **Cert Manager**: tolerations, affinity, nodeSelector, доверенный CA, DNS-конфигурация, extra args контроллера.

Полный список — в справочнике [[versions/v2.29.1/inventory/addons|addons.yaml]].

## Соответствие defaults ролей

Все заданные флаги `*_enabled` со значением `false` совпадают с defaults ролей `kubernetes-apps` (этап 2), где они также `false`. **Расхождений не обнаружено.** Примечание: в sample флаги записаны как булев `false`, в справочнике defaults — строкой `"false"`; это одно и то же значение. Подробности: [[versions/v2.29.1/discrepancies|Расхождения inventory vs defaults]].
