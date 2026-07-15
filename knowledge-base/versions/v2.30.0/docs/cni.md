---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/CNI/cilium.md
  - docs/CNI/cni.md
  - docs/advanced/dns-stack.md
  - docs/advanced/netcheck.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - cni
  - cilium
  - dns
reliability: authoritative
---

# CNI и DNS в v2.30.0

Дайджест документации `docs/` тега v2.30.0 (commit `f4ccdb5`). Из CNI детально проиндексирован только Cilium. Значения по умолчанию и полный список переменных — в [[versions/v2.30.0/variables/cni|Переменные CNI]].

## Обзор поддерживаемых CNI

Kubespray поддерживает несколько сетевых плагинов. В этом срезе детально разобран только **Cilium**. Остальные CNI перечислены ниже со ссылками на их доки в теге и помечены как «не проиндексирован детально».

| CNI | Документация в теге | Статус в базе знаний |
|-----|---------------------|----------------------|
| Cilium | `docs/CNI/cilium.md` | проиндексирован детально (ниже) |
| Calico | `docs/CNI/calico.md` | не проиндексирован детально |
| Flannel | `docs/CNI/flannel.md` | не проиндексирован детально |
| Kube-OVN | `docs/CNI/kube-ovn.md` | не проиндексирован детально |
| Kube-router | `docs/CNI/kube-router.md` | не проиндексирован детально |
| Macvlan | `docs/CNI/macvlan.md` | не проиндексирован детально |
| Multus | `docs/CNI/multus.md` | не проиндексирован детально |

### Плагин «cni» (кастомная конфигурация)

Источник: `docs/CNI/cni.md`.

Плагин `cni` только распаковывает CNI-плагины версии `cni_version` в `/opt/cni/bin` и указывает CRI-реализации container runtime использовать CNI. Предназначен для ручной/кастомной конфигурации CNI (например, ручные таблицы маршрутизации + bridge + loopback вне области Kubespray), а также для неподдерживаемых Kubespray CNI-плагинов, которые вы устанавливаете самостоятельно. После развёртывания вы **обязаны** сами заполнить `/etc/cni/net.d` валидной CNI-конфигурацией.

---

## Cilium (детально)

Источник: `docs/CNI/cilium.md`.

### Непривилегированный агент

По умолчанию Cilium ставится с `securityContext.privileged: false`. В этом режиме нужно задать в инвентаре:

```yml
kube_owner: root
```

### IPAM (управление IP-адресами)

Режим IPAM по умолчанию — «Cluster Scope». Задаётся переменной:

```yml
cilium_ipam_mode: cluster-pool   # например: cluster-pool, kubernetes
```

- `cilium_pool_cidr` — Pod CIDR кластера. По умолчанию берётся из `kube_pods_subnet`. Внимание: если сеть узлов в том же диапазоне — потеряется связность между узлами.
- `cilium_pool_cidr_ipv6` — используется при `cilium_enable_ipv6`; по умолчанию из `kube_pods_subnet_ipv6`.
- `cilium_pool_mask_size` — размер сегмента IP, выделяемого узлу из общего Pod CIDR (`node.ipam.podCIDRs`) в режиме «Cluster Scope». По умолчанию из `kube_network_node_prefix`.
- `cilium_pool_mask_size_ipv6` — то же для IPv6; по умолчанию из `kube_network_node_prefix_ipv6`.

### IP Load Balancer Pools

Пулы LB IPAM задаются переменной `cilium_loadbalancer_ip_pools` (список объектов с `name`, `cidrs`, `ranges` — `start`/`stop`).

### BGP Control Plane

- Включение: `cilium_enable_bgp_control_plane: true`.
- Новый API bgpv2 (Cilium v1.16+): `cilium_bgp_cluster_configs`, `cilium_bgp_peer_configs`, `cilium_bgp_advertisements`, `cilium_bgp_node_config_overrides`.
- Устаревший API (< v1.16): `cilium_bgp_peering_policies`.

### Замена kube-proxy (kube-proxy replacement)

Cilium может работать без kube-proxy через `cilium_kube_proxy_replacement`:
- значение `strict` для версий Cilium < v1.16;
- значение `true` для Cilium v1.16+ (`strict` больше не принимается, но Kubespray сам конвертирует его в `true` на v1.16+).

Без kube-proxy Cilium должен глобально знать адрес kube-apiserver (для агентов и операторов). В этом режиме допустимо использовать только локальный apiserver loadbalancer, и только когда он использует тот же порт, что и kube-apiserver (по умолчанию так и есть).

### Cilium Operator

Дополнительные аргументы контейнера cilium-operator — `cilium_operator_custom_args` (принимает массив или строку). Дополнительные тома — `cilium_operator_extra_volumes` и их монтирование — `cilium_operator_extra_volume_mounts`. Для отладки предусмотрена переменная `CILIUM_DEBUG` (флаг добавлять не требуется).

### Версия и дополнительная конфигурация

- `cilium_version` — версия Cilium (в доке тега пример: `"1.18.6"`).
- `cilium_config_extra_vars` — добавление произвольных ключей в конфиг Cilium.

### Режим выделения identity

Cilium назначает identity каждому endpoint. Поддерживаются два режима:
- `crd` — хранение identity как CRD в Kubernetes (`kubectl get ciliumid`);
- `kvstore` — хранение identity в etcd kvstore.

Имя переменной в доке тега явно не приведено — уточняйте в [[versions/v2.30.0/variables/cni|Переменные CNI]] / defaults роли `network_plugin/cilium`.

### Прозрачное шифрование

Поддерживается IPsec и Wireguard:
- IPsec: `cilium_encryption_enabled: true`, `cilium_encryption_type: "ipsec"`, плюс ключ `cilium_ipsec_key` (base64, генерируется вручную — Kubespray процесс генерации не автоматизирует, но создание секрета берёт на себя).
- Wireguard: `cilium_encryption_enabled: true`, `cilium_encryption_type: "wireguard"`. Доступно с Cilium 1.10.0+, требует Wireguard в режиме ядра на Linux 5.6+.

### Bandwidth Manager

Включение: `cilium_enable_bandwidth_manager: true`. Поддерживает аннотацию Pod `kubernetes.io/egress-bandwidth`. Требует ядро Linux v5.1.x+. Не работает в связке с L7 Cilium Network Policies (для выбранных на egress Pod'ов enforcement отключается).

### Host Firewall

`cilium_enable_host_firewall: true`. Выключен по умолчанию — может разорвать связность кластера.

### Policy Audit Mode

`cilium_policy_audit_mode: true`. В этом режиме сетевые политики не применяются (только аудит влияния). Выключен по умолчанию, в production включать не следует.

### Hubble

```yml
cilium_enable_hubble: true        # поддержка hubble в cilium
cilium_hubble_install: true       # установка hubble-relay, hubble-ui
cilium_hubble_tls_generate: true  # установка hubble-certgen и генерация сертификатов
```

Метрики Hubble: `cilium_enable_hubble_metrics: true` и список `cilium_hubble_metrics` (например: `dns`, `drop`, `tcp`, `flow`, `icmp`, `http`).

### Особенности апгрейда: таймауты rolling-restart

Cilium использует BPF ядра: компиляция при инициализации/обновлении даёт задержку старта, растущую с числом узлов и endpoint'ов. В рамках `cluster.yml` DaemonSet перезапускается, и дефолтные таймауты не подходят для больших кластеров:

```yaml
cilium_rolling_restart_wait_retries_count: 30
cilium_rolling_restart_wait_retries_delay_seconds: 10
```

Суммарное время (`count * delay`) должно быть не меньше `(число_узлов * время_старта_pod)`. Дефолтные CPU requests/limits для Cilium — консервативные `100m:500m`, для больших кластеров лимит стоит увеличить.

---

## DNS-стек

Источник: `docs/advanced/dns-stack.md`.

Kubespray настраивает Kubernetes DNS как авторитативный DNS-сервер для домена `dns_domain` и его поддоменов `svc`, `default.svc` (всего до `ndots: 5` уровней). Узлы вне кластера (внешнее хранилище, отдельная группа etcd) считаются non-cluster — их DNS-резолвинг настраивает пользователь.

### Глобальные переменные DNS

- `ndots` — значение `ndots` в `/etc/resolv.conf`. Высокий `ndots` вместе с множеством search-доменов ухудшает производительность DNS.
- `dns_timeout` — значение `timeout` в `/etc/resolv.conf`.
- `dns_attempts` — значение `attempts` в `/etc/resolv.conf`.
- `searchdomains` — дополнительные search-домены сверх кластерных (`default.svc.{{ dns_domain }}`, `svc.{{ dns_domain }}`). Лимит: 6 имён / 256 символов (с учётом дефолтных — фактически 4 имени / 239 символов).
- `remove_default_searchdomains: true` — убирает дефолтные кластерные search-домены.
- `nameservers` — используется только при `resolvconf_mode: host_resolvconf`; добавляются в `/etc/resolv.conf` узлов *после* `upstream_dns_servers` как резервные. Если не задано — выбирается дефолтный резолвер (в зависимости от cloud provider или `8.8.8.8`).
- `upstream_dns_servers` — DNS-серверы, добавляемые *после* кластерного DNS; используются всеми режимами `resolvconf_mode` как резерв, важны на раннем этапе развёртывания.
- `dns_upstream_forward_extra_opts` — словарь опций для forward-блока coredns/nodelocaldns.
- `coredns_kubernetes_extra_opts` — доп. опции для kubernetes-плагина coredns.
- `coredns_kubernetes_extra_domains` — доп. домены, пересылаемые в kubernetes-плагин coredns.
- `coredns_additional_configs` — произвольная доп. конфигурация CoreDNS.
- `coredns_rewrite_block` — блок плагина rewrite для внутреннего переписывания сообщений.
- `coredns_external_zones` — массив внешних зон, куда coredns пересылает запросы (вставляется перед дефолтной kubernetes-зоной).
- `dns_etchosts` — содержимое hosts-файла для coredns (и nodelocaldns, если включён).
- `enable_coredns_reverse_dns_lookups` — обратные DNS-запросы в coredns. По умолчанию `true`.
- `coredns_default_zone_cache_block` — строковый блок настройки кэширования CoreDNS на дефолтной зоне.
- `old_dns_domains` — старые/дополнительные dns-домены (при смене `dns_domain`), чтобы запросы по старому домену обрабатывались корректно.
- `systemd_resolved_disable_stub_listener` — задаёт `DNSStubListener=no` при использовании systemd-resolved. По умолчанию `true` на Flatcar; включают при ошибках CoreDNS `address already in use`.

### dns_mode (настройка кластерного DNS)

- `coredns` (по умолчанию) — CoreDNS как основной кластерный DNS для всех запросов.
- `coredns_dual` — CoreDNS + вторичный стек CoreDNS.
- `manual` — coredns не ставится; задаётся `manual_dns_server`, настраиваемый на узлах для Pod DNS.
- `none` — DNS не устанавливается вовсе; кластер остаётся без работающего DNS.

### resolvconf_mode (DNS для hostNetwork-подов и не-k8s контейнеров)

- `host_resolvconf` (по умолчанию) — модифицирует `/etc/resolv.conf` узлов и конфиг dhclient. Реализован в 2 стадии: ранняя (`dns_early: true`) использует `upstream_dns_servers` и `nameservers`, затем перенастройка на кластерный DNS первым. Существующие записи из `/etc/resolv.conf` (включая base/head/cloud-init и dhclient) вычищаются.
- `docker_dns` — добавляет флаги `--dns`/`--dns-search`/`--dns-opt` демону docker. Порядок nameservers: кластерный → `upstream_dns_servers` → системные. DNS-опции по умолчанию: `ndots:{{ ndots }}`, `timeout:2`, `attempts:2`; переопределяются через `docker_dns_options`.
- `none` — ничего не делает с `/etc/resolv.conf`; hostNetwork-поды и не-k8s контейнеры не резолвят имена сервисов кластера.

### Nodelocal DNS cache

`enable_nodelocaldns: true` — поды обращаются к локальному кэширующему агенту DNS на том же узле (минуя iptables DNAT и conntrack). **С релиза 2.10 включён по умолчанию.**

- `nodelocaldns_external_zones` — массив внешних зон для nodelocaldns.
- `dns_etchosts` — см. раздел coredns выше (общая переменная).
- `nodelocaldns_additional_configs` — доп. конфигурация.
- `enable_nodelocaldns_secondary: true` — резервный nodelocaldns-под на каждом узле (HA). Внимание: при включённом secondary primary перестаёт снимать свои iptables-правила — при одновременном отказе обоих возможен DNS-blackout.
- `nodelocaldns_secondary_skew_seconds: 5` — временная дельta (сек) выживания secondary при одновременном обновлении обоих daemonset.

### Ограничения DNS

- Нет способа настроить форвардинг неавторитативных запросов Kubedns к произвольным рекурсивным резолверам.
- Нет способа задать кастомный `ndots` для SkyDNS.
- `searchdomains`: лимит 6 имён / 256 символов (фактически 4 / 239 из-за дефолтных `svc`, `default.svc`; с `remove_default_searchdomains: true` — снова 6).
- `nameservers`: лимит 3 сервера, из них 1 слот зарезервирован под нужды кластера, т.е. не более 2 кастомных; смягчается через `upstream_dns_servers`.

---

## Network Checker (netcheck)

Источник: `docs/advanced/netcheck.md`.

При `deploy_netchecker: true` (по умолчанию `false`) Kubespray разворачивает Network Checker Application из сторонних образов `mirantis/k8s-netchecker` (сервер + агенты). Приложение автоматически проверяет pod-to-pod связность через cluster IP и работу DNS-резолвинга; проверки идут периодически, покрывают standard и host network поды. Kubespray только разворачивает приложение, но не запускает проверку.

Отчёт о связности по кластеру:

```
curl http://localhost:31081/api/v1/connectivity_check
```

Переменные:
- `netchecker_port: 31081`
- `agent_report_interval: 15`
- `netcheck_namespace: default`

Приложение проверяет DNS-резолвинг FQDN вида `netcheck_namespace.dns_domain` (например `netchecker-service.default.svc.cluster.local`). При развёртывании в неdefault-namespace нужно скорректировать `searchdomains`, чтобы search-домены содержали этот namespace.

---

## Источники

- `docs/CNI/cilium.md` — https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0/docs/CNI/cilium.md
- `docs/CNI/cni.md` — https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0/docs/CNI/cni.md
- `docs/advanced/dns-stack.md` — https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0/docs/advanced/dns-stack.md
- `docs/advanced/netcheck.md` — https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0/docs/advanced/netcheck.md

См. также: [[versions/v2.30.0/variables/cni|Переменные CNI]] · [[versions/v2.30.0/README|Срез v2.30.0]]
