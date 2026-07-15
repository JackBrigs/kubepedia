---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: inventory
source_paths:
  - inventory/sample/inventory.ini
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - hosts
  - topology
reliability: authoritative
---

# Sample-inventory: inventory.ini (v2.28.1)

Разбор `inventory/sample/inventory.ini` — файла описания хостов и групп. Ссылка на срез: [[versions/v2.28.1/README|Срез v2.28.1]].

## Топология sample

Комментарий в начале файла описывает конфигурацию: **HA-топология со stacked etcd** (etcd на тех же нодах, что и control plane) и **3 рабочих узла**. Все хосты в sample закомментированы — это шаблон, который пользователь заполняет своими нодами.

## Группы хостов

Файл определяет три явных блока групп:

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

| Группа | Назначение | В sample |
|---|---|---|
| `kube_control_plane` | Узлы control plane: kube-apiserver, kube-controller-manager, kube-scheduler | 3 закомментированных узла (node1-3) |
| `etcd` | Кластер etcd (хранилище состояния кластера) | `[etcd:children]` → включает всю группу `kube_control_plane` (stacked etcd) |
| `kube_node` | Рабочие узлы (worker), запускающие поды нагрузки | 3 закомментированных узла (node4-6) |

### Про `[etcd:children]`

Секция `[etcd:children]` со строкой `kube_control_plane` означает, что группа `etcd` **наследует** всех членов группы `kube_control_plane`. Это и есть stacked-топология: etcd работает на тех же нодах, что и control plane. Для внешнего (external) etcd пользователь перечислил бы отдельные хосты прямо в `[etcd]`.

## Группы, подразумеваемые Kubespray, но отсутствующие в sample

Sample-файл минимален. Kubespray дополнительно использует группы, которые в этом файле не объявлены явно, но формируются автоматически или добавляются пользователем:

| Группа | Назначение |
|---|---|
| `k8s_cluster` | Агрегирующая группа: `kube_control_plane` + `kube_node`. Именно к ней привязаны group_vars из `group_vars/k8s_cluster/` (k8s-cluster.yml, addons.yml). Формируется на уровне статической групповой структуры Kubespray, а не в sample.ini |
| `calico_rr` | Calico route reflectors. Пустая по умолчанию; при непустой группе включается `peer_with_calico_rr` (см. defaults). В sample.ini не объявлена |
| `bastion` | Хост-бастион для SSH ProxyCommand (см. `ansible_ssh_common_args` в defaults). В sample.ini не объявлена |

Привязка group_vars: файлы `inventory/sample/group_vars/k8s_cluster/*.yml` применяются к группе `k8s_cluster`, то есть ко всем control plane и worker узлам одновременно.

## Переменные хостов

В комментариях-примерах у каждого узла показаны переменные уровня хоста:

- **`ansible_host`** — IP/имя для SSH-подключения Ansible (в примере внешние адреса 95.54.0.x).
- **`ip`** — IP, на который привязываются сервисы Kubernetes, если он должен отличаться от адреса интерфейса по умолчанию (в примере внутренние 10.3.0.x). Из вводного комментария файла: задать `ip`, чтобы биндить сервисы на другой интерфейс.
- **`etcd_member_name`** — имя члена кластера etcd (`etcd1`, `etcd2`, `etcd3`). Узлы, не входящие в etcd, могут не задавать значение или задать пустую строку.

## Источник истины

Значения переменных кластера разбираются в [[versions/v2.28.1/inventory/k8s-cluster|k8s-cluster.yaml]] и [[versions/v2.28.1/inventory/addons|addons.yaml]]. Данный файл описывает только структуру групп хостов.
