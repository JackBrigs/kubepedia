---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: inventory
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - discrepancies
reliability: authoritative
---

# Расхождения sample-inventory ↔ roles/*/defaults (v2.31.0)

Сверка по правилу раздела 6.2 CLAUDE.md: значения **реально заданных** (`is_set: true`) переменных sample сравниваются с defaults ролей. **Приоритет за кодом ролей.**

Проверено 577 переменных sample из 5 срезов; реально заданы — 92.

## 1. Расхождения действующих значений

**Не обнаружено** (`discrepancies: []` по всем срезам). Все реально заданные переменные sample совпадают со значениями по умолчанию ролей. В частности, `unsafe_show_logs: false` в sample совпадает с эффективным (non-CI) значением defaults.

## 2. Мягкие наблюдения (закомментированные примеры расходятся с defaults)

Не являются действующими расхождениями (переменные закомментированы):

- `containerd_snapshotter: "native"` (`all/containerd.yml`) — default роли `overlayfs`.
- Cilium-примеры в `k8s-net-cilium.yml`: `cilium_identity_allocation_mode` (`kvstore` vs `crd`), `cilium_ipam_mode` (`kubernetes` vs `cluster-pool`), `cilium_bpf_map_dynamic_size_ratio` (`"0.0"` vs `"0.0025"`), `cilium_enable_host_legacy_routing` (`true` vs `false`), `cilium_mtu` (`""` vs `"0"`).

## 3. Несовпадения имён и переменные вне defaults

- `cilium_ipsec_node_encryption` (sample) ↔ `cilium_encryption_node_encryption` (defaults роли).
- Переменные sample, отсутствующие в defaults роли Cilium: `cilium_tofqdns_enable_poller`, `cilium_enable_legacy_services` (обе deprecated), `cilium_hubble_event_buffer_capacity`, `cilium_hubble_event_queue_size`.

## 4. Опечатки в исходных примерах sample (перенесены дословно)

- `aws_ebs_csi_extra_volume_tags` и `azure_csi_tags` — несбалансированная кавычка в примере (`all/aws.yml`, `all/azure.yml`).

## 5. Изменения sample относительно v2.30.0

- В `addons.yml` **удалены** переменные Kubernetes Dashboard и `ingress_nginx` (роли убраны в v2.31.0).
- В `k8s-cluster.yml` **добавлены** закомментированные примеры структурированной AuthenticationConfiguration (`kube_apiserver_use_authentication_config_file`, `kube_apiserver_authentication_config_jwt`, `kube_apiserver_authentication_config_anonymous`).

---

Связанные справочники: [[versions/v2.31.0/inventory/k8s-cluster|inventory/k8s-cluster]] · [[versions/v2.31.0/inventory/all|inventory/all]] · [[versions/v2.31.0/inventory/cni-cilium|inventory/cni-cilium]] · [[versions/v2.31.0/inventory/cloud-providers|inventory/cloud-providers]] · [[versions/v2.31.0/inventory/addons|inventory/addons]]

Назад: [[versions/v2.31.0/README|Срез v2.31.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
