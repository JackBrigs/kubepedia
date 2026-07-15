---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_paths:
  - docs/advanced/proxy.md
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - proxy
  - no-proxy
reliability: authoritative
---

# Настройка прокси-окружения в v2.30.0

Источник: `docs/advanced/proxy.md`.

При заданных HTTP/HTTPS прокси все узлы и loadbalancer автоматически
исключаются из проксирования через генерацию переменной `no_proxy` в
`roles/kubespray_defaults/tasks/no_proxy.yml`.

## Основные переменные

- `http_proxy` — например `"http://example.proxy.tld:port"`.
- `https_proxy` — например `"http://example.proxy.tld:port"`.
- `https_proxy_cert_file` — путь к кастомному CA (например
  `/path/to/host/custom/ca.crt`); CA должен уже присутствовать на каждом
  целевом узле.

## Управление no_proxy

- `no_proxy` — полностью переопределяет автогенерацию: при заполнении только
  этой переменной адреса узлов и loadbalancer в `no_proxy` не добавляются
  (пример: `"node1,node1_ip,node2,node2_ip...additional_host"`).
- `additional_no_proxy` — добавить адреса к автоматически сгенерированному
  `no_proxy` (все узлы кластера и loadbalancer сохраняются).
- `no_proxy_exclude_workers: true` — включать в `no_proxy` только узлы
  control plane. По умолчанию воркеры входят в `no_proxy`, из-за чего при
  добавлении/удалении воркеров container engine перезапускается на всех узлах
  (перезапуск всех подов); этот флаг устраняет такое поведение.

## Mitogen

Документ `docs/advanced/mitogen.md` в теге v2.30.0 **отсутствует** (файл
удалён из репозитория на этой версии; в `docs/` нет ни файла, ни упоминаний
mitogen). Соответственно на v2.30.0 Mitogen как ускоритель Ansible через
документацию не описан и считается неподдерживаемым/устаревшим.

## Источники

- `docs/advanced/proxy.md`
- [[versions/v2.30.0/variables/container-runtime|Переменные рантайма]]
- [[versions/v2.30.0/README|Срез v2.30.0]]
