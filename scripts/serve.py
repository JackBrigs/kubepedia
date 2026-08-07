#!/usr/bin/env python3
"""Резидентная база: веб-чат и HTTP-ручка.

    kubepedia serve                  # http://127.0.0.1:8787 — только эта машина
    kubepedia serve --host 0.0.0.0   # видно из локальной сети (телефон в том же wifi)
    kubepedia serve --port 9000

Смысл резидентности: корпус разбирается один раз на старте, дальше ответ стоит
~25 мс. CLI платит разбор (или чтение кэша) на каждый запуск; здесь не платит
никто. Правку базы процесс замечает сам — см. `KB.maybe_reload`.

Ручки:
    GET  /                — веб-чат
    GET  /api/ask?q=...   — JSON-ответ (`full=1` — целиком причина и все шаги)
    POST /api/ask         — тело запроса это сырой вывод команды; он триажится
    GET  /health          — живость и размер базы

Зависимостей нет: только стандартная библиотека. Никакой модели в цепочке —
отвечает база, поэтому ответ приходит мгновенно и одинаково каждый раз.
"""
import argparse
import json
import os
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kbapi  # noqa: E402

UI = os.path.join(HERE, "webui.html")
MAX_BODY = 1 << 20  # 1 МБ: вставленный лог бывает большим, но не безразмерным


class Handler(BaseHTTPRequestHandler):
    kb = None
    server_version = "kubepedia"
    sys_version = ""

    def log_message(self, fmt, *a):
        # Обращения к базе — это запросы пользователя, часто с именами хостов
        # из вставленного лога. В stdout они не нужны: там их увидит любой,
        # кому видно окно с сервером.
        pass

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _answer(self, text, full=False, top=3):
        self.kb.maybe_reload()
        res = self.kb.ask(text, top=top)
        res["full"] = bool(full)
        res["docs"] = len(self.kb)
        # Внутренние идентификаторы документов наружу не уходят: пользователь
        # работает с заголовками и фактами, а не с адресацией графа.
        for h in res.get("hits", []):
            h.pop("id", None)
        for s in res.get("signals", []):
            for h in s.get("hits", []):
                h.pop("id", None)
        self._send(200, json.dumps(res, ensure_ascii=False))

    def do_GET(self):
        u = urllib.parse.urlparse(self.path)
        if u.path == "/":
            try:
                with open(UI, "rb") as f:
                    self._send(200, f.read(), "text/html; charset=utf-8")
            except OSError:
                self._send(500, "нет файла интерфейса webui.html", "text/plain; charset=utf-8")
            return
        if u.path == "/health":
            self.kb.maybe_reload()
            self._send(200, json.dumps({"ok": True, "docs": len(self.kb)}))
            return
        if u.path == "/api/ask":
            q = urllib.parse.parse_qs(u.query)
            text = (q.get("q") or [""])[0]
            full = (q.get("full") or ["0"])[0] not in ("0", "", "false")
            try:
                top = max(1, min(10, int((q.get("top") or ["3"])[0])))
            except ValueError:
                top = 3
            self._answer(text, full=full, top=top)
            return
        self._send(404, json.dumps({"error": "нет такой ручки"}))

    def do_POST(self):
        u = urllib.parse.urlparse(self.path)
        if u.path != "/api/ask":
            self._send(404, json.dumps({"error": "нет такой ручки"}))
            return
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            n = 0
        if n <= 0 or n > MAX_BODY:
            self._send(413, json.dumps({"error": f"тело должно быть от 1 байта до {MAX_BODY}"}))
            return
        raw = self.rfile.read(n).decode("utf-8", "replace")
        q = urllib.parse.parse_qs(u.query)
        full = (q.get("full") or ["0"])[0] not in ("0", "", "false")
        self._answer(raw, full=full)


def main():
    ap = argparse.ArgumentParser(description="Резидентная база: веб-чат и HTTP-ручка")
    ap.add_argument("--host", default="127.0.0.1",
                    help="127.0.0.1 — только эта машина; 0.0.0.0 — видно из локальной сети")
    ap.add_argument("--port", type=int, default=8787)
    args = ap.parse_args()

    print("Разбираю базу…", flush=True)
    Handler.kb = kbapi.KB()
    srv = ThreadingHTTPServer((args.host, args.port), Handler)
    where = f"http://{'127.0.0.1' if args.host == '0.0.0.0' else args.host}:{args.port}"
    print(f"База: {len(Handler.kb)} документов")
    print(f"Веб-чат: {where}")
    if args.host == "0.0.0.0":
        print("Слушаю на всех интерфейсах — с телефона в том же wifi открывайте по IP машины.")
    print("Остановить: Ctrl+C")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nостановлен")
    return 0


if __name__ == "__main__":
    sys.exit(main())
