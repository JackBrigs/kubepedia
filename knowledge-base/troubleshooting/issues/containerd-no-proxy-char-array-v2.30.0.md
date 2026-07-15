---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: github_pr
source_url: https://github.com/kubernetes-sigs/kubespray/pull/12981
retrieved_at: 2026-07-14
topics:
  - containerd
  - proxy
  - no-proxy
affected_versions:
  - v2.29.0
  - v2.29.1
  - v2.30.0
fixed_versions:
  - v2.29.2
  - v2.31.0
reliability: confirmed
---

# containerd/proxy: `NO_PROXY` рендерится как массив символов (затрагивает v2.30.0)

## Симптом

При настроенном прокси (`http_proxy`/`https_proxy` + `additional_no_proxy`) файл `/etc/systemd/system/containerd.service.d/http-proxy.conf` формируется некорректно: `NO_PROXY` выводится как список отдельных символов (`['1','7','2','.',...]`) вместо строки через запятую. Прокси для containerd настраивается неверно.

## Корневая причина

Переменная `no_proxy` собирается кастомным Jinja-циклом в `roles/network_facts/tasks/no_proxy.yml` (факт `no_proxy_prepare`, folded scalar `>-` с циклом `for item in ...`, `delegate_to: localhost`). При native-Jinja шаблонизации новых версий Ansible результат интерпретируется как массив символов.

## Проверка по коду тега v2.30.0

Уязвимый код присутствует — `roles/network_facts/tasks/no_proxy.yml`:
- строка 15: `{%- for item in (groups[cluster_or_control_plane] + ...) | unique -%}`;
- строка 27: `delegate_to: localhost`.

Фикс #12981 влит в master 2026-03, то есть **после** тега v2.30.0 (2026-01-30); бэкпорта в ветку release-2.30 нет. Для сравнения: в v2.31.0 файл `no_proxy.yml` удалён, логика перенесена в `roles/network_facts/tasks/main.yaml` с фильтрами `flatten`+`join` — то есть в v2.31.0 исправлено.

## Решение

PR [#12981](https://github.com/kubernetes-sigs/kubespray/pull/12981) (master → v2.31.0), бэкпорт release-2.29 [#13110](https://github.com/kubernetes-sigs/kubespray/pull/13110) → v2.29.2. Issue [#12977](https://github.com/kubernetes-sigs/kubespray/issues/12977).

**Обходной путь на v2.30.0:** задать `no_proxy` вручную корректной строкой через запятую.

## Версии

- **Затронуто:** v2.29.0, v2.29.1, **v2.30.0** (уязвимый код подтверждён в теге).
- **Исправлено:** v2.29.2 (release-2.29) и v2.31.0 (master). **В v2.30.0 не исправлено** — обновление до v2.31.0 или обходной путь.

## Связанное

[[versions/v2.30.0/docs/proxy|Дайджест: proxy]] · [[versions/v2.30.0/variables/container-runtime|Переменные рантайма]] · парная запись v2.29.1: [[troubleshooting/issues/containerd-no-proxy-char-array-v2.29.1|containerd NO_PROXY (v2.29.1)]]
