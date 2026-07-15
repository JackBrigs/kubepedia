---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/operations/upgrades.md
  - docs/upgrades/migrate_docker2containerd.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - upgrade
  - migration
reliability: authoritative
---

# Обновление кластера в v2.30.0

Дайджест по обновлению Kubernetes-кластера, развёрнутого через Kubespray. Источники — только `docs/` тега `v2.30.0` (commit `f4ccdb5`).

## Общий принцип

Kubespray обновляет кластер так же, как выполняет первичное развёртывание: каждый компонент раскладывается в фиксированном порядке. Версии компонентов можно контролировать явно, задавая переменные версий.

Переменные версий компонентов (`docs/operations/upgrades.md`):

- `docker_version`
- `docker_containerd_version` (актуально при `container_manager == docker`)
- `containerd_version` (актуально при `container_manager == containerd`)
- `kube_version`
- `etcd_version`
- `calico_version`
- `calico_cni_version`
- `flannel_version`

> Предупреждение: попытка обновиться со старого релиза сразу до последнего **не поддерживается** и, скорее всего, что-то сломает.

## Последовательное обновление по минорным версиям (КЛЮЧЕВОЕ ПРАВИЛО)

> Не пропускайте минорные релизы (патч-релизы пропускать можно) — обновляйтесь **по одному тегу за раз**.

Пример на списке тегов:

- `v2.22.0 -> v2.23.2 -> v2.24.0` : ✓ (допустимо)
- `v2.22.0 -> v2.24.0` : ✕ (запрещено, пропущен минорный релиз)

Порядок действий при последовательном обновлении:

- если версия Kubernetes **не** задана явно в инвентаре (`group_vars/k8s_cluster.yml`) — просто делается `git checkout` следующего тега и запускается `upgrade-cluster.yml`;
- если версия Kubernetes задана в инвентаре — нужно либо обновить её перед запуском, либо указать целевую версию явно: `ansible-playbook -i inventory/mycluster/hosts.ini -b upgrade-cluster.yml -e kube_version=1.11.3`. Иначе обновление оставит кластер на той же версии k8s, что записана в инвентаре.

Замечания:
- при обновлении версий сверяйте изменения между sample-инвентарём и вашим инвентарём; устаревший инвентарь может привести к падению обновления и неработоспособному первому мастеру;
- между версиями бывают несовместимые изменения (например, изменение форматов переменных в `k8s_cluster.yml`), из-за которых нельзя перескочить сразу через минорную версию;
- при обновлении может потребоваться `pip3 install -r requirements.txt`.

## Небезопасное обновление (unsafe upgrade)

Обновление только `kube_version` через `cluster.yml` с флагом `-e upgrade_cluster_setup=true`:

```ShellSession
ansible-playbook cluster.yml -i inventory/sample/hosts.ini -e kube_version=1.19.7 -e upgrade_cluster_setup=true
```

Переменная `upgrade_cluster_setup=true` нужна, чтобы немедленно мигрировать деплои компонентов (например, `kube-apiserver`) внутри кластера — это обычно выполняется только при graceful-обновлении. Без graceful-процедуры (без cordon/drain) это «небезопасный» путь.

## Graceful-обновление (плавное)

Kubespray поддерживает cordon, drain и uncordon узлов при обновлении. Для этого используется **отдельный playbook** `upgrade-cluster.yml`.

Важно: `upgrade-cluster.yml` применяется **только для обновления уже существующего кластера** — должен быть развёрнут хотя бы один `kube_control_plane`.

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.19.7
```

### Управление параллелизмом: `serial`

Количество одновременно обновляемых узлов задаётся ansible-переменной `serial`:

- если `serial` не задан — узлы обновляются пачками по **20%** доступных узлов;
- `serial=1` — по одному узлу за раз.

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 -e "serial=1"
```

### Паузы при обновлении

Для ручного контроля процедуры доступны переменные пауз.

Пауза **перед** обновлением каждого узла (осмотр подов, ручные действия):

- `upgrade_node_confirm: true` — пауза перед обновлением каждого узла; продолжение после ввода `yes` в терминале;
- `upgrade_node_pause_seconds: 60` — пауза на 60 секунд перед обновлением каждого узла; автоматическое продолжение.

Пауза **после** обновления каждого узла, но **до** uncordon (перезагрузка для применения обновлений ядра, тестирование ещё cordon-нутого узла):

- `upgrade_node_post_upgrade_confirm: true` — пауза после обновления узла до uncordon; продолжение по вводу `yes`;
- `upgrade_node_post_upgrade_pause_seconds: 60` — пауза на 60 секунд после обновления узла до uncordon; автоматическое продолжение.

## Обновление по узлам (`--limit`)

Если не нужно обновлять все узлы за один запуск, используется `--limit` с паттернами Ansible.

Перед использованием `--limit` обязательно запустить `facts.yml` **без** limit, чтобы обновить кэш фактов для всех узлов:

```ShellSession
ansible-playbook playbooks/facts.yml -b -i inventory/sample/hosts.ini
```

Далее сначала обновляются группы control plane и etcd:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "kube_control_plane:etcd"
```

Затем остальные узлы в любом порядке и количестве:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "node4:node6:node7:node12"
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "node5*"
```

## Порядок обновления компонентов (upgrade order)

Компоненты обновляются в том же порядке, в котором устанавливались в playbook:

1. Docker
2. Containerd
3. etcd
4. kubelet и kube-proxy
5. network_plugin (например, Calico)
6. kube-apiserver, kube-scheduler, kube-controller-manager
7. Add-ons (например, KubeDNS)

## Обновление отдельных компонентов (component-based)

Обновление отдельных компонентов через `cluster.yml --tags`. Не покрыто CI, работоспособность не гарантируется, применимо **только к полностью развёрнутым здоровым узлам**. Подробнее про теги: [[versions/v2.30.0/ansible-tags|Ansible-теги]].

- Docker: `cluster.yml --tags=docker`
- etcd: `cluster.yml --tags=etcd`
- etcd без ротации сертификатов: `cluster.yml --tags=etcd --limit=etcd --skip-tags=etcd-secrets`
- kubelet: `cluster.yml --tags=node --skip-tags=k8s-gen-certs`
- master-компоненты Kubernetes: `cluster.yml --tags=master`
- network-плагины: `cluster.yml --tags=network`
- все add-ons: `cluster.yml --tags=apps`
- только helm (при `helm_enabled: true`): `cluster.yml --tags=helm`

Все команды с флагами `-b -i inventory/sample/hosts.ini`.

Переменные etcd см. [[versions/v2.30.0/variables/etcd|Переменные etcd]].

## Обновление до v2.19 (историческое замечание)

`etcd_kubeadm_enabled` объявлена устаревшей в v2.19; та же функциональность достигается установкой `etcd_deployment_type: kubeadm`. С v2.19 переменная `etcd_deployment_type` размещается в `group_vars/all/etcd.yml`, а не в `group_vars/etcd.yml` (из-за проблем со scope). При наличии кластера с etcd, развёрнутым через kubeadm, нужно удалить `etcd_kubeadm_enabled`, перенести `etcd_deployment_type` в `group_vars/all/etcd.yml` и задать `etcd_deployment_type: kubeadm`.

## Обновление системных пакетов (system upgrade)

Обновление APT/YUM-пакетов при cordon-нутых узлах:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e system_upgrade=true
```

- узлы перезагружаются при наличии обновлений пакетов (`system_upgrade_reboot: on-upgrade`);
- значение можно изменить на `always` или `never`;
- при `system_upgrade_reboot` не равном `never` загрузки (downloads) происходят дважды.

## Миграция с Docker на Containerd

> Миграция container engine **официально не поддерживается** Kubespray. Процедура экспериментальная, включает ручные шаги и несколько запусков `cluster.yml`, гарантий работоспособности нет.

С Kubespray 2.18.0 containerd уже является контейнерным движком по умолчанию. При возможности **безопаснее** сбросить (reset) и заново развернуть весь кластер с новым движком, чем мигрировать.

Важные соображения:
- для минимального простоя узлы обрабатываются по одному: cordon и drain перед обработкой каждого;
- если запускать `cluster.yml` разом (без обработки по одному), простой значительно больше, и Docker придётся вручную удалить со всех узлов до запуска playbook;
- пока идёт миграция, никакие другие изменения конфигурации кластера через Kubespray выполнять нельзя;
- требуется полный root-доступ к каждому узлу.

Перед началом скорректировать инвентарь:

```yaml
# Файл: k8s_cluster/k8s-cluster.yml
resolvconf_mode: host_resolvconf
container_manager: containerd

# Файл: etcd.yml
etcd_deployment_type: host
```

Шаги миграции (повторяются для каждого узла):

1. Выбрать один или несколько узлов для обработки. Рекомендуется начать с control plane и etcd вместе, затем каждый worker по отдельности.
2. Cordon и drain узла.
3. Остановить демоны docker и kubelet: `service kubelet stop`, `service docker stop`.
4. Удалить docker и зависимости: `apt-get remove -y --allow-change-held-packages containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras`. Возможна недостающая зависимость `pigz` — `apt-get install pigz`.
5. Запустить `cluster.yml` с `--limit`: `ansible-playbook -i inventory/sample/hosts.ini cluster.yml --limit=NODENAME`. Это переустанавливает containerd; kubelet сразу подхватывает новый движок. Опционально удалить `/var/lib/docker` (`rm -fr /var/lib/docker`). Наблюдать контейнеры — `crictl ps -a`.
6. Заменить аннотацию cri-socket узла (Kubespray этого не делает): `kubectl annotate node NODENAME --overwrite kubeadm.alpha.kubernetes.io/cri-socket=/var/run/containerd/containerd.sock`. Требуется kubeadm для будущих обновлений кластера.
7. Перезагрузить узел перед uncordon.

Замечание: при использовании лог-агрегатора формат логов меняется — docker пишет JSON, containerd использует свой space-delimited формат.

## Источники

- `docs/operations/upgrades.md`
- `docs/upgrades/migrate_docker2containerd.md`
- [[versions/v2.30.0/README|Срез v2.30.0]]
