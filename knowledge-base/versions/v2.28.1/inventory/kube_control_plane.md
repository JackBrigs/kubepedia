---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: inventory
source_paths:
  - inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - inventory
  - control-plane
  - resources
reliability: authoritative
---

# Sample-inventory: kube_control_plane.yml (v2.28.1)

Разбор файла `inventory/sample/group_vars/k8s_cluster/kube_control_plane.yml` тега **v2.28.1** (commit `a20891a`). Источник истины — [[versions/v2.28.1/inventory/kube_control_plane|kube_control_plane.yaml]]; здесь человекочитаемое изложение.

Ссылка на срез: [[versions/v2.28.1/README|Срез v2.28.1]].

## Назначение

Файл задаёт **резервирование ресурсов** (CPU, память, эфемерное хранилище, PID) **только для узлов группы `kube_control_plane`**. Group_vars этой группы применяются исключительно к control plane, поэтому здесь удобно задать более высокие лимиты, чем на рабочих нодах.

Все **8 переменных закомментированы** (примеры), `is_set: false`. Пользователь раскомментирует нужные и подставляет свои значения.

## Переменные

| Переменная | Пример (control plane) | Назначение |
|---|---|---|
| `kube_memory_reserved` | `512Mi` | Память под компоненты Kubernetes |
| `kube_cpu_reserved` | `200m` | CPU под компоненты Kubernetes |
| `kube_ephemeral_storage_reserved` | `2Gi` | Эфемерное хранилище под компоненты K8s |
| `kube_pid_reserved` | `"1000"` | PID под компоненты K8s |
| `system_memory_reserved` | `256Mi` | Память под системные демоны хоста |
| `system_cpu_reserved` | `250m` | CPU под системные демоны хоста |
| `system_ephemeral_storage_reserved` | `2Gi` | Эфемерное хранилище под системные демоны |
| `system_pid_reserved` | `"1000"` | PID под системные демоны хоста |

## Отличие примеров от значений для рабочих нод

Те же по имени переменные `kube_reserved` / `system_reserved` есть и в `k8s-cluster.yml` (там примеры для рабочих нод). Значения примеров различаются:

| Переменная | Пример здесь (control plane) | Пример в `k8s-cluster.yml` (worker) |
|---|---|---|
| `kube_memory_reserved` | `512Mi` | `256Mi` |
| `kube_cpu_reserved` | `200m` | `100m` |
| `system_memory_reserved` | `256Mi` | `512Mi` |
| `system_cpu_reserved` | `250m` | `500m` |

`kube_control_plane.yml` дополнительно содержит `system_pid_reserved` (пример `"1000"`), которого нет среди примеров `k8s-cluster.yml`.

## Соответствие defaults ролей

Все переменные закомментированы, значений не переопределяют. Самостоятельных одноимённых переменных в `roles/*/defaults` нет — резервирование настраивается пользователем на уровне group_vars. **Расхождений не обнаружено.** Подробности: [[versions/v2.28.1/discrepancies|Расхождения inventory vs defaults]].

## Связанные заметки

- [[versions/v2.28.1/inventory/k8s-cluster|k8s-cluster.yaml (справочник)]]
- [[versions/v2.28.1/README|Срез v2.28.1]]
