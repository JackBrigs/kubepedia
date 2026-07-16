# Kubepedia — версионно-осведомлённая база знаний по Kubespray

**Kubepedia** — это AI-first граф знаний о Kubernetes, Kubespray и компонентах,
которыми управляет Kubespray. Каждый факт привязан к конкретным версиям Kubespray,
к которым он применим, и подтверждён кодом соответствующего git-тега.

- Строится строго по **коду тегов Kubespray** (не блоги и не `master`)
- **Версионно-осведомлён**: один документ на сущность, значения — таблицей по релизам
- **Атомарный и графовый**: маленькие документы, связанные типизированными связями
- **Машиночитаемый индекс**: отвечает на базовые вопросы без LLM
- **Проверяется**: каждый документ проходит `scripts/validate_kds.py` перед вливанием

## Быстрый старт

Смотрите граф знаний в [`kb/`](kb/) — каждый документ самодостаточен.

Запросы к сгенерированному индексу (JSON Lines) без всякого LLM:

```ShellSession
# все управляемые компоненты и их диапазон версий
jq -r 'select(.type=="component") | "\(.id)\t\(.component_version)"' index/documents.jsonl

# всё, что покрывает Kubespray v2.31.0
jq -r 'select(.kubespray_version | test("2.31")) | "\(.type)\t\(.id)"' index/documents.jsonl

# какой run-тег перегенерирует сертификаты etcd?
grep -rl "etcd certificates" kb/kubespray/ansible-tags/
```

Перегенерация индекса и валидация базы:

```ShellSession
pip install pyyaml jsonschema
python3 scripts/generate_index.py
python3 scripts/validate_kds.py
```

## Документы

- [Архитектура и контракт](standards/) — [project](standards/project.md),
  [workflow](standards/workflow.md), [sources](standards/sources.md),
  [спецификация документа (KDS)](standards/kds.md),
  [валидация](standards/validation.md), [лог решений](standards/decisions.md)
- [Слой Kubernetes](kb/kubernetes/) — поддержка версий, версии control plane,
  конфиг kubeadm
- [Переменные Kubespray](kb/kubespray/variables/)
- [Ansible run-теги](kb/kubespray/ansible-tags/)
- [Управляемые компоненты](kb/components/)
- [Бэклог](BACKLOG.md)

## Проиндексированные версии

Базовая — **Kubespray v2.29.0**, покрытие последовательно до новейшего релиза:

- v2.29.0, v2.29.1, v2.30.0, v2.31.0 (Kubernetes **1.31 – 1.35**)

## Требования

- **Python 3** с **PyYAML** (и **jsonschema** для полной проверки метаданных)
- `jq` (опционально) для запросов к индексу
- Локальный чекаут тега Kubespray при расширении базы — факты сверяются по коду
  источника, а не додумываются
