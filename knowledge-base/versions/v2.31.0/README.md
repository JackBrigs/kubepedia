---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: docs
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
retrieved_at: 2026-07-14
topics:
  - moc
  - v2-31-0
reliability: authoritative
---

# Kubespray v2.31.0 — срез базы знаний (MOC)

- **Тег:** `v2.31.0`
- **Commit:** `1c9add48975060f45396b34d8e022c30d7f80dab` (`1c9add4`)
- **Дата тега:** 2026-04-24
- **Предыдущая версия:** v2.30.0
- **Ограничение среза:** из CNI детально проиндексирован только Cilium; из container runtime — containerd
- **Статус среза:** проиндексирован полностью (этапы 1–9), база прошла валидацию
- **Kubernetes по умолчанию:** 1.35.4 | **8 breaking changes** относительно v2.30.0 (удалены ingress-nginx/dashboard/netchecker, cgroup v1 off)
- **Сравнение:** [[diffs/v2.30.0__v2.31.0|Отчёт v2.30.0 → v2.31.0]]

## Содержание среза

| Раздел | Файл/директория | Статус |
|---|---|---|
| Метаданные среза | `meta.yaml` | готово (версии компонентов — этап 2) |
| Справочник переменных | `variables/` | готово (этап 2): 1101 переменная, полнота сверена |
| Компоненты и версии | `components.yaml` | готово (этап 2): 39 компонентов |
| Ansible-теги запуска | `ansible-tags.yaml` | готово (этап 3): 120 тегов (удалены dashboard/ingress-nginx/netchecker) |
| Разбор inventory | `inventory/` | готово (этап 4): 577 переменных |
| Расхождения inventory vs defaults | `discrepancies.md` | готово (этап 4): расхождений нет |
| Дайджесты документации | `docs/` | готово (этап 5): 10 дайджестов |
| Разбор GitHub Release | `release-notes.md` | готово (этап 6): 8 breaking changes |
| Troubleshooting | `troubleshooting/` (общий раздел) | готово (этап 7): 2 проблемы, 7 из v2.30.0 исправлены |
| Сравнение с v2.30.0 | `diffs/v2.30.0__v2.31.0.md` | готово (этап 8) |

Назад к индексу: [[INDEX|Kubespray Encyclopedia — INDEX]]
