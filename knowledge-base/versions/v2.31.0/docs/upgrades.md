---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/operations/upgrades.md
  - docs/upgrades/migrate_docker2containerd.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - upgrade
  - migration
reliability: authoritative
---

# Обновление кластера в Kubespray v2.31.0

Дайджест документации `docs/` тега v2.31.0 по обновлению Kubernetes и миграции с Docker на containerd. Связанные заметки: [[versions/v2.31.0/ansible-tags|Ansible-теги]], [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]], [[versions/v2.31.0/README|Срез v2.31.0]].

## Общий принцип (docs/operations/upgrades.md)

Kubespray обновляет так же, как разворачивает: каждый компонент укладывается в фиксированном порядке. Версии компонентов можно задавать явно через переменные: `docker_version`, `docker_containerd_version` (при `container_manager: docker`), `containerd_version` (при `container_manager: containerd`), `kube_version`, `etcd_version`, `calico_version`, `calico_cni_version`, `flannel_version`.

> Предупреждение: прыжок со старого релиза сразу на последний **не поддерживается** и, скорее всего, что-то сломает.

## Последовательность минорных версий (Multiple upgrades)

- **Нельзя пропускать минорные релизы** — обновляться строго по одному тегу за раз (патч-релизы пропускать можно).
- Пример: `v2.22.0 → v2.23.2 → v2.24.0` — допустимо; `v2.22.0 → v2.24.0` — недопустимо.
- Если версия Kubernetes **не** задана явно в inventory (`k8s_cluster.yml`) — достаточно сделать `git checkout` следующего тега и запустить `upgrade-cluster.yml`.
- Если `kube_version` задан в inventory — обновить его перед запуском либо передать явно: `-e kube_version=1.11.3`. Иначе кластер останется на прежней версии K8s.
- Между версиями могут меняться форматы переменных и появляться deprecations. Важное историческое предупреждение из документа: форматы переменных в `k8s_cluster.yml` изменились между 2.8.5 и 2.9.0; если не обновить копию inventory — **обновление упадёт**, а первый master останется нерабочим до исправления и повторного запуска.
- Рекомендация: при обновлении сверять расхождения между sample inventory и своим inventory. При обновлении также может понадобиться `pip3 install -r requirements.txt`.

## Небезопасное обновление (Unsafe upgrade)

Обновление только `kube_version` через `cluster.yml` с флагом `-e upgrade_cluster_setup=true`:

```ShellSession
ansible-playbook cluster.yml -i inventory/sample/hosts.ini -e kube_version=1.18.10 -e upgrade_cluster_setup=true
# затем повторить со следующей версией
ansible-playbook cluster.yml -i inventory/sample/hosts.ini -e kube_version=1.19.7 -e upgrade_cluster_setup=true
```

`upgrade_cluster_setup=true` нужен, чтобы немедленно мигрировать деплои компонентов (например kube-apiserver) внутри кластера — то, что обычно делается только в graceful-обновлении. Это НЕ включает cordon/drain — отсюда «unsafe».

## Graceful-обновление (docs/operations/upgrades.md)

Отдельный плейбук `upgrade-cluster.yml` поддерживает cordon, drain и uncordon узлов. Применим **только к существующему** кластеру (нужен минимум 1 уже развёрнутый kube_control_plane).

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.19.7
```

### serial — сколько узлов обновлять одновременно

Ansible-переменная `serial` управляет размером батча. Если не задана — обновление идёт батчами по **20%** доступных узлов. `serial=1` — по одному узлу за раз:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 -e "serial=1"
```

### Пауза в ходе обновления (Pausing the upgrade)

Пауза **перед** обновлением каждого узла:
- `upgrade_node_confirm: true` — пауза до ручного подтверждения (ввод «yes» в терминале);
- `upgrade_node_pause_seconds: 60` — пауза на N секунд, затем автопродолжение.

Пауза **после** обновления узла, но **до** uncordon (например для перезагрузки под ядро):
- `upgrade_node_post_upgrade_confirm: true` — до ручного подтверждения;
- `upgrade_node_post_upgrade_pause_seconds: 60` — на N секунд.

## Обновление по узлам (Node-based upgrade)

Использовать `--limit` для частичного обновления. Перед `--limit` обязательно прогнать `facts.yml` без limit, чтобы обновить кэш фактов всех узлов:

```ShellSession
ansible-playbook playbooks/facts.yml -b -i inventory/sample/hosts.ini
```

Затем сначала обновить control plane и etcd:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "kube_control_plane:etcd"
```

После этого — остальные узлы в любом порядке и количестве:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "node4:node6:node7:node12"
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "node5*"
```

## Обновление до v2.19 (историческая заметка)

`etcd_kubeadm_enabled` устарела в v2.19 — та же функциональность через `etcd_deployment_type: kubeadm`. С 2.19 переменная `etcd_deployment_type` размещается в `group_vars/all/etcd.yml` вместо `group_vars/etcd.yml` (проблемы scope). Если etcd разворачивался через kubeadm — удалить `etcd_kubeadm_enabled`, перенести `etcd_deployment_type` в `group_vars/all/etcd.yml` и задать `kubeadm`. Если `etcd_kubeadm_enabled` не был `true` — изменений не требуется.

## Порядок обновления компонентов (Upgrade order)

Компоненты обновляются в порядке установки:

1. Docker
2. Containerd
3. etcd
4. kubelet и kube-proxy
5. network_plugin (например Calico)
6. kube-apiserver, kube-scheduler, kube-controller-manager
7. Add-ons (например KubeDNS)

### Покомпонентное обновление (Component-based upgrades)

Через Ansible-теги (не покрыто CI, работает только для полностью развёрнутых здоровых узлов). Справочник тегов — [[versions/v2.31.0/ansible-tags|Ansible-теги]]. Примеры:

```ShellSession
# docker
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=docker
# etcd
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=etcd
# etcd без ротации сертификатов etcd
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=etcd --limit=etcd --skip-tags=etcd-secrets
# kubelet
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=node --skip-tags=k8s-gen-certs
# master-компоненты
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=master
# сетевые плагины
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=network
# все аддоны
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=apps
# только helm (при helm_enabled: true)
ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=helm
```

## Обновление системных пакетов (System upgrade)

Обновление APT/YUM-пакетов при закордоненных узлах:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e system_upgrade=true
```

- Узлы перезагружаются при наличии обновлений пакетов (`system_upgrade_reboot: on-upgrade`). Значения: `always` или `never`.
- Загрузки произойдут дважды, если `system_upgrade_reboot` не равен `never`.

## Миграция с Docker на containerd (docs/upgrades/migrate_docker2containerd.md)

> **Официально не поддерживается.** Ручные шаги + многократные запуски `cluster.yml`, без гарантий. Экспериментальные рекомендации. С Kubespray 2.18.0 containerd — движок по умолчанию; безопаснее сбросить и переразвернуть кластер целиком.

Тестовое окружение из документа: Ubuntu 18.04 LTS, baremetal/VM, Kubernetes 1.21.5, Kubespray 2.18.0.

Важно: для минимального downtime узлы обрабатываются по одному (cordon+drain перед каждым). Docker нужно удалять с узлов вручную до запуска плейбука (issue #8431). Во время миграции нельзя менять другую конфигурацию кластера через Kubespray. Нужен полный root-доступ ко всем узлам.

Предварительная правка inventory:

```yaml
# k8s_cluster/k8s-cluster.yml
resolvconf_mode: host_resolvconf
container_manager: containerd

# etcd.yml
etcd_deployment_type: host
```

Шаги (повторяются для каждого узла):
1. Выбрать узлы (рекомендуется начать с control plane + etcd вместе, затем worker'ы по одному).
2. Cordon + drain узла.
3. Остановить демоны: `service kubelet stop`, `service docker stop`.
4. Удалить docker и зависимости: `apt-get remove -y --allow-change-held-packages containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras`. При необходимости `apt-get install pigz` (нужен для распаковки слоёв образов).
5. Запустить `cluster.yml` с `--limit=NODENAME` — переустанавливает containerd, kubelet сразу подхватывает новый движок. Опционально после этого `rm -fr /var/lib/docker`. Проверка контейнеров: `crictl ps -a`.
6. Заменить аннотацию cri-socket на узле (Kubespray этого не делает): `kubectl annotate node NODENAME --overwrite kubeadm.alpha.kubernetes.io/cri-socket=/var/run/containerd/containerd.sock` — нужна kubeadm для будущих апгрейдов.
7. Перезагрузить узел перед uncordon.

Замечание: containerd пишет логи в собственном space-delimited формате (не Docker JSON) — при наличии лог-агрегатора (fluentd+Graylog) нужно скорректировать фильтры/парсеры.

## Источники

- docs/operations/upgrades.md
- docs/upgrades/migrate_docker2containerd.md
- [[versions/v2.31.0/README|Срез v2.31.0]]
