---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - control-plane
  - resource-reservation
reliability: authoritative
---

# Sample-inventory: kube_control_plane.yml (v2.27.1)

Разбор нового sample-файла `kube_control_plane.yml` из группы `k8s_cluster`.
Источник истины — [[versions/v2.27.1/inventory/kube_control_plane|kube_control_plane.yaml (справочник)]];
здесь человекочитаемое изложение.

Ссылка на срез: [[versions/v2.27.1/README|Срез v2.27.1]].

## Что это за файл

`kube_control_plane.yml` — **новый** sample-файл, появившийся в v2.27.1 (в v2.27.0 его
не было). Он задаёт group_vars для группы `kube_control_plane` и предназначен для
резервирования ресурсов на узлах control plane. Все 8 переменных в файле
**закомментированы** — по умолчанию резервирование не задано, значения берутся из
defaults роли `node` (`roles/kubernetes/node/defaults/main.yml`).

## Зачем добавлен (изменение v2.27.0 → v2.27.1)

До v2.27.1 закомментированные примеры резервирования для control plane находились в
`k8s-cluster.yml` и использовали имена `kube_master_*` / `system_master_*`. Таких
переменных в коде ролей Kubespray **не существует** — это была ошибка sample-файла.
В v2.27.1 ошибочные примеры удалены из `k8s-cluster.yml`, а вместо них добавлен этот
файл с **корректными** именами переменных (`kube_*_reserved` / `system_*_reserved`),
которые действительно обрабатываются ролью `node`. Помещённые в group_vars группы
`kube_control_plane`, они применяются именно к узлам control plane.

## Переменные

| Переменная | Пример в sample | Default роли node | Назначение |
|---|---|---|---|
| `kube_memory_reserved` | `512Mi` | `256Mi` | Память для kube-компонентов control plane |
| `kube_cpu_reserved` | `200m` | `100m` | CPU для kube-компонентов control plane |
| `kube_ephemeral_storage_reserved` | `2Gi` | — | Эфемерное хранилище для kube-компонентов |
| `kube_pid_reserved` | `"1000"` | — | Число PID для kube-компонентов |
| `system_memory_reserved` | `256Mi` | `512Mi` | Память для системных демонов ОС |
| `system_cpu_reserved` | `250m` | `500m` | CPU для системных демонов ОС |
| `system_ephemeral_storage_reserved` | `2Gi` | — | Эфемерное хранилище системных демонов |
| `system_pid_reserved` | `"1000"` | — | Число PID для системных демонов |

Всего в справочнике: **8 переменных**, все закомментированы (`is_set: false`).

## Соответствие defaults ролей

Реально заданных (`is_set: true`) переменных в файле нет, поэтому расхождений с
defaults ролей быть не может. Имена переменных совпадают с обрабатываемыми ролью
`node`, значения-примеры носят иллюстративный характер.
