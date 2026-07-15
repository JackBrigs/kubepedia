---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: inventory
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - discrepancies
reliability: authoritative
---

# Расхождения sample-inventory ↔ roles/*/defaults (v2.30.0)

Сверка по правилу раздела 6.2 CLAUDE.md: значения **реально заданных** (`is_set: true`) переменных sample сравниваются с defaults ролей. **Приоритет за кодом ролей.**

Проверено 583 переменных sample из 5 срезов (`k8s-cluster`, `addons`, `all`, `cloud-providers`, `cni-cilium`); реально заданы — 94.

## 1. Расхождения действующих значений

### `unsafe_show_logs`

- **sample:** `false` (жёстко), `inventory/sample/group_vars/all/all.yml`
- **defaults:** вычисляется по env `CI_PROJECT_URL`, `roles/kubespray_defaults/defaults/main/download.yml`
- **Характер:** расхождение формы, не поведения — вне CI обе стороны дают `false`. Приоритет за кодом; sample-`group_vars` переопределяет defaults на `false`.

Единственное расхождение действующих значений (идентично ситуации в v2.29.1).

## 2. Мягкое наблюдение

- Закомментированный пример `containerd_snapshotter: "native"` в `all/containerd.yml` отличается от фактического default роли `overlayfs`. Переменная закомментирована, действующим значением не является.

## 3. Заданные в sample, но вне справочников defaults

Раскомментированы в sample, но отсутствуют как самостоятельные переменные в defaults ролей (сравнивать не с чем): `kubeadm_certificate_key`, `volume_cross_zone_attachment`, а также ряд `loadbalancer_*`, `ntp_*`, `kube_webhook_*`, `docker_container_storage_setup` и др. — это пользовательские настройки sample.

---

Связанные справочники: [[versions/v2.30.0/inventory/k8s-cluster|inventory/k8s-cluster]] · [[versions/v2.30.0/inventory/all|inventory/all]] · [[versions/v2.30.0/inventory/cni-cilium|inventory/cni-cilium]] · [[versions/v2.30.0/inventory/cloud-providers|inventory/cloud-providers]] · [[versions/v2.30.0/inventory/addons|inventory/addons]]

Назад: [[versions/v2.30.0/README|Срез v2.30.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
