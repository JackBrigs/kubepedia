---
project: kubespray
kubespray_version: v2.27.1
git_commit: 45140b5
source_type: code
source_path: versions/v2.27.1/ansible-tags.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.1
retrieved_at: 2026-07-15
topics:
  - ansible-tags
  - playbooks
  - run-tags
reliability: authoritative
---

# Ansible-теги запуска Kubespray v2.27.1

Справочник тегов, которые передаются в `ansible-playbook ... --tags` / `--skip-tags`. **Это не Git-теги версий** — здесь речь о тегах задач и ролей внутри плейбуков Kubespray. Источник истины — парный файл `ansible-tags.yaml`; ниже — человекочитаемый обзор.

- **Всего тегов в v2.27.1:** 127 (извлечены из `playbooks/*.yml` и `roles/*/tasks/**`, полнота сверена программно).
- **Безопасность изолированного запуска (`standalone_run`):** safe — 57, risky — 63, unsafe — 7.
- Колонка «Изолированно» ниже: **safe** — можно запускать отдельным `--tags`; **risky** — как правило требует `download` и/или фактов с других узлов, живого control plane; **unsafe** — деструктивно или бессмысленно вне своего сценария.

> ⚠️ **Отличия версии v2.27.1 от v2.29.1** (подробности — в поле `notes` соответствующих записей YAML):
> - Роль контрол-плейна в `cluster.yml` помечена тегом **`master`** (в v2.29.1 — `control-plane`). Тег `control-plane` в v2.27.1 покрывает лишь вспомогательные задачи (каталоги + серийники etcd-сертификатов).
> - Подготовка ОС — тег **`bootstrap-os`** (через дефис) и роль `roles/bootstrap-os`; в v2.29.1 переименованы в `bootstrap_os`.
> - Факты собирает `playbooks/facts.yml` (в v2.29.1 — `internal_facts.yml`); инвентарь нормализуется inline-плеем `group_by` в `boilerplate.yml`.
> - Cilium ставится из **статических манифестов** (в v2.29.1 — через `cilium-cli`); `cilium_min_version_required = 1.10`.
> - Есть теги, отсутствующие в v2.29.1: **`weave`**, **`cephfs-provisioner`**, **`rbd-provisioner`**, **`cloud-provider`**, **`etchosts`**, **`krew`**.
> - Установка системных пакетов встроена в `preinstall` (тег `system-packages` на `0070-system-packages.yml`); отдельной роли `system_packages` нет.

## Как пользоваться

```bash
# только преднастройка узлов, без скачивания
ansible-playbook -i inventory/hosts.yaml cluster.yml --tags preinstall --skip-tags download
# развернуть/обновить только etcd
ansible-playbook -i inventory/hosts.yaml cluster.yml --tags etcd
# переустановить/обновить контрол-плейн (в v2.27.1 — именно master)
ansible-playbook -i inventory/hosts.yaml cluster.yml --tags master
```

## Базовые / подготовка узлов

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `always` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Специальный тег Ansible: задачи и плеи, помеченные always, выполняются при любом запуске независимо от --tags/--skip-tags (отменить можно только явным -… |
| `asserts` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Проверочные (assert) задачи без изменений на узлах. |
| `bastion` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Настраивает SSH-конфигурацию для прыжкового узла (bastion). |
| `bootstrap-os` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | risky | Первичная подготовка ОС узлов. |
| `check` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Предварительные проверки окружения управляющей машины/узлов: соответствие версии Ansible диапазону (minimal_ansible_version <= v < maximal_ansible_versi… |
| `cloud-provider` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Проверочные (assert) задачи корректности настроек облачного провайдера, без изменений на узлах. |
| `dns` | reset.yml, remove-node.yml | risky | Удаление DNS-настроек при сбросе узла (роль reset). |
| `download` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Загрузка бинарников и container-образов ролью download: подготовка каталогов и переменных (prep_download), получение kubeadm и списка нужных образов, ск… |
| `etchosts` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Настройка /etc/hosts на узлах. |
| `facts` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Сбор фактов и вычисление производных переменных без изменений на узлах. |
| `files` | reset.yml, remove-node.yml | unsafe | Удаление файлов и каталогов при сбросе узла (роль reset). |
| `init` | cluster.yml, upgrade-cluster.yml | risky | Инициализация для Windows-узлов (роль win_nodes/kubernetes_patch, hosts kube_control_plane[0]). |
| `ip6tables` | reset.yml, remove-node.yml | risky | Сброс правил IPv6-фаервола при reset. |
| `iptables` | reset.yml, remove-node.yml | risky | Сброс правил IPv4-фаервола при reset. |
| `localhost` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml, remove-node.yml | safe | Особые шаги, выполняемые на управляющей машине (ansible runner) и делегатах. |
| `mounts` | reset.yml, remove-node.yml | risky | Размонтирование каталогов kubelet при сбросе узла (роль reset). |
| `preinstall` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Предварительная подготовка узлов ролью kubernetes/preinstall: отключение swap, вычисление фактов (0020-set_facts), проверка настроек (0040-verify-settin… |
| `resolvconf` | cluster.yml, upgrade-cluster.yml, scale.yml, reset.yml | safe | Настройка /etc/resolv.conf (и systemd-resolved/NetworkManager DNS) для узлов и подов. |
| `services` | reset.yml, remove-node.yml | unsafe | Остановка и удаление systemd-сервисов при сбросе узла (роль reset). |
| `system-packages` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Установка системных пакетов. |
| `system-upgrade` | upgrade-cluster.yml | risky | Обновление системных пакетов ОС в ходе апгрейда кластера (роль upgrade/system-upgrade). |
| `upload` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Распространение образов/бинарников по узлам кластера в рамках роли download. |
| `win_nodes` | cluster.yml, upgrade-cluster.yml | risky | Специфичные для Windows задачи (роль win_nodes/kubernetes_patch, hosts kube_control_plane[0]). |

## Control plane / узлы / etcd / жизненный цикл

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `client` | cluster.yml, upgrade-cluster.yml | safe | Запускает роль kubernetes/client на узлах контрол-плейна (тег навешен на роль на уровне плейбука, внутренних тегов у роли нет — выполняется вся роль). |
| `cluster-roles` | cluster.yml, upgrade-cluster.yml | safe | Роль kubernetes-apps/cluster_roles: базовая RBAC-настройка кластера. |
| `control-plane` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | ВНИМАНИЕ (приоритет у кода над docs): в v2.27.1 тег control-plane НЕ разворачивает роль контрол-плейна (её разворачивает тег master, см. |
| `etcd` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Тег уровня роли etcd (навешен на роль целиком в install_etcd.yml и scale.yml). |
| `etcd-secrets` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Управляет сертификатами и ключами etcd. |
| `etcd_metrics` | cluster.yml, upgrade-cluster.yml | risky | Публикует Endpoints и Service для сбора метрик etcd. |
| `etcdctl` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Устанавливает клиентские утилиты etcd. |
| `etcdutl` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Полный синоним etcdctl по коду: тот же import_role etcdctl_etcdutl в roles/etcd/tasks/main.yml и roles/kubernetes/control-plane/tasks/kubeadm-etcd.yml п… |
| `haproxy` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Разворачивает локальный балансировщик apiserver на базе HAProxy. |
| `k8s-pre-upgrade` | cluster.yml, upgrade-cluster.yml | risky | Предобновление контрол-плейна. |
| `kube-apiserver` | cluster.yml, upgrade-cluster.yml | risky | Вопреки названию тега («Configuring static pod kube-apiserver» в docs) по коду тег не разворачивает сам под apiserver (это делает kubeadm). |
| `kube-controller-manager` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | По коду тег навешен только на задачи создания каталогов Kubernetes в roles/kubernetes/preinstall/0050-create_directories.yml (kube_config_dir, kube_mani… |
| `kube-vip` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Устанавливает kube-vip для виртуального IP/балансировки apiserver на узлах контрол-плейна. |
| `kubeadm` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Собирает всё, что связано с kubeadm-присоединением узлов и конфигурацией kubelet. |
| `kubeadm_token` | cluster.yml, upgrade-cluster.yml | unsafe | Управляет bootstrap-токенами kubeadm для присоединения узлов. |
| `kubectl` | cluster.yml, upgrade-cluster.yml | safe | Устанавливает и настраивает kubectl на узлах контрол-плейна. |
| `kubelet` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Полностью настраивает сервис kubelet. |
| `master` | cluster.yml, upgrade-cluster.yml | risky | Основной тег развёртывания/переконфигурации контрол-плейна в v2.27.1. |
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
| `reset_containerd` | cluster.yml, scale.yml, upgrade-cluster.yml | unsafe | Теардаун-задачи containerd (roles/container-engine/containerd/tasks/reset.yml): останавливают и отключают сервис containerd и удаляют его артефакты — /e… |
| `reset_crio` | cluster.yml, scale.yml, upgrade-cluster.yml | unsafe | Теардаун-задачи CRI-O (roles/container-engine/cri-o/tasks/reset.yml): удаляют apt/yum-репозитории CRI-O, чистят метаданные yum, удаляют crictl и /etc/cr… |
| `validate-container-engine` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Первый шаг роли container-engine (roles/container-engine/validate-container-engine). |
| `youki` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает низкоуровневый OCI-рантайм youki. |

## Сеть / CNI / DNS

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `annotate` | cluster.yml, upgrade-cluster.yml, scale.yml | risky | Проставляет аннотации узлам для сетевого плагина kube-router. |
| `calico` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Calico (роль network_plugin/calico, подключается при kube_network_plugin == 'calico'). |
| `calico_rr` | cluster.yml | risky | Настраивает Calico Route Reflector: в cluster.yml для группы calico_rr подключается роль network_plugin/calico/rr с тегами ['network', 'calico_rr']. |
| `cilium` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Cilium (роль network_plugin/cilium, подключается при kube_network_plugin == 'cilium' или cilium_deploy_additionally). |
| `cni` | cluster.yml, upgrade-cluster.yml | safe | ВНИМАНИЕ: по коду тега (приоритет у кода над docs/ansible/ansible.md, где тег описан как «CNI plugins for Network Plugins») тег cni в v2.27.1 навешан ед… |
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
| `weave` | cluster.yml, scale.yml, upgrade-cluster.yml | risky | Разворачивает CNI-плагин Weave Net (удалён в поздних версиях Kubespray). |

## Приложения (kubernetes-apps)

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `apps` | cluster.yml, upgrade-cluster.yml | risky | Сквозной тег для развёртывания прикладных дополнений кластера (роль kubernetes-apps в плейбуке "Install Kubernetes apps"). |
| `argocd` | cluster.yml, upgrade-cluster.yml | risky | Разворачивает Argo CD (роль kubernetes-apps/argocd). |
| `cert-manager` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает cert-manager (роль kubernetes-apps/ingress_controller/cert_manager). |
| `dashboard` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает Kubernetes Dashboard (задача "Kubernetes Apps \| Dashboard" в роли kubernetes-apps/ansible). |
| `gateway_api` | cluster.yml, upgrade-cluster.yml | safe | Устанавливает CRD Gateway API (роль kubernetes-apps/gateway_api). |
| `helm` | cluster.yml, upgrade-cluster.yml | safe | Устанавливает клиент Helm на узлы control-plane (роль kubernetes-apps/helm). |
| `ingress-controller` | cluster.yml, upgrade-cluster.yml | safe | Составной тег роли kubernetes-apps/ingress_controller. |
| `ingress-nginx` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает NGINX Ingress Controller (роль kubernetes-apps/ingress_controller/ingress_nginx). |
| `ingress_alb` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает AWS ALB Ingress Controller (роль kubernetes-apps/ingress_controller/alb_ingress_controller). |
| `krew` | cluster.yml, upgrade-cluster.yml | risky | Устанавливает менеджер плагинов kubectl — krew (роль kubernetes-apps/krew). |
| `kubelet-csr-approver` | cluster.yml, upgrade-cluster.yml | risky | Устанавливает kubelet-csr-approver (роль kubernetes-apps/kubelet-csr-approver). |
| `metallb` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает балансировщик MetalLB (роль kubernetes-apps/metallb). |
| `metrics_server` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает Kubernetes Metrics Server (роль kubernetes-apps/metrics_server). |
| `node_feature_discovery` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает Node Feature Discovery (роль kubernetes-apps/node_feature_discovery). |
| `policy-controller` | cluster.yml, upgrade-cluster.yml | safe | Роль kubernetes-apps/policy_controller. |
| `registry` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает встроенный Docker Registry в кластере (роль kubernetes-apps/registry). |
| `scheduler_plugins` | cluster.yml, upgrade-cluster.yml | risky | Разворачивает Scheduler Plugins (роль kubernetes-apps/scheduler_plugins). |

## Хранилище / CSI / провиженеры / облачные провайдеры

| Тег | Плейбуки | Изолированно | Что делает |
|---|---|---|---|
| `aws-ebs-csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает CSI-драйвер AWS EBS. |
| `azure-csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает CSI-драйвер Azure Disk. |
| `cephfs-provisioner` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний CephFS-провиженер томов (роль kubernetes-apps/external_provisioner/cephfs_provisioner). |
| `cinder-csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает CSI-драйвер OpenStack Cinder. |
| `csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Зонтичный тег, объединяющий развёртывание всех включённых CSI-драйверов и связанных с ними ресурсов внутри роли kubernetes-apps. |
| `external-cloud-controller` | cluster.yml, upgrade-cluster.yml | safe | Зонтичный тег роли kubernetes-apps/external_cloud_controller. |
| `external-hcloud` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний Hetzner Cloud (hcloud) cloud-controller-manager. |
| `external-huaweicloud` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний Huawei Cloud cloud-controller-manager. |
| `external-oci` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний Oracle Cloud Infrastructure (OCI) cloud-controller-manager. |
| `external-openstack` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний OpenStack cloud-controller-manager. |
| `external-provisioner` | cluster.yml, upgrade-cluster.yml | safe | Зонтичный тег роли kubernetes-apps/external_provisioner. |
| `external-vsphere` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний vSphere cloud-controller-manager (CPI). |
| `gcp-pd-csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает CSI-драйвер GCP Persistent Disk. |
| `local-path-provisioner` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает Rancher local-path-provisioner. |
| `local-volume-provisioner` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает sig-storage local-volume-provisioner. |
| `persistent_volumes` | cluster.yml, upgrade-cluster.yml, scale.yml | safe | Зонтичный тег для настройки StorageClass'ов CSI-томов. |
| `persistent_volumes_aws_ebs_csi` | cluster.yml, upgrade-cluster.yml | safe | Создаёт StorageClass "aws-ebs-csi" для AWS EBS. |
| `persistent_volumes_azure_csi` | cluster.yml, upgrade-cluster.yml | safe | Создаёт StorageClass "azure-csi" для Azure Disk. |
| `persistent_volumes_cinder_csi` | cluster.yml, upgrade-cluster.yml | safe | Создаёт StorageClass "cinder-csi" для OpenStack Cinder. |
| `persistent_volumes_gcp_pd_csi` | cluster.yml, upgrade-cluster.yml | safe | Создаёт StorageClass "gcp-pd-csi" для GCP Persistent Disk. |
| `persistent_volumes_upcloud_csi` | cluster.yml, upgrade-cluster.yml | safe | Создаёт StorageClass "upcloud-csi" для UpCloud. |
| `rbd-provisioner` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний Ceph RBD-провиженер томов (роль kubernetes-apps/external_provisioner/rbd_provisioner). |
| `snapshot` | cluster.yml, upgrade-cluster.yml | safe | Создаёт VolumeSnapshotClass для OpenStack Cinder. |
| `snapshot-controller` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает внешний snapshot-controller CSI. |
| `snapshots` | cluster.yml, upgrade-cluster.yml | safe | Зонтичный тег роли kubernetes-apps/snapshots. |
| `upcloud-csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает CSI-драйвер UpCloud. |
| `vsphere-csi-driver` | cluster.yml, upgrade-cluster.yml | safe | Разворачивает CSI-драйвер vSphere. |

## Ключевые находки (расхождения кода и документации, отличия от v2.29.1)

Во всех случаях приоритет отдан коду тега v2.27.1 (раздел 5.1 CLAUDE.md); расхождения зафиксированы в поле `notes` соответствующих записей YAML.

- **`master` — рабочий тег контрол-плейна.** В `cluster.yml` роль `kubernetes/control-plane` подключена под тегом `master` (в v2.29.1 — `control-plane`). В `upgrade-cluster.yml` — тоже `master` (с `upgrade_cluster_setup: true`). Тег `master` в `docs/ansible/ansible.md` не документирован.
- **`control-plane` почти пуст.** По коду навешан только на вычисление серийников клиентских etcd-сертификатов (`roles/etcd`) и создание каталогов (`preinstall/0050`). Он НЕ переустанавливает apiserver — используйте `master`.
- **`cilium` — статические манифесты.** В v2.27.1 Cilium разворачивается через `kubectl apply` набора манифестов (ConfigMap, DaemonSet, Deployment cilium-operator, RBAC), а не через `cilium-cli`. Минимальная версия `cilium_min_version_required = 1.10`.
- **`bootstrap-os` (дефис).** Тег и роль называются `bootstrap-os`; установка системных пакетов интегрирована в `preinstall` (`0070-system-packages.yml`) — отдельной роли `system_packages` нет.
- **`always` без ролей нормализации.** Инвентарь приводится к общему виду inline-плеем `group_by` в `boilerplate.yml` (не роли `dynamic_groups`/`validate_inventory`), факты собирает `playbooks/facts.yml`. Часть задач `kubespray-defaults` (fallback_ip, no_proxy, `etcd_deployment_type`) помечена `always`.
- **Только в v2.27.1:** `weave` (CNI Weave Net), `cephfs-provisioner` и `rbd-provisioner` (внешние Ceph-провиженеры), `cloud-provider` (assert-проверки настроек облака), `etchosts` (правка `/etc/hosts`), `krew` (менеджер плагинов kubectl). Все удалены в поздних релизах.
- **`cni` ≠ установка бинарников CNI.** Как и в v2.29.1, тег `cni` стоит только на создании каталога манифестов в патче `win_nodes` (`tags: [init, cni]`). Бинарники CNI (`/opt/cni/bin`) ставит тег `network`.
- **`kube-apiserver` / `kube-controller-manager` уже своих имён.** По коду — лишь создание каталогов в `preinstall` (плюс encrypt-at-rest для apiserver); статические поды разворачивает kubeadm.
- **`etcdctl` и `etcdutl` идентичны** — общий `import_role etcdctl_etcdutl` помечен обоими тегами.
- **`coredns` также применяет nodelocaldns** — общая задача помечена обоими тегами.
- **`gateway_api` — часть `kubernetes-apps`.** Роль `kubernetes-apps/gateway_api` подключается через мета-роль (тег `apps`) и доступна в `cluster.yml` и `upgrade-cluster.yml`; манифест рендерится из локального шаблона. В v2.29.1 её вынесли в `common_crds` (только `cluster.yml`).
- **`scheduler_plugins` на K8s 1.29+ ничего не делает.** Роль подключается только при `kube_major_version < 1.29`.
- **`reset_containerd` / `reset_crio`** вызываются не из `reset.yml`, а из `validate-container-engine` при смене рантайма. Помечены `unsafe`.

## Деструктивные и требующие осторожности теги

- **unsafe (7):** `files`, `kubeadm_token`, `post-remove`, `reset`, `reset_containerd`, `reset_crio`, `services` — сброс/удаление сервисов, данных, узлов; теардаун контейнерных движков; управление bootstrap-токенами.
- **risky (63):** большинство компонентных тегов — требуют артефактов `download`, фактов с других узлов или работающего control plane. Обоснование по каждому — в поле `notes` YAML.

Назад: [[versions/v2.27.1/README|Срез v2.27.1]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
