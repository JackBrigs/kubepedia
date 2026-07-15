---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/getting_started/getting-started.md
  - docs/getting_started/setting-up-your-first-cluster.md
  - docs/getting_started/comparisons.md
  - docs/ansible/ansible.md
  - docs/ansible/inventory.md
  - docs/ansible/vars.md
  - docs/ansible/ansible_collection.md
  - docs/operations/ha-mode.md
  - docs/operations/integration.md
  - docs/operations/port-requirements.md
  - docs/operations/large-deployments.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - installation
  - getting-started
  - ansible
  - ha
reliability: authoritative
---

# Установка кластера в v2.30.0

Дайджест по установке Kubespray, собранный строго из `docs/` тега **v2.30.0** (commit `f4ccdb5`). Сжатая выжимка, не перевод; имена переменных, команды и номера портов сохранены точно.

## Требования и подготовка

- Хост управления (ansible runner): Linux или Mac с Python 3.
- Ansible ставится в изолированное окружение Python (`venv`) из `requirements.txt`, поставляемого в репозитории Kubespray под конкретную версию Ansible.
- Kubespray поддерживает несколько версий Ansible и поставляет разные `requirements.txt` под них; доступная версия Ansible ограничена вашей версией Python.

### Совместимость Ansible и Python

Таблица из `docs/ansible/ansible.md`:

| Версия Ansible | Версия Python |
|----------------|---------------|
| >= 2.17.3      | 3.10-3.12     |

Симптом несовместимости: `pip` не находит требуемую версию Ansible при установке `requirements.txt` — значит, версия Python не подходит под поддерживаемую версию Ansible.

### Установка Ansible в venv

```ShellSession
VENVDIR=kubespray-venv
KUBESPRAYDIR=kubespray
python3 -m venv $VENVDIR
source $VENVDIR/bin/activate
cd $KUBESPRAYDIR
pip install -r requirements.txt
```

Kubespray поставляет кастомные Ansible-модули в каталоге `library/`. Если Ansible их не находит, укажите путь через переменную окружения:

```ShellSession
export ANSIBLE_LIBRARY=<kubespray_dir>/library
```

### Запуск через готовый Docker-образ

Альтернатива venv — предсобранный образ с Quay (гарантирует правильные версии Ansible и зависимостей). Инвентарь и SSH-ключ пробрасываются через bind mounts:

```ShellSession
git checkout v2.30.0
docker pull quay.io/kubespray/kubespray:v2.30.0
docker run --rm -it --mount type=bind,source="$(pwd)"/inventory/sample,dst=/inventory \
  --mount type=bind,source="${HOME}"/.ssh/id_rsa,dst=/root/.ssh/id_rsa \
  quay.io/kubespray/kubespray:v2.30.0 bash
# внутри контейнера:
ansible-playbook -i /inventory/inventory.ini --private-key /root/.ssh/id_rsa cluster.yml
```

## Структура inventory (группы хостов)

Инвентарь может храниться в форматах YAML, JSON или INI-подобном. Основа — три группы (`docs/ansible/inventory.md`):

- **kube_node** — узлы, на которых запускаются pod'ы.
- **kube_control_plane** — серверы с компонентами control plane (apiserver, scheduler, controller).
- **etcd** — серверы кластера etcd; для отказоустойчивости нужно минимум 3.

Правила пересечения групп:

- Если `kube_node` включает узлы из `etcd`, etcd становится schedulable для рабочих нагрузок. Для standalone etcd группы не должны пересекаться.
- Узел, играющий роль и control-plane, и node, должен входить в обе группы: `kube_control_plane` и `kube_node`.
- Для standalone и unschedulable control plane узел определяется только в `kube_control_plane` (не в `kube_node`).

Специальные группы:

- **calico_rr** — для продвинутых сценариев сети Calico (route reflector).
- **bastion** — bastion-хост, если узлы недоступны напрямую.

Группа **k8s_cluster** формируется динамически как объединение `kube_node`, `kube_control_plane` и `calico_rr`. Используется внутренне и для задания переменных всего кластера (`<inventory>/group_vars/k8s_cluster/*.yml`).

### Пример инвентаря (INI)

```ini
node1 ansible_host=95.54.0.12 ip=10.3.0.1
node2 ansible_host=95.54.0.13 ip=10.3.0.2
node3 ansible_host=95.54.0.14 ip=10.3.0.3
...
[kube_control_plane]
node1
node2

[etcd]
node1
node2
node3

[kube_node]
node2
node3
node4
node5
node6
```

### Bastion-хост

Для узлов только с приватными IP добавьте в инвентарь строку (замените `x.x.x.x` на публичный IP bastion):

```ini
[bastion]
bastion ansible_host=x.x.x.x
```

### Подготовка каталога инвентаря

```ShellSession
cp -rfp inventory/sample inventory/mycluster
# затем править:
inventory/mycluster/inventory.ini
inventory/mycluster/group_vars/all.yml                 # для каждого узла, включая etcd
inventory/mycluster/group_vars/k8s_cluster.yml         # для каждого узла кластера (не etcd, если отдельный)
inventory/mycluster/group_vars/kube_control_plane.yml  # для control plane
inventory/mycluster/group_vars/kube_node.yml           # для worker-узлов
```

### Источники переменных и приоритет (precedence)

Из `docs/ansible/ansible.md` — рекомендуемые слои переменных:

| Слой                              | Комментарий                                        |
|-----------------------------------|----------------------------------------------------|
| inventory vars                    |                                                    |
| — **inventory group_vars**        | используется чаще всего                            |
| — inventory host_vars             | переопределения для конкретного хоста              |
| **extra vars** (высший приоритет) | `ansible-playbook -e @foo.yml`                     |

Extra vars лучше использовать для переопределения внутренних переменных Kubespray (`roles/vars/`), которые не входят в публичный интерфейс и могут меняться без предупреждения.

Ключевые кластерные переменные см. в [[versions/v2.30.0/variables/k8s-cluster|Переменные ядра]] (например `cluster_name`, `container_manager` по умолчанию `containerd`, `kube_network_plugin` по умолчанию Calico, `kube_service_addresses` = `10.233.0.0/18`, `kube_pods_subnet` = `10.233.64.0/18`, `kube_proxy_mode`, `kube_version`).

## Способы запуска

### Основная установка

```ShellSession
ansible-playbook -i inventory/mycluster/ cluster.yml -b -v \
  --private-key=~/.ssh/private_key
```

Флаг `-b` (become) — повышение привилегий до root. При установке через collection используется `--become --become-user=root`.

### Добавление узлов

Полное повторное применение `cluster.yml` или минимальный вариант через `scale.yml`:

```ShellSession
ansible-playbook -i inventory/mycluster/hosts.yml scale.yml -b -v \
  --private-key=~/.ssh/private_key
```

### Удаление узлов

```ShellSession
ansible-playbook -i inventory/mycluster/hosts.yml remove-node.yml -b -v \
  --private-key=~/.ssh/private_key \
  --extra-vars "node=nodename,nodename2"
```

Особенности: узлы дренируются, останавливаются сервисы, удаляются сертификаты, затем `kubectl delete node`. Playbook **не поддерживает удаление первого control-plane или etcd-узла**. Для полностью недоступного по SSH узла добавьте `--extra-vars reset_nodes=false` (можно задать `reset_nodes=false` как host var).

### Сброс кластера

```ShellSession
ansible-playbook -i inventory/mycluster/ -b -v --private-key=~/.ssh/id_rsa reset.yml
```

### Установка как Ansible collection

Kubespray можно установить как коллекцию (`docs/ansible/ansible_collection.md`): описать её в `requirements.yml` (`type: git`, `version:` — нужный тег/ветка), установить `ansible-galaxy install -r requirements.yml`, затем импортировать playbook `kubernetes_sigs.kubespray.cluster` и запустить.

### Запуск по Ansible-тегам

Установку можно фильтровать через `--tags` / `--skip-tags`. Полный справочник тегов запуска — [[versions/v2.30.0/ansible-tags|Ansible-теги]]. Примеры из документации:

```ShellSession
# только DNS-конфигурация, без OS-конфигурации и загрузки образов
ansible-playbook -i inventory/sample/hosts.ini cluster.yml \
  --tags preinstall,facts --skip-tags=download,bootstrap_os

# только удаление IP DNS-резолвера кластера из /etc/resolv.conf
ansible-playbook -i inventory/sample/hosts.ini -e dns_mode='none' cluster.yml --tags resolvconf

# подготовить образы локально на ansible runner без установки/выгрузки на узлы
ansible-playbook -i inventory/sample/hosts.ini cluster.yml \
  -e download_run_once=true -e download_localhost=true \
  --tags download --skip-tags upload,upgrade
```

Предупреждение из документации: `--tags`/`--skip-tags` использовать осознанно, только при полном понимании последствий.

### Доступ к кластеру

- По умолчанию `kube_control_plane` имеет небезопасный доступ к kube-apiserver через порт **8080** (kubectl использует `http://localhost:8080`).
- Удалённый доступ — на любом IP любого узла `kube_control_plane` по порту **6443** (требует аутентификации).
- Опции доставки kubeconfig на ansible-хост: `kubectl_localhost: true` (скачивает `kubectl` в `/usr/local/bin/`), `kubeconfig_localhost: true` (кладёт `admin.conf` в `inventory/mycluster/artifacts/`). Путь настраивается через `artifacts_dir`.
- Kubernetes Dashboard по умолчанию ставится в namespace `kube-system` (переопределяется `dashboard_namespace`), обслуживается только по https.

## HA-режим (высокая доступность)

Отказоустойчивые endpoint'ы требуются для etcd и kube-apiserver (`docs/operations/ha-mode.md`).

### etcd

Клиенты etcd (kube-api-masters) настроены со списком всех peer'ов etcd. Если в кластере etcd несколько инстансов — HA уже обеспечено.

### kube-apiserver

Два основных подхода:

- **Localhost load balancing (по умолчанию)**: nginx-прокси на каждом non-master узле. Управляется `loadbalancer_apiserver_localhost` (по умолчанию `True`; `False`, если задан внешний `loadbalancer_apiserver`). Порт локального балансировщика — `loadbalancer_apiserver_port` (по умолчанию равен `kube_apiserver_port`). Имя контейнера — `loadbalancer_apiserver_pod_name`. Kubespray настраивает kubelet и kube-proxy на использование локального балансировщика только на non-master узлах.
- **Внешний load balancer**: либо роль [kube-vip], либо собственный LB. Пример конфигурации внешнего HAProxy (frontend VIP, backends по `6443`) приведён в документации. Соответствующие переменные:

```yml
apiserver_loadbalancer_domain_name: "my-apiserver-lb.example.com"
loadbalancer_apiserver:
  address: <VIP>
  port: 8383
```

Важные замечания:

- Для внешнего LB используйте порт, отличный от того, на котором слушает API (apiserver по умолчанию биндится на все интерфейсы), либо задайте `kube_apiserver_bind_address`, чтобы API слушал только на конкретном интерфейсе.
- Доменное имя (или дефолтное `lb-apiserver.kubernetes.local`) добавляется в `/etc/hosts` всех узлов группы `k8s_cluster` и включается в self-signed TLS-сертификаты.
- `loadbalancer_apiserver` и `loadbalancer_apiserver_localhost` взаимоисключающие.
- Для внешне управляемого (не Kubespray) LB TLS-терминацию Kubespray не обеспечивает; внешние VIP можно добавить в `supplementary_addresses_in_ssl_keys`, чтобы они попали в сертификаты кластера.

### etcd за внешним LB

Для L4/L7-балансировки etcd переопределяют в group_vars: `etcd_access_addresses`, `etcd_client_url`, `etcd_cert_alt_names`, `etcd_cert_alt_ips`.

## Требования к портам

Из `docs/operations/port-requirements.md`. Порты должны быть открыты между хостами; часть — опциональна в зависимости от конфигурации.

### Kubernetes — control plane

| Протокол | Порт  | Назначение              |
|----------|-------|-------------------------|
| TCP      | 22    | ssh для ansible         |
| TCP      | 2379  | etcd client port        |
| TCP      | 2380  | etcd peer port          |
| TCP      | 6443  | kubernetes api          |
| TCP      | 10250 | kubelet api             |
| TCP      | 10257 | kube-scheduler          |
| TCP      | 10259 | kube-controller-manager |

### Kubernetes — worker-узлы

| Протокол | Порт        | Назначение          |
|----------|-------------|---------------------|
| TCP      | 22          | ssh для ansible     |
| TCP      | 10250       | kubelet api         |
| TCP      | 30000-32767 | kube nodePort range |

### Calico (если используется)

| Протокол       | Порт  | Назначение                           |
|----------------|-------|--------------------------------------|
| TCP            | 179   | Calico networking (BGP)              |
| UDP            | 4789  | Calico CNI с включённым VXLAN        |
| TCP            | 5473  | Calico CNI с включённым Typha        |
| UDP            | 51820 | Calico с IPv4 Wireguard              |
| UDP            | 51821 | Calico с IPv6 Wireguard              |
| IPENCAP / IPIP | -     | Calico CNI с включённым IPIP         |

### Cilium (если используется)

| Протокол | Порт  | Назначение                          |
|----------|-------|-------------------------------------|
| TCP      | 4240  | Cilium health checks (cilium-health)|
| TCP      | 4244  | Hubble server                       |
| TCP      | 4245  | Hubble Relay                        |
| UDP      | 8472  | VXLAN overlay                       |
| TCP      | 9962  | Cilium-agent Prometheus metrics     |
| TCP      | 9963  | Cilium-operator Prometheus metrics  |
| TCP      | 9964  | Cilium-proxy Prometheus metrics     |
| UDP      | 51871 | WireGuard encryption tunnel endpoint|
| ICMP     | -     | health checks                       |

### Addons

| Протокол | Порт | Назначение                |
|----------|------|---------------------------|
| TCP      | 9100 | node exporter             |
| TCP/UDP  | 7472 | metallb metrics ports     |
| TCP/UDP  | 7946 | metallb L2 operating mode |

## Крупные развёртывания

Рекомендации из `docs/operations/large-deployments.md`:

- Настроить Ansible-параметры `forks` и `timeout` под большое число узлов (для 200 узлов — например `--forks=50`, `--timeout=600`).
- Переопределить `foo_image_repo` на внутренний registry.
- Включить `download_run_once: true` и/или `download_localhost: true`.
- Настроить глобальную переменную `retry_stagger` (для примера — `retry_stagger: 60`), чтобы дозировать нагрузку на delegate-узел (первый control-plane) при повторных загрузках/выгрузках.
- Тюнинг DNS: `dns_replicas`, `dns_cpu_limit`, `dns_cpu_requests`, `dns_memory_limit`, `dns_memory_requests` (limits >= requests).
- Тюнинг CPU/memory для ролей: `foo_memory_limit`, `foo_memory_requests`, `foo_cpu_limit`, `foo_cpu_requests`.
- Надёжность kubelet/кластера: `kubelet_status_update_frequency`, `kube_controller_node_monitor_grace_period`, `kube_controller_node_monitor_period`, `kube_apiserver_pod_eviction_not_ready_timeout_seconds`, `kube_apiserver_pod_eviction_unreachable_timeout_seconds`.
- Размеры сетевых префиксов: `kube_network_node_prefix`, `kube_service_addresses`, `kube_pods_subnet`.
- Добавить узлы `calico_rr` при использовании Calico/Canal — быстрее восстановление после сбоев сети.
- Вынести события etcd в отдельный инстанс: `etcd_events_cluster_setup: true`.

## Kubespray в сравнении с другими инструментами

Из `docs/getting_started/comparisons.md`:

- **vs Kops**: Kubespray работает на bare metal и большинстве облаков, используя Ansible для provisioning и оркестрации; Kops сам выполняет provisioning и жёстче привязан к особенностям облака.
- **vs Kubeadm**: Kubespray выполняет generic-конфигурацию OS, начальную кластеризацию (с сетевыми плагинами) и bootstrap control plane. Начиная с v2.3 Kubespray использует `kubeadm` внутренне для создания кластера.

## Интеграция в собственный ansible-репозиторий

Из `docs/operations/integration.md`: Kubespray можно подключить как git submodule в существующий ansible-репозиторий, добавить пути в `ansible.cfg` (`library`, `roles_path`), сопоставить свои группы инвентаря с именами Kubespray (`kube_node:children`, `etcd:children`, `kube_control_plane:children`) и импортировать `cluster.yml` через `import_playbook`. Форк держат синхронизированным с upstream; работу ведут в отдельной ветке (не в master форка).

## Источники

- `docs/getting_started/getting-started.md`
- `docs/getting_started/setting-up-your-first-cluster.md`
- `docs/getting_started/comparisons.md`
- `docs/ansible/ansible.md`
- `docs/ansible/inventory.md`
- `docs/ansible/vars.md`
- `docs/ansible/ansible_collection.md`
- `docs/operations/ha-mode.md`
- `docs/operations/integration.md`
- `docs/operations/port-requirements.md`
- `docs/operations/large-deployments.md`
- Тег: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0 (commit `f4ccdb5`)

Связанные заметки: [[versions/v2.30.0/ansible-tags|Ansible-теги]], [[versions/v2.30.0/variables/k8s-cluster|Переменные ядра]], [[versions/v2.30.0/README|Срез v2.30.0]]
