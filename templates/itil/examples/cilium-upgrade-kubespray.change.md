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

## Оценка риска
- **Только соседние миноры.** Skip минора не поддерживается Cilium → при необходимости стейджить
  промежуточный минор через `cilium_version`.
- **Kubespray не делает preflight/миграции CRD** — оператор выполняет их сам.
- **Смена дефолтов/требований по целевой версии** (проверить перед апгрейдом): требование к ядру,
  ENI-masquerade, identity-labels, миграции CRD (BGP/IPPool), депрекация/удаление флагов (KPR),
  IPsec+host-routing. Держать старые дефолты через `cilium_upgrade_compatibility=<current-minor>`,
  снять после валидации.

## План внедрения
0. Бэкап `cilium-config` + etcd-снапшот; зафиксировать здоровье (`cilium status --brief`).
1. **Preflight** целевой версии (пред-пул образа + валидация CNP/CRD):
   `helm install cilium-preflight cilium/cilium --version <target> -n kube-system --set preflight.enabled=true --set agent=false --set operator.enabled=false` → дождаться Ready → удалить.
2. Задать `cilium_version: "<target>"` (+ `cilium_upgrade_compatibility` на текущий минор) в group_vars.
3. Прогнать: `ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b --tags=cilium`
   (метод A — `upgrade-cluster.yml`).
4. Валидация (гейт go/no-go).
5. Снять `cilium_upgrade_compatibility`, converge, повторить проверку.

## План проверки (test / validation)
`cilium status --brief` зелёный · rollout `ds/cilium ds/cilium-envoy deploy/cilium-operator` завершён ·
`cilium connectivity test` без ошибок · `ciliumendpoints` стабильны (нет массовых дропов identity).

## План отката (backout / remediation)
До снятия `cilium_upgrade_compatibility` — вернуть `cilium_version` на прежний минор + converge.
**Точка невозврата:** после миграции CRD (BGP v2, IPPool) или churn identity чистого отката нет →
страховка: бэкап `cilium-config` (шаг 0) и etcd-снапшот.

## Расписание
Окно обслуживания; при multi-minor — по одному минору за окно. Change schedule: не пересекать с
другими сетевыми изменениями.

## PIR
Целевая версия стабильна, `cilium_upgrade_compatibility` снят, connectivity зелёный, инцидентов нет.
При стабильной повторяемости — процедура остаётся Standard Change model.

## Связанные записи
- Раннбук базы (пошагово для конкретного скачка, напр. 1.15.9 → 1.18.4).
- Known Errors: KPR-toggles removed, ENI masquerade flip, serviceaccount-identity drops, IPsec host-routing.
- Problem: CVE, требующий апгрейда (если триггер — security).
