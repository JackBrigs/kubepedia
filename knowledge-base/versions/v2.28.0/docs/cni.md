---
project: kubespray
kubespray_version: v2.28.0
git_commit: 63cdf87
source_type: docs
source_paths:
  - docs/CNI/cilium.md
  - docs/CNI/cni.md
  - docs/advanced/dns-stack.md
  - docs/advanced/netcheck.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0
retrieved_at: 2026-07-15
topics:
  - cni
  - cilium
  - dns
reliability: authoritative
---

# CNI и DNS-стек в v2.28.0

Дайджест документации `docs/` тега v2.28.0. В проекте детально индексируется только CNI **Cilium**; остальные плагины перечислены справочно. Также разобран DNS-стек (CoreDNS / nodelocaldns) и утилита проверки сети netchecker.

> Отличия от v2.29.1: (1) в `docs/CNI/cilium.md` тега v2.28.0 пример версии — `cilium_version: "1.17.3"` (в v2.29.1 — `"1.18.4"`); (2) в v2.28.0 ещё присутствует CNI **Weave** (`docs/CNI/weave.md`), удалённый в v2.29.1. Файлы `cni.md`, `dns-stack.md`, `netcheck.md` идентичны v2.29.1.

Связанные заметки: [[versions/v2.28.0/variables/cni|Переменные CNI]] · [[versions/v2.28.0/ansible-tags|Ansible-теги]] · [[versions/v2.28.0/README|Срез v2.28.0]].

---

## Cilium (детально)

Источник: `docs/CNI/cilium.md`.

### IPAM (управление IP-адресами)

- Режим задаётся `cilium_ipam_mode`. По умолчанию — «Cluster Scope» (`cluster-pool`). Другие значения, например, `kubernetes`.
- `cilium_pool_cidr` — CIDR пула Pod-адресов кластера. По умолчанию берётся из `kube_pods_subnet`. Предупреждение: если сеть узлов лежит в том же диапазоне, будет потеряна связность с другими узлами.
- `cilium_pool_cidr_ipv6` — CIDR IPv6 пула при `cilium_enable_ipv6`. По умолчанию `kube_pods_subnet_ipv6`.
- `cilium_pool_mask_size` — размер сегмента, выделяемого узлу из кластерного Pod CIDR (`node.ipam.podCIDRs`) в режиме Cluster Scope. По умолчанию `kube_network_node_prefix`.
- `cilium_pool_mask_size_ipv6` — то же для IPv6-пула. По умолчанию `kube_network_node_prefix_ipv6`.

### IP Load Balancer Pools

- `cilium_loadbalancer_ip_pools` — список пулов LB IPAM с полями `name`, `cidrs`, `ranges` (`start`/`stop`).

### BGP Control Plane

- Включается через `cilium_enable_bgp_control_plane: true`.
- Новый BGPv2 API (Cilium v1.16+) управляется набором CRD:
  - `cilium_bgp_cluster_configs` — экземпляры BGP (`bgpInstances`, `localASN`, `peers`, `nodeSelector`).
  - `cilium_bgp_peer_configs` — конфигурации пиров (`gracefulRestart`, `families` с `afi`/`safi`/`advertisements`).
  - `cilium_bgp_advertisements` — анонсы (`advertisementType: PodCIDR | Service`, атрибуты BGP-communities, селекторы).
  - `cilium_bgp_node_config_overrides` — переопределения на уровне узла (`routerID`, `localPort`, локальные адреса пиров).
- Легаси BGP Peering Policies (Cilium < v1.16): `cilium_bgp_peering_policies` (`virtualRouters`, `localASN`, `neighbors`, `serviceSelector`).

### Kube-proxy replacement

- Cilium может работать без kube-proxy: `cilium_kube_proxy_replacement`.
- Значения: `strict` (для Cilium < v1.16) или `true` (Cilium v1.16+ больше не принимает `strict`; kubespray сам конвертирует `strict` → `true` при v1.16+).
- В этом режиме Cilium (агенты и оператор) должен глобально знать адрес kube-apiserver. Использовать локальный apiserver-loadbalancer можно только если он слушает тот же порт, что и kube-apiserver (по умолчанию так и есть).

### Cilium Operator

- Оператор выполняет задачи уровня кластера (один раз на кластер, а не на каждый узел), не служит целям установки.
- Доп. аргументы контейнера: `cilium_operator_custom_args` (массив или строка). Для отладки использовать переменную `CILIUM_DEBUG`, а не отдельный флаг.
- Доп. тома: `cilium_operator_extra_volumes` + монтирование `cilium_operator_extra_volume_mounts`.

### Версия и произвольная конфигурация

- Версия Cilium — `cilium_version` (пример в доке тега v2.28.0: `"1.17.3"`).
- Произвольные параметры конфигурации через `cilium_config_extra_vars` (словарь, например `enable-endpoint-routes: true`).

### Режим выделения identity

- Cilium назначает identity каждому endpoint для базового контроля связности. Два режима:
  - `crd` — identity хранятся как CRD в Kubernetes (`kubectl get ciliumid`).
  - `kvstore` — identity хранятся в etcd kvstore.

### Прозрачное шифрование (Transparent Encryption)

- Шифрование трафика между endpoint'ами и host-трафика: IPsec или Wireguard.
- Включение: `cilium_encryption_enabled: true` + `cilium_encryption_type: "ipsec"` либо `"wireguard"`.
- IPsec дополнительно требует секретный ключ `cilium_ipsec_key` (передаётся в base64; kubespray сам создаёт секрет, но генерацию ключа не автоматизирует).
- Wireguard доступен только в Cilium 1.10.0+; kubespray поддерживает дистрибутивы с Wireguard в режиме ядра на Linux 5.6+.

### Прочие возможности

- **Bandwidth Manager** — `cilium_enable_bandwidth_manager: true`. Поддерживает аннотацию `kubernetes.io/egress-bandwidth`. Требует ядро Linux 5.1.x+. Не работает совместно с L7 Cilium Network Policies (для выбранных на egress Pod'ов enforcement отключается).
- **Host Firewall** — `cilium_enable_host_firewall: true`. По умолчанию выключен (может нарушить связность кластера).
- **Policy Audit Mode** — `cilium_policy_audit_mode: true`. Политики не применяются, только оценивается их влияние. По умолчанию выключен, в проде включать не следует.

### Hubble (наблюдаемость)

- Установка (в `k8s-net-cilium.yml`):
  - `cilium_enable_hubble: true` — поддержка hubble в Cilium.
  - `cilium_hubble_install: true` — установка hubble-relay, hubble-ui.
  - `cilium_hubble_tls_generate: true` — установка hubble-certgen и генерация сертификатов.
- Проверка UI: `kubectl port-forward -n kube-system svc/hubble-ui 12000:80`, далее `http://localhost:12000/`.
- Метрики: `cilium_enable_hubble_metrics: true` + список `cilium_hubble_metrics` (`dns`, `drop`, `tcp`, `flow`, `icmp`, `http`).

### Замечания по обновлению

- Cilium использует BPF ядра: быстрый рантайм, но компиляция при инициализации/обновлении даёт задержку. Pod'ы DaemonSet Cilium могут стартовать долго — время растёт с числом узлов и endpoint'ов.
- В рамках `cluster.yml` DaemonSet перезапускается; дефолтные таймауты не подходят для больших кластеров.
- Настройка таймаутов ожидания rolling-restart:
  - `cilium_rolling_restart_wait_retries_count: 30`
  - `cilium_rolling_restart_wait_retries_delay_seconds: 10`
  - Суммарное время (`count * delay`) должно быть не меньше `(число_узлов * cilium_pod_start_time)`.
- Дефолтные CPU requests/limits Cilium-подов консервативны (`100m`/`500m`), что замедляет старт; при больших кластерах CPU-лимит стоит поднять.

> Примечание: режимы маршрутизации (tunnel / native routing) и подробные значения по умолчанию в тексте `docs/CNI/cilium.md` тега v2.28.0 отдельными разделами не описаны — конкретные дефолты и режим датаплейна см. в [[versions/v2.28.0/variables/cni|переменных CNI]] (роль `roles/network_plugin/cilium/defaults`).

---

## Универсальный плагин CNI

Источник: `docs/CNI/cni.md`.

Плагин `cni` только распаковывает CNI-плагины версии `cni_version` в `/opt/cni/bin` и указывает CRI-рантайму использовать CNI. Предназначен для собственной конфигурации CNI (кастомные таблицы маршрутизации + bridge + loopback вне рамок kubespray) и для неподдерживаемых kubespray плагинов, устанавливаемых отдельно. После установки пользователь обязан сам заполнить `/etc/cni/net.d` валидной конфигурацией CNI.

---

## Прочие CNI-плагины (не проиндексированы детально)

По правилам проекта из CNI детально разбирается только Cilium. Остальные плагины перечислены справочно:

- Calico — `docs/CNI/calico.md` — не проиндексирован детально.
- Flannel — `docs/CNI/flannel.md` — не проиндексирован детально.
- Weave — `docs/CNI/weave.md` — не проиндексирован детально (присутствует в v2.28.0; удалён в v2.29.1).
- Kube-OVN — `docs/CNI/kube-ovn.md` — не проиндексирован детально.
- Kube-router — `docs/CNI/kube-router.md` — не проиндексирован детально.
- Macvlan — `docs/CNI/macvlan.md` — не проиндексирован детально.
- Multus — `docs/CNI/multus.md` — не проиндексирован детально.

---

## DNS-стек (CoreDNS / nodelocaldns)

Источник: `docs/advanced/dns-stack.md`.

Kubespray настраивает Kubernetes DNS как авторитетный DNS-сервер для домена `dns_domain` и его поддоменов `svc`, `default.svc` (всего до `ndots: 5` уровней). Узлы вне кластера (внешнее хранилище, отдельная группа etcd) считаются non-cluster — их DNS настраивает пользователь.

### Глобальные DNS-переменные

- `ndots` — значение ndots в `/etc/resolv.conf`. Много search-доменов при высоком ndots ухудшают производительность DNS.
- `dns_timeout` — timeout в `/etc/resolv.conf`.
- `dns_attempts` — attempts в `/etc/resolv.conf`.
- `searchdomains` — дополнительные search-домены (сверх кластерных `default.svc.{{ dns_domain }}`, `svc.{{ dns_domain }}`). Лимит систем: 6 имён и 256 символов суммарно.
- `remove_default_searchdomains: true` — убирает кластерные search-домены по умолчанию.
- `nameservers` — используется только при `resolvconf_mode: host_resolvconf`; добавляется в `/etc/resolv.conf` хостов **после** `upstream_dns_servers` как резервные. Если не задано — выбирается дефолтный резолвер (в зависимости от cloud provider или `8.8.8.8`).
- `upstream_dns_servers` — DNS-серверы, добавляемые **после** кластерного DNS. Используются всеми `resolvconf_mode`; резерв на ранней стадии развёртывания, когда кластерного DNS ещё нет.
- `dns_upstream_forward_extra_opts` — опции forward-блока в конфигурации coredns и nodelocaldns (словарь). По умолчанию — только хардкод-опции из шаблонов `coredns-config.yml.j2` и `nodelocaldns-config.yml.j2`.

### Дополнительная конфигурация CoreDNS

- `coredns_kubernetes_extra_opts` — доп. опции плагина kubernetes.
- `coredns_kubernetes_extra_domains` — доп. домены для плагина kubernetes.
- `coredns_additional_configs` — произвольная доп. конфигурация CoreDNS.
- `coredns_rewrite_block` — блок плагина rewrite для внутреннего переписывания запросов.
- `coredns_external_zones` — массив внешних зон, куда coredns форвардит запросы; вставляется перед kubernetes-зоной. Поля: `zones`, `nameservers`, `cache`, опц. `rewrite`. По умолчанию не задано.
- `dns_etchosts` — контент, используемый coredns (и nodelocaldns) как файл `/etc/hosts`.
- `enable_coredns_reverse_dns_lookups` — обратные DNS-запросы в конфиге coredns. По умолчанию `true`.
- `coredns_default_zone_cache_block` — строковый блок настройки кэширования CoreDNS для дефолтной зоны (плагин cache: max TTL, success, denial, prefetch).
- `old_dns_domains` — старые/дополнительные dns-домены; coredns и nodelocaldns начинают корректно обрабатывать запросы к старому домену (полезно при смене `dns_domain`).
- `systemd_resolved_disable_stub_listener` — задаёт `DNSStubListener=no` при systemd-resolved. По умолчанию `true` на Flatcar; помогает при ошибках CoreDNS `address already in use`.

### dns_mode (как настраивается кластерный DNS)

- `coredns` (по умолчанию) — CoreDNS как основной кластерный DNS для всех запросов.
- `coredns_dual` — CoreDNS основной плюс вторичный стек CoreDNS.
- `manual` — coredns не ставится; на узлах настраивается `manual_dns_server` для обработки Pod DNS (для собственного DNS-сервера после развёртывания).
- `none` — DNS-решение не ставится вовсе; кластер остаётся без функционирующего DNS.

### resolvconf_mode (DNS для hostNetwork Pod'ов и не-k8s контейнеров)

- `host_resolvconf` (по умолчанию) — модифицирует `/etc/resolv.conf` хостов и конфиг dhclient, указывая на кластерный DNS. Реализован в 2 стадии: сначала (`dns_early: true`) используются `upstream_dns_servers` и `nameservers`, затем перенастраивается на кластерный DNS первым, остальные — как резерв. Существующие записи в `/etc/resolv.conf` вычищаются (включая base/head/cloud-init и dhclient).
- `docker_dns` — настраивает демон docker флагами `--dns`/`--dns-search`/`--dns-opt`. Добавляет кластерный nameserver, `upstream_dns_servers`, системные nameservers; search-домены — кластерные + `searchdomains` + системные; опции — `ndots:{{ ndots }}`, `timeout:2`, `attempts:2` (переопределяются через `docker_dns_options`). Для обычных Pod'ов k8s игнорирует эти опции; для `hostNetwork: true` — DNS настраивает docker.
- `none` — ничего не делает с `/etc/resolv.conf`; `hostNetwork: true` Pod'ы и не-k8s контейнеры не смогут резолвить сервисные имена кластера.

### Nodelocal DNS cache

- `enable_nodelocaldns: true` — Pod'ы обращаются к локальному кэширующему агенту DNS на том же узле, минуя iptables DNAT и conntrack. Промахи кэша для кластерных имён (суффикс `cluster.local`) агент запрашивает у core-dns. **С релиза 2.10 включён по умолчанию.**
- `nodelocaldns_external_zones` — массив внешних зон для nodelocaldns (`zones`, `nameservers`, `cache`).
- `dns_etchosts` — тот же контент /etc/hosts, что и у coredns.
- `nodelocaldns_additional_configs` — доп. конфигурация CoreDNS для nodelocaldns.
- **Nodelocal DNS HA:** `enable_nodelocaldns_secondary: true` — резервный nodelocaldns-под на каждом узле. Внимание: при включённой вторичке первичный не убирает свои iptables-правила; при отказе обоих daemonset'ов на узле возможен DNS-blackout. `nodelocaldns_secondary_skew_seconds: 5` — дельта времени выживания вторички при одновременном обновлении.

### Ограничения DNS

- Нет настройки форвардинга Kubedns/SkyDns к произвольным рекурсивным резолверам; нет способа задать кастомный `ndots` для SkyDNS.
- `searchdomains`: лимит 6 имён / 256 символов; из-за дефолтных `svc`, `default.svc` фактически 4 имени / 239 символов (с `remove_default_searchdomains: true` — снова 6).
- `nameservers`: лимит 3 сервера; фактически не более 2 кастомных (один слот зарезервирован под нужды кластера), смягчается через `upstream_dns_servers`.

---

## Network Checker (netchecker)

Источник: `docs/advanced/netcheck.md`.

- `deploy_netchecker` (по умолчанию `false`) — разворачивает Network Checker Application (образы `mirantis/k8s-netchecker`). Состоит из сервера и агентов; проверяет связность pod-to-pod через cluster IP и работу DNS-резолва. Kubespray только разворачивает приложение, но не запускает проверку.
- Отчёт: `curl http://localhost:31081/api/v1/connectivity_check`.
- Переменные: `netchecker_port: 31081`, `agent_report_interval: 15`, `netcheck_namespace: default`.
- Приложение проверяет FQDN вида `netchecker-service.{{ netcheck_namespace }}.svc.{{ dns_domain }}`; при нестандартном namespace нужно скорректировать `searchdomains`.

---

## Источники

- `docs/CNI/cilium.md` (v2.28.0)
- `docs/CNI/cni.md` (v2.28.0)
- `docs/advanced/dns-stack.md` (v2.28.0)
- `docs/advanced/netcheck.md` (v2.28.0)
- Прочие CNI (перечислены справочно, не проиндексированы): `docs/CNI/calico.md`, `docs/CNI/flannel.md`, `docs/CNI/weave.md`, `docs/CNI/kube-ovn.md`, `docs/CNI/kube-router.md`, `docs/CNI/macvlan.md`, `docs/CNI/multus.md`
- Репозиторий тега: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.0

Связанные заметки: [[versions/v2.28.0/variables/cni|Переменные CNI]] · [[versions/v2.28.0/ansible-tags|Ansible-теги]] · [[versions/v2.28.0/README|Срез v2.28.0]]
