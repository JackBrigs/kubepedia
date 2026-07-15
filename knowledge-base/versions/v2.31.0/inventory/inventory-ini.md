---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: inventory
source_path: inventory/sample/inventory.ini
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - inventory
  - hosts
reliability: authoritative
---

# Sample inventory.ini: группы хостов (v2.31.0)

Разбор файла `inventory/sample/inventory.ini` тега `v2.31.0` (commit `1c9add4`).
Файл задаёт топологию кластера и распределение узлов по группам Ansible.

## Описываемая топология

Sample описывает **HA-топологию со stacked etcd** (etcd размещается на тех же узлах, что и
control-plane) и **3 рабочими узлами**. Все примеры хостов закомментированы — пользователь
подставляет свои узлы.

## Группы хостов

| Группа | Тип | Содержимое в sample | Назначение |
|---|---|---|---|
| `kube_control_plane` | группа хостов | `node1`, `node2`, `node3` (закомментированы) | Узлы control-plane Kubernetes |
| `etcd` | `[etcd:children]` | включает группу `kube_control_plane` | Члены кластера etcd (stacked — совпадают с control-plane) |
| `kube_node` | группа хостов | `node4`, `node5`, `node6` (закомментированы) | Рабочие узлы (worker) |

Группа `etcd` задана как `[etcd:children]` и наследует хосты из `kube_control_plane`,
поэтому etcd разворачивается на тех же узлах, что и control-plane (stacked etcd).

## Пример записи хоста

Закомментированные примеры в sample:

```ini
[kube_control_plane]
# node1 ansible_host=95.54.0.12  # ip=10.3.0.1 etcd_member_name=etcd1
# node2 ansible_host=95.54.0.13  # ip=10.3.0.2 etcd_member_name=etcd2
# node3 ansible_host=95.54.0.14  # ip=10.3.0.3 etcd_member_name=etcd3

[etcd:children]
kube_control_plane

[kube_node]
# node4 ansible_host=95.54.0.15  # ip=10.3.0.4
# node5 ansible_host=95.54.0.16  # ip=10.3.0.5
# node6 ansible_host=95.54.0.17  # ip=10.3.0.6
```

## Переменные хоста

| Переменная | Назначение |
|---|---|
| `ansible_host` | IP/адрес, по которому Ansible подключается к узлу по SSH |
| `ip` | IP, на котором привязываются сервисы Kubernetes (если отличается от интерфейса по умолчанию) |
| `etcd_member_name` | Имя члена кластера etcd. Задаётся для узлов группы `etcd`; узлы вне etcd могут не задавать значение или задать пустую строку |

## Замечания

- Согласно комментариям файла, переменную `ip` следует настроить, если сервисы Kubernetes
  нужно привязать к адресу, отличному от интерфейса по умолчанию.
- `etcd_member_name` необходимо задавать для узлов, входящих в кластер etcd.
- Группа `kube_cluster` в файле явно не объявлена, но используется в group_vars
  (`inventory/sample/group_vars/k8s_cluster/`) — она формируется автоматически как объединение
  `kube_control_plane` и `kube_node`.

## Навигация

- [[versions/v2.31.0/inventory/k8s-cluster|Sample inventory: k8s-cluster]]
- [[versions/v2.31.0/inventory/addons|Sample inventory: addons]]
- [[versions/v2.31.0/README|Срез v2.31.0]]
