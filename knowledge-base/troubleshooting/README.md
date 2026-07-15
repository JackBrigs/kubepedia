---
project: kubespray
source_type: docs
retrieved_at: 2026-07-14
topics:
  - troubleshooting
  - moc
reliability: authoritative
---

# Troubleshooting — подтверждённые проблемы (MOC)

Проблемы отобраны строго по разделу 10 методики: только с **подтверждённой корневой причиной** (merged PR / принятый мейнтейнерами Issue) и **привязкой к версии**. Каждая запись проверена по коду тега v2.29.1.

Все записи имеют `reliability: confirmed`. Отклонённые кандидаты (без подтверждённой причины, без merged PR, без привязки к версии) в базу не включены.

# Нижняя цепочка v2.27.0 → v2.29.0

14 подтверждённых проблем, добавленных для новой цепочки. Каждая проверена git-ancestry (фикс-коммит — предок соответствующего тега, `git merge-base --is-ancestor`) и по коду тегов. Важно по хронологии: v2.28.0 (20.05.2025) вышел раньше патчей v2.27.1 (27.06) и v2.28.1 (26.08) — патч-релизы это бэкпорты, поэтому `affected`/`fixed` проставлены по фактическому наличию фикса в дереве тега, а не по номеру версии.

## Баги v2.27.0 (исправлены в v2.27.1 / v2.28.0)

| Проблема | Компонент | Исправлено в | Источник |
|---|---|---|---|
| [[troubleshooting/issues/control-plane-upgrade-reconfiguration-v2.27.0\|Реконфигурация control-plane при upgrade не выполнялась]] | upgrade/control-plane | v2.27.1, v2.28.0 | PR #12015 (бэкпорт #12103) |
| [[troubleshooting/issues/etcd-cert-symlinks-control-plane-v2.27.0\|Симлинки сертификатов etcd на control-plane]] | etcd | v2.27.1, v2.28.0 | PR #12181 (бэкпорт #12192) |
| [[troubleshooting/issues/offline-manage-images-podman-image-id-v2.27.0\|Offline: manage-offline-images и image id под Podman]] | offline | v2.27.1, v2.28.1, v2.29.0 | PR #12314 / #12316 |

## Баги v2.28.0 (исправлены в v2.28.1 / v2.29.0)

| Проблема | Компонент | Исправлено в | Источник |
|---|---|---|---|
| [[troubleshooting/issues/etcd-initial-cluster-quoted-urls-v2.28.0\|Кавычки в etcd initial-cluster ломали scale]] | etcd/scale | v2.28.1, v2.29.0 | PR #12342 (бэкпорт #12352) |
| [[troubleshooting/issues/cilium-values-booleans-json-render-v2.28.0\|JSON-рендер булевых в cilium-values]] | cilium | v2.28.1, v2.29.0 | PR #12280 (#12283) |
| [[troubleshooting/issues/cilium-upgrade-install-vs-upgrade-v2.28.0\|Cilium: install вместо upgrade при обновлении]] | cilium/upgrade | v2.28.1, v2.29.0 | PR #12254 (бэкпорт #12324) |
| [[troubleshooting/issues/kubeadm-skip-phases-1.32-v2.28.0\|kubeadm skip-phases на K8s 1.32]] | kubeadm | v2.28.1, v2.29.0 | PR #12351 (#12354) |
| [[troubleshooting/issues/cilium-config-extra-vars-not-rendered-v2.28.0\|`cilium_config_extra_vars` не рендерились]] | cilium | v2.28.1, v2.29.0 | PR #12335 (#12338) |
| [[troubleshooting/issues/apiserver-san-missing-default-addresses-v2.28.0\|SAN apiserver без адресов по умолчанию (тянется с v2.27.0)]] | control-plane | v2.28.1, v2.29.0 | PR #12413 (бэкпорт #12505) |

## Баги v2.28.1 (исправлены только в v2.29.0, бэкпорта в release-2.28 нет)

| Проблема | Компонент | Затронуто | Источник |
|---|---|---|---|
| [[troubleshooting/issues/kubeadm-ignore-preflight-errors-all-v2.28.1\|`kubeadm_ignore_preflight_errors` = all]] | kubeadm | v2.27.0…v2.28.1 → v2.29.0 | PR #12606 |
| [[troubleshooting/issues/kubeadm-file-discovery-kubeconfig-missing-v2.28.1\|File discovery: отсутствует kubeconfig на вторичных узлах]] | kubeadm/upgrade | v2.27.0…v2.28.1 → v2.29.0 | PR #12132 |
| [[troubleshooting/issues/etcd-cert-extraction-cilium-crd-v2.28.1\|Извлечение сертификатов etcd для Cilium CRD]] | etcd/cilium | v2.28.0, v2.28.1 → v2.29.0 | PR #12565 |
| [[troubleshooting/issues/reset-cluster-cni-timeout-loop-v2.28.1\|reset: таймаут-петля при удалении CNI]] | reset | v2.28.0, v2.28.1 → v2.29.0 | PR #12300 |
| [[troubleshooting/issues/coredns-nodelocaldns-redeploy-config-change-v2.28.1\|CoreDNS/nodelocaldns не передеплоивались при смене конфигурации]] | coredns | v2.28.0, v2.28.1 → v2.29.0 | PR #12401 |

Все 14 проблем исправлены не позднее v2.29.0 — уже индексированных v2.29.1 / v2.30.0 / v2.31.0 они **не затрагивают** (проверено ancestry).

### Отклонено при разборе цепочки v2.27.0–v2.29.0 (раздел 10)

Не заведены: ingress-nginx CVE-2025-1974 (обновление версии, ingress-nginx вне детального охвата); CoreDNS PDB/nodelocaldns_secondary #11957 (узкая правка синтаксиса); fallback_ip cacheable #12182 (вспом. правка кэша фактов); Calico kubecontrollersconfigurations #12039 (Calico\* вне охвата); Cilium BGP AnsibleUnsafeText #12430/#12432 (узкий BGP-кейс, кандидат); Hubble-Relay peer discovery #12346/#12374 (узкий, кандидат); PodSecurity admission #12478 (edge-настройка security); `cilium_policy_audit_mode` #12569 (мелкая правка).

---

## Исправлено в v2.29.1 (баги v2.29.0)

Проблемы, которые были в v2.29.0 и устранены патчем v2.29.1 — актуальны для тех, кто ещё на v2.29.0.

| Проблема | Компонент | Источник |
|---|---|---|
| [[troubleshooting/issues/cilium-loadbalancer-mode-not-rendered-v2.29.1\|`cilium_loadbalancer_mode` игнорировался (loadbalancer vs loadBalancer)]] | cilium | PR #12705 (Issue #12666) |
| [[troubleshooting/issues/cilium-hubble-export-schema-v2.29.1\|Hubble export не применялся (схема Cilium 1.18)]] | cilium | PR #12718 |
| [[troubleshooting/issues/etcd-remove-external-member-fails-v2.29.1\|Удаление внешнего члена etcd прерывало плейбук]] | etcd | PR #12685 |
| [[troubleshooting/issues/calico-apiserver-rbac-k8s-1.33-v2.29.1\|Calico apiserver RBAC на K8s 1.33+]] | calico* | PR #12695 |
| [[troubleshooting/issues/calico-hostendpoints-watch-rbac-v2.29.1\|Calico: отсутствовал verb `watch` для hostendpoints]] | calico* | PR #12644 |

## Затрагивает v2.29.1 (ещё не исправлено в этой версии)

Проблемы, присутствующие в коде v2.29.1 — важны для тех, кто **уже на v2.29.1**. Указан обходной путь и версия с исправлением.

| Проблема | Компонент | Исправлено в | Источник |
|---|---|---|---|
| [[troubleshooting/issues/containerd-no-proxy-char-array-v2.29.1\|`NO_PROXY` рендерится как массив символов]] | containerd/proxy | v2.29.2 / v2.30.0 | PR #12981, #13110 (Issue #12977) |
| [[troubleshooting/issues/etcd-remove-node-not-idempotent-v2.29.1\|`remove-node.yml` не идемпотентен (член etcd уже удалён)]] | etcd | v2.29.2 / v2.30.1 | PR #12949, #12960 (Issue #12947) |
| [[troubleshooting/issues/cilium-native-routing-cidr-null-v2.29.1\|Пустые `native_routing_cidr` → `null` в Helm-values]] | cilium | v2.31.0 (нет бэкпорта в 2.29/2.30) | PR #13109 (Issue #13089) |

\* Calico — CNI вне детального охвата базы (индексируется только Cilium); записи приведены для полноты, так как исправления входят в v2.29.1.

---

# Kubespray v2.30.0

## Исправлено в v2.30.0 (баги ≤ v2.29.1)

| Проблема | Компонент | Источник |
|---|---|---|
| [[troubleshooting/issues/cilium-hardcoded-apiserver-ip-ha-v2.30.0\|Cilium: захардкоженный IP apiserver ломал HA]] | cilium | PR #12624 (Issue #12623) |
| [[troubleshooting/issues/etcd-cert-dir-recursive-perms-calico-v2.30.0\|etcd: рекурсивные права 0700 ломали Calico (etcd datastore)]] | etcd/calico* | PR #12908 |

## Затрагивает v2.30.0 (ещё не исправлено в этой версии)

| Проблема | Компонент | Исправлено в | Источник |
|---|---|---|---|
| [[troubleshooting/issues/gateway-api-1.4.1-checksum-mismatch-v2.30.0\|Gateway API v1.4.1: неверная контрольная сумма — сбой download]] | gateway-api | v2.31.0 (+ release-2.30) | PR #13006/#13010 (Issue #13122) |
| [[troubleshooting/issues/kubeadm-patches-not-removed-v2.30.0\|kubeadm: устаревшие patches не удаляются]] | kubeadm | v2.31.0 (+ release-2.30) | PR #13019/#13020 |
| [[troubleshooting/issues/apiserver-sans-undefined-lb-domain-v2.30.0\|Неопределённая `apiserver_loadbalancer_domain_name` ломает apiserver_sans]] | control-plane | v2.31.0 (+ release-2.30) | PR #13009/#13014 |
| [[troubleshooting/issues/cilium-identity-allocation-mode-undefined-v2.30.0\|kubeadm падает при неопределённой `cilium_identity_allocation_mode`]] | cilium/kubeadm | v2.31.0 | PR #13121 |
| [[troubleshooting/issues/containerd-no-proxy-char-array-v2.30.0\|`NO_PROXY` рендерится как массив символов]] | containerd/proxy | v2.29.2 / v2.31.0 | PR #12981 (Issue #12977) |
| [[troubleshooting/issues/etcd-remove-node-not-idempotent-v2.30.0\|`remove-node.yml` не идемпотентен (член etcd уже удалён)]] | etcd | v2.29.2 / v2.30.1 | PR #12949/#12962 (Issue #12947) |
| [[troubleshooting/issues/cilium-native-routing-cidr-null-v2.30.0\|Пустые `native_routing_cidr` → `null` в Helm-values]] | cilium | v2.31.0 | PR #13109 (Issue #13089) |

Примечание: тег **v2.30.1 на момент составления базы не выпущен** (следующий тег — v2.31.0). Бэкпорты в ветку release-2.30 существуют, но как выпущенный патч линии v2.30.x недоступны — для v2.30.0 актуальны обходные пути либо обновление до v2.31.0.

---

---

# Kubespray v2.31.0

## Все 7 проблем, затрагивавших v2.30.0, ИСПРАВЛЕНЫ в v2.31.0

Проверено по коду тега v2.31.0: NO_PROXY (no_proxy.yml удалён, flatten+join), remove-node идемпотентность (guard `when`), native_routing_cidr (закавычено), kubeadm_patches (очистка добавлена), apiserver_sans (`| d('')`), cilium_identity_allocation_mode (перенесена в kubespray_defaults), Gateway API checksum (неактуально — v2.31.0 на Gateway API 1.5.1). Детали — в [[diffs/v2.30.0__v2.31.0|отчёте сравнения]].

## Затрагивает v2.31.0

| Проблема | Компонент | Статус фикса | Источник |
|---|---|---|---|
| [[troubleshooting/issues/cilium-operator-generic-offline-registry-v2.31.0\|Cilium: неверный образ оператора в offline-реестре]] | cilium/offline | влит после тега (v2.31.1/v2.32.0) | PR #13270 (Issue #13252) |
| [[troubleshooting/issues/kubelet-conf-server-indent-crashloop-v2.31.0\|kubelet crash-loop: неверный отступ `server:` в kubelet.conf]] | kubeadm/kubelet | **PR открыт, не влит** | Issue #13277 / PR #13284 |

## Затрагивает ВСЕ индексированные версии (v2.29.1 / v2.30.0 / v2.31.0)

| Проблема | Компонент | Статус фикса | Источник |
|---|---|---|---|
| [[troubleshooting/issues/etcd-events-inverted-ignore-errors-v2.31.0\|etcd-events: инвертированное `ignore_errors` — ложные сбои при масштабировании]] | etcd | влит в master после v2.31.0 (в релизах пока нет) | PR #13343 (Issue #13342) |

## Наблюдения — свежие открытые Issues/PR (мониторинг 2026-07-15, НЕ authoritative)

Причина/фикс не подтверждены мейнтейнером; в основную базу не добавлены (раздел 10). Отслеживать:

| Issue/PR | Статус | Симптом | Компонент |
|---|---|---|---|
| [#13364](https://github.com/kubernetes-sigs/kubespray/issues/13364) | open (2026-07-14) | лишняя bpf-запись в fstab при Cilium | cilium |
| [#13347](https://github.com/kubernetes-sigs/kubespray/issues/13347) | open (2026-07-09) | Calico apiserver не стартует из-за нехватки RBAC | calico* |
| [#12852](https://github.com/kubernetes-sigs/kubespray/issues/12852) | open (обновл. 2026-07-12) | сбой kubeadm upgrade при смене image path | kubeadm/upgrade |
| [#13284](https://github.com/kubernetes-sigs/kubespray/pull/13284) | open PR | фикс отступа `server:` в kubelet.conf (см. запись выше) | kubeadm |

Отклонены при мониторинге как неприменимые/косметические: PR #13352 (`kube.py` `mutually_exclusive` — косметика, без рантайм-эффекта), PR #13361 (cri-dockerd + K8s ≥1.36 — новее дефолтных версий K8s во всех индексированных срезах; docker вне детального охвата).

## Отклонённые кандидаты (для протокола)

Не прошли планку раздела 10 (нет подтверждённой причины / merged-фикса / привязки к версии), в базу не добавлены:

- Issue #12419 (Cilium native tunneling) — нет подтверждённой причины и merged-фикса;
- Issue #12779 (kubelet не регистрируется с Cilium при scale) — причина не подтверждена мейнтейнером;
- Issue #12880 (upgrade 2.28→2.29.1) — открыт, похоже на version-skew пользователя, причина не подтверждена;
- Issue #12515 (invalid phase name addon/coredns) — привязан к v2.28.1, не к v2.29.x;
- Issue #11682 — `triage/not-reproducible`.

Отклонённые кандидаты v2.30.0:
- Issue #13277 (kubelet crash-loop, неверный отступ `server:`) — подтверждён для v2.31/K8s 1.35+, PR #13284 открыт, к v2.30.0 не привязан;
- Issue #12818 (`kubeadm_init_phases_skip` для init и upgrade) — PR #13066 открыт, к v2.30.0 не подтверждён;
- Issue #12852 (kubeadm upgrade при смене image path, RHEL 8) — открыт, причина не подтверждена;
- Issue #13222 (cilium-operator CrashLoop при Gateway API 1.5.x) — относится к более позднему циклу (в v2.30.0 Gateway API 1.4.x);
- PR #12870, #12794, #13280 — cleanup/без описанного бага с привязкой к v2.30.0.

Отклонённые кандидаты v2.31.0:
- Issue #13278 (calico_rr `any_errors_fatal` прерывает cluster.yml) — открыт, merged-фикса нет;
- Issue #13267 (Cilium CrashLoop при native routing + tunnel disabled) — заявлен для v2.30.0, открыт, к v2.31.0 не подтверждён;
- Issue #13335/PR #13336 (Cilium host firewall после reboot) — enhancement, PR открыт;
- Issue #13345 (etcd-events handler throttle), #13351 (косметика kube.py), #13125 (pod-infra flag, v2.30.0) — без подтверждённого merged-фикса с привязкой к v2.31.0.

## Обновление парных записей v2.29.1

Запись [[troubleshooting/issues/containerd-no-proxy-char-array-v2.29.1|NO_PROXY (v2.29.1)]] исправлена: фикс #12981 влит в master уже **после** тега v2.30.0, поэтому корректные `fixed_versions` — v2.29.2 и **v2.31.0** (не v2.30.0). Баг присутствует и в v2.30.0 (см. парную запись выше).

Назад: [[versions/v2.29.1/README|Срез v2.29.1]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
