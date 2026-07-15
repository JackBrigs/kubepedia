---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/CNI/cilium.md
  - docs/CNI/cni.md
  - docs/advanced/dns-stack.md
  - docs/advanced/netcheck.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - cni
  - cilium
  - dns
reliability: authoritative
---

# CNI и DNS в v2.31.0 (дайджест документации)

Дайджест по разделам `docs/CNI/` и `docs/advanced/` тега `v2.31.0`.
Детально проиндексирован только **Cilium** (см. `docs/CNI/cilium.md`). Прочие CNI
перечислены в конце с пометкой «не проиндексирован детально».

Переменные см. в [[versions/v2.31.0/variables/cni|Переменные CNI]].

---

## Cilium (`docs/CNI/cilium.md`)

### Непривилегированный агент
По умолчанию Cilium ставится с `securityContext.privileged: false`. Требуется
задать в инвентаре:

- `kube_owner: root`

### Управление IP-адресами (IPAM)
IPAM отвечает за выделение и управление IP для endpoint'ов Cilium. Режим по умолчанию — «Cluster Scope».

- `cilium_ipam_mode` — режим IPAM (например `cluster-pool`, `kubernetes`).
- `cilium_pool_cidr` — Pod CIDR кластера. По умолчанию берёт `kube_pods_subnet`.
  Предупреждение: если сеть узлов в том же диапазоне — потеря связности с другими узлами.
- `cilium_pool_cidr_ipv6` — используется при `cilium_enable_ipv6`. По умолчанию `kube_pods_subnet_ipv6`.
- `cilium_pool_mask_size` — размер сегмента, выделяемого из общего Pod CIDR на узел (`node.ipam.podCIDRs`).
  По умолчанию `kube_network_node_prefix`. Применяется в режиме «Cluster Scope».
- `cilium_pool_mask_size_ipv6` — то же для IPv6. По умолчанию `kube_network_node_prefix_ipv6`.

### IP Load Balancer Pools
- `cilium_loadbalancer_ip_pools` — пулы IP для LB IPAM (поля `name`, `cidrs`, `ranges` со `start`/`stop`).

### BGP Control Plane
- `cilium_enable_bgp_control_plane: true` — включает BGP Control Plane.

Новый BGP API v2 (bgpv2, Cilium v1.16+) — набор ресурсов:
- `cilium_bgp_cluster_configs` — BGP-инстансы (`bgpInstances`, `localASN`, `peers`, `nodeSelector`).
- `cilium_bgp_peer_configs` — конфигурация пиров (`gracefulRestart`, `families`, advertisements).
- `cilium_bgp_advertisements` — анонсы (`advertisementType`: `PodCIDR`, `Service`; communities, selector).
- `cilium_bgp_node_config_overrides` — переопределения на уровне узла (`routerID`, `localPort`, `peers`).

Legacy BGP (< v1.16):
- `cilium_bgp_peering_policies` — политики BGP-пиринга (`virtualRouters`, `localASN`, `neighbors`).

### Замена kube-proxy
- `cilium_kube_proxy_replacement` — `strict` (< v1.16) или `true` (v1.16+; `strict` больше
  не принимается, kubespray конвертирует его в `true` для v1.16+).
  Без kube-proxy Cilium нужен адрес kube-apiserver, задаётся глобально для всех компонентов;
  в этом режиме используется только localhost apiserver loadbalancer на том же порту, что и kube-apiserver.

### Cilium Operator
- `cilium_operator_custom_args` — доп. аргументы контейнера cilium-operator (массив или строка).
- `cilium_operator_extra_volumes` / `cilium_operator_extra_volume_mounts` — доп. тома и их монтирование.
- Для отладки использовать переменную `CILIUM_DEBUG`, а не кастомный флаг.

### Версия Cilium
- `cilium_version: "1.19.3"` — в v2.31.0 пример версии обновлён с `1.18.6` (v2.30.0) на `1.19.3`.

### Прочая конфигурация
- `cilium_config_extra_vars` — произвольные ключи в ConfigMap (например `enable-endpoint-routes: true`).
- Режим выделения identity: `crd` (CRD, `kubectl get ciliumid`) или `kvstore` (identities в etcd kvstore).
  Конкретное имя переменной в этом doc не указано — см. `variables/cni`.

### Прозрачное шифрование
- `cilium_encryption_enabled: true`
- `cilium_encryption_type` — `ipsec` или `wireguard`.
- `cilium_ipsec_key` — для IPsec; секретный ключ задаётся вручную (kubespray не генерирует), base64.
- Wireguard: доступен с Cilium 1.10.0+; требует Wireguard в kernel-mode на Linux 5.6+.

### Дополнительные функции
- `cilium_enable_bandwidth_manager: true` — Bandwidth Manager (аннотация `kubernetes.io/egress-bandwidth`).
  Требует kernel v5.1.x+; не работает вместе с L7 Cilium Network Policies.
- `cilium_enable_host_firewall: true` — Host Firewall (по умолчанию выключен, может нарушить связность).
- `cilium_policy_audit_mode: true` — режим аудита политик (политики не применяются; не для прод).

### Hubble
- `cilium_enable_hubble: true` — поддержка Hubble.
- `cilium_hubble_install: true` — установка hubble-relay, hubble-ui.
- `cilium_hubble_tls_generate: true` — hubble-certgen и генерация сертификатов.
- `cilium_enable_hubble_metrics: true` + `cilium_hubble_metrics` (список: `dns`, `drop`, `tcp`, `flow`, `icmp`, `http`).

### Замечания по обновлению
- Cilium DaemonSet перезапускается в рамках `cluster.yml`; из-за BPF-компиляции старт долгий и масштабируется с числом узлов/endpoint'ов.
- `cilium_rolling_restart_wait_retries_count: 30`
- `cilium_rolling_restart_wait_retries_delay_seconds: 10`
- Правило: суммарное время (count * delay) ≥ `число_узлов * время_старта_пода_Cilium`.
- По умолчанию CPU requests/limits пода Cilium — 100m:500m (консервативно, медленный старт).

---

## CNI (generic, `docs/CNI/cni.md`)

Плагин `cni` только распаковывает CNI-плагины версии `cni_version` в `/opt/cni/bin`
и указывает CRI использовать cni. Предназначен для кастомной конфигурации CNI
(ручные таблицы маршрутизации + bridge + loopback вне охвата kubespray) и для
неподдерживаемых kubespray CNI, устанавливаемых вручную после. После развёртывания
необходимо самостоятельно заполнить `/etc/cni/net.d` валидной конфигурацией CNI.

---

## DNS-стек (`docs/advanced/dns-stack.md`)

Kubespray настраивает Kubernetes DNS как authoritative-сервер для `dns_domain`
и поддоменов `svc`, `default.svc` (макс. `ndots: 5` уровней). Узлы вне кластера
(внешнее хранилище, отдельная группа etcd) считаются non-cluster — DNS для них настраивает пользователь.

### Глобальные переменные DNS
- `ndots` — значение `ndots` в `/etc/resolv.conf`. Высокий `ndots` + много search-доменов → падение производительности DNS.
- `dns_timeout` — значение `timeout` в `/etc/resolv.conf`.
- `dns_attempts` — значение `attempts` в `/etc/resolv.conf`.
- `searchdomains` — доп. search-домены сверх кластерных (`default.svc.{{ dns_domain }}`, `svc.{{ dns_domain }}`).
  Лимит систем: 6 имён / 256 символов суммарно (с учётом кластерных фактически 4 имени / 239 символов).
- `remove_default_searchdomains: true` — убирает кластерные search-домены по умолчанию (возвращает лимит к 6 именам).
- `nameservers` — только для `resolvconf_mode: host_resolvconf`; добавляются в `/etc/resolv.conf`
  ПОСЛЕ `upstream_dns_servers` как резервные. Если не задано — выбирается дефолтный резолвер (по облаку или `8.8.8.8`).
- `upstream_dns_servers` — DNS-серверы, добавляемые ПОСЛЕ кластерного DNS; используются всеми `resolvconf_mode`.
  Резерв на раннем этапе развёртывания, пока кластерный DNS недоступен.

### CoreDNS / nodelocaldns конфигурация
- `dns_upstream_forward_extra_opts` — опции блока forward в CoreDNS/nodelocaldns (словарь).
- `coredns_kubernetes_extra_opts` — доп. опции плагина kubernetes в CoreDNS.
- `coredns_kubernetes_extra_domains` — доп. домены, форвардящиеся в плагин kubernetes.
- `coredns_additional_configs` — доп. конфигурация CoreDNS.
- `coredns_rewrite_block` — блок плагина rewrite (внутреннее переписывание сообщений).
- `coredns_external_zones` — массив внешних зон для форварда (поля `zones`, `nameservers`, `cache`, `rewrite`);
  вставляется перед дефолтной kubernetes-зоной. Можно задавать как YAML или INI.
- `dns_etchosts` — содержимое hosts-файла для CoreDNS (и nodelocaldns, если включён).
- `enable_coredns_reverse_dns_lookups` — обратные DNS-запросы в CoreDNS. По умолчанию `true`.
- `coredns_default_zone_cache_block` — строковый блок настройки кэширования дефолтной зоны (плагин cache).
- `old_dns_domains` — обработка старых/дополнительных dns_domain при смене домена кластера.
- `systemd_resolved_disable_stub_listener` — `DNSStubListener=no` для systemd-resolved.
  По умолчанию `true` на Flatcar; включать при ошибках CoreDNS `address already in use`.

### dns_mode (настройка кластерного DNS)
- `coredns` (по умолчанию) — CoreDNS как основной кластерный DNS.
- `coredns_dual` — CoreDNS + вторичный стек CoreDNS.
- `manual` — CoreDNS не ставится; задаётся `manual_dns_server`, настраиваемый на узлах для DNS подов.
- `none` — DNS не устанавливается вовсе (кластер функционально нерабочий).

### resolvconf_mode (DNS для hostNetwork-подов и не-k8s контейнеров)
- `host_resolvconf` (по умолчанию) — правит `/etc/resolv.conf` хостов и dhclient на кластерный DNS.
  Два этапа: ранний (`dns_early: true`) с `upstream_dns_servers`/`nameservers`, затем переключение на кластерный DNS первым.
  Существующие записи в `/etc/resolv.conf` вычищаются (включая base/head/cloud-init и dhclient).
- `docker_dns` — добавляет daemon docker флаги `--dns/--dns-search/--dns-opt`.
  Опции переопределяются через `docker_dns_options` (по умолчанию `ndots:{{ ndots }}`, `timeout:2`, `attempts:2`).
- `none` — `/etc/resolv.conf` не трогается; hostNetwork-поды и не-k8s контейнеры не резолвят имена сервисов кластера.

### Nodelocal DNS cache
- `enable_nodelocaldns` — локальный кэширующий агент DNS на каждом узле (обход iptables DNAT и conntrack).
  Включён по умолчанию начиная с релиза 2.10.
- `nodelocaldns_external_zones` — внешние зоны для nodelocaldns (`zones`, `nameservers`, `cache`).
- `nodelocaldns_additional_configs` — доп. конфигурация.
- `enable_nodelocaldns_secondary: true` — HA: дублирующий nodelocaldns-под на узле.
  Замечание: при включённом secondary primary больше не убирает свои iptables-правила — при одновременном сбое обоих подов на узле возможен DNS-blackout.
- `nodelocaldns_secondary_skew_seconds: 5` — допуск (сек) выживания secondary при одновременном обновлении обоих daemonset'ов.

### Ограничения DNS (из doc)
- Нет настройки forward для запросов, на которые SkyDNS не отвечает с authority.
- Нет способа задать кастомный `ndots` для SkyDNS.
- `searchdomains`: лимит 6 имён / 256 символов (с дефолтными поддоменами фактически 4 / 239).
- `nameservers`: лимит 3 серверов, из них 1 зарезервирован под нужды кластера (фактически до 2 кастомных).

---

## Network Checker (`docs/advanced/netcheck.md`)

- `deploy_netchecker` — развёртывание Network Checker (образы `mirantis/k8s-netchecker`).
  По умолчанию `false`. Проверяет pod-to-pod связность через cluster IP и работу DNS-резолва.
  Kubespray только разворачивает приложение, но сам проверку не запускает (агенты запускают периодически).
- Отчёт: `curl http://localhost:31081/api/v1/connectivity_check`.
- Переменные приложения:
  - `netchecker_port: 31081`
  - `agent_report_interval: 15`
  - `netcheck_namespace: default`
- Приложение проверяет FQDN вида `netcheck_namespace.dns_domain` (например `netchecker-service.default.svc.cluster.local`).
  При смене namespace нужно скорректировать `searchdomains`.

---

## Прочие CNI (не проиндексированы детально)

По условию проекта из CNI детально индексируется только Cilium. Следующие
документы присутствуют на теге v2.31.0, но детально не разбирались:

- `docs/CNI/calico.md`
- `docs/CNI/flannel.md`
- `docs/CNI/kube-ovn.md`
- `docs/CNI/kube-router.md`
- `docs/CNI/macvlan.md`
- `docs/CNI/multus.md`

---

## Источники

- `docs/CNI/cilium.md` (детально)
- `docs/CNI/cni.md`
- `docs/advanced/dns-stack.md`
- `docs/advanced/netcheck.md`
- Тег: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0 (commit `1c9add4`)

Связанные заметки: [[versions/v2.31.0/variables/cni|Переменные CNI]], [[versions/v2.31.0/README|Срез v2.31.0]]
