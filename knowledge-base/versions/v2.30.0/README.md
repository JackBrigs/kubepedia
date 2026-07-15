---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
retrieved_at: 2026-07-14
topics:
  - moc
  - v2-30-0
reliability: authoritative
---

# Kubespray v2.30.0 — срез базы знаний (MOC)

- **Тег:** `v2.30.0`
- **Commit:** `f4ccdb5e72395eaf9f3444056ebd1a6625ddb89a` (`f4ccdb5`)
- **Дата тега:** 2026-01-30
- **Предыдущая версия:** v2.29.1
- **Источник:** https://github.com/kubernetes-sigs/kubespray/tree/v2.30.0
- **Ограничение среза:** из CNI детально проиндексирован только Cilium; из container runtime — containerd
- **Статус среза:** проиндексирован полностью (этапы 1–9), база прошла валидацию
- **Kubernetes по умолчанию:** 1.34.3 | **6 breaking changes** относительно v2.29.1 (см. release-notes)
- **Сравнение:** [[diffs/v2.29.1__v2.30.0|Отчёт v2.29.1 → v2.30.0]]

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово (версии компонентов — этап 2) |
| Справочник переменных | `variables/` | готово (этап 2): 1206 переменных |
| Компоненты и версии | `components.yaml` | готово (этап 2): 44 компонента |
| Ansible-теги запуска | `ansible-tags.yaml` | готово (этап 3): 123 тега (удалён `master`) |
| Разбор inventory | `inventory/` | готово (этап 4): 583 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово (этап 4): 1 расхождение значений |
| Дайджесты документации | `docs/` | готово (этап 5): 10 дайджестов |
| Разбор GitHub Release | `release-notes.md` | готово (этап 6): breaking changes + версии |
| Troubleshooting | `troubleshooting/` (общий раздел) | готово (этап 7): 9 проблем |
| Сравнение с v2.29.1 | `diffs/v2.29.1__v2.30.0.md` | готово (этап 8) |

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
