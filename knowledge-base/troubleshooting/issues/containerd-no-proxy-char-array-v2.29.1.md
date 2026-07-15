---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
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
fixed_versions:
  - v2.29.2
  - v2.31.0
reliability: confirmed
---

# containerd/proxy: `NO_PROXY` рендерится как массив символов (затрагивает v2.29.1)

## Симптом

При настроенном прокси (`http_proxy`/`https_proxy` + `additional_no_proxy`) файл `/etc/systemd/system/containerd.service.d/http-proxy.conf` формируется некорректно: значение `NO_PROXY` выводится как список отдельных символов, а не как строка через запятую:

```
"NO_PROXY=['1', '7', '2', '.', '3', '1', '.', '1', '3', '2', '.', '8', '8', ...]"
```

вместо ожидаемого:

```
"NO_PROXY=172.31.132.88,...,svc,svc.cluster.local"
```

В результате прокси для containerd настраивается неверно — ломается работа кластеров за прокси / в air-gapped-окружениях.

## Корневая причина

Переменная `no_proxy` собирается кастомным Jinja-циклом в задаче `roles/network_facts/tasks/no_proxy.yml` (факт `no_proxy_prepare`, folded scalar `>-` с циклом `for item in ...`, затем `delegate_to: localhost`). При native-Jinja шаблонизации новых версий Ansible результат в ряде случаев интерпретируется как итерируемая строка (массив символов), а не как единая строка. По формулировке автора исправления — проблема «начиная с версии 2.29» из-за изменения в шаблонизации Ansible.

## Решение

PR [#12981](https://github.com/kubernetes-sigs/kubespray/pull/12981) (влит в master) убрал кастомный Jinja-цикл, заменив его на фильтры `flatten` + `join`, и перешёл на `run_once` вместо делегирования на localhost. Бэкпорт в ветку release-2.29 — PR [#13110](https://github.com/kubernetes-sigs/kubespray/pull/13110). Исходный Issue: [#12977](https://github.com/kubernetes-sigs/kubespray/issues/12977).

**Обходной путь до обновления:** задать `no_proxy` вручную корректной строкой через запятую.

## Проверка по коду тега v2.29.1

Уязвимый код присутствует в теге — `roles/network_facts/tasks/no_proxy.yml`:
- строка 5: `no_proxy_prepare: >-`;
- строка 15: `{%- for item in (groups[cluster_or_control_plane] + ...) | unique -%}`;
- строка 27: `delegate_to: localhost`.

Это в точности та реализация, которую заменил фикс. Шаблон `roles/container-engine/containerd/templates/http-proxy.conf.j2` подставляет `NO_PROXY={{ no_proxy }}` напрямую, поэтому некорректно собранное значение попадает в unit-файл.

## Версии

- **Затронуто:** v2.29.0, v2.29.1 (по заявлению автора PR — «начиная с 2.29»; уязвимый код присутствует в коде тега v2.29.1).
- **Исправлено:** патч ветки release-2.29 (будущий v2.29.2, бэкпорт #13110) и master → **v2.31.0** (#12981, влит в master 2026-03, после тега v2.30.0). **Внимание:** в **v2.30.0 баг НЕ исправлен** — фикс #12981 влит уже после тега v2.30.0 (2026-01-30), бэкпорта в release-2.30 нет. См. парную запись для v2.30.0.
- **Оговорка:** репортёр Issue воспроизвёл симптом на v2.30 (Ansible-core 2.17.5); срабатывание зависит от native-Jinja шаблонизации используемой версии Ansible. v2.29.1 требует Ansible ≥ 2.17.3, что соответствует условиям проявления.

## Связанное

[[versions/v2.29.1/docs/proxy|Дайджест: proxy]] · [[versions/v2.29.1/docs/offline|Дайджест: offline]] · [[versions/v2.29.1/variables/container-runtime|Переменные рантайма]]
