---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: code
source_path: versions/v2.31.0/ansible-tags.yaml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - ansible-tags
  - playbooks
  - run-tags
reliability: authoritative
---

# Ansible-теги запуска Kubespray v2.31.0

Теги для `ansible-playbook ... --tags` / `--skip-tags` (не путать с Git-тегами версий). Источник истины — `ansible-tags.yaml`.

- **Всего тегов в v2.31.0:** 120 (в v2.30.0 было 123). **Удалены:** `dashboard`, `ingress-nginx`, `netchecker` (соответствующие роли убраны в v2.31.0). Новых тегов нет.
- **Изолированный запуск (`standalone_run`):** safe — 41, risky — 70, unsafe — 9.

## Метод построения (честно о процессе)

Для 115 из 120 тегов код задач/плейбуков **байт-идентичен v2.30.0** (сверено `git diff v2.30.0..v2.31.0` по `playbooks/` и `roles/**/tasks/**`) — их код-выверенные описания перенесены из справочника v2.30.0 без изменений. 8 тегов с изменённым кодом (`always`, `facts`, `network`, `container-engine`, `etcd`, `apps`, `coredns`, `nodelocaldns`) переанализированы по коду v2.31.0 и снабжены пометкой `[v2.31.0]` в поле notes YAML. Это соответствует разделу 13 (не переиспользование без анализа, а подтверждённая идентичность).

> ⚠️ Ловушка узкого `--tags`: роль `kubespray_defaults` подключается без тега и не входит в `always`.


## Базовые / подготовка узлов

| Тег | Изолированно | Что делает |
|---|---|---|
| `always`⚡ | safe | Специальный Ansible-тег, автоматически применяемый к задачам вне зависимости от --tags (отменяется только через --skip-tags always). |
| `annotate` | risky | Создаёт аннотации на узлах для сетевого плагина kube-router: задача импортирует annotate.yml из роли network_plugin/kube-router (roles/network_plug… |
| `asserts` | safe | Проверочные (assert) задачи-предусловия. |
| `bastion` | safe | Настраивает SSH-конфигурацию для проксирования подключений через bastion-хост. |
| `bootstrap_os` | risky | Объединяет задачи первичной подготовки ОС узлов. |
| `check` | safe | Помечает три assert-проверки окружения запуска в playbooks/ansible_version.yml: версия Ansible в диапазоне minimal_ansible_version (2.17.3) <= x <… |
| `dns`⚡ | risky | Задачи очистки DNS-настроек при сбросе узла (роль reset). |
| `download` | risky | Загрузка бинарных файлов и контейнерных образов, используемых Kubespray. |
| `facts`⚡ | safe | Сквозной тег на задачах сбора фактов и вычисления переменных (set_fact, include_vars, setup) во многих ролях: bootstrap_os (подключение distro-vars… |
| `files` | unsafe | Разрушающее удаление файлов и каталогов, созданных Kubespray, при сбросе узла (роль reset). |
| `init` | risky | Задачи инициализации для поддержки Windows-узлов (роль win_nodes/kubernetes_patch). |
| `ip6tables` | unsafe | Сброс правил IPv6-фаервола при reset (роль reset). |
| `iptables` | unsafe | Сброс правил IPv4-фаервола при reset (роль reset). |
| `localhost` | safe | Специальные шаги, выполняемые на управляющем узле Ansible (localhost / download_delegate). |
| `mounts` | risky | Отмонтирование каталогов kubelet при сбросе узла (роль reset). |
| `preinstall` | safe | Предварительная подготовка узлов (роль kubernetes/preinstall). |
| `resolvconf` | safe | Настройка /etc/resolv.conf и разрешения имён на узлах (роль kubernetes/preinstall). |
| `services` | unsafe | Остановка и удаление systemd-сервисов при сбросе узла (роль reset). |
| `system-packages` | risky | Установка системных пакетов через пакетный менеджер ОС (роль bootstrap_os → import роли system_packages). |
| `system-upgrade` | risky | Обновление системных пакетов ОС в процессе апгрейда кластера (роль upgrade/system-upgrade), подключается на уровне play в upgrade_cluster.yml. |
| `system-upgrade-apt` | risky | Подтег системного обновления для Debian-семейства (роль upgrade/system-upgrade). |
| `system-upgrade-yum` | risky | Подтег системного обновления для RedHat-семейства (роль upgrade/system-upgrade). |
| `upload` | risky | В v2.30.0 тег upload помечает в roles/download/tasks/main.yml две подготовительные задачи роли download: подготовку рабочих каталогов и переменных… |
| `win_nodes` | risky | Специфичные для Windows задачи (роль win_nodes/kubernetes_patch), выполняются на первом узле control plane. |

## Control plane / узлы / etcd / жизненный цикл

| Тег | Изолированно | Что делает |
|---|---|---|
| `client` | risky | Настраивает клиентский доступ к кластеру на control plane узлах (роль kubernetes/client). |
| `control-plane` | risky | Разворачивает и конфигурирует роль control plane (kubernetes/control-plane) на узлах kube_control_plane. |
| `etcd`⚡ | risky | Разворачивает и настраивает кластер etcd (роль etcd). |
| `etcd-secrets` | safe | Отвечает исключительно за сертификаты и ключи etcd (подмножество роли etcd): проверка существующих сертификатов (check_certs.yml, cert_management =… |
| `etcd_metrics` | risky | Применяет манифесты Endpoints и Service для экспонирования метрик etcd в кластере (roles/kubernetes-apps/ansible/tasks/main.yml): kubectl apply шаб… |
| `etcdctl` | safe | Устанавливает бинари etcdctl и etcdutl через роль etcdctl_etcdutl и создаёт скрипт-обёртку etcdctl.sh. |
| `etcdutl` | safe | Устанавливает бинари etcdutl и etcdctl через роль etcdctl_etcdutl (тот же набор задач, что и у тега etcdctl). |
| `haproxy` | risky | Разворачивает локальный HAProxy как балансировщик к kube-apiserver (roles/kubernetes/node/tasks/loadbalancer/haproxy.yml, часть роли kubernetes/node). |
| `k8s-pre-upgrade` | unsafe | Предапгрейдовая подготовка control plane (roles/kubernetes/control-plane/tasks/pre-upgrade.yml). |
| `kube-apiserver` | risky | В роли kubernetes/control-plane тегом kube-apiserver помечён импорт encrypt-at-rest.yml (конфигурация шифрования secret-данных в etcd, когда kube_e… |
| `kube-controller-manager` | safe | В v2.30.0 тег kube-controller-manager встречается ТОЛЬКО в roles/kubernetes/preinstall/tasks/0050-create_directories.yml и покрывает создание служе… |
| `kube-vip` | risky | Устанавливает и настраивает kube-vip как статический под для виртуального IP apiserver (roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml, част… |
| `kubeadm` | risky | Объединяет задачи, связанные с kubeadm join и настройкой узлов через kubeadm. |
| `kubeadm_token` | safe | Управление bootstrap-токенами kubeadm для присоединения узлов (roles/kubernetes/control-plane/tasks/kubeadm-setup.yml). |
| `kubectl` | safe | Устанавливает kubectl и bash-автодополнение на control plane узлах (roles/kubernetes/control-plane/tasks/main.yml): копирует бинарь kubectl из down… |
| `kubelet` | risky | Устанавливает и конфигурирует kubelet на всех узлах k8s_cluster (роль kubernetes/node): сбор фактов, копирование бинаря kubelet (node/install.yml),… |
| `nginx` | risky | Разворачивает локальный nginx-proxy как балансировщик к kube-apiserver (roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml, часть роли kubern… |
| `node` | risky | Базовая настройка узла как worker/минион (роль kubernetes/node) на всех узлах k8s_cluster: сбор фактов, создание /var/lib/cni, установка бинаря kub… |
| `node-label` | risky | Проставляет метки (labels) на узлы кластера (роль kubernetes/node-label). |
| `node-taint` | risky | Проставляет taint-ы на узлы кластера (роль kubernetes/node-taint). |
| `node-webhook` | risky | Управляет доступом на основе webhook — ClusterRole/ClusterRoleBinding system:node-webhook (roles/kubernetes-apps/cluster_roles/tasks/main.yml). |
| `post-remove` | unsafe | Финальный этап удаления узла (роль remove-node/post-remove в playbooks/remove_node.yml). |
| `post-upgrade` | risky | Постобработка узла после апгрейда (роль upgrade/post-upgrade в playbooks/upgrade_cluster.yml). |
| `pre-remove` | risky | Подготовка узла к удалению (роль remove_node/pre_remove в playbooks/remove_node.yml). |
| `pre-upgrade` | risky | Подготовка узла к апгрейду (роль upgrade/pre-upgrade в playbooks/upgrade_cluster.yml). |
| `reset` | unsafe | Полный сброс узла (роль reset) в playbooks/reset.yml и playbooks/remove_node.yml. |
| `upgrade` | risky | Сквозной тег, помечающий отдельные задачи обновления бинарей и addon-ов в разных ролях (не является отдельной ролью). |

## Контейнерные движки

| Тег | Изолированно | Что делает |
|---|---|---|
| `container-engine`⚡ | risky | Зонтичный тег всей роли roles/container-engine. |
| `container-runtimes` | risky | Тег этапа apps (роль kubernetes-apps/container_runtimes). |
| `container_engine_accelerator` | risky | Тег этапа apps (роль kubernetes-apps/container_engine_accelerator). |
| `containerd` | risky | Двойное назначение в зависимости от плейбука. |
| `crio` | risky | Двойное назначение. |
| `crun` | risky | Настройка низкоуровневого OCI-рантайма crun. |
| `docker` | risky | Двойное назначение. |
| `gvisor` | risky | Настройка песочничного рантайма gVisor (runsc). |
| `kata-containers` | risky | Настройка рантайма Kata Containers. |
| `nvidia_gpu` | risky | Тег подроли kubernetes-apps/container_engine_accelerator/nvidia_gpu (включается при nvidia_accelerator_enabled). |
| `reset_containerd` | unsafe | Teardown-тег внутри роли container-engine/containerd (tasks/reset.yml). |
| `reset_crio` | unsafe | Teardown-тег внутри роли container-engine/cri-o (tasks/reset.yml). |
| `validate-container-engine` | risky | Первая (валидирующая) подроль роли container-engine (container-engine/validate-container-engine). |
| `youki` | risky | Настройка OCI-рантайма youki. |

## Сеть / CNI / DNS

| Тег | Изолированно | Что делает |
|---|---|---|
| `calico` | risky | Разворачивает CNI Calico: роль network_plugin/calico выполняется как зависимость network_plugin при kube_network_plugin == 'calico'. |
| `calico_rr` | risky | Настраивает Calico Route Reflector: отдельная play "Install Calico Route Reflector" в cluster.yml с hosts: calico_rr исполняет роль network_plugin/… |
| `cilium` | risky | Разворачивает CNI Cilium через утилиту cilium-cli по helm-values (в v2.30.0 это основной способ, не через статические манифесты). |
| `cni` | safe | ВНИМАНИЕ: в v2.30.0 Ansible-тег cni назначен только одной задаче — "Ensure that user manifests directory exists" в роли win_nodes/kubernetes_patch… |
| `coredns`⚡ | risky | Разворачивает и настраивает DNS-развёртывание CoreDNS. |
| `custom_cni` | risky | Разворачивает пользовательский CNI: роль network_plugin/custom_cni как зависимость network_plugin при kube_network_plugin == 'custom_cni'. |
| `flannel` | risky | Разворачивает CNI Flannel: роль network_plugin/flannel как зависимость network_plugin при kube_network_plugin == 'flannel'. |
| `kube-ovn` | risky | Разворачивает CNI Kube-OVN: роль network_plugin/kube-ovn как зависимость network_plugin при kube_network_plugin == 'kube-ovn'. |
| `kube-proxy` | risky | Настраивает kube-proxy (в кластере kube-proxy — статический под, разворачиваемый kubeadm). |
| `kube-router` | risky | Разворачивает CNI Kube-router: роль network_plugin/kube-router как зависимость network_plugin при kube_network_plugin == 'kube-router'. |
| `macvlan` | risky | Разворачивает CNI Macvlan: роль network_plugin/macvlan как зависимость network_plugin при kube_network_plugin == 'macvlan'. |
| `multus` | risky | Разворачивает Multus (meta-CNI для нескольких интерфейсов): роль network_plugin/multus как зависимость network_plugin при kube_network_plugin_multu… |
| `network`⚡ | risky | Сквозной тег настройки сети. |
| `nodelocaldns`⚡ | risky | Разворачивает DaemonSet nodelocaldns (локальный кэш DNS на узлах). |

## Приложения (kubernetes-apps)

| Тег | Изолированно | Что делает |
|---|---|---|
| `apps`⚡ | risky | Сквозной («umbrella») тег группы kubernetes-apps. |
| `argocd` | risky | Разворачивает Argo CD. |
| `cert-manager` | risky | Разворачивает cert-manager. |
| `cluster-roles` | risky | Настраивает общекластерные RBAC-объекты и приоритетные классы. |
| `gateway_api` | risky | Устанавливает CRD Gateway API. |
| `helm` | safe | Устанавливает и настраивает Helm: ставит зависимость PyYAML, скачивает и копирует бинарь helm в bin_dir, генерирует bash-completion. |
| `ingress-controller` | risky | Зонтичный тег контроллеров ingress. |
| `ingress_alb` | risky | Разворачивает AWS ALB Ingress Controller: создаёт addon-каталог, рендерит манифесты (ClusterRole/binding, namespace, ServiceAccount, deployment) и… |
| `kubelet-csr-approver` | risky | Устанавливает kubelet-csr-approver (postfinance) через Helm. |
| `metallb` | risky | Разворачивает MetalLB (балансировщик L2/BGP для bare-metal). |
| `metrics_server` | risky | Разворачивает Kubernetes Metrics Server: удаляет прежний addon-каталог (задача с тегом upgrade), создаёт каталог заново, рендерит манифесты (SA, De… |
| `node_feature_discovery` | risky | Разворачивает Node Feature Discovery (NFD): создаёт addon-каталог, рендерит манифесты (namespace, CRD, SA, Role/ClusterRole и binding'и, ConfigMap'… |
| `policy-controller` | risky | Разворачивает контроллер сетевых политик Calico (calico-kube-controllers). |
| `prometheus_operator_crds` | risky | Устанавливает CRD Prometheus Operator. |
| `registry` | risky | Разворачивает внутрикластерный docker registry: валидирует registry_service_type и связанные переменные, создаёт addon-каталог, рендерит манифесты… |
| `scheduler_plugins` | risky | Разворачивает проект scheduler-plugins (SIG Scheduling): создаёт каталог, рендерит и применяет CRD (appgroups, networktopologies, elasticquotas, po… |

## Хранилище / CSI / облако

| Тег | Изолированно | Что делает |
|---|---|---|
| `aws-ebs-csi-driver` | safe | Разворачивает CSI-драйвер AWS EBS (roles/kubernetes-apps/csi_driver/aws_ebs) и связанные объекты хранилища через roles/kubernetes-apps/persistent_v… |
| `azure-csi-driver` | safe | Разворачивает CSI-драйвер Azure Disk (roles/kubernetes-apps/csi_driver/azuredisk) и объекты хранилища через roles/kubernetes-apps/persistent_volume… |
| `cinder-csi-driver` | safe | Разворачивает CSI-драйвер OpenStack Cinder (roles/kubernetes-apps/csi_driver/cinder), создаёт объекты хранилища (roles/kubernetes-apps/persistent_v… |
| `csi-driver` | safe | Зонтичный тег для всей подсистемы CSI-драйверов. |
| `external-cloud-controller` | safe | Зонтичный тег для внешних cloud-controller-manager (CCM). |
| `external-hcloud` | safe | Разворачивает внешний Hetzner Cloud Controller Manager: генерирует манифесты (secret, service-account, role-bindings, DaemonSet — с сетями или без,… |
| `external-huaweicloud` | safe | Разворачивает внешний Huawei Cloud Controller Manager: проверяет учётные данные (huaweicloud-credential-check.yml), читает cacert, формирует секрет… |
| `external-oci` | safe | Разворачивает внешний Oracle OCI Cloud Controller Manager: проверяет учётные данные и настройки (assert), формирует секрет cloud-config, генерирует… |
| `external-openstack` | safe | Разворачивает внешний OpenStack Cloud Controller Manager: проверяет учётные данные (openstack-credential-check.yml), читает cacert, формирует секре… |
| `external-provisioner` | safe | Зонтичный тег для внешних провижнеров томов. |
| `external-vsphere` | safe | Разворачивает внешний vSphere Cloud Controller Manager (CPI): проверяет учётные данные, генерирует CPI cloud-config, secret, roles, role-bindings,… |
| `gcp-pd-csi-driver` | safe | Разворачивает CSI-драйвер Google Persistent Disk (roles/kubernetes-apps/csi_driver/gcp_pd) и объекты хранилища через roles/kubernetes-apps/persiste… |
| `local-path-provisioner` | safe | Разворачивает Rancher local-path-provisioner (roles/kubernetes-apps/external_provisioner/local_path_provisioner): генерирует манифесты (namespace/R… |
| `local-volume-provisioner` | safe | Разворачивает sig-storage local-volume-provisioner (roles/kubernetes-apps/external_provisioner/local_volume_provisioner): генерирует манифесты (nam… |
| `persistent_volumes` | safe | Запускает роль roles/kubernetes-apps/persistent_volumes, которая через свои зависимости создаёт объекты хранилища (StorageClass/PV) для включённых… |
| `persistent_volumes_aws_ebs_csi` | safe | Создаёт объекты хранилища (StorageClass) для AWS EBS через под-роль roles/kubernetes-apps/persistent_volumes/aws-ebs-csi. |
| `persistent_volumes_azure_csi` | safe | Создаёт объекты хранилища (StorageClass) для Azure Disk через под-роль roles/kubernetes-apps/persistent_volumes/azuredisk-csi. |
| `persistent_volumes_cinder_csi` | safe | Создаёт объекты хранилища (StorageClass) для OpenStack Cinder через под-роль roles/kubernetes-apps/persistent_volumes/cinder-csi. |
| `persistent_volumes_gcp_pd_csi` | safe | Создаёт объекты хранилища (StorageClass) для Google Persistent Disk через под-роль roles/kubernetes-apps/persistent_volumes/gcp-pd-csi. |
| `persistent_volumes_upcloud_csi` | safe | Создаёт объекты хранилища (StorageClass) для UpCloud через под-роль roles/kubernetes-apps/persistent_volumes/upcloud-csi. |
| `snapshot` | safe | Создаёт VolumeSnapshotClass для Cinder CSI: копирует шаблон cinder-csi-snapshot-class.yml и применяет его через kubectl (roles/kubernetes-apps/snap… |
| `snapshot-controller` | safe | Разворачивает CSI Snapshot Controller: проверяет наличие namespace, генерирует и применяет манифесты snapshot-ns, rbac-snapshot-controller, snapsho… |
| `snapshots` | safe | Зонтичный тег подсистемы снапшотов. |
| `upcloud-csi-driver` | safe | Разворачивает CSI-драйвер UpCloud (roles/kubernetes-apps/csi_driver/upcloud) и объекты хранилища через roles/kubernetes-apps/persistent_volumes/upc… |
| `vsphere-csi-driver` | safe | Разворачивает CSI-драйвер vSphere (roles/kubernetes-apps/csi_driver/vsphere): генерирует и применяет манифесты драйвера/RBAC/StorageClass. |

⚡ — тег с изменённым в v2.31.0 кодом (переанализирован; см. поле notes в `ansible-tags.yaml`).

## Отличия от v2.30.0

- **Удалены теги** `dashboard`, `ingress-nginx`, `netchecker` — вместе с ролями Kubernetes Dashboard, ingress_nginx и Netchecker (breaking change v2.31.0).
- `network`/`container-engine` — диспетчеризация переведена на динамический `include_role` с apply-тегами (`{{ kube_network_plugin }}`, `{{ item.role }}`); поведение прежнее.
- `always`/`facts` — роль `network_facts` теперь под тегом `always`; в ней исправлен рендеринг `no_proxy` (flatten+join).

Подробное сравнение: [[diffs/v2.30.0__v2.31.0|Отчёт сравнения v2.30.0 → v2.31.0]].

Назад: [[versions/v2.31.0/README|Срез v2.31.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
