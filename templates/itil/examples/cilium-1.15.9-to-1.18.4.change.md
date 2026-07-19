# CHG-2026-0142 · Обновление Cilium 1.15.9 → 1.18.4 (Kubespray)

| Поле | Значение |
|---|---|
| Источник (RFC) | RFC-2026-0207 |
| Тип | **Normal** (после успешного PIR → перевести в **Standard Change model**) |
| Статус | New → Assessed → Authorized → Scheduled → Implemented → Reviewed |
| Инициатор / Владелец | Platform Engineering / SRE-Networking |
| Change authority | CAB (высокий blast-radius: CNI всего кластера) |
| Приоритет | High = impact (весь дата-плейн) × urgency (плановая, блокирует дальнейшие апгрейды) |

## Описание и обоснование
Апгрейд Cilium 1.15.9 → 1.18.4. Cilium апгрейдится только между соседними минорами; Kubespray-теги
перескакивают 1.16, поэтому недостающий минор доставляется вручную через `cilium_version` +
`cluster.yml`. Причина: тех-долг + security-фиксы + подготовка к 1.19.

## Затронутые сервисы и CIs
- Сервисы: pod-networking, Service/LB, NetworkPolicy, (опц.) BGP/IPsec/ClusterMesh/Hubble.
- CIs: `cilium` (DaemonSet), `cilium-operator`, `cilium-envoy`, ConfigMap `cilium-config`, CRD Cilium.

## Оценка риска
- Уровень: **High**.
- Риски и митигации:
  1. Kubespray перескакивает 1.16 (нарушение consecutive-minor) → стейджим 1.16.x через `cilium_version`.
  2. Ядро ≥5.10 обязательно с 1.18 → пре-чек `uname -r` на всех нодах до хопа к 1.18.
  3. ENI-masquerade дефолт true→false → задать `cilium_enable_ipv4_masquerade: true` при ENI IPAM.
  4. Churn serviceaccount-identity → исключить метку, если не используется.
  5. BGP CRD v2alpha1→v2 → миграция до хопа к 1.18.
  6. KPR piecemeal toggles депрекейтед → перевести на единый `kube_proxy_replacement`.
  7. IPsec+KPR+BPF-masq → host-routing CVE-2025-37959 → патч ядра или `--enable-host-legacy-routing=true`.

## План внедрения (implementation plan)
Шаг 0: бэкап `cilium-config` + etcd-снапшот, зафиксировать здоровье (`cilium status`).
Хопы (для каждого: preflight-DaemonSet целевой версии → `cilium_version` + `cilium_upgrade_compatibility`
на предыдущий минор → `ansible-playbook -i <inv> kubespray/cluster.yml -b --tags=cilium` → валидация):
  1. 1.15.9 → 1.16.x (учесть: Envoy-DS дефолтно, `IPPool.spec.cidrs`→`.blocks`, deny-семантика пустых селекторов).
  2. 1.16.x → 1.17.x (учесть: убраны Consul / managed-etcd / metallb-bgp; proto-diff дефолтно).
  3. 1.17.x → **1.18.4** (пре-чеки риска 2–7 выше).
Финал: снять `cilium_upgrade_compatibility`, converge, повторить connectivity test.
Полная процедура — раннбук базы «Cilium 1.15.9 → 1.18.4».

## План проверки (test / validation)
Гейт go/no-go на каждом хопе: `cilium status --brief` зелёный, rollout завершён,
`cilium connectivity test` без ошибок, `ciliumendpoints` стабильны (нет массовых дропов identity).

## План отката (backout / remediation)
До снятия `cilium_upgrade_compatibility`: возврат `cilium_version` на предыдущий минор + converge.
**Точка невозврата:** миграция CRD (BGP v2, IPPool) или churn identity — далее чистого отката нет;
страховка — бэкап `cilium-config` (шаг 0) и etcd-снапшот.

## Расписание (schedule)
Окно обслуживания; хопы можно разнести. Change schedule: не пересекать с другими сетевыми изменениями.

## Авторизация
CAB: <решение / дата>.

## Журнал внедрения (implementation log)
<Заполняется по факту: время каждого хопа, результат валидации, отклонения.>

## Post-Implementation Review (PIR)
Подтвердить: 1.18.4 стабильна, `cilium_upgrade_compatibility` снят, connectivity зелёный, инцидентов нет.
При успехе — перевести процедуру в **Standard Change model** (пред-авторизована).

## Связанные записи
- Known Errors: KEDB (KPR-toggles removed, ENI masquerade flip, serviceaccount-identity drops, IPsec host-routing).
- Problem: PRB (CVE-2025-37959 — eBPF host-routing kernel).
- Раннбук базы: «Cilium 1.15.9 → 1.18.4».
