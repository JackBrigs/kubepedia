---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12685
retrieved_at: 2026-07-14
topics:
  - etcd
  - nodes
  - remove-node
affected_versions:
  - v2.29.0
fixed_versions:
  - v2.29.1
reliability: confirmed
---

# etcd: удаление внешнего (не stacked) члена кластера прерывало плейбук (исправлено в v2.29.1)

## Симптом

При удалении узла etcd, развёрнутого **отдельно** от control plane (external etcd, узел не входит в кластер Kubernetes), плейбук удаления падал: задача «Lookup node IP in kubernetes» прерывала выполнение целиком, и член etcd не удалялся.

## Корневая причина

Прежняя логика удаляла члена etcd, определяя его по IP-адресу через сопоставление с узлом Kubernetes. Для standalone-узла etcd (не являющегося узлом k8s) такой поиск IP не находил соответствия и прерывал плейбук. Сопоставление было текстовым и зависело от нескольких переменных.

## Решение

PR [#12685](https://github.com/kubernetes-sigs/kubespray/pull/12685) (исходный #12682, commit `59b3c686a`) сменил стратегию: член etcd теперь определяется по `peerURLs` из JSON-вывода `etcdctl`, без зависимости от того, является ли узел etcd членом кластера Kubernetes, и без новых переменных.

## Проверка по коду тега v2.29.1

`roles/remove-node/remove-etcd-node/tasks/main.yml`:

```yaml
command: "{{ bin_dir }}/etcdctl member list -w json"
# ...
- "{{ '%x' | format(((etcd_members.stdout | from_json).members
     | selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID) }}"
```

Член etcd выбирается по `peerURLs.0 == etcd_peer_url`, ID берётся из JSON. Коммит `59b3c686a` входит в диапазон `v2.29.0..v2.29.1`.

## Версии

- **Затронуто:** v2.29.0 (при удалении external-etcd узла).
- **Исправлено:** v2.29.1.

## Связанное

[[versions/v2.29.1/docs/nodes|Дайджест: узлы и восстановление]] · [[versions/v2.29.1/variables/etcd|Переменные etcd]] · [[versions/v2.29.1/ansible-tags|Ansible-теги (pre-remove/post-remove)]]
