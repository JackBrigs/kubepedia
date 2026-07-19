# CHG-<YYYY>-<NNNN> · Обновление Cilium через Kubespray (<current> → <target>)

| Поле | Значение |
|---|---|
| Тип | **Standard Change model** (пред-авторизованная процедура для рутинного апгрейда CNI). **Эскалация в Normal**, если скачок > 1 минора или задеты breaking-дефолты (см. риски). |
| Статус | Scheduled → Implemented → Reviewed |
| Владелец | SRE / Networking |
| Change authority | Standard: пред-авторизовано процедурой. Normal (при эскалации): CAB |
| Приоритет | по ситуации = impact (дата-плейн кластера) × urgency |

## Описание
Обновление CNI Cilium с `<current>` до `<target>` на Kubespray-кластере штатными средствами Kubespray.
Версия Cilium управляется переменной `cilium_version`.

## Метод (выбрать один)
- **A. Штатный (через тег Kubespray):** обновить Kubespray на тег, где `cilium_version = <target>`, и
  прогнать `upgrade-cluster.yml`. Cilium обновляется вместе с кластером. **Проверить:** не прыгает ли
  тег через минор Cilium — Cilium поддерживает только **соседние миноры**.
- **B. Точечный (override на текущем теге):** оставить тег, задать `cilium_version: "<target>"` в
  `group_vars` и прогнать `cluster.yml -b --tags=cilium`. Двигаем только CNI, по одному минору.

## Затронутые сервисы и CIs
- Сервисы: pod-networking, Service/LoadBalancer, NetworkPolicy, (опц.) BGP/IPsec/ClusterMesh/Hubble.
- CIs: DaemonSet `cilium`, `cilium-operator`, `cilium-envoy`; ConfigMap `cilium-config`; CRD Cilium.

## Влияние на сервис (impact) — ОЖИДАЕТСЯ ПРОСТОЙ СЕТИ
**Как применяет Kubespray:** роль запускает `cilium` CLI (`cilium install`/`upgrade`, Helm под капотом) с первого control-plane **сразу на весь кластер**, не по-нодово с drain. А при **`cilium_remove_old_resources: true`** Kubespray **сносит весь Cilium** (`kubectl delete` DaemonSet, operator, `cilium-config`, RBAC, Hubble, секреты) и ставит заново — **это переустановка CNI: новые поды без сети, датаплейн может просесть = реальный простой**. Так прошла миграция манифесты→Helm на v2.29.

Дальше — что происходит при обычном (не teardown) апгрейде: агент — DaemonSet, катится rolling по нодам; на время рестарта агента на ноде:
- **установленные L3/L4-потоки** обычно продолжают форвардиться eBPF-датаплейном (переживают рестарт агента), НО
- **новые соединения** и распространение изменений NetworkPolicy на этой ноде — с задержкой/краткими дропами (единицы–десятки секунд);
- **cilium-envoy** (если включены L7-политики / Ingress через Cilium) при рестарте **разрывает L7-проксируемый трафик** на ноде;
- при **kube-proxy replacement** сервис-балансировка на ноде кратко деградирует для новых сессий;
- **churn identity** (напр. на 1.18) → transient policy-drops между подами.

**Итого:** ожидается **кратковременный по-нодовый простой сети** для новых соединений / L7 / применения политик,
пока агент/Envoy перезапускаются. При **serial-раскатке** одновременно затронута **одна нода**; blast radius —
весь кластер (это CNI).

**При multi-minor / breaking-дефолтах** (masquerade flip, eBPF host-routing, service proto-diff, миграция CRD)
возможны **сбросы установленных соединений и более длительные перерывы** — относиться как к изменению с реальным
простоем, планировать окно и, при возможности, drain критичных нагрузок / поэтапную раскатку по зонам.

## Оценка риска
| Риск | Вероятность | Влияние | Митигация |
|---|---|---|---|
| Кратковременный простой сети при рестарте агента/Envoy (новые conn / L7 / политики) | **Высокая (ожидаемо)** | Средн. | Окно обслуживания; serial-раскатка (одна нода зараз); drain критичных подов; уведомить владельцев сервисов |
| Skip минора (тег Kubespray прыгает через минор) — вне поддержки Cilium | Средняя | Высок. | Стейджить промежуточный минор через `cilium_version` (только соседние) |
| Breaking-дефолты целевой версии (masquerade, host-routing, KPR-флаги, identity) | Средняя | **Высок.** (сбросы, потеря SNAT, deny-политики) | Держать старые дефолты `cilium_extra_values: {upgradeCompatibility: <current-minor>}`; сверить upgrade-notes целевой версии |
| Миграция CRD (BGP v2, IPPool) — точка невозврата | Средняя | Высок. | Мигрировать CRD до апгрейда; после — чистого отката нет |
| Требование к ядру (напр. ≥5.10 с 1.18) не выполнено | Низкая | **Критич.** (нода не поднимется) | Пре-чек `uname -r` на всех нодах до апгрейда |
| Kubespray не делает preflight/миграции CRD | Высокая | Средн. | Выполнить cilium preflight и миграции вручную (шаги ниже) |

## План внедрения
0. Бэкап `cilium-config` + etcd-снапшот; зафиксировать здоровье (`cilium status --brief`).
1. **Preflight** целевой версии (пред-пул образа + валидация CNP/CRD):
   `helm install cilium-preflight cilium/cilium --version <target> -n kube-system --set preflight.enabled=true --set agent=false --set operator.enabled=false` → дождаться Ready → удалить.
2. Задать `cilium_version: "<target>"` (+ `upgradeCompatibility` (в `cilium_extra_values`) на текущий минор) в group_vars.
3. Прогнать: `ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b --tags=cilium`
   (метод A — `upgrade-cluster.yml`).
4. Валидация (гейт go/no-go).
5. Убрать `upgradeCompatibility` из `cilium_extra_values`, converge, повторить проверку.

## План проверки (test / validation)
`cilium status --brief` зелёный · rollout `ds/cilium ds/cilium-envoy deploy/cilium-operator` завершён ·
`cilium connectivity test` без ошибок · `ciliumendpoints` стабильны (нет массовых дропов identity).

## План отката (backout / remediation)
До снятия `upgradeCompatibility (cilium_extra_values)` — вернуть `cilium_version` на прежний минор + converge.
**Точка невозврата:** после миграции CRD (BGP v2, IPPool) или churn identity чистого отката нет →
страховка: бэкап `cilium-config` (шаг 0) и etcd-снапшот.

## Расписание
Окно обслуживания; при multi-minor — по одному минору за окно. Change schedule: не пересекать с
другими сетевыми изменениями.

## PIR
Целевая версия стабильна, `upgradeCompatibility (cilium_extra_values)` снят, connectivity зелёный, инцидентов нет.
При стабильной повторяемости — процедура остаётся Standard Change model.

## Связанные записи
- Раннбук базы (пошагово для конкретного скачка, напр. 1.15.9 → 1.18.4).
- Known Errors: KPR-toggles removed, ENI masquerade flip, serviceaccount-identity drops, IPsec host-routing.
- Problem: CVE, требующий апгрейда (если триггер — security).
