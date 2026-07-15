---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: docs
source_paths:
  - docs/advanced/proxy.md
  - docs/advanced/mitogen.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - proxy
  - no-proxy
  - mitogen
reliability: authoritative
---

# Прокси в v2.27.0

Дайджест документации по настройке прокси строго с тега `v2.27.0` (commit `9ec9b3a`).

## HTTP/HTTPS прокси

Источник: `docs/advanced/proxy.md`.

Задание прокси для http и https:

```yaml
http_proxy: "http://example.proxy.tld:port"
https_proxy: "http://example.proxy.tld:port"
```

При установке `http_proxy`/`https_proxy` все узлы кластера и loadbalancer
**автоматически исключаются** из проксирования — переменная `no_proxy`
генерируется в `roles/kubespray-defaults/tasks/no_proxy.yml`.

Пользовательский CA (сертификат должен уже присутствовать на всех целевых узлах):

```yaml
https_proxy_cert_file: /path/to/host/custom/ca.crt
```

## no_proxy и additional_no_proxy

- `no_proxy` — если задать явно, он **полностью переопределяет**
  автогенерацию: адреса узлов и loadbalancer в no_proxy добавлены НЕ будут.

  ```yaml
  no_proxy: "node1,node1_ip,node2,node2_ip...additional_host"
  ```

- `additional_no_proxy` — добавляет адреса к автоматически сгенерированному
  no_proxy (который уже содержит все узлы кластера и loadbalancer), не отменяя
  автогенерацию.

  ```yaml
  additional_no_proxy: "additional_host1,additional_host2"
  ```

## Влияние проксирования на узлы

- По умолчанию все worker-узлы входят в `no_proxy`. Из-за этого при добавлении
  или удалении worker-узлов container engine (docker) перезапускается на всех
  узлах (перезапускаются все pod'ы), так как меняется значение no_proxy.
- Чтобы включить в `no_proxy` только узлы control plane (и избежать такого
  перезапуска при изменении состава worker'ов):

  ```yaml
  no_proxy_exclude_workers: true
  ```

## Mitogen (ускорение Ansible) — DEPRECATED

Источник: `docs/advanced/mitogen.md`.

Mitogen ускоряет выполнение Ansible (по данным документации — в 1.25x–7x,
снижение нагрузки на CPU минимум в 2x), но **поддержка в kubespray признана
устаревшей (deprecated)**: upstream не выпустил версию под ansible 4.x
(ansible-base 2.11.x) и выше, CI-поддержка убрана, регрессии не проверяются.
Плейбук установки (`contrib/mitogen/mitogen.yml`) и документация будут удалены
в одной из будущих версий. Включение (для справки): через `ansible.cfg`
(`strategy=mitogen_linear`, `strategy_plugins = plugins/mitogen/ansible_mitogen/plugins/strategy`)
или переменные окружения `ANSIBLE_STRATEGY`, `ANSIBLE_STRATEGY_PLUGINS`.
К проксированию не относится — приведён как средство ускорения с пометкой об устаревании.

## Источники

- `docs/advanced/proxy.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.27.0/docs/advanced/proxy.md
- `docs/advanced/mitogen.md` — https://github.com/kubernetes-sigs/kubespray/blob/v2.27.0/docs/advanced/mitogen.md

Связанные заметки: [[versions/v2.27.0/docs/offline|Оффлайн-развёртывание и зеркала]] · [[versions/v2.27.0/variables/download|Переменные download]] · [[versions/v2.27.0/README|Срез v2.27.0]]
