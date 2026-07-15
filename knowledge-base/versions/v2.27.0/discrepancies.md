---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: inventory
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - inventory
  - discrepancies
reliability: authoritative
---

# Расхождения sample-inventory ↔ roles/*/defaults (v2.27.0)

Сверка выполнена по правилу раздела 6.2 CLAUDE.md: сравниваются значения **реально
заданных** (`is_set: true`) переменных из `inventory/sample/` со значениями по
умолчанию из `roles/*/defaults`. **Приоритет всегда за кодом ролей**; sample-инвентарь
при этом переопределяет defaults на этапе выполнения (group_vars имеют более высокий
приоритет, чем defaults роли).

Проверено **640 переменных** sample из 5 срезов (`all` — 135, `k8s-cluster` — 129,
`cni-cilium` — 82, `addons` — 124, `cloud-providers` — 170); реально заданы
(не закомментированы) — **100** (20 + 59 + 1 + 20 + 0). Закомментированные примеры в
сравнении действующих значений не участвуют.

## 1. Расхождения действующих значений

**Расхождений действующих значений не обнаружено.**

Проверенные заданные переменные, присутствующие в defaults ролей, совпадают со
значениями sample. В частности:

| Переменная | sample | default роли | Файл defaults |
|---|---|---|---|
| `bin_dir` | `/usr/local/bin` | `/usr/local/bin` | `roles/kubespray-defaults/defaults/main/main.yml` |
| `kube_version` | `v1.31.4` | `v1.31.4` | `roles/kubespray-defaults/defaults/main/main.yml` |
| `container_manager` | `containerd` | `containerd` | `roles/kubespray-defaults/defaults/main/main.yml` |
| `etcd_data_dir` | `/var/lib/etcd` | `/var/lib/etcd` | `roles/etcd/defaults/main.yml` |
| `etcd_deployment_type` | `host` | `host` | `roles/kubespray-defaults/defaults/main/main.yml` |
| `ntp_enabled` / `ntp_manage_config` | `false` / `false` | `false` / `false` | `roles/kubernetes/preinstall/defaults/main.yml` |
| `docker_bin_dir` | `/usr/bin` | `/usr/bin` | `roles/container-engine/docker/defaults/main.yml` |
| `cilium_l2announcements` | `false` | `false` | `roles/network_plugin/cilium/defaults/main.yml` |
| `unsafe_show_logs` | `false` | `false` | `roles/kubespray-defaults/defaults/main/download.yml` |

> [!important] Отличие v2.27.0 от v2.29.1 по `unsafe_show_logs`
> В v2.29.1 default роли `unsafe_show_logs` вычислялся по CI-переменной окружения
> (`lookup('env','CI_PROJECT_URL') == ...`), из-за чего фиксировалось расхождение
> формы. В **v2.27.0** default — жёсткий `false`, поэтому значение sample (`false`)
> **полностью совпадает** с defaults. Расхождения по этой переменной в v2.27.0 нет.

## 2. Мягкие наблюдения (закомментированные примеры расходятся с defaults)

Не являются расхождениями действующих значений — переменные в sample
**закомментированы** и служат иллюстрацией. Зафиксированы, потому что пример
отличается от фактического default роли и может ввести пользователя в заблуждение.

| Переменная | Пример в sample | Default роли | Файл sample |
|---|---|---|---|
| `containerd_snapshotter` | `native` | `overlayfs` | `all/containerd.yml` |
| `cilium_ipam_mode` | `kubernetes` | `cluster-pool` | `k8s_cluster/k8s-net-cilium.yml` |
| `cilium_bpf_map_dynamic_size_ratio` | `"0.0"` | `"0.0025"` | `k8s_cluster/k8s-net-cilium.yml` |

> [!note] Меньше расхождений примеров, чем в v2.29.1
> В v2.27.0 закомментированные примеры Cilium `cilium_identity_allocation_mode`
> (`kvstore`), `cilium_kube_proxy_replacement` (`partial`) и
> `cilium_enable_host_legacy_routing` (`true`) **совпадают** с defaults роли v2.27.0
> (в v2.29.1 эти примеры расходились с обновлёнными defaults). Пример
> `cilium_version: "v1.15.9"` также совпадает с defaults.

## 3. Несовпадения имён и переменные вне defaults

- В v2.27.0 переменная шифрования node-to-node в sample и в defaults роли имеет
  **одинаковое** имя `cilium_ipsec_node_encryption` (в v2.29.1 роль переименовала её
  в `cilium_encryption_node_encryption`). Несовпадения имён здесь нет.
- Переменные sample, отсутствующие в defaults роли Cilium (примеры удалённых upstream
  опций): `cilium_tofqdns_enable_poller`, `cilium_enable_legacy_services` (удалены в
  Cilium 1.9), `cilium_clusterrole_rules_operator_extra_vars`.
- Заданные в sample, но отсутствующие как самостоятельные переменные в defaults ролей
  (сравнивать не с чем): `kubeadm_certificate_key`, `metallb_namespace`,
  `volume_cross_zone_attachment`, `krew_root_dir`, ряд `docker_*` (задаются только в
  sample и в шаблонах через `| default(...)`).
- Флаги включения аддонов в sample записаны булевым `false`, в справочниках defaults —
  часто строкой `"false"`: семантически идентично, расхождением не считается.
- Аддоны `cephfs_provisioner_enabled` и `rbd_provisioner_enabled` (`false`) специфичны
  для v2.27.0; их defaults ролей также `false` — расхождения нет.

## 4. Опечатки в исходных примерах sample (перенесены дословно)

- `aws_ebs_csi_extra_volume_tags` и `azure_csi_tags` — незакрытая одинарная кавычка в
  примере (`all/aws.yml`, `all/azure.yml`). Перенесены как есть, отмечены в `comment`.
- `cilium_enable_hubble_ui` — незакрытая двойная кавычка в закомментированном примере
  (`k8s_cluster/k8s-net-cilium.yml`, строка `cilium_enable_hubble_ui: "{{ cilium_enable_hubble }}`).
  Так как строка закомментирована, на кластер не влияет.

---

Связанные справочники: [[versions/v2.27.0/inventory/k8s-cluster|inventory/k8s-cluster]] ·
[[versions/v2.27.0/inventory/all|inventory/all]] ·
[[versions/v2.27.0/inventory/cni-cilium|inventory/cni-cilium]] ·
[[versions/v2.27.0/inventory/cloud-providers|inventory/cloud-providers]] ·
[[versions/v2.27.0/inventory/addons|inventory/addons]]

Назад: [[versions/v2.27.0/README|Срез v2.27.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
