#!/usr/bin/env python3
"""Телеграм-бот над базой — доступ с телефона.

    kubepedia bot                    # токен из окружения или ~/.config/kubepedia/bot.token

Почему именно длинные опросы, а не вебхук: бот сам ходит наружу к api.telegram.org
и держит соединение. Машине не нужен белый адрес, проброс портов и сертификат —
работает из-за NAT, с ноутбука, из дома. Вебхук потребовал бы всего этого сразу.

Чего это НЕ решает: пока машина спит, бот не отвечает. Для доступа в любое время
процесс должен жить на чём-то, что не засыпает.

Доступ закрыт списком: база отвечает только тем chat_id, что перечислены явно.
Бот в телеграме находится по имени кем угодно, и без списка это означало бы, что
внутренняя инженерная база отвечает случайному человеку. Незнакомому бот называет
его chat_id и молчит по существу — этого хватает, чтобы вписать себя в список.

Токен в репозиторий не кладётся. Порядок поиска:
    1) переменная окружения KUBEPEDIA_BOT_TOKEN
    2) файл ~/.config/kubepedia/bot.token  (первая строка)
Список доступа — KUBEPEDIA_BOT_ALLOW="123,456" или ~/.config/kubepedia/bot.allow.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kbapi  # noqa: E402

CONF = os.path.expanduser("~/.config/kubepedia")
API = "https://api.telegram.org/bot{token}/{method}"
TG_LIMIT = 4096          # предел телеграма на сообщение
POLL_TIMEOUT = 30        # столько держится длинный опрос
CHUNK = TG_LIMIT - 120   # запас на служебную обвязку


def _first_line(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.readline().strip()
    except OSError:
        return ""


def token():
    return os.environ.get("KUBEPEDIA_BOT_TOKEN", "").strip() or _first_line(
        os.path.join(CONF, "bot.token"))


def allowlist():
    raw = os.environ.get("KUBEPEDIA_BOT_ALLOW", "").strip()
    if not raw:
        try:
            with open(os.path.join(CONF, "bot.allow"), encoding="utf-8") as f:
                raw = ",".join(line.strip() for line in f if line.strip()
                               and not line.startswith("#"))
        except OSError:
            raw = ""
    out = set()
    for part in raw.replace(" ", ",").split(","):
        if part.strip().lstrip("-").isdigit():
            out.add(int(part.strip()))
    return out


def call(tok, method, **params):
    url = API.format(token=tok, method=method)
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(urllib.request.Request(url, data=data),
                                timeout=POLL_TIMEOUT + 15) as r:
        return json.loads(r.read().decode("utf-8"))


def split(text, limit=CHUNK):
    """Разрезать длинный ответ по границам строк, а не посреди слова."""
    out, cur = [], ""
    for line in text.splitlines(keepends=True):
        while len(line) > limit:              # одна строка длиннее предела
            out.append((cur + line[:limit]).rstrip())
            cur, line = "", line[limit:]
        if len(cur) + len(line) > limit:
            out.append(cur.rstrip())
            cur = line
        else:
            cur += line
    if cur.strip():
        out.append(cur.rstrip())
    return out or ["(пусто)"]


HELP = (
    "Спросите базу: пришлите текст ошибки или симптом.\n\n"
    "Можно прислать сырой вывод команды целиком (describe, логи пода, journalctl) — "
    "он разберётся по сигналам, каждый отдельно.\n\n"
    "Отвечает база знаний, а не модель: ответ приходит сразу и одинаков каждый раз. "
    "Если разбора нет — так и будет сказано, это дыра в покрытии, а не отказ."
)


def serve(tok, kb, allow):
    offset = None
    print(f"База: {len(kb)} документов. Доступ открыт для: "
          f"{', '.join(map(str, sorted(allow))) if allow else '— (список пуст)'}")
    if not allow:
        print("Список доступа пуст: бот назовёт chat_id тому, кто напишет, "
              "но отвечать по существу не будет.")
    print("Слушаю. Остановить: Ctrl+C")

    while True:
        try:
            res = call(tok, "getUpdates", timeout=POLL_TIMEOUT,
                       **({"offset": offset} if offset else {}))
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as e:
            # Сеть отваливается — это норма для долгоживущего процесса, не повод падать.
            print(f"сеть: {e}; повтор через 5 с")
            time.sleep(5)
            continue
        if not res.get("ok"):
            print(f"телеграм ответил: {res}")
            time.sleep(5)
            continue

        for upd in res.get("result", []):
            offset = upd["update_id"] + 1
            msg = upd.get("message") or upd.get("edited_message")
            if not msg:
                continue
            chat = msg["chat"]["id"]
            text = msg.get("text") or msg.get("caption") or ""
            if not text.strip():
                continue

            if chat not in allow:
                call(tok, "sendMessage", chat_id=chat,
                     text=("Доступ к базе закрыт списком.\n\n"
                           f"Ваш chat_id: {chat}\n\n"
                           "Впишите его в ~/.config/kubepedia/bot.allow "
                           "(или в KUBEPEDIA_BOT_ALLOW) и перезапустите бота."))
                print(f"отказано: chat_id {chat}")
                continue

            if text.strip() in ("/start", "/help"):
                call(tok, "sendMessage", chat_id=chat, text=HELP)
                continue

            kb.maybe_reload()
            t0 = time.perf_counter()
            res_ = kb.ask(text)
            answer = kbapi.render_text(res_)
            for part in split(answer):
                call(tok, "sendMessage", chat_id=chat, text=part,
                     disable_web_page_preview="true")
            print(f"chat {chat}: {res_['mode']}, "
                  f"{'ответ' if res_['ok'] else 'без ответа'}, "
                  f"{(time.perf_counter() - t0) * 1000:.0f} мс")


def main():
    ap = argparse.ArgumentParser(description="Телеграм-бот над базой Kubepedia")
    ap.add_argument("--whoami", action="store_true",
                    help="проверить токен и выйти (покажет имя бота)")
    args = ap.parse_args()

    tok = token()
    if not tok:
        print("Нет токена. Положите его в ~/.config/kubepedia/bot.token "
              "или в KUBEPEDIA_BOT_TOKEN.", file=sys.stderr)
        print("Токен выдаёт @BotFather в телеграме: /newbot.", file=sys.stderr)
        return 2

    try:
        me = call(tok, "getMe")
    except Exception as e:
        print(f"Телеграм недоступен: {e}", file=sys.stderr)
        return 1
    if not me.get("ok"):
        print(f"Токен не принят: {me}", file=sys.stderr)
        return 1
    name = me["result"].get("username")
    print(f"Бот: @{name}")
    if args.whoami:
        return 0

    print("Разбираю базу…", flush=True)
    kb = kbapi.KB()
    try:
        serve(tok, kb, allowlist())
    except KeyboardInterrupt:
        print("\nостановлен")
    return 0


if __name__ == "__main__":
    sys.exit(main())
