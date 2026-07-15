---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
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
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - installation
  - getting-started
  - ansible
  - ha
reliability: authoritative
---

# Установка Kubespray v2.31.0

Дайджест документации `docs/` тега v2.31.0 по установке кластера: Ansible-окружение, инвентарь, запуск, HA, порты, крупные развёртывания. Связанные заметки: [[versions/v2.31.0/ansible-tags|Ansible-теги]], [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]], [[versions/v2.31.0/README|Срез v2.31.0]].

## Установка Ansible (docs/ansible/ansible.md)

- Kubespray поддерживает несколько версий Ansible и поставляет разные `requirements.txt`. Рекомендуется ставить в отдельный Python virtualenv.
- Порядок установки:

```ShellSession
VENVDIR=kubespray-venv
KUBESPRAYDIR=kubespray
python3 -m venv $VENVDIR
source $VENVDIR/bin/activate
cd $KUBESPRAYDIR
pip install -r requirements.txt
```

- Совместимость версий (единственная строка таблицы в этом теге): Ansible `>=2.18.0, <2.19.0` требует Python `3.11-3.13`. Если pip не находит нужную версию Ansible — версия Python несовместима.
- Kubespray поставляет собственные модули; если Ansible их не находит, указать `export ANSIBLE_LIBRARY=<kubespray_dir>/library`.

### Готовый Docker-образ (альтернатива venv)

Гарантированно правильные версии — образ из Quay. Пример (в доке приведён на v2.30.0, применимо аналогично к нужному тегу):

```ShellSession
git checkout v2.30.0
docker pull quay.io/kubespray/kubespray:v2.30.0
docker run --rm -it --mount type=bind,source="$(pwd)"/inventory/sample,dst=/inventory \
  --mount type=bind,source="${HOME}"/.ssh/id_rsa,dst=/root/.ssh/id_rsa \
  quay.io/kubespray/kubespray:v2.30.0 bash
ansible-playbook -i /inventory/inventory.ini --private-key /root/.ssh/id_rsa cluster.yml
```

## Источники переменных и приоритет (docs/ansible/ansible.md, vars.md)

Kubespray ожидает настройку через один из источников (приоритет по возрастанию):

| Слой | Комментарий |
|------|-------------|
| inventory group_vars | самый используемый |
| inventory host_vars | переопределения на уровне хоста |
| extra vars (`-e @foo.yml`) | всегда выигрывают приоритет |

- Extra vars предназначены для переопределения внутренних переменных Kubespray (`roles/vars/`), которые **не являются частью интерфейса** и могут меняться/исчезать без предупреждения.
- Ключевые «общие» переменные версий компонентов: `docker_version`, `docker_containerd_version` (при `container_manager: docker`), `containerd_version` (при `container_manager: containerd`), `kube_version`, `etcd_version`, `calico_version`, `calico_cni_version`, `flannel_version`.
- Сетевые: `kube_network_plugin` (по умолчанию Calico), `kube_proxy_mode` (iptables/ipvs/nftables), `kube_service_addresses` (по умолчанию `10.233.0.0/18`), `kube_pods_subnet` (по умолчанию `10.233.64.0/18`), `kube_network_node_prefix`, `skydns_server` (`10.233.0.3`), `dns_domain`/`cluster_name` (по умолчанию `cluster.local`), `container_manager` (по умолчанию `containerd`).
- Адресация хостов: `ip` (обычно публичный, для привязки сервисов), `access_ip` (обычно приватный, для доступа с других хостов), `ip6`/`access_ip6` для IPv6. При неопределённости используются факты `ansible_default_ipv4.address`.
- Dual Stack: `ipv4_stack` (по умолчанию `true`), `ipv6_stack` (по умолчанию `false`). Оба `true` — dual stack (приоритет у IPv4). Можно сделать IPv6-only, задав `ipv4_stack: false`. Переменная `enable_dual_stack_networks` устарела.
- Подробный разбор переменных ядра — в [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]].

## Инвентарь (docs/ansible/inventory.md)

Инвентарь состоит из 3 групп:

- **kube_node** — узлы, где запускаются pod'ы;
- **kube_control_plane** — узлы control plane (apiserver, scheduler, controller);
- **etcd** — узлы etcd (рекомендуется минимум 3 для отказоустойчивости).

Правила пересечения групп:
- если `kube_node` содержит узлы `etcd` — etcd будет schedulable для нагрузок;
- узел может быть одновременно в `kube_control_plane` и `kube_node`; unschedulable control plane — только в `kube_control_plane`.

Специальные группы: **calico_rr** (route reflector для Calico), **bastion** (хост-бастион для узлов без прямого доступа). Группа **k8s_cluster** формируется динамически как объединение `kube_node` + `kube_control_plane` + `calico_rr` и используется для общекластерных переменных `<inventory>/group_vars/k8s_cluster/*.yml`.

Форматы инвентаря: YAML, JSON или INI-подобный. Пример INI с привязкой сервисов на отдельный IP через `ip=`:

```ini
node1 ansible_host=95.54.0.12 ip=10.3.0.1
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
```

Бастион добавляется строкой `bastion ansible_host=x.x.x.x` в группе `[bastion]`.

## Сборка своего инвентаря и запуск (docs/getting_started/getting-started.md)

Каталоги group_vars, которые редактируются под кластер:
- `group_vars/all.yml` — для всех узлов, включая etcd;
- `group_vars/k8s_cluster.yml` — для всех узлов кластера (кроме отдельного etcd);
- `group_vars/kube_control_plane.yml` — control plane;
- `group_vars/kube_node.yml` — worker'ы.

Установка кластера:

```ShellSession
ansible-playbook -i inventory/mycluster/ cluster.yml -b -v --private-key=~/.ssh/private_key
```

- Добавление узлов: тот же `cluster.yml` либо `scale.yml` (минимально необходимое для установки kubelet на worker'е). Подробнее — [[versions/v2.31.0/docs/nodes|Узлы и восстановление]].
- Удаление узлов: `remove-node.yml` с `--extra-vars "node=<nodename>,<nodename2>"`. Для недостижимого по SSH узла добавить `reset_nodes=false`. Первый control plane или etcd-узел удалить нельзя.

### Подключение к API (getting-started.md)

- По умолчанию kube_control_plane настроены с небезопасным доступом к kube-apiserver через порт **8080** (kubectl на самом control plane использует `http://localhost:8080`, kubeconfig не нужен).
- Удалённо API доступен на любом IP любого kube_control_plane на порту **6443** (требует аутентификации).
- Получение kubeconfig на ansible-хост: `kubectl_localhost: true` (скачивает kubectl в `/usr/local/bin/` + bash completion + скрипт `inventory/mycluster/artifacts/kubectl.sh`) и `kubeconfig_localhost: true` (кладёт `admin.conf` в `inventory/mycluster/artifacts/`). Каталог задаётся `artifacts_dir`.

## Пошаговый пример на GCP (docs/getting_started/setting-up-your-first-cluster.md)

Прикладной гайд «первый кластер» на Google Cloud Platform (аналог Kubernetes The Hard Way, но через Kubespray). Ключевые моменты:
- 3 контроллера + 3 worker'а на Ubuntu Server 24.04 (`e2-standard-2`, boot-disk 200GB, `--can-ip-forward`), приватная сеть `10.240.0.0/24`.
- Firewall: внутренний трафик разрешает `tcp,udp,icmp` (vxlan/udp обязателен для Calico); внешний — `tcp:80,tcp:6443,tcp:443,tcp:22,icmp`.
- Kubespray в venv, `pip install -r requirements.txt`, `cp -rfp inventory/sample inventory/mycluster`.
- В `group_vars/k8s_cluster/k8s_cluster.yml` задать `supplementary_addresses_in_ssl_keys` (IP контроллеров) для доступа к API извне VPC; `kube_network_plugin` по умолчанию `calico`.
- Аддоны включаются в `group_vars/k8s_cluster/addons.yml` (пример: `metrics_server_enabled: true`).
- Запуск: `ansible-playbook -i inventory/mycluster/ -u $USERNAME -b -v --private-key=~/.ssh/id_rsa cluster.yml` (до ~20 минут).
- Сброс состояния кластера без удаления VM — `reset.yml`.

> Примечание: в тексте гайда встречается устаревший `git checkout release-2.17` и вывод старых версий K8s (v1.17.9) — это иллюстративные артефакты документа, не относящиеся к v2.31.0.

## Kubespray как Ansible-коллекция (docs/ansible/ansible_collection.md)

Установка через `ansible-galaxy`:
1. Настроить инвентарь и group vars.
2. В `requirements.yml`:

```yaml
collections:
- name: https://github.com/kubernetes-sigs/kubespray
  type: git
  version: master # использовать нужный тег/ветку
```

3. `ansible-galaxy install -r requirements.yml`.
4. Плейбук: `ansible.builtin.import_playbook: kubernetes_sigs.kubespray.cluster`.
5. `ansible-playbook -i INVENTORY --become --become-user=root PLAYBOOK`.

## Kubespray внутри своего репозитория плейбуков (docs/operations/integration.md)

Интеграция форка Kubespray как git submodule в существующий Ansible-репозиторий:
- `git submodule add https://github.com/YOUR_GITHUB/kubespray.git kubespray`; форк добавить как `upstream`, работать в отдельной ветке (не в master форка).
- В `ansible.cfg` расширить пути: `library = ./library/:3d/kubespray/library/`, `roles_path = ./roles/:3d/kubespray/roles/`.
- Смапить свои inventory-группы на группы Kubespray (`kube_node`, `etcd`, `kube_control_plane` через `:children`).
- Подключить: `ansible.builtin.import_playbook: 3d/kubespray/cluster.yml`.
- Контрибьютинг обратно в upstream: подпись CNCF CLA, cherry-pick коммитов в fix-ветку, squash, PR.

## HA (высокая доступность) API-эндпоинтов (docs/operations/ha-mode.md)

HA-эндпоинты нужны для etcd и kube-apiserver.

- **etcd**: клиенты (kube-api-masters) знают список всех peer'ов etcd; при нескольких инстансах HA обеспечивается автоматически.
- **kube-apiserver**: балансировщик через reverse proxy. Kubespray включает nginx-based localhost-балансировщик на каждом не-master узле (localhost loadbalancing). Управляется `loadbalancer_apiserver_localhost` (по умолчанию `True`; `False` при заданном внешнем `loadbalancer_apiserver`). Порт локального LB — `loadbalancer_apiserver_port` (по умолчанию = `kube_apiserver_port`). Имя контейнера LB — `loadbalancer_apiserver_pod_name`.
- Если localhost-LB не используется — либо роль [kube-vip], либо собственный внешний LB. По умолчанию (без LB) — не-HA эндпоинт на `access_ip`/IP первого узла `kube_control_plane`.
- Внешний LB: задать `apiserver_loadbalancer_domain_name`, `loadbalancer_apiserver: {address, port}`. Домен (или дефолтный `lb-apiserver.kubernetes.local`) вписывается в `/etc/hosts` всех узлов `k8s_cluster` и в самоподписанные TLS-сертификаты. Порт VIP должен отличаться от порта, на котором слушает API, либо задать `kube_apiserver_bind_address`.
- `loadbalancer_apiserver` и `loadbalancer_apiserver_localhost` взаимоисключающи.
- Внешние VIP можно добавить в сертификаты через `supplementary_addresses_in_ssl_keys`.
- etcd за внешним LB: переопределить `etcd_access_addresses`, `etcd_client_url`, `etcd_cert_alt_names`, `etcd_cert_alt_ips`.

## Требования к портам (docs/operations/port-requirements.md)

### Control plane

| Протокол | Порт | Назначение |
|----------|------|-----------|
| TCP | 22 | ssh для ansible |
| TCP | 2379 | etcd client |
| TCP | 2380 | etcd peer |
| TCP | 6443 | kubernetes api |
| TCP | 10250 | kubelet api |
| TCP | 10257 | kube-scheduler |
| TCP | 10259 | kube-controller-manager |

### Worker

| Протокол | Порт | Назначение |
|----------|------|-----------|
| TCP | 22 | ssh для ansible |
| TCP | 10250 | kubelet api |
| TCP | 30000-32767 | диапазон NodePort |

### Calico

| Протокол | Порт | Назначение |
|----------|------|-----------|
| TCP | 179 | BGP |
| UDP | 4789 | VXLAN |
| TCP | 5473 | Typha |
| UDP | 51820 | IPv4 WireGuard |
| UDP | 51821 | IPv6 WireGuard |
| IPENCAP/IPIP | - | режим IPIP |

### Cilium

| Протокол | Порт | Назначение |
|----------|------|-----------|
| TCP | 4240 | cilium-health |
| TCP | 4244 | Hubble server |
| TCP | 4245 | Hubble Relay |
| UDP | 8472 | VXLAN overlay |
| TCP | 9962 | метрики cilium-agent |
| TCP | 9963 | метрики cilium-operator |
| TCP | 9964 | метрики cilium-proxy |
| UDP | 51871 | WireGuard tunnel |
| ICMP | - | health checks |

### Аддоны

| Протокол | Порт | Назначение |
|----------|------|-----------|
| TCP | 9100 | node exporter |
| TCP/UDP | 7472 | метрики metallb |
| TCP/UDP | 7946 | metallb L2 |

## Крупные развёртывания (docs/operations/large-deployments.md)

Рекомендации для больших кластеров:
- Ansible: увеличить `forks` и `timeout` (пример для 200 узлов: `--forks=50`, `--timeout=600`, `retry_stagger: 60`).
- Локальный registry: переопределить `foo_image_repo`; включить `download_run_once: true` и/или `download_localhost: true`.
- Настроить `retry_stagger` (нагрузка на delegate — первый control plane при повторных download/push).
- DNS: `dns_replicas`, `dns_cpu_limit`, `dns_cpu_requests`, `dns_memory_limit`, `dns_memory_requests` (limits >= requests).
- Лимиты/реквесты CPU/памяти: `foo_memory_limit`, `foo_memory_requests`, `foo_cpu_limit`, `foo_cpu_requests`.
- Надёжность kubelet: `kubelet_status_update_frequency`, `kube_controller_node_monitor_grace_period`, `kube_controller_node_monitor_period`, `kube_apiserver_pod_eviction_not_ready_timeout_seconds`, `kube_apiserver_pod_eviction_unreachable_timeout_seconds`.
- Сетевые префиксы: `kube_network_node_prefix`, `kube_service_addresses`, `kube_pods_subnet`.
- Добавлять `calico_rr` узлы для Calico/Canal (быстрее восстановление после сбоев сети).
- Отдельный etcd для событий: `etcd_events_cluster_setup: true`.

## Сравнение с альтернативами (docs/getting_started/comparisons.md)

- **vs Kops**: Kubespray работает на bare metal и большинстве облаков, использует Ansible; Kops сам провижинит инфраструктуру и жёстче интегрирован с конкретным облаком (лучше для одной платформы).
- **vs Kubeadm**: Kubespray выполняет generic OS-конфигурацию (мир «OS operators» Ansible) + начальную кластеризацию с CNI + bootstrap control plane. С v2.3 Kubespray использует `kubeadm` внутри для создания кластера.

## Пример запуска по Ansible-тегам (docs/ansible/ansible.md)

Полный справочник тегов запуска — [[versions/v2.31.0/ansible-tags|Ansible-теги]]. Примеры из документа:

```ShellSession
# только DNS-конфигурация, без download и bootstrap_os
ansible-playbook -i inventory/sample/hosts.ini cluster.yml --tags preinstall,facts --skip-tags=download,bootstrap_os

# удалить IP DNS-резолвера кластера из /etc/resolv.conf
ansible-playbook -i inventory/sample/hosts.ini -e dns_mode='none' cluster.yml --tags resolvconf

# подготовить образы локально на ansible-раннере, без установки/аплоада
ansible-playbook -i inventory/sample/hosts.ini cluster.yml \
    -e download_run_once=true -e download_localhost=true \
    --tags download --skip-tags upload,upgrade
```

## Источники

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
- [[versions/v2.31.0/README|Срез v2.31.0]]
