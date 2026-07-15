---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12624
retrieved_at: 2026-07-14
topics:
  - cilium
  - ha
  - apiserver
affected_versions:
  - v2.29.1
fixed_versions:
  - v2.30.0
reliability: confirmed
---

# Cilium: захардкоженный IP API-сервера ломал HA-кластер при падении первого control-plane (исправлено в v2.30.0)

## Симптом

В HA-кластере при выключении/недоступности **первого** control-plane узла поды `cilium-operator` и `cilium-agent` теряли связь с API: `dial tcp <first-cp-ip>:6443: connect: no route to host`. Поды переходили в NotReady, сеть кластера отказывала. Обход через `cilium_config_extra_vars` не помогал — переменная окружения `KUBERNETES_SERVICE_HOST` уже была вшита в запущенные поды.

## Корневая причина

Cilium указывал на IP только первого control-plane узла (`k8sServiceHost`), а не на локальный/внешний балансировщик apiserver. При отказе первого узла связь терялась.

## Решение (breaking change v2.30.0)

PR [#12624](https://github.com/kubernetes-sigs/kubespray/pull/12624) (merged 2026-01-01, Issue [#12623](https://github.com/kubernetes-sigs/kubespray/issues/12623)): `k8sServiceHost` / `k8sServicePort` теперь берутся из `kube_apiserver_global_endpoint`.

## Проверка по коду тега v2.30.0

`roles/network_plugin/cilium/templates/values.yaml.j2`:
- строка 10: `k8sServiceHost: "{{ kube_apiserver_global_endpoint | urlsplit('hostname') }}"`;
- строка 11: `k8sServicePort: "{{ kube_apiserver_global_endpoint | urlsplit('port') }}"`.

## Действие, требуемое при обновлении на v2.30.0

Release note (action required): убедитесь, что `kube_apiserver_global_endpoint` корректно настроен и **доступен со всех узлов** — иначе Cilium не сможет достучаться до apiserver.

## Версии

- **Затронуто:** ≤ v2.29.1 (захардкоженный IP первого control-plane).
- **Исправлено:** v2.30.0.

## Связанное

[[versions/v2.30.0/variables/cni|Переменные CNI]] · [[versions/v2.30.0/release-notes|Release notes v2.30.0 (breaking changes)]] · [[versions/v2.30.0/docs/cni|Дайджест: CNI/Cilium]]
