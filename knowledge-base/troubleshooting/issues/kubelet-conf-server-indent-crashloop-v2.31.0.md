---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: github_issue
source_url: https://github.com/kubernetes-sigs/kubespray/issues/13277
retrieved_at: 2026-07-14
topics:
  - kubeadm
  - kubelet
  - upgrade
affected_versions:
  - v2.31.0
fixed_versions: []
reliability: confirmed
---

# kubelet crash-loop после апгрейда: неверный отступ `server:` в kubelet.conf — затрагивает v2.31.0

> Статус фикса: корневая причина подтверждена кодом, но исправляющий PR [#13284](https://github.com/kubernetes-sigs/kubespray/pull/13284) на момент составления записи **открыт и не влит**. Запись добавлена как подтверждённая по коду проблема с обходным путём (раздел 10).

## Симптом

После апгрейда на Kubernetes 1.35+ воркеры уходят в NotReady, kubelet в crash-loop с ошибкой `invalid configuration: no server found for cluster 'default-cluster'`. Проявляется при включённом локальном балансировщике apiserver (localhost LB).

## Корневая причина

Задача `lineinfile` в `roles/kubernetes/kubeadm/tasks/main.yml` записывает строку `server:` с жёстко заданным отступом в 4 пробела, из-за чего поле оказывается вне вложенного блока `cluster:` в `kubelet.conf` (kubeadm-стиль требует 8 пробелов для вложенных полей). kubelet не находит server для кластера.

## Проверка по коду тега v2.31.0

`roles/kubernetes/kubeadm/tasks/main.yml` (строки 104–107):

```yaml
lineinfile:
  dest: "{{ kube_config_dir }}/kubelet.conf"
  regexp: 'server:'
  line: '    server: {{ kube_apiserver_endpoint }}'   # <- 4 пробела отступа
```

Отступ 4 пробела подтверждает описанную проблему.

## Решение

Предложенный фикс — PR [#13284](https://github.com/kubernetes-sigs/kubespray/pull/13284) (использует `backrefs: true` с сохранением исходного отступа). **PR открыт, не влит** — исправления в релизе пока нет. Issue [#13277](https://github.com/kubernetes-sigs/kubespray/issues/13277).

**Обходной путь на v2.31.0:** после апгрейда проверить `{{ kube_config_dir }}/kubelet.conf` на затронутых воркерах и вручную исправить отступ строки `server:` (8 пробелов, внутри блока `cluster:`), затем перезапустить kubelet.

## Версии

- **Затронуто:** **v2.31.0** (прямая связь с дефолтным Kubernetes 1.35 и localhost LB).
- **Исправлено:** пока нет (PR #13284 открыт). Держать на контроле.

## Связанное

[[versions/v2.31.0/docs/upgrades|Дайджест: обновление]] · [[versions/v2.31.0/ansible-tags|Ansible-теги (kubeadm/kubelet)]]
