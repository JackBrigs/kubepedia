---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/13009
retrieved_at: 2026-07-14
topics:
  - control-plane
  - certificates
  - kubeadm
affected_versions:
  - v2.30.0
fixed_versions:
  - v2.31.0
reliability: confirmed
---

# control-plane: неопределённая `apiserver_loadbalancer_domain_name` ломает формирование `apiserver_sans` (затрагивает v2.30.0)

## Симптом

Ошибка при формировании списка SAN сертификата kube-apiserver, когда `apiserver_loadbalancer_domain_name` не определена (актуально при развёртывании без внешнего LB и при регенерации сертификатов в ходе обновления).

## Корневая причина

В сборке факта `apiserver_sans` значение `apiserver_loadbalancer_domain_name` добавляется в список **без проверки на `undefined`** (в отличие от соседнего `loadbalancer_apiserver.address | d('')`). Если переменная не задана, шаблонизация падает до фильтра `select`.

## Проверка по коду тега v2.30.0

`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`, блок `_apiserver_sans` (строки 28–41):

```yaml
apiserver_sans: "{{ _apiserver_sans | flatten | select | unique }}"
vars:
  _apiserver_sans:
    - ...
    - "{{ apiserver_loadbalancer_domain_name }}"        # <- без | default('')
    - "{{ loadbalancer_apiserver.address | d('') }}"    # <- здесь guard есть
```

Строка 39 не имеет `| default('')` — при неопределённой переменной задача падает. Баг присутствует.

## Решение

PR [#13009](https://github.com/kubernetes-sigs/kubespray/pull/13009) «Undefined check for apiserver_loadbalancer_domain_name in apiserver_sans» (master → v2.31.0), бэкпорт в release-2.30 — PR [#13014](https://github.com/kubernetes-sigs/kubespray/pull/13014).

**Обходной путь на v2.30.0:** явно задать `apiserver_loadbalancer_domain_name` в inventory (даже при отсутствии внешнего LB — например, доменное имя первого control-plane), либо собрать роль из ветки release-2.30.

## Версии

- **Затронуто:** v2.30.0.
- **Исправлено:** v2.31.0 (master). Бэкпорт в release-2.30 (будущий v2.30.1, тег не выпущен).

## Связанное

[[versions/v2.30.0/variables/k8s-cluster|Переменные ядра (apiserver_loadbalancer_domain_name)]] · [[versions/v2.30.0/docs/nodes|Дайджест: узлы]]
