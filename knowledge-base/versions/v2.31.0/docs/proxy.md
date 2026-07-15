---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_paths:
  - docs/advanced/proxy.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - proxy
reliability: authoritative
---

# Настройка environment proxy в Kubespray v2.31.0

Дайджест документации по настройке HTTP/HTTPS-прокси для развёртывания.

Примечание: файл `docs/advanced/mitogen.md` в теге v2.31.0 отсутствует.

См. также: [[versions/v2.31.0/variables/download|Переменные download]].

## Основное

При задании `http_proxy` и `https_proxy` все узлы и loadbalancer автоматически исключаются из прокси через генерацию переменной `no_proxy` в `roles/kubespray_defaults/tasks/no_proxy.yml`. Дополнительные ресурсы для исключения добавляются в `additional_no_proxy`. Для полного переопределения `no_proxy` заполняется только `no_proxy` — тогда адреса узлов и loadbalancer в него не добавляются.

## HTTP- и HTTPS-прокси

```yaml
http_proxy: "http://example.proxy.tld:port"
https_proxy: "http://example.proxy.tld:port"
```

## Кастомный CA

CA уже должен присутствовать на каждом целевом узле:

```yaml
https_proxy_cert_file: /path/to/host/custom/ca.crt
```

## no_proxy

- **Полное переопределение** (отменяет автогенерацию `no_proxy`):

```yaml
no_proxy: "node1,node1_ip,node2,node2_ip...additional_host"
```

- **Дополнительные адреса** к автогенерируемому no_proxy (все узлы кластера и loadbalancer):

```yaml
additional_no_proxy: "additional_host1,additional_host2"
```

## Исключение воркеров из no_proxy

Так как воркеры по умолчанию входят в `no_proxy`, при добавлении/удалении воркеров docker engine перезапускается на всех узлах (перезапуск всех подов). Чтобы включать в `no_proxy` только узлы control plane:

```yaml
no_proxy_exclude_workers: true
```

## Источники

- docs/advanced/proxy.md
- [[versions/v2.31.0/variables/download|Переменные download]]
- [[versions/v2.31.0/README|Срез v2.31.0]]
