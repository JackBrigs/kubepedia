---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: inventory
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - discrepancies
reliability: authoritative
---

# Расхождения sample-inventory ↔ roles/*/defaults (v2.29.0)

Сверка выполнена по правилу раздела 6.2 CLAUDE.md: сравниваются значения **реально заданных** (`is_set: true`) переменных из `inventory/sample/` со значениями по умолчанию из `roles/*/defaults`. **Приоритет всегда за кодом ролей**; sample-инвентарь при этом переопределяет defaults на этапе выполнения (group_vars имеют более высокий приоритет, чем defaults роли).

Проверено 598 переменных sample из 5 срезов (`k8s-cluster`, `addons`, `all`, `cloud-providers`, `cni-cilium`); реально заданы (не закомментированы) — 94. Закомментированные примеры в сравнении действующих значений не участвуют.

## 1. Расхождения действующих значений

Расхождений среди действующих (реально заданных) значений в теге v2.29.0 **не выявлено**
(по всем 5 срезам).

Отдельно отмечаем `unsafe_show_logs`: в sample он задан `false`
(`inventory/sample/group_vars/all/all.yml`), и default роли
`roles/kubespray_defaults/defaults/main/download.yml` в v2.29.0 — тоже литерал `false`,
значения совпадают. (В следующем патче v2.29.1 default этой переменной заменён на
выражение по CI-переменной окружения
`{{ lookup('env', 'CI_PROJECT_URL') == 'https://gitlab.com/kargo-ci/kubernetes-sigs-kubespray' }}`,
из-за чего в v2.29.1 появляется расхождение формы; в v2.29.0 его ещё нет.)

## 2. Мягкие наблюдения (закомментированные примеры расходятся с defaults)

Не являются расхождениями действующих значений — переменные в sample **закомментированы** и служат иллюстрацией. Зафиксированы, потому что пример в sample устарел или отличается от фактического default роли и может ввести пользователя в заблуждение.

| Переменная | Пример в sample | Default роли | Файл sample |
|---|---|---|---|
| `containerd_snapshotter` | `native` | `overlayfs` | `all/containerd.yml` |
| `cilium_identity_allocation_mode` | `kvstore` | `crd` | `k8s_cluster/k8s-net-cilium.yml` |
| `cilium_kube_proxy_replacement` | `partial` | `false` | `k8s_cluster/k8s-net-cilium.yml` |
| `cilium_ipam_mode` | `kubernetes` | `cluster-pool` | `k8s_cluster/k8s-net-cilium.yml` |
| `cilium_bpf_map_dynamic_size_ratio` | `0.0` | `0.0025` | `k8s_cluster/k8s-net-cilium.yml` |
| `cilium_enable_host_legacy_routing` | `true` | `false` | `k8s_cluster/k8s-net-cilium.yml` |

## 3. Несовпадения имён и переменные вне defaults

- **`cilium_ipsec_node_encryption` (sample)** соответствует по смыслу **`cilium_encryption_node_encryption` (defaults роли)** — имена различаются. Источник: `k8s_cluster/k8s-net-cilium.yml` vs `roles/network_plugin/cilium/defaults/main.yml`.
- Переменные sample, отсутствующие в defaults роли Cilium (примеры удалённых upstream опций): `cilium_tofqdns_enable_poller`, `cilium_enable_legacy_services` (удалены в Cilium 1.9), `cilium_clusterrole_rules_operator_extra_vars`.
- Заданные в sample, но отсутствующие как самостоятельные переменные в defaults ролей (сравнивать не с чем): `kubeadm_certificate_key`, `metallb_namespace`, `volume_cross_zone_attachment`.
- Флаги включения аддонов в sample записаны булевым `false`, в справочнике defaults — строкой `"false"`: семантически идентично, расхождением не считается.

## 4. Опечатки в исходных примерах sample (перенесены дословно)

- `aws_ebs_csi_extra_volume_tags` и `azure_csi_tags` — незакрытая одинарная кавычка в примере (`all/aws.yml`, `all/azure.yml`). Значения перенесены как есть, отмечены в `comment` соответствующих записей.

---

Связанные справочники: [[versions/v2.29.0/inventory/k8s-cluster|inventory/k8s-cluster]] · [[versions/v2.29.0/inventory/all|inventory/all]] · [[versions/v2.29.0/inventory/cni-cilium|inventory/cni-cilium]] · [[versions/v2.29.0/inventory/cloud-providers|inventory/cloud-providers]] · [[versions/v2.29.0/inventory/addons|inventory/addons]]

Назад: [[versions/v2.29.0/README|Срез v2.29.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
