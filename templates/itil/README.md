# ITIL 4 — шаблоны сервис-менеджмент документов

Слой **вывода** поверх базы знаний Kubepedia. База остаётся в формате KDS (`kb/`, под валидацией);
здесь — деливераблы для ITSM (Jira Service Management / ServiceNow и т.п.), которые **рендерятся из
базы** по запросу. ITIL 4 (стабильная, полностью документированная версия; записи ITIL 5 наследуются
отсюда).

## Как ложится база на ITIL 4
| Контент базы | Артефакт ITIL 4 | Практика |
|---|---|---|
| Раннбук / процедура апгрейда | **RFC** → **Change Record** (Normal), после обкатки → **Standard Change model** | Change Enablement |
| Troubleshooting-док | **Known Error** (KEDB) | Problem Management |
| CVE / повторяющийся дефект | **Problem Record** | Problem Management |
| Сбой | **Incident Record** | Incident Management |

## Файлы
- `change-request.rfc.template.md` — RFC (запрос на изменение, инициация).
- `change-record.template.md` — Change Record (полный ЖЦ изменения: оценка → авторизация → внедрение → PIR).
- `known-error.template.md` — Known Error (KEDB).
- `problem-record.template.md` — Problem Record.
- `examples/` — заполненные примеры (Cilium 1.15.9 → 1.18.4: RFC + Change).

## Поток
RFC (ask) → авторизация change authority → Change Record ведёт изменение до **PIR** → при повторяемости
процедура становится **Standard Change model** (пред-авторизована, без CAB каждый раз).

## Правила заполнения
- Плейсхолдеры `<...>` заменить.
- Приоритет = **impact × urgency**.
- Тип изменения: **Standard** (пред-авторизовано, низкий риск) / **Normal** (оценка+авторизация+окно) /
  **Emergency** (срочно; бумагу можно урезать, **тестирование — нет**).
- **Backout/remediation обязателен.** Если чистого отката нет — явно указать точку невозврата.
- ID (RFC/CHG/KEDB/PRB) выдаёт ваш ITSM; здесь — иллюстративные.
