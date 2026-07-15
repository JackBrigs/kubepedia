---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.27.1
retrieved_at: 2026-07-15
topics:
  - release
  - versions
  - changelog
  - patch-release
reliability: authoritative
---

# GitHub Release Kubespray v2.27.1

- **Тег:** `v2.27.1` (commit `45140b5`, subject «Fix: galaxy.yml set version to 2.27.1 (#12345)»)
- **Дата тега (git):** 27 июня 2025
- **Дата публикации Release на GitHub:** 28 июля 2025
- **Тип:** **патч-релиз** (bugfix + обновления версий) поверх v2.27.0. Новых breaking changes сверх v2.27.0 не заявлено.
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.27.1

> [!note] Отношение к v2.27.0
> v2.27.1 — исправительный релиз в той же минорной ветке. Все breaking changes и
> крупные изменения (формат `kubeadm_patches`, автогенерация группы `k8s_cluster`,
> устаревание in-tree cloud-провайдеров, требование кэшированных фактов при `--limit`
> и т.д.) относятся к v2.27.0 и продолжают действовать; см. срез
> [[versions/v2.27.0/release-notes|release-notes v2.27.0]]. Ниже — только дельта v2.27.0 → v2.27.1.

## Обновления версий компонентов (v2.27.0 → v2.27.1)

Сверено с кодом тега (`roles/kubespray-defaults/defaults/main/download.yml`) и
справочником [[versions/v2.27.1/components|components]].

| Компонент | v2.27.0 | v2.27.1 | Переменная |
|---|---|---|---|
| Kubernetes | 1.31.4 | **1.31.9** | `kube_version` |
| etcd | 3.5.16 | **3.5.21** | `etcd_version` (по `etcd_supported_versions`) |
| containerd | 1.7.24 | **1.7.27** | `containerd_version` |
| runc | v1.2.3 | **v1.2.6** | `runc_version` |
| CRI-O | 1.31.0 | **1.31.6** | `crio_version` (по `crio_supported_versions`) |
| cri-dockerd | 0.3.11 | **0.3.16** | `cri_dockerd_version` |
| CNI plugins | v1.4.0 | **v1.4.1** | `cni_version` |
| Calico | v3.29.1 | **v3.29.4** | `calico_version` |
| cilium-cli | v0.16.0 | **v0.16.24** | `cilium_cli_version` |
| ingress-nginx | v1.12.0 | **v1.12.1** | `ingress_nginx_version` |
| ingress-nginx certgen | v1.5.0 | **v1.5.2** | `ingress_nginx_kube_webhook_certgen_image_tag` |

**Без изменений** (проверено по коду): Cilium остаётся **v1.15.9** (менялась только `cilium_cli_version`),
crictl — **v1.31.1**, CoreDNS — **1.11.3**, Helm — **3.16.4**.

Минимально поддерживаемая версия Kubernetes — **1.29.0** (`kube_version_min_required`), без изменений.

## Новые/изменённые переменные

- **`kubeadm_image_pull_serial: true`** — новая переменная в
  `roles/kubernetes/control-plane/defaults/main/main.yml`. Управляет полем `imagePullSerial`
  конфигурации kubeadm: скачивать образы последовательно (`true`, по умолчанию) или параллельно.
- **`external_cloud_provider`** — добавлен допустимый вариант **`manual`**
  (`roles/kubespray-defaults/defaults/main/main.yml`). Значение `manual` **не устанавливает**
  cloud controller manager — управление CCM берёт на себя оператор.
- **inventory sample:** добавлен новый файл
  `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml` с закомментированными
  примерами резервирования ресурсов control plane (`kube_*_reserved` / `system_*_reserved`).
  Из `k8s-cluster.yml` при этом удалены ошибочные примеры `kube_master_*` / `system_master_*`
  (таких переменных в коде ролей нет). См. [[versions/v2.27.1/inventory/kube_control_plane|kube_control_plane.yaml]].

## Исправления (по заметкам релиза)

- **ingress-nginx** обновлён до **v1.12.1** для устранения критических уязвимостей
  (в заметках упомянуты **CVE-2025-1974** и другие).
- Исправлено развёртывание **CoreDNS** при использовании pod disruption budgets.
- Исправлена совместимость с **Podman** в скрипте offline-управления образами
  (`contrib/offline/manage-offline-container-images.sh`).
- Исправлена установка symlink-ов сертификатов **etcd** на узлах control plane
  (`roles/etcd/tasks/gen_certs_script.yml`).
- Исправлена переконфигурация control plane через **kubeadm** при обновлении кластера
  (`roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml`).
- Исправлены права доступа для **Calico** `kubecontrollersconfigurations`
  (`roles/network_plugin/calico/templates/calico-kube-cr.yml.j2`).
- Добавлен шаблон конфигурации kubeadm **v1beta4**
  (`roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2`).

## Breaking changes

**Новых breaking changes относительно v2.27.0 в заметках релиза не задокументировано.**
Обновление в пределах v2.27.0 → v2.27.1 сводится к смене версий компонентов и
исправлениям; изменений формата конфигурации, требующих ручной переработки inventory
пользователя, нет (кроме уже действовавших в v2.27.0).

## Ansible-теги запуска

Набор Ansible run-тегов **не изменился** относительно v2.27.0 — правки касались только
содержимого задач, но не атрибутов `tags:`. Справочник тегов среза остаётся актуальным:
[[versions/v2.27.1/ansible-tags|ansible-tags]].

## Примечания

- Дата тега по git (27 июня 2025) и дата публикации Release на GitHub (28 июля 2025)
  различаются — тег создаётся раньше публикации заметок. В `meta.yaml` зафиксированы обе.
- Часть версий (etcd, CRI-O) обновилась, но **не была явно перечислена** во входном задании
  на обновление среза; значения подтверждены по `download.yml` тега v2.27.1 и отражены здесь
  и в `components.yaml`.

---

Связанные срезы: [[versions/v2.27.1/components|Компоненты и версии]] · [[versions/v2.27.1/meta|meta.yaml]]

Назад: [[versions/v2.27.1/README|Срез v2.27.1]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
