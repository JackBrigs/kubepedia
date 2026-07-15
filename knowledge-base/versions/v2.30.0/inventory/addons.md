---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/addons.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - addons
reliability: authoritative
---

# Sample-inventory: addons.yml (v2.30.0)

Разбор `inventory/sample/group_vars/k8s_cluster/addons.yml` тега v2.30.0 (commit `f4ccdb5`). Источник истины — [[versions/v2.30.0/inventory/addons|addons.yaml]]. Ссылка на срез: [[versions/v2.30.0/README|Срез v2.30.0]].

## Обзор

Файл включает/выключает дополнительные компоненты кластера. **16 переменных заданы явно** (флаги включения аддонов и несколько параметров MetalLB/ingress), **76 приведены как закомментированные примеры** тонкой настройки. Все реально заданные значения совпадают с defaults ролей `kubernetes-apps` — расхождений нет (см. [[versions/v2.30.0/inventory/discrepancies|discrepancies]]).

## Флаги включения аддонов (is_set: true)

| Переменная | Значение | Аддон |
|---|---|---|
| `helm_enabled` | `false` | Helm CLI |
| `registry_enabled` | `false` | Внутрикластерный registry |
| `metrics_server_enabled` | `false` | Metrics Server |
| `local_path_provisioner_enabled` | `false` | Rancher Local Path Provisioner |
| `local_volume_provisioner_enabled` | `false` | Local Volume Provisioner |
| `gateway_api_enabled` | `false` | CRD Gateway API |
| `ingress_nginx_enabled` | `false` | Ingress NGINX |
| `ingress_alb_enabled` | `false` | AWS ALB Ingress |
| `cert_manager_enabled` | `false` | cert-manager |
| `metallb_enabled` | `false` | MetalLB |
| `argocd_enabled` | `false` | Argo CD |
| `kube_vip_enabled` | `false` | kube-vip |
| `node_feature_discovery_enabled` | `false` | Node Feature Discovery |

По умолчанию **все аддоны выключены**. `dashboard_enabled` в этом файле закомментирован (is_set: false).

## Явно заданные параметры (не только флаги)

Помимо флагов, раскомментированы три параметра:

- `metallb_speaker_enabled: "{{ metallb_enabled }}"` — speaker включается вместе с MetalLB.
- `metallb_namespace: "metallb-system"` — namespace MetalLB.
- `ingress_publish_status_address: ""` — адрес публикации статуса Ingress (единственная активная переменная блока ingress_nginx).

## Закомментированные блоки настройки

Каждый аддон сопровождается развёрнутым набором закомментированных параметров-примеров:

- **Registry** — `registry_namespace`, `registry_storage_class`, `registry_disk_size`.
- **Metrics Server** — порт, TLS, resolution, replicas, hostNetwork.
- **Local Path / Local Volume Provisioner** — namespace, StorageClass'ы, каталоги, tolerations.
- **Ingress NGINX** — тип сервиса, NodePort'ы, аннотации, ConfigMap'ы (TCP/UDP services), класс, tolerations.
- **cert-manager** — namespace, affinity/tolerations/nodeselector, DNS, доверенный CA, extra args.
- **MetalLB** — `metallb_protocol`, порты и полный `metallb_config` с пулами адресов, L2/L3 и BGP-пирами.
- **Argo CD** — `argocd_namespace`, `argocd_admin_password` (по умолчанию генерируется в secret `argocd-initial-admin-secret`).
- **kube-vip** — ARP/BGP, VIP-адрес, `loadbalancer_apiserver`, интерфейс, режим сервисов, node labeling.
- **Node Feature Discovery** — ServiceAccount'ы gc/worker, `node_feature_discovery_master_config`.
- **CSI snapshots** — `csi_snapshot_controller_enabled` (cinder_csi включает автоматически), `snapshot_controller_namespace`.

## Связанные материалы

- Дефолты ролей аддонов: [[versions/v2.30.0/variables/addons|variables/addons.yaml]]
- Ядро кластера: [[versions/v2.30.0/inventory/k8s-cluster|inventory/k8s-cluster.yaml]]
