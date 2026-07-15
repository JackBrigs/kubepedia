---
project: kubespray
kubespray_version: v2.29.0
git_commit: 9991412
source_type: docs
source_paths: [docs/operations/upgrades.md, docs/upgrades/migrate_docker2containerd.md]
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0
retrieved_at: 2026-07-14
topics: [upgrade, migration]
reliability: authoritative
---

# Обновление кластера в v2.29.0

Дайджест построен строго по документации тега `v2.29.0` (commit `9991412`): `docs/operations/upgrades.md` и `docs/upgrades/migrate_docker2containerd.md`. Это выжимка, а не дословный перевод; имена переменных, тегов и команд приведены точно.

## Общий принцип

Kubespray выполняет обновление тем же способом, что и первичное развёртывание: каждый компонент раскладывается в фиксированном порядке (см. раздел «Порядок обновления»). Версии отдельных компонентов можно контролировать явным заданием переменных версий.

Переменные версий компонентов, которыми можно управлять точечно:

- `docker_version`
- `docker_containerd_version` (актуальна при `container_manager == docker`)
- `containerd_version` (актуальна при `container_manager == containerd`)
- `kube_version`
- `etcd_version`
- `calico_version`
- `calico_cni_version`
- `flannel_version`

## Строго последовательное обновление по минорным версиям (ключевое)

> **Предупреждение из документа:** «Do not skip minor releases (patches releases are ok) when upgrading — upgrade by one tag at a time.»

- **Нельзя пропускать минорные релизы** — обновляться нужно по одному тегу за раз. Патч-релизы (третья цифра) пропускать можно.
- Попытка обновиться со старого релиза сразу на самый свежий **не поддерживается** и, скорее всего, что-то сломает (issue #3849).
- Пример допустимого/недопустимого маршрута из документа:
  - `v2.22.0 → v2.23.2 → v2.24.0` : ✓ (по одному минорному тегу, патчи внутри допустимы)
  - `v2.22.0 → v2.24.0` : ✕ (пропущен минорный `v2.23.x`)
- Это ровно тот принцип, на котором построена база знаний: последовательность `v2.29.0 → v2.30.0 → v2.31.0 → ...` без пропусков.

### Процедура множественного обновления

1. Если версия Kubernetes **не задана явно** в инвентаре (`group_vars/k8s_cluster.yml`) — достаточно выполнить `git checkout` следующего тега и запустить `upgrade-cluster.yml`.
2. Если версия **задана явно** в инвентаре — либо обновить её перед запуском, либо передать целевую версию флагом: `-e kube_version=<версия>`. Иначе обновление оставит кластер на прежней версии k8s из инвентаря.
3. Между тегами может потребоваться `pip3 install -r requirements.txt` (замечание в документе).
4. При переходе через границы версий сверять свой инвентарь с sample-инвентарём: форматы переменных между версиями меняются. Пример из документа: между 2.8.5 и 2.9.0 поменялся формат переменных в `k8s_cluster.yml`; если не обновить копию инвентаря — **обновление упадёт**, и первый control plane останется нерабочим до починки и повторного запуска.

## Небезопасное (unsafe) обновление

Обновление отдельно `kube_version` через `cluster.yml` с флагом `-e upgrade_cluster_setup=true`:

```ShellSession
ansible-playbook cluster.yml -i inventory/sample/hosts.ini -e kube_version=1.18.10 -e upgrade_cluster_setup=true
```

Затем повтор с новой версией (`-e kube_version=1.19.7`).

- `upgrade_cluster_setup=true` нужен, чтобы **немедленно** мигрировать деплой компонентов control plane (например, `kube-apiserver`) внутри кластера — то, что обычно делается только при graceful-обновлении (issues #4139, #4736).

## Graceful (плавное) обновление

Для плавного обновления есть отдельный плейбук `upgrade-cluster.yml`, который поддерживает **cordon → drain → uncordon** узлов.

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.19.7
```

- `upgrade-cluster.yml` пригоден **только для обновления уже существующего кластера** — должен быть развёрнут минимум 1 `kube_control_plane`.

### Управление параллелизмом: `serial`

- Число одновременно обновляемых узлов задаётся ansible-переменной `serial`.
- Если `serial` не задан — узлы обновляются пачками по **20 %** доступных узлов.
- `serial=1` — по одному узлу за раз.

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 -e "serial=1"
```

### Паузы в ходе обновления

Паузы **перед** обновлением каждого узла (для инспекции подов, ручных действий):

- `upgrade_node_confirm: true` — пауза перед обновлением каждого узла; продолжение после ручного подтверждения вводом `yes`.
- `upgrade_node_pause_seconds: 60` — пауза на 60 секунд перед обновлением каждого узла; продолжение автоматически.

Паузы **после** обновления узла, но **до** его uncordon (для перезагрузки под обновление ядра, тестирования ещё cordon-нутого узла):

- `upgrade_node_post_upgrade_confirm: true` — пауза после обновления узла до uncordon; продолжение по вводу `yes`.
- `upgrade_node_post_upgrade_pause_seconds: 60` — пауза на 60 секунд после обновления узла до uncordon.

## Пошаговое (по узлам) обновление через `--limit`

Если не нужно обновлять все узлы за один прогон, используется `--limit`.

- **Перед** использованием `--limit` обязательно прогнать `playbooks/facts.yml` без limit, чтобы обновить кэш фактов по всем узлам:

```ShellSession
ansible-playbook playbooks/facts.yml -b -i inventory/sample/hosts.ini
```

- Сначала обновляются группы control plane и etcd (issue #5147):

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "kube_control_plane:etcd"
```

- Затем прочие узлы в любом порядке и количестве:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "node4:node6:node7:node12"
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e kube_version=1.20.7 --limit "node5*"
```

## Порядок обновления компонентов

Компоненты обновляются в том же порядке, в каком устанавливались в плейбуке:

1. Docker
2. Containerd
3. etcd
4. kubelet и kube-proxy
5. network_plugin (например, Calico)
6. kube-apiserver, kube-scheduler, kube-controller-manager
7. Add-ons (например, KubeDNS)

## Обновление отдельных компонентов (component-based)

Позволяет обновлять конкретные компоненты, чтобы снизить риск или сэкономить время. **Не покрыто CI**, работоспособность не гарантируется. Работает только для полностью развёрнутых, здоровых узлов.

- Обновить docker: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=docker`
- Обновить etcd: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=etcd`
- Обновить etcd без ротации сертификатов etcd: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=etcd --limit=etcd --skip-tags=etcd-secrets`
- Обновить kubelet: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=node --skip-tags=k8s-gen-certs`
- Обновить компоненты master: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=master`
- Обновить сетевые плагины: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=network`
- Обновить все add-ons: `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=apps`
- Обновить только helm (если `helm_enabled: true`): `ansible-playbook -b -i inventory/sample/hosts.ini cluster.yml --tags=helm`

Подробности по тегам запуска: [[versions/v2.29.0/ansible-tags|Ansible-теги запуска v2.29.0]].

## Обновление системных пакетов (system upgrade)

Обновление пакетов APT/YUM, пока узлы cordon-нуты:

```ShellSession
ansible-playbook upgrade-cluster.yml -b -i inventory/sample/hosts.ini -e system_upgrade=true
```

- Узлы перезагружаются при наличии обновлений пакетов: `system_upgrade_reboot: on-upgrade` (значение по умолчанию). Можно изменить на `always` или `never`.
- Замечание: загрузки (downloads) произойдут **дважды**, если `system_upgrade_reboot` не равен `never`.

## Историческое предостережение по etcd (обновление до v2.19)

- `etcd_kubeadm_enabled` объявлен устаревшим начиная с v2.19. Та же функциональность достигается заданием `etcd_deployment_type: kubeadm`.
- Развёртывание etcd через kubeadm — экспериментальное; доступно только для новых кластеров или тех, где `etcd_kubeadm_enabled` было `true` при развёртывании.
- С v2.19 переменная `etcd_deployment_type` размещается в `group_vars/all/etcd.yml` (вместо `group_vars/etcd.yml`) из-за проблем со scope. При кластере с etcd, развёрнутым через kubeadm: удалить `etcd_kubeadm_enabled`, перенести `etcd_deployment_type` в `group_vars/all/etcd.yml` и задать `etcd_deployment_type: kubeadm`.

Связанные переменные: [[versions/v2.29.0/variables/etcd|Переменные etcd v2.29.0]].

## Миграция с Docker на Containerd

> **Важно:** миграция container engine **официально не поддерживается** Kubespray. Процедура экспериментальна, покрывает один сценарий и включает ручные шаги и несколько запусков `cluster.yml`.

- С Kubespray 2.18.0 containerd — контейнерный движок по умолчанию. Если есть возможность — **безопаснее** сбросить (reset) и переразвернуть кластер целиком на новом движке.
- Для минимального простоя узлы обрабатываются по одному: cordon/drain перед обработкой. Один прогон `cluster.yml` на всё сразу даёт значительно больший простой. Docker нужно удалять вручную со всех узлов до запуска плейбука (issue #8431).
- Пока миграция не завершена, менять другую конфигурацию кластера через Kubespray нельзя. Нужен полный root-доступ ко всем узлам.

Правки инвентаря перед началом:

```yaml
# Файл: k8s_cluster/k8s-cluster.yml
resolvconf_mode: host_resolvconf
container_manager: containerd

# Файл: etcd.yml
etcd_deployment_type: host
```

Шаги миграции (для каждого узла):

1. Выбрать один или несколько узлов. Рекомендация документа: начать с control plane и etcd вместе, затем каждый worker по отдельности.
2. Cordon и drain узла.
3. Остановить демоны docker и kubelet: `service kubelet stop`, `service docker stop`.
4. Удалить docker и зависимости: `apt-get remove -y --allow-change-held-packages containerd.io docker-ce docker-ce-cli docker-ce-rootless-extras`. Может понадобиться `apt-get install pigz` (для распаковки слоёв образов).
5. Запустить `cluster.yml` с `--limit`: `ansible-playbook -i inventory/sample/hosts.ini cluster.yml --limit=NODENAME`. Это переустанавливает containerd; kubelet сразу подхватывает новый движок. Опционально после этого можно удалить `/var/lib/docker` (`rm -fr /var/lib/docker`). Наблюдать контейнеры: `crictl ps -a`.
6. Заменить аннотацию cri-socket на узле (Kubespray этого не делает): `kubectl annotate node NODENAME --overwrite kubeadm.alpha.kubernetes.io/cri-socket=/var/run/containerd/containerd.sock`. Аннотация нужна kubeadm для будущих обновлений.
7. Перезагрузить узел перед uncordon.

Замечание: при агрегации логов (fluentd+Graylog и т. п.) нужно скорректировать фильтры/парсеры — containerd использует не Json, а собственный формат с разделителем-пробелом.

## Источники

- `docs/operations/upgrades.md` (тег v2.29.0)
- `docs/upgrades/migrate_docker2containerd.md` (тег v2.29.0)
- Ссылки в документе: issues #3849, #4139, #4736, #5147, #8431
- [[versions/v2.29.0/README|Срез v2.29.0]]
