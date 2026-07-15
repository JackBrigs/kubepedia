---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12181
retrieved_at: 2026-07-15
topics:
  - etcd
  - control-plane
  - certificates
affected_versions:
  - v2.27.0
fixed_versions:
  - v2.27.1
  - v2.28.0
reliability: confirmed
---

# etcd: отсутствие node-специфичных сертификатов etcd на control-plane-узлах ломало kubeadm (исправлено в v2.27.1)

## Симптом

kubeadm на control-plane-узле не находил ожидаемые сертификаты etcd, названные по имени
другого control-plane-узла (`node-<hostname>.pem`), поскольку каждый узел генерировал только
свой набор сертификатов. Это приводило к сбою настройки control plane со stacked etcd.

## Корневая причина

kubeadm ожидает одинаковый путь к сертификатам etcd на всех `kube_control_plane`-узлах, тогда
как Kubespray генерировал node-специфичные файлы `node-<inventory_hostname>*.pem` только
локально. На других control-plane-узлах соответствующих файлов не было.

## Проверка по коду тега v2.27.0

В v2.27.0 в `roles/etcd/tasks/gen_certs_script.yml` отсутствует блок создания symlink-ов
(проверено: `git grep 'Pretend all control plane have all certs' v2.27.0` — совпадений нет).
Начиная с v2.28.0 и в v2.27.1 блок присутствует:

```yaml
- name: Gen_certs | Pretend all control plane have all certs (with symlinks)
  file:
    state: link
    src: "{{ etcd_cert_dir }}/node-{{ inventory_hostname }}{{ item[0] }}.pem"
    dest: "{{ etcd_cert_dir }}/node-{{ item[1] }}{{ item[0] }}.pem"
  loop: "{{ suffixes | product(groups['kube_control_plane']) }}"
```

## Решение

Мастер-фикс — PR [#12181](https://github.com/kubernetes-sigs/kubespray/pull/12181)
«Workaround missing etcd certs on control plane node» (commit `fcc294600`), вошёл в v2.28.0.
Бэкпорт в release-2.27 — PR #12192 (commit `d10000ee9`), вошёл в v2.27.1. Symlink-и «выдают»
на каждом control-plane-узле сертификаты остальных узлов, чтобы kubeadm нашёл ожидаемые пути.

## Версии

- **Затронуто:** v2.27.0.
- **Исправлено:** v2.27.1 (бэкпорт #12192) и v2.28.0 (мастер #12181). В v2.28.x/v2.29.x проблема отсутствует.

## Связанное

[[versions/v2.27.0/variables/etcd|Переменные etcd]] · [[versions/v2.27.0/docs/etcd|Дайджест: etcd]]
