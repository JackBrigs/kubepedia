---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: code
source_path: versions/v2.29.0/ansible-tags.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics:
  - ansible-tags
  - playbooks
  - run-tags
reliability: authoritative
---

# Ansible-теги запуска Kubespray v2.29.0

Справочник тегов, которые передаются в `ansible-playbook ... --tags` / `--skip-tags`. **Это не Git-теги версий** — здесь речь о тегах задач и ролей внутри плейбуков Kubespray. Источник истины — парный файл `ansible-tags.yaml`; ниже — человекочитаемый обзор.

- **Всего тегов в v2.29.0:** 124 (извлечены из `playbooks/*.yml` и `roles/*/tasks/**`, полнота сверена программно).
- **Безопасность изолированного запуска (`standalone_run`):** safe — 53, risky — 64, unsafe — 7.
- Колонка «Изолированно» ниже: **safe** — можно запускать отдельным `--tags`; **risky** — как правило требует `download` и/или фактов с других узлов, живого control plane; **unsafe** — деструктивно или бессмысленно вне своего сценария.

## Как пользоваться

```bash
# только преднастройка узлов, без скачивания
ansible-playbook -i inventory/hosts.yaml cluster.yml --tags preinstall --skip-tags download
# развернуть/обновить только etcd
ansible-playbook -i inventory/hosts.yaml cluster.yml --tags etcd
```

> ⚠️ **Ловушка узкого `--tags`.** Роль `kubespray_defaults` подключается в плеях **без тега** и потому НЕ входит в `always`. При очень узком `--tags` её переменные могут не задаться, и задачи выбранного тега получат неполный контекст. Учитывайте это при точечных запусках.


## Базовые / подготовка узлов

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `always` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Специальный тег Ansible: задачи и плеи, помеченные always, выполняются при любом запуске независимо от --tags/--skip-tags (отменить можно только явным --skip… |
| `annotate` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Проставляет аннотации узлам для сетевого плагина kube-router. |
| `asserts` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Проверочные (assert) задачи без изменений на узлах. |
| `bastion` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Настраивает SSH-конфигурацию для прыжкового узла (bastion). |
| `bootstrap_os` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | risky | Всё, что связано с первичной подготовкой ОС узлов. |
| `check` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Предварительные проверки окружения управляющей машины/узлов: соответствие версии Ansible диапазону (minimal_ansible_version <= v < maximal_ansible_version),… |
| `dns` | reset.yml, remove-node.yml | risky | Удаление DNS-настроек при сбросе узла (роль reset). |
| `download` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Загрузка бинарников и container-образов ролью download: подготовка каталогов и переменных (prep_download), получение kubeadm и списка нужных образов, скачива… |
| `facts` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Сбор фактов и вычисление производных переменных без изменений на узлах. |
| `files` | reset.yml, remove-node.yml | unsafe | Удаление файлов и каталогов при сбросе узла (роль reset). |
| `init` | cluster.yml, upgrade-cluster.yml | risky | Инициализация для Windows-узлов (роль win_nodes/kubernetes_patch, hosts kube_control_plane[0]). |
| `ip6tables` | reset.yml, remove-node.yml | risky | Сброс правил IPv6-фаервола при reset. |
| `iptables` | reset.yml, remove-node.yml | risky | Сброс правил IPv4-фаервола при reset. |
| `localhost` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Особые шаги, выполняемые на управляющей машине (ansible runner) и делегатах. |
| `mounts` | reset.yml, remove-node.yml | risky | Размонтирование каталогов kubelet при сбросе узла (роль reset). |
| `preinstall` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Предварительная подготовка узлов ролью kubernetes/preinstall: отключение swap, вычисление фактов (0020-set_facts), проверка настроек (0040-verify-settings),… |
| `resolvconf` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml | safe | Настройка /etc/resolv.conf (и systemd-resolved/NetworkManager DNS) для узлов и подов. |
| `services` | reset.yml, remove-node.yml | unsafe | Остановка и удаление systemd-сервисов при сбросе узла (роль reset). |
| `system-packages` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | risky | Установка системных пакетов через пакетный менеджер ОС. |
| `system-upgrade` | upgrade-cluster.yml | risky | Обновление системных пакетов ОС в ходе апгрейда кластера (роль upgrade/system-upgrade). |
| `system-upgrade-apt` | upgrade-cluster.yml | risky | Ветка обновления системных пакетов для Debian-семейства внутри роли upgrade/system-upgrade. |
| `system-upgrade-yum` | upgrade-cluster.yml | risky | Ветка обновления системных пакетов для RedHat-семейства внутри роли upgrade/system-upgrade. |
| `upload` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Распространение образов/бинарников по узлам кластера в рамках роли download. |
| `win_nodes` | cluster.yml, upgrade-cluster.yml | risky | Специфичные для Windows задачи (роль win_nodes/kubernetes_patch, hosts kube_control_plane[0]). |

## Control plane / узлы / etcd / жизненный цикл

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `client` | cluster.yml, upgrade-cluster.yml | safe | Запускает роль kubernetes/client на узлах контрол-плейна (тег навешен на роль на уровне плейбука, внутренних тегов у роли нет — выполняется вся роль). |
| `control-plane` | cluster.yml | risky | Основной тег развёртывания/переконфигурации роли контрол-плейна в cluster.yml. |
| `etcd` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Тег уровня роли etcd (навешен на роль целиком в install_etcd.yml и scale.yml). |
| `etcd-secrets` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Управляет сертификатами и ключами etcd. |
| `etcd_metrics` | cluster.yml, upgrade-cluster.yml | risky | Публикует Endpoints и Service для сбора метрик etcd. |
| `etcdctl` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Устанавливает клиентские утилиты etcd. |
| `etcdutl` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Полный синоним etcdctl по коду: тот же import_role etcdctl_etcdutl в roles/etcd/tasks/main.yml и roles/kubernetes/control-plane/tasks/kubeadm-etcd.yml помече… |
| `haproxy` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Разворачивает локальный балансировщик apiserver на базе HAProxy. |
| `k8s-pre-upgrade` | cluster.yml, upgrade-cluster.yml | risky | Предобновление контрол-плейна. |
| `kube-apiserver` | cluster.yml, upgrade-cluster.yml | risky | Вопреки названию тега («Configuring static pod kube-apiserver» в docs) по коду тег не разворачивает сам под apiserver (это делает kubeadm). |
| `kube-controller-manager` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | По коду тег навешен только на задачи создания каталогов Kubernetes в roles/kubernetes/preinstall/0050-create_directories.yml (kube_config_dir, kube_manifest_… |
| `kube-vip` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Устанавливает kube-vip для виртуального IP/балансировки apiserver на узлах контрол-плейна. |
| `kubeadm` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Собирает всё, что связано с kubeadm-присоединением узлов и конфигурацией kubelet. |
| `kubeadm_token` | cluster.yml, upgrade-cluster.yml | unsafe | Управляет bootstrap-токенами kubeadm для присоединения узлов. |
| `kubectl` | cluster.yml, upgrade-cluster.yml | safe | Устанавливает и настраивает kubectl на узлах контрол-плейна. |
| `kubelet` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Полностью настраивает сервис kubelet. |
| `master` | upgrade-cluster.yml | risky | Легаси-синоним control-plane для сценария обновления. |
| `nginx` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Разворачивает локальный nginx-прокси (LB) к apiserver'ам на узлах, не являющихся контрол-плейном. |
| `node` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Тег уровня роли kubernetes/node — конфигурация compute-узла. |
| `node-label` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Проставляет метки узлам. |
| `node-taint` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Проставляет тейнты узлам. |
| `node-webhook` | cluster.yml, upgrade-cluster.yml | risky | Очистка устаревших RBAC-объектов веб-хука регистрации узлов. |
| `post-remove` | remove-node.yml | unsafe | Финальная стадия удаления узла. |
| `post-upgrade` | upgrade-cluster.yml | risky | Пост-обработка после обновления узла. |
| `pre-remove` | remove-node.yml | risky | Подготовка узла к удалению/смене рантайма. |
| `pre-upgrade` | upgrade-cluster.yml | risky | Подготовка узла к обновлению. |
| `reset` | reset.yml, remove-node.yml | unsafe | Полный сброс состояния Kubernetes на узле. |
| `upgrade` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Сквозной тег обновления бинарей/образов и очистки легаси-аддонов. |

## Контейнерные движки

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `container-engine` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Зонтичный тег роли roles/container-engine (подключается через roles/container-engine/meta/main.yml). |
| `container-runtimes` | cluster.yml, upgrade-cluster.yml | risky | Применяет объекты RuntimeClass для включённых низкоуровневых рантаймов на control plane. |
| `container_engine_accelerator` | cluster.yml, upgrade-cluster.yml | risky | Зонтичный тег роли roles/kubernetes-apps/container_engine_accelerator, которая при nvidia_accelerator_enabled подключает подроль nvidia_gpu. |
| `containerd` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает и настраивает движок containerd на узлах (roles/container-engine/containerd). |
| `crio` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает и настраивает движок CRI-O на узлах (roles/container-engine/cri-o). |
| `crun` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает низкоуровневый OCI-рантайм crun. |
| `docker` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает движок Docker и его CRI-обёртку. |
| `gvisor` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает песочничный рантайм gVisor. |
| `kata-containers` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает низкоуровневый рантайм Kata Containers в двух местах. |
| `nvidia_gpu` | cluster.yml, upgrade-cluster.yml | risky | Тег подроли roles/kubernetes-apps/container_engine_accelerator/nvidia_gpu. |
| `reset_containerd` | cluster.yml, scale.yml, upgrade-cluster.yml | unsafe | Теардаун-задачи containerd (roles/container-engine/containerd/tasks/reset.yml): останавливают и отключают сервис containerd и удаляют его артефакты — /etc/sy… |
| `reset_crio` | cluster.yml, scale.yml, upgrade-cluster.yml | unsafe | Теардаун-задачи CRI-O (roles/container-engine/cri-o/tasks/reset.yml): удаляют apt/yum-репозитории CRI-O, чистят метаданные yum, удаляют crictl и /etc/crictl.… |
| `validate-container-engine` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Первый шаг роли container-engine (roles/container-engine/validate-container-engine). |
| `youki` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает низкоуровневый OCI-рантайм youki. |

## Сеть / CNI / DNS

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `calico` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Calico (роль network_plugin/calico, подключается при kube_network_plugin == 'calico'). |
| `calico_rr` | cluster.yml | risky | Настраивает Calico Route Reflector: в cluster.yml для группы calico_rr подключается роль network_plugin/calico/rr с тегами ['network', 'calico_rr']. |
| `cilium` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Cilium. |
| `cni` | cluster.yml, upgrade-cluster.yml | safe | ВНИМАНИЕ: по коду тега (приоритет у кода над docs/ansible/ansible.md, где тег описан как «CNI plugins for Network Plugins») тег cni в v2.29.0 навешан единств… |
| `coredns` | cluster.yml, upgrade-cluster.yml | risky | Разворачивает/обновляет кластерный DNS CoreDNS. |
| `custom_cni` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает пользовательский CNI (роль network_plugin/custom_cni, kube_network_plugin == 'custom_cni'). |
| `flannel` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Flannel (роль network_plugin/flannel, подключается при kube_network_plugin == 'flannel'). |
| `kube-ovn` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Kube-OVN (роль network_plugin/kube-ovn, подключается при kube_network_plugin == 'kube-ovn'). |
| `kube-proxy` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Конфигурирует kube-proxy и связанные с ним параметры узлов. |
| `kube-router` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин kube-router (роль network_plugin/kube-router, подключается при kube_network_plugin == 'kube-router'). |
| `macvlan` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин macvlan (роль network_plugin/macvlan, подключается при kube_network_plugin == 'macvlan'). |
| `multus` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает Multus — метаплагин для нескольких сетевых интерфейсов у подов (роль network_plugin/multus). |
| `netchecker` | cluster.yml, upgrade-cluster.yml | risky | Устанавливает приложение Netchecker для проверки сетевой связности между подами. |
| `network` | cluster.yml, scale.yml, upgrade-cluster.yml, reset.yml | risky | Сквозной тег конфигурирования сети кластера. |
| `nodelocaldns` | cluster.yml, upgrade-cluster.yml | risky | Разворачивает DaemonSet NodeLocal DNSCache. |

## Приложения (kubernetes-apps)

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `apps` | cluster.yml, upgrade_cluster.yml | risky | Сквозной тег для развёртывания прикладных дополнений кластера (роль kubernetes-apps в плейбуке "Install Kubernetes apps"). |
| `argocd` | cluster.yml, upgrade_cluster.yml | risky | Разворачивает Argo CD (роль kubernetes-apps/argocd). |
| `cert-manager` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает cert-manager (роль kubernetes-apps/ingress_controller/cert_manager). |
| `cluster-roles` | cluster.yml, upgrade_cluster.yml | safe | Роль kubernetes-apps/cluster_roles: базовая RBAC-настройка кластера. |
| `dashboard` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает Kubernetes Dashboard (задача "Kubernetes Apps \| Dashboard" в роли kubernetes-apps/ansible). |
| `gateway_api` | cluster.yml | safe | Устанавливает CRD Gateway API (роль kubernetes-apps/common_crds/gateway_api). |
| `helm` | cluster.yml, upgrade_cluster.yml | safe | Устанавливает клиент Helm на узлы control-plane (роль kubernetes-apps/helm). |
| `ingress-controller` | cluster.yml, upgrade_cluster.yml | safe | Составной тег роли kubernetes-apps/ingress_controller. |
| `ingress-nginx` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает NGINX Ingress Controller (роль kubernetes-apps/ingress_controller/ingress_nginx). |
| `ingress_alb` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает AWS ALB Ingress Controller (роль kubernetes-apps/ingress_controller/alb_ingress_controller). |
| `kubelet-csr-approver` | cluster.yml, upgrade_cluster.yml | risky | Устанавливает kubelet-csr-approver (роль kubernetes-apps/kubelet-csr-approver). |
| `metallb` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает балансировщик MetalLB (роль kubernetes-apps/metallb). |
| `metrics_server` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает Kubernetes Metrics Server (роль kubernetes-apps/metrics_server). |
| `node_feature_discovery` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает Node Feature Discovery (роль kubernetes-apps/node_feature_discovery). |
| `policy-controller` | cluster.yml, upgrade_cluster.yml | safe | Роль kubernetes-apps/policy_controller. |
| `prometheus_operator_crds` | cluster.yml | safe | Устанавливает CRD Prometheus Operator (роль kubernetes-apps/common_crds/prometheus_operator_crds). |
| `registry` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает встроенный Docker Registry в кластере (роль kubernetes-apps/registry). |
| `scheduler_plugins` | cluster.yml, upgrade_cluster.yml | risky | Разворачивает Scheduler Plugins (роль kubernetes-apps/scheduler_plugins). |

## Хранилище / CSI / облачные провайдеры

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `aws-ebs-csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает CSI-драйвер AWS EBS. |
| `azure-csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает CSI-драйвер Azure Disk. |
| `cinder-csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает CSI-драйвер OpenStack Cinder. |
| `csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Зонтичный тег, объединяющий развёртывание всех включённых CSI-драйверов и связанных с ними ресурсов внутри роли kubernetes-apps. |
| `external-cloud-controller` | cluster.yml, upgrade_cluster.yml | safe | Зонтичный тег роли kubernetes-apps/external_cloud_controller. |
| `external-hcloud` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает внешний Hetzner Cloud (hcloud) cloud-controller-manager. |
| `external-huaweicloud` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает внешний Huawei Cloud cloud-controller-manager. |
| `external-oci` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает внешний Oracle Cloud Infrastructure (OCI) cloud-controller-manager. |
| `external-openstack` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает внешний OpenStack cloud-controller-manager. |
| `external-provisioner` | cluster.yml, upgrade_cluster.yml | safe | Зонтичный тег роли kubernetes-apps/external_provisioner. |
| `external-vsphere` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает внешний vSphere cloud-controller-manager (CPI). |
| `gcp-pd-csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает CSI-драйвер GCP Persistent Disk. |
| `local-path-provisioner` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает Rancher local-path-provisioner. |
| `local-volume-provisioner` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает sig-storage local-volume-provisioner. |
| `persistent_volumes` | cluster.yml, upgrade_cluster.yml, scale.yml | safe | Зонтичный тег для настройки StorageClass'ов CSI-томов. |
| `persistent_volumes_aws_ebs_csi` | cluster.yml, upgrade_cluster.yml | safe | Создаёт StorageClass "aws-ebs-csi" для AWS EBS. |
| `persistent_volumes_azure_csi` | cluster.yml, upgrade_cluster.yml | safe | Создаёт StorageClass "azure-csi" для Azure Disk. |
| `persistent_volumes_cinder_csi` | cluster.yml, upgrade_cluster.yml | safe | Создаёт StorageClass "cinder-csi" для OpenStack Cinder. |
| `persistent_volumes_gcp_pd_csi` | cluster.yml, upgrade_cluster.yml | safe | Создаёт StorageClass "gcp-pd-csi" для GCP Persistent Disk. |
| `persistent_volumes_upcloud_csi` | cluster.yml, upgrade_cluster.yml | safe | Создаёт StorageClass "upcloud-csi" для UpCloud. |
| `snapshot` | cluster.yml, upgrade_cluster.yml | safe | Создаёт VolumeSnapshotClass для OpenStack Cinder. |
| `snapshot-controller` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает внешний snapshot-controller CSI. |
| `snapshots` | cluster.yml, upgrade_cluster.yml | safe | Зонтичный тег роли kubernetes-apps/snapshots. |
| `upcloud-csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает CSI-драйвер UpCloud. |
| `vsphere-csi-driver` | cluster.yml, upgrade_cluster.yml | safe | Разворачивает CSI-драйвер vSphere. |

## Ключевые находки (расхождения кода и документации)

Во всех случаях приоритет отдан коду тега v2.29.0 (раздел 5.1 CLAUDE.md); расхождения зафиксированы в поле `notes` соответствующих записей YAML.

- **`always` не включает `kubespray_defaults`.** Под `always` висят лишь проверка версии Ansible, валидация инвентаря и сбор базовых фактов. Переменные по умолчанию задаёт роль `kubespray_defaults`, подключённая без тега.
- **`master` — легаси-синоним `control-plane`, но только в обновлении.** В `cluster.yml` роль control-plane идёт под тегом `control-plane`, а в `upgrade-cluster.yml` — под тегом `master` (с `upgrade_cluster_setup: true`). В таблице `docs/ansible/ansible.md` тег `master` отсутствует.
- **`kube-apiserver` / `kube-controller-manager` уже своих имён.** По коду они навешаны лишь на создание каталогов в `preinstall` (плюс encrypt-at-rest для apiserver), а сами статические поды разворачивает kubeadm. Документация же обещает «configuring static pod».
- **`cni` ≠ установка бинарников CNI.** В коде тег `cni` стоит единственным местом — на создании каталога манифестов в патче `win_nodes`. Установку бинарников CNI (`/opt/cni/bin`) выполняет тег `network`.
- **`upgrade` в роли `download` нет.** Несмотря на пример из docs `--skip-tags upload,upgrade`, в `roles/download` есть только тег `upload`; `upgrade` — сквозной тег обновления в ролях etcd, node, control-plane, metrics_server, cert_manager.
- **`reset_containerd` / `reset_crio` вызываются не из `reset.yml`.** Эти теги срабатывают из `validate-container-engine` при смене контейнерного рантайма (деинсталляция «чужого» движка) во время cluster/scale/upgrade. Помечены `unsafe`.
- **`scheduler_plugins` на K8s 1.29+ ничего не делает.** Роль подключается только при `kube_major_version < 1.29`; при дефолтной 1.33.5 тег фактически пуст.
- **`etcdctl` и `etcdutl` идентичны по эффекту** — общий `import_role etcdctl_etcdutl` помечен обоими тегами и ставит обе утилиты.
- **`coredns` также применяет nodelocaldns** — общая задача помечена обоими тегами.

## Деструктивные и требующие осторожности теги

- **unsafe (7):** `files`, `services` (reset: удаление конфигов/бинарников/данных, остановка kubelet/containerd/etcd), `reset_containerd`, `reset_crio`, `kubeadm_token`, `post-remove`, `reset`.
- **risky (64):** большинство компонентных тегов — требуют артефактов `download`, фактов с других узлов или работающего control plane. Обоснование по каждому — в поле `notes` YAML.

Назад: [[versions/v2.29.0/README|Срез v2.29.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
