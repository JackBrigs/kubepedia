---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
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
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics: [installation, getting-started, ansible, ha]
reliability: authoritative
---

# Установка и базовая эксплуатация Kubespray v2.28.0

Дайджест по установке и первичной эксплуатации кластера, собранный строго из каталога `docs/` тега `v2.28.0` (commit `63cdf87`). Дословные команды, имена переменных и номера портов сохранены как в оригинале.

> Отличия от v2.29.1: (1) `docs/ansible/ansible.md` — команда `pip install -U -r requirements.txt` (с `-U`), таблица совместимости `>= 2.16.4 | 3.10-3.12`, пример docker-образа с тегом `v2.27.0`, в списке Ansible-тегов ещё присутствуют `master (DEPRECATED)` и `weave`, есть примечание про `bash scripts/gen_tags.sh`; (2) `docs/ansible/ansible_collection.md` содержит раздел «Requirements» (удалён в v2.29.1), шаги пронумерованы 1–4; (3) `docs/getting_started/setting-up-your-first-cluster.md` — туториал на Ubuntu Server **18.04** (`ubuntu-1804-lts`), firewall-правило явно включает `vxlan`. Файлы `getting-started.md`, `comparisons.md`, `inventory.md`, `ha-mode.md`, `port-requirements.md`, `large-deployments.md`, `integration.md` идентичны v2.29.1 (в `vars.md` — лишь опечатка `ipv6_stacke`, позже исправленная).

Связанные срезы базы: [[versions/v2.28.0/ansible-tags|Ansible-теги]], [[versions/v2.28.0/variables/k8s-cluster|Переменные ядра]], [[versions/v2.28.0/inventory/k8s-cluster|Inventory ядра]].

---

## 1. Требования и подготовка

### 1.1. Что нужно на управляющем хосте (ansible-хост)

- Окружение Linux или macOS с Python 3.
- Установленный Ansible из поставки Kubespray. Рекомендуется ставить его в отдельное python-виртуальное окружение.
- Клиент `kubectl` (опционально, для доступа к API).

Источник: `docs/getting_started/setting-up-your-first-cluster.md`, `docs/ansible/ansible.md`.

### 1.2. Установка Ansible

Kubespray поддерживает несколько версий Ansible и поставляет разные файлы `requirements.txt`. Выбор версии Ansible ограничен доступной версией Python.

Рекомендуемая установка в virtualenv:

```ShellSession
VENVDIR=kubespray-venv
KUBESPRAYDIR=kubespray
python3 -m venv $VENVDIR
source $VENVDIR/bin/activate
cd $KUBESPRAYDIR
pip install -U -r requirements.txt
```

Таблица совместимости Ansible и Python (из `docs/ansible/ansible.md` тега v2.28.0):

| Версия Ansible | Версия Python |
|----------------|---------------|
| >= 2.16.4      | 3.10-3.12     |

Если pip выдаёт ошибку `No matching distribution found for ansible==...` — версия Python несовместима с поддерживаемой Kubespray версией Ansible (например, для Python 3.8 и ниже максимум ставится ansible 6.7.0, а нужен минимум Python 3.9).

### 1.3. Альтернатива: готовый Docker-образ

Чтобы гарантированно получить корректные версии Ansible, коллекций и python-зависимостей, можно использовать готовый образ из Quay (`quay.io/kubespray/kubespray`). Инвентарь и SSH-ключ пробрасываются в контейнер через bind-mount:

```ShellSession
git checkout v2.27.0
docker pull quay.io/kubespray/kubespray:v2.27.0
docker run --rm -it --mount type=bind,source="$(pwd)"/inventory/sample,dst=/inventory \
  --mount type=bind,source="${HOME}"/.ssh/id_rsa,dst=/root/.ssh/id_rsa \
  quay.io/kubespray/kubespray:v2.27.0 bash
# внутри контейнера:
ansible-playbook -i /inventory/inventory.ini --private-key /root/.ssh/id_rsa cluster.yml
```

Примечание: в примере из документации тега v2.28.0 фигурирует тег образа `v2.27.0` (в v2.29.1 пример обновлён до `v2.29.0`).

### 1.4. Kubespray как Ansible collection

Kubespray можно установить как Ansible-коллекцию (`docs/ansible/ansible_collection.md`). В тексте тега v2.28.0 присутствует раздел **Requirements** (удалён в v2.29.1):

- инвентарь с нужными группами хостов (см. README);
- каталог `group_vars`, имена переменных в котором **должны** совпадать с переменными из `inventory/local/group_vars`.

Порядок использования (шаги 1–4 в v2.28.0):

1. добавить Kubespray в `requirements.yml` (тип `git`, поле `version` — нужный тег или ветка);
2. установить: `ansible-galaxy install -r requirements.yml`;
3. создать плейбук, импортирующий playbook Kubespray: `ansible.builtin.import_playbook: kubernetes_sigs.kubespray.cluster`;
4. обновить INVENTORY и PLAYBOOK и запустить: `ansible-playbook -i INVENTORY --become --become-user=root PLAYBOOK`.

### 1.5. Требования к SSH

Kubespray конфигурирует узлы по SSH. Нужно обеспечить SSH-доступ ansible-хоста ко всем узлам (порт 22). Если узлы недоступны напрямую (только приватные IP) — используется bastion-хост (см. раздел 2.3).

---

## 2. Структура inventory (группы хостов)

Источник: `docs/ansible/inventory.md`.

Инвентарь состоит из **3 основных групп**:

- **kube_node** — узлы Kubernetes, на которых запускаются pod'ы (worker-узлы).
- **kube_control_plane** — серверы control plane (apiserver, scheduler, controller).
- **etcd** — серверы кластера etcd. Для отказоустойчивости рекомендуется не менее 3 серверов.

Правила пересечения групп:

- если сервер входит и в `kube_control_plane`, и в `kube_node` — он совмещает роль control plane и рабочего узла;
- если сервер только в `kube_control_plane` (не в `kube_node`) — это standalone, непланируемый (unschedulable) control plane;
- если `etcd` пересекается с `kube_node` — узлы etcd становятся планируемыми для нагрузок Kubernetes; для standalone etcd группы не должны пересекаться.

Две **специальные группы**:

- **calico_rr** — узлы Calico route reflector (для продвинутых сценариев сети Calico);
- **bastion** — bastion-хост для доступа к узлам без прямой достижимости.

Группа **k8s_cluster** формируется **динамически** как объединение `kube_node`, `kube_control_plane` и `calico_rr`. Она используется внутренне и для задания переменных всего кластера через `<inventory>/group_vars/k8s_cluster/*.yml`.

### 2.1. Пример inventory (INI)

Инвентарь может храниться в трёх форматах: YAML, JSON или INI-подобном. Пример:

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

Переменная `ip` привязывает сервисы Kubernetes к конкретному IP, отличному от IP интерфейса по умолчанию.

### 2.2. Файлы group_vars

Основная настройка кластера ведётся через файлы group_vars (из `docs/getting_started/getting-started.md`):

- `inventory/mycluster/group_vars/all.yml` — для каждого узла, включая etcd;
- `inventory/mycluster/group_vars/k8s_cluster.yml` — для всех узлов кластера (не etcd, если он выделен отдельно);
- `inventory/mycluster/group_vars/kube_control_plane.yml` — для control plane;
- `inventory/mycluster/group_vars/kube_node.yml` — для worker-узлов.

Ключевые файлы туториала: `inventory/mycluster/group_vars/k8s_cluster/k8s_cluster.yml` (основная конфигурация, в т.ч. `kube_network_plugin`, `supplementary_addresses_in_ssl_keys`) и `inventory/mycluster/group_vars/k8s_cluster/addons.yml` (аддоны, например `metrics_server_enabled`).

### 2.3. Bastion-хост

Если узлы имеют только приватные IP, добавляется bastion (публичный IP заменяет `x.x.x.x`):

```ini
[bastion]
bastion ansible_host=x.x.x.x
```

### 2.4. Приоритет источников переменных

Из `docs/ansible/ansible.md`. Kubespray ожидает настройку через один из источников (по возрастанию приоритета):

| Слой | Комментарий |
|------|-------------|
| inventory group_vars | наиболее используемый |
| inventory host_vars | переопределения на уровне хоста |
| extra vars (`-e @foo.yml`) | всегда побеждают по приоритету |

**Важно:** extra vars стоит применять только для переопределения внутренних переменных Kubespray (`roles/vars/`), которые не являются частью публичного интерфейса и могут меняться без предупреждения. Подробнее о переменных — [[versions/v2.28.0/variables/k8s-cluster|Переменные ядра]] (источник `docs/ansible/vars.md`).

---

## 3. Основные способы запуска

Источники: `docs/getting_started/getting-started.md`, `docs/ansible/ansible.md`.

### 3.1. Установка кластера

```ShellSession
ansible-playbook -i inventory/mycluster/ cluster.yml -b -v \
  --private-key=~/.ssh/private_key
```

Флаг `-b` (become) — выполнение с повышением привилегий, `-v` — подробный вывод.

### 3.2. Добавление узлов (scale.yml)

Новый узел добавляется в нужную группу инвентаря, затем вместо `cluster.yml` запускается `scale.yml`:

```ShellSession
ansible-playbook -i inventory/mycluster/hosts.yml scale.yml -b -v \
  --private-key=~/.ssh/private_key
```

### 3.3. Удаление узлов (remove-node.yml)

Удаляемые узлы указываются через `--extra-vars`. Плейбук сначала drain'ит узлы, останавливает сервисы, удаляет сертификаты и выполняет `kubectl delete`:

```ShellSession
ansible-playbook -i inventory/mycluster/hosts.yml remove-node.yml -b -v \
--private-key=~/.ssh/private_key \
--extra-vars "node=nodename,nodename2"
```

Особенности:
- удаление **первого** control plane или etcd-узла не поддерживается — эти узлы должны оставаться;
- если узел недостижим по SSH — добавить `--extra-vars reset_nodes=false`, чтобы пропустить reset (можно задать `reset_nodes=false` как host var).

### 3.4. Сброс кластера (reset.yml)

Возврат VM в исходное состояние без удаления самих машин:

```ShellSession
ansible-playbook -i inventory/mycluster/ -u $USERNAME -b -v --private-key=~/.ssh/id_rsa reset.yml
```

### 3.5. Запуск по Ansible-тегам

Kubespray поддерживает выборочный запуск через `--tags` / `--skip-tags`. Полный справочник тегов и их поведения — [[versions/v2.28.0/ansible-tags|Ansible-теги]]. Примеры из `docs/ansible/ansible.md`:

Только DNS-конфигурация, без OS-настройки и загрузки образов:

```ShellSession
ansible-playbook -i inventory/sample/hosts.ini cluster.yml --tags preinstall,facts --skip-tags=download,bootstrap_os
```

Удаление IP DNS-резолвера кластера из `/etc/resolv.conf`:

```ShellSession
ansible-playbook -i inventory/sample/hosts.ini -e dns_mode='none' cluster.yml --tags resolvconf
```

Предзагрузка всех образов локально на ansible-хосте без установки/загрузки на узлы:

```ShellSession
ansible-playbook -i inventory/sample/hosts.ini cluster.yml \
    -e download_run_once=true -e download_localhost=true \
    --tags download --skip-tags upload,upgrade
```

Предупреждение из документации: использовать `--tags`/`--skip-tags` осознанно, только при полном понимании последствий.

Примечания по v2.28.0: в списке Ansible-тегов ещё присутствуют тег `master (DEPRECATED)` (в v2.29.1 удалён, вместо него `control-plane`) и тег `weave` (удалён в v2.29.1 вместе с CNI Weave); есть примечание, что список тегов можно сгенерировать командой `bash scripts/gen_tags.sh`. Поддержка **Mitogen** объявлена устаревшей (deprecated).

---

## 4. HA-режим (высокая доступность endpoint'ов)

Источник: `docs/operations/ha-mode.md`. Высокодоступные endpoint'ы требуются для двух компонентов: **кластера etcd** и **инстансов kube-apiserver**.

### 4.1. etcd

Клиенты etcd (kube-api-masters) конфигурируются со списком всех etcd-пиров. Если кластер etcd многоузловой — HA уже обеспечена.

### 4.2. kube-apiserver: два основных подхода

**A. Localhost loadbalancing (по умолчанию).** На каждом не-master узле работает nginx-прокси (localhost-балансировщик). Менее эффективен, чем выделенный LB (лишние health-check'и apiserver), но практичен без внешнего LB/VIP. Управляется переменной:

- `loadbalancer_apiserver_localhost` — по умолчанию `True` (или `False`, если задан внешний `loadbalancer_apiserver`);
- `loadbalancer_apiserver_port` — порт локального балансировщика, по умолчанию равен `kube_apiserver_port`;
- `loadbalancer_apiserver_pod_name` — имя контейнера балансировщика.

Kubespray настраивает kubelet и kube-proxy на использование локального балансировщика только на не-master узлах.

**B. Внешний loadbalancer (external LB).** Если локальный балансировщик отключён, для HA нужна роль [kube-vip](/docs/ingress/kube-vip.md) либо собственный внешний LB. Без них настраивается только не-HA endpoint, указывающий на `access_ip` (или IP первого узла в `kube_control_plane`).

Пример конфигурации внешнего HAProxy (управляется вне Kubespray):

```raw
listen kubernetes-apiserver-https
  bind <VIP>:8383
  mode tcp
  ...
  server master1 <IP1>:6443 check check-ssl verify none inter 10000
  server master2 <IP2>:6443 check check-ssl verify none inter 10000
  balance roundrobin
```

Соответствующие переменные для «cluster-aware» внешнего LB:

```yml
apiserver_loadbalancer_domain_name: "my-apiserver-lb.example.com"
loadbalancer_apiserver:
  address: <VIP>
  port: 8383
```

Важные замечания:
- apiserver по умолчанию слушает на всех интерфейсах, поэтому порт VIP должен отличаться от порта API, либо нужно задать `kube_apiserver_bind_address`;
- доменное имя (по умолчанию `lb-apiserver.kubernetes.local`) вписывается в `/etc/hosts` всех узлов группы `k8s_cluster` и в самоподписанные TLS-сертификаты;
- `loadbalancer_apiserver` и `loadbalancer_apiserver_localhost` **взаимоисключающие**;
- при использовании внешнего LB, не управляемого Kubespray, TLS-терминацию обеспечивает сам LB; дополнительные VIP можно внести в сертификаты через `supplementary_addresses_in_ssl_keys`.

Связанные адресные переменные (`docs/ansible/vars.md`): `loadbalancer_apiserver` (все хосты подключаются к этому адресу вместо localhost) и `loadbalancer_apiserver_localhost` (внутренний балансированный endpoint, взаимоисключающий с первым).

### 4.3. etcd за внешним LB

Для внешней балансировки etcd (L4/TCP или L7 с SSL Passthrough) переопределяются: `etcd_access_addresses`, `etcd_client_url`, `etcd_cert_alt_names`, `etcd_cert_alt_ips`.

---

## 5. Требования к портам

Источник: `docs/operations/port-requirements.md`. Если сеть закрыта firewall'ом, нужно открыть перечисленные порты между узлами. Часть портов опциональна и зависит от конфигурации.

### 5.1. Kubernetes — control plane

| Протокол | Порт  | Описание |
|----------|-------|----------|
| TCP | 22 | ssh для ansible |
| TCP | 2379 | etcd client port |
| TCP | 2380 | etcd peer port |
| TCP | 6443 | kubernetes api |
| TCP | 10250 | kubelet api |
| TCP | 10257 | kube-scheduler |
| TCP | 10259 | kube-controller-manager |

### 5.2. Kubernetes — worker-узлы

| Протокол | Порт | Описание |
|----------|------|----------|
| TCP | 22 | ssh для ansible |
| TCP | 10250 | kubelet api |
| TCP | 30000-32767 | диапазон kube nodePort |

### 5.3. Calico

| Протокол | Порт | Описание |
|----------|------|----------|
| TCP | 179 | Calico networking (BGP) |
| UDP | 4789 | Calico CNI с включённым VXLAN |
| TCP | 5473 | Calico CNI с включённым Typha |
| UDP | 51820 | Calico с IPv4 Wireguard |
| UDP | 51821 | Calico с IPv6 Wireguard |
| IPENCAP / IPIP | - | Calico CNI с включённым IPIP |

### 5.4. Cilium

| Протокол | Порт | Описание |
|----------|------|----------|
| TCP | 4240 | Cilium health checks (`cilium-health`) |
| TCP | 4244 | Hubble server |
| TCP | 4245 | Hubble Relay |
| UDP | 8472 | VXLAN overlay |
| TCP | 9962 | Cilium-agent Prometheus metrics |
| TCP | 9963 | Cilium-operator Prometheus metrics |
| TCP | 9964 | Cilium-proxy Prometheus metrics |
| UDP | 51871 | WireGuard encryption tunnel endpoint |
| ICMP | - | health checks |

### 5.5. Аддоны

| Протокол | Порт | Описание |
|----------|------|----------|
| TCP | 9100 | node exporter |
| TCP/UDP | 7472 | metallb metrics ports |
| TCP/UDP | 7946 | metallb L2 operating mode |

---

## 6. Особенности крупных развёртываний

Источник: `docs/operations/large-deployments.md`. При масштабных развёртываниях рекомендуется:

- настроить параметры Ansible `forks` и `timeout` под большое число узлов;
- переопределить переменные образов `foo_image_repo` на внутренний (intranet) registry;
- включить `download_run_once: true` и/или `download_localhost: true` (см. downloads);
- настроить глобальную переменную `retry_stagger` для разумной нагрузки на delegate-узел (первый control plane) при повторных попытках загрузки/выгрузки;
- настроить DNS-приложения: `dns_replicas`, `dns_cpu_limit`, `dns_cpu_requests`, `dns_memory_limit`, `dns_memory_requests` (limits >= requests);
- настроить CPU/memory limits и requests в defaults ролей (`foo_memory_limit`, `foo_memory_requests`, `foo_cpu_limit`, `foo_cpu_requests`);
- для надёжности настроить `kubelet_status_update_frequency`, `kube_controller_node_monitor_grace_period`, `kube_controller_node_monitor_period`, `kube_apiserver_pod_eviction_not_ready_timeout_seconds`, `kube_apiserver_pod_eviction_unreachable_timeout_seconds`;
- настроить размеры сетевых префиксов: `kube_network_node_prefix`, `kube_service_addresses`, `kube_pods_subnet`;
- добавить узлы `calico_rr` при использовании Calico/Canal (быстрее восстановление после сбоев сети);
- включить `etcd_events_cluster_setup: true` — хранение событий в отдельном выделенном инстансе etcd.

**Пример** для 200 узлов: `--forks=50`, `--timeout=600`, `retry_stagger: 60`.

---

## 7. Подключение к кластеру

Источник: `docs/getting_started/getting-started.md`.

- По умолчанию узлы `kube_control_plane` имеют небезопасный доступ к kube-apiserver через порт **8080** (localhost, kubeconfig не нужен — kubectl использует `http://localhost:8080`).
- Удалённое подключение возможно на любой IP любого узла `kube_control_plane` через порт **6443**, но требует аутентификации (kubeconfig).
- Kubeconfig на ansible-хост: `kubectl_localhost: true` (скачивает kubectl в `/usr/local/bin/` + скрипт `inventory/mycluster/artifacts/kubectl.sh`) и `kubeconfig_localhost: true` (кладёт `admin.conf` в `inventory/mycluster/artifacts/`). Каталог настраивается через `artifacts_dir`.

Замечание: в `admin.conf` имя контроллера может быть приватным IP — при внешнем доступе заменить на публичный IP или адрес LB.

### 7.1. Kubernetes Dashboard

Поддерживается kubernetes-dashboard v2.0.x. По умолчанию разворачивается в namespace `kube-system` (переопределяется `dashboard_namespace`), работает только по https. Proxy URL: `http://localhost:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/#/login`.

---

## 8. Сравнение с другими инструментами

Источник: `docs/getting_started/comparisons.md`.

- **Kubespray vs Kops:** Kubespray работает на bare metal и большинстве облаков, используя Ansible; Kops сам выполняет provisioning и жёстче интегрирован с конкретным облаком. Kubespray предпочтителен при работе с несколькими платформами и наличии Ansible-опыта.
- **Kubespray vs Kubeadm:** Kubespray выполняет generic-настройку ОС + начальный bootstrap кластера (с сетевыми плагинами) и с версии **v2.3** внутренне использует `kubeadm` для создания кластера.

---

## 9. Пошаговый пример (туториал)

Источник: `docs/getting_started/setting-up-your-first-cluster.md` — прикладной пошаговый гайд по развёртыванию первого кластера на Google Cloud Platform (3 controller + 3 worker). Ключевые шаги:

1. подготовка инфраструктуры GCP (VPC `kubernetes-the-kubespray-way`, subnet `10.240.0.0/24`, firewall для internal и external доступа: `tcp:80,tcp:6443,tcp:443,tcp:22,icmp`); важно разрешить vxlan для работы Calico — в примере тега v2.28.0 internal-правило задаётся как `--allow tcp,udp,icmp,vxlan` (в v2.29.1 — `tcp,udp,icmp`);
2. создание 3 controller и 3 worker инстансов на **Ubuntu Server 18.04** (`--image-family ubuntu-1804-lts`, `--image-project ubuntu-os-cloud`), настройка SSH-доступа;
3. подготовка Kubespray в virtualenv, `cp -rfp inventory/sample inventory/mycluster`, правка `inventory.ini` (controller-* в `kube_control_plane`, worker-* в `kube_node`, задать `ip`);
4. правка `group_vars/k8s_cluster/k8s_cluster.yml` (`supplementary_addresses_in_ssl_keys` с IP контроллеров для внешнего доступа к API; `kube_network_plugin` по умолчанию `calico`) и `addons.yml` (`metrics_server_enabled`);
5. запуск: `ansible-playbook -i inventory/mycluster/ -u $USERNAME -b -v --private-key=~/.ssh/id_rsa cluster.yml` (до ~20 минут);
6. доступ к кластеру: копирование `/etc/kubernetes/admin.conf` с контроллера, подмена server-IP на внешний, `export KUBECONFIG=...`, `kubectl get nodes`;
7. smoke-тесты: `kubectl top nodes` (метрики), проверка сети между pod'ами (busybox ping), deployment nginx, port-forward, NodePort, DNS между namespace'ами;
8. очистка: `kubectl delete ...`, `reset.yml`, удаление инстансов/сети GCP.

Примечание: команды туториала используют `git checkout release-2.17` и образы с K8s v1.17.9 — это исторический пример из документации, а не версии, поставляемые тегом v2.28.0. Актуальные версии компонентов — см. [[versions/v2.28.0/components|Компоненты v2.28.0]].

---

## Источники

Все файлы — из каталога `docs/` тега `v2.28.0` (commit `63cdf87`):

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

Назад: [[versions/v2.28.0/README|Срез v2.28.0]]
