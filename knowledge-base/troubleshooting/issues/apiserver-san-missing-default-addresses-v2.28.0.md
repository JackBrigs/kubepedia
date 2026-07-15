---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12413
retrieved_at: 2026-07-15
topics:
  - control-plane
  - kubeadm
  - certificates
affected_versions:
  - v2.27.0
  - v2.27.1
  - v2.28.0
fixed_versions:
  - v2.28.1
  - v2.29.0
reliability: confirmed
---

# kube-apiserver: в SAN сертификата не попадали default-адреса узлов (исправлено в v2.28.1)

## Симптом

В SAN (Subject Alternative Names) сертификата kube-apiserver отсутствовали адреса по умолчанию
control-plane-узлов (default IPv4/IPv6), что могло приводить к ошибкам проверки TLS при
обращении к API по этим адресам.

## Корневая причина

В `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml` адреса собирались одной переменной
`sans_address` через вложенный `map('extract', hostvars, ['ansible_default_ipv6', 'ansible_default_ipv4', 'address'])`.
Такой цепочечный extract (вложенный доступ по ключам) не давал корректно собрать default-адреса
обоих семейств — часть адресов терялась.

## Проверка по коду тегов

Буговая `sans_address` присутствует в `kubeadm-setup.yml` тегов v2.27.0, v2.27.1, v2.28.0
(`git grep 'sans_address:'`). В v2.28.1 (её tag-коммит `a20891ab6` и есть этот фикс) и v2.29.0
переменная заменена на раздельные `sans_ipv4_address` / `sans_ipv6_address`.

## Решение

PR [#12413](https://github.com/kubernetes-sigs/kubespray/pull/12413) «Fix SAN address collection
from ansible_default_ipv{4,6}» (master, commit `56c830713`) разбивает сбор на два поля:

```yaml
sans_ipv4_address: "{{ groups['kube_control_plane'] | map('extract', hostvars, ['ansible_default_ipv4', 'address']) | ... }}"
sans_ipv6_address: "{{ groups['kube_control_plane'] | map('extract', hostvars, ['ansible_default_ipv6', 'address']) | ... }}"
```

Бэкпорт в release-2.28 — PR #12505 (commit `a20891ab6`, tag-коммит v2.28.1).

## Версии

- **Затронуто:** v2.27.0, v2.27.1, v2.28.0 (буговый `sans_address` подтверждён по коду).
- **Исправлено:** v2.28.1 (бэкпорт #12505) и v2.29.0 (master #12413).

## Связанное

[[versions/v2.28.0/variables/k8s-cluster|Переменные k8s-cluster (SANs)]] · [[versions/v2.28.0/docs/security|Дайджест: безопасность/сертификаты]]
