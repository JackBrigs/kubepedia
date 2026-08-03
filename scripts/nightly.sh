#!/bin/bash
# Периодическая актуализация базы — то, что должно происходить само.
#
# Три слоя стареют независимо, и у каждого свой сторож:
#   свежесть   — новые теги Kubespray и влитые PR апстрима (журнал наблюдения)
#   уязвимости — сверка матриц базы с osv.dev; здесь устаревание означает не
#                «неполно», а «неверно», поэтому проверяется каждый прогон
#   целостность— индекс, валидация KDS, сверка версий с тегнутым исходником
#
# Скрипт НИЧЕГО не правит в знаниях. Он обновляет журнал и сообщает о расхождениях;
# решение, что из этого становится документом, остаётся за человеком — это правило
# проекта, а не осторожность.
#
# Запуск из cron. Cron даёт пустое окружение, поэтому PATH задаётся явно.
set -uo pipefail

REPO="/Users/bredikhin.yu/claude-workspace/projects/kubepedia"
PY="$REPO/.venv/bin/python"
LOGDIR="$REPO/reports/nightly"
LOG="$LOGDIR/$(date +%Y-%m-%d).log"

# cron не наследует пользовательский PATH: без этого не найдутся git, gh и python
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
# ключ для push: агента в cron нет, поэтому указываем напрямую
export GIT_SSH_COMMAND="ssh -i $HOME/.ssh/id_ecdsa -o StrictHostKeyChecking=accept-new"

mkdir -p "$LOGDIR"
exec >>"$LOG" 2>&1

say() { echo; echo "=== $* — $(date '+%H:%M:%S')"; }
DRIFT=0

say "начало прогона"
cd "$REPO" || { echo "!! нет каталога $REPO"; exit 1; }
[ -x "$PY" ] || PY="$(command -v python3)"

say "свежесть и наблюдение за апстримом"
"$PY" scripts/freshness.py --upstream --journal || echo "!! freshness завершился с ошибкой"

say "пере-свип CVE"
# ненулевой код здесь означает расхождение матриц с osv.dev — это находка, а не поломка
if ! "$PY" scripts/cve_sweep.py; then
    echo "!! РАСХОЖДЕНИЕ ПО CVE — матрицы разошлись с osv.dev, нужен разбор"
    DRIFT=1
fi

say "индекс и проверки"
"$PY" scripts/generate_index.py >/dev/null || echo "!! не собрался индекс"
"$PY" scripts/validate_kds.py    || { echo "!! ВАЛИДАЦИЯ НЕ ПРОШЛА — коммита не будет"; exit 2; }
"$PY" scripts/check_versions.py  || echo "!! расхождение версий с исходником"

say "фиксация изменений"
if [ -z "$(git status --porcelain)" ]; then
    echo "изменений нет"
else
    git add -A
    git commit -q -m "Периодика $(date +%Y-%m-%d): журнал наблюдения и проверки

Автоматический прогон. Знания не правятся: обновлён журнал апстрима и
результаты проверок. Расхождения, если они есть, разбираются человеком.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
    if git push -q origin main; then echo "запушено"; else echo "!! push не прошёл — смотри ключ и сеть"; fi
fi

say "итог"
if [ "$DRIFT" = 1 ]; then
    echo "ТРЕБУЕТСЯ ВНИМАНИЕ: расхождение по CVE"
else
    echo "всё чисто"
fi
exit 0
