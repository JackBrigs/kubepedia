#!/usr/bin/env python3
"""Структурный ответ базы — общее ядро для всех способов доступа.

`ask.py` печатает в терминал: он и разбирает запрос, и решает, как это выглядит.
Для веб-чата и телеграм-бота нужен тот же разбор, но в виде данных — иначе каждый
новый вход начнёт заново реализовывать ранжирование, пороги уверенности и правила
триажа, и три входа неизбежно разойдутся в ответах.

Поэтому логика не дублируется: модуль переиспользует функции `ask.py` (поиск,
пороги, выделение сигналов) и только собирает их результат в словарь. Печать
остаётся в `ask.py` и не меняется — терминальный вывод должен остаться прежним.

    from kbapi import KB, ask
    kb = KB()                       # разбирает базу один раз
    kb.ask("cilium pods crashloop") # -> dict
"""
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ask as engine  # noqa: E402
import kdslib  # noqa: E402


class _Args:
    """Движок написан под argparse; здесь та же форма, но без разбора командной строки."""

    def __init__(self, top=3, tags=(), dtype=None, signals=3):
        self.top = top
        self.tag = list(tags)
        self.dtype = dtype
        self.signals = signals
        self.full = False
        self.paths = False


# Короткая форма причины: столько же, сколько печатает терминал без --full.
CAUSE_TRIM = 600


def _hit(sc, why, doc, titles):
    """Один разбор в виде данных: и коротко, и целиком — решает уже показывающий."""
    cause = engine.deref(engine.section_text(doc["body"], engine.CAUSE_SECTIONS), titles)
    fix = engine.deref(engine.section_text(doc["body"], engine.FIX_SECTIONS), titles)
    short = engine.norm(cause)
    return {
        # id нужен для схлопывания повторов между сигналами, наружу его не показывают
        "id": doc["id"],
        "title": doc["title"],
        "path": doc["path"],
        "type": doc["type"],
        "confidence": doc["confidence"] or "н/д",
        "envelope": engine.envelope(doc),
        "score": sc,
        "why": list(why[:3]),
        "cause": short[:CAUSE_TRIM] + ("…" if len(short) > CAUSE_TRIM else ""),
        "cause_full": cause,
        "fix": engine.bullets(fix, 3),
        "fix_full": fix,
    }


HINT_EN = ("Знания в базе на английском: попробуйте слова прямо из текста ошибки "
           "(например «NotReady cni», «Permission denied») или сузьте тегом.")


class KB:
    """База, разобранная один раз и живущая в памяти.

    Для CLI это не имеет значения — процесс всё равно умирает после ответа. Для
    сервера и бота это и есть смысл: корпус читается на старте, каждый следующий
    запрос стоит миллисекунды.
    """

    # Как часто вообще проверять, не изменилась ли база. Сама проверка стоит ~11 мс
    # (обход и stat), но на каждый запрос она удваивала бы время ответа впустую:
    # база правится руками, а не потоком.
    RELOAD_CHECK_SEC = 5.0

    def __init__(self):
        self._load()

    def _load(self):
        self.docs = engine.load_docs()
        self.titles = {d["id"]: d["title"] for d in self.docs}
        self.sig = self._signature()
        self.checked = time.monotonic()

    @staticmethod
    def _signature():
        return kdslib._corpus_signature(kdslib.iter_doc_paths(engine.KB))

    def maybe_reload(self):
        """Перечитать базу, если её правили.

        Резидентный процесс живёт долго, и без этого он отвечал бы из копии,
        снятой на старте: правку документа было бы видно только после перезапуска,
        а это ровно тот случай, когда никто не догадается перезапустить.
        """
        now = time.monotonic()
        if now - self.checked < self.RELOAD_CHECK_SEC:
            return False
        self.checked = now
        try:
            sig = self._signature()
        except OSError:
            return False
        if sig == self.sig:
            return False
        self._load()
        return True

    def __len__(self):
        return len(self.docs)

    def ask(self, text, top=3, tags=(), dtype=None, signals=3):
        """Разобрать запрос. Сырой вывод команды распознаётся сам — как в терминале."""
        text = text or ""
        if not text.strip():
            return {"mode": "query", "query": "", "ok": False,
                    "note": "Пустой запрос.", "hits": [], "near": [], "total": 0}
        args = _Args(top=top, tags=tags, dtype=dtype, signals=signals)
        # Текст в эту проверку идёт как есть: «сырой это вывод или запрос» решается
        # в том числе по переводам строк, и strip() у двухстрочного лога отрезает
        # последний — вставленный лог начинает искаться как одна длинная строка.
        if engine.looks_raw(text):
            return self._triage(text, args)
        return self._query(text.strip(), args)

    def _query(self, query, args):
        scored = engine.search(query, self.docs, args)
        if not scored:
            engine.log_gap(query, "query")
            return {"mode": "query", "query": query, "ok": False, "total": 0,
                    "note": f"По запросу «{query}» в базе ничего не найдено. {HINT_EN}",
                    "hits": [], "near": []}
        hits = engine.confident(scored, args.top)
        if not hits:
            engine.log_gap(query, "query", scored[0][0], scored[0][2]["title"])
            return {"mode": "query", "query": query, "ok": False, "total": len(scored),
                    "note": (f"Уверенных совпадений нет (лучший счёт {scored[0][0]} — "
                             f"слишком слабо). {HINT_EN}"),
                    "hits": [], "near": [d["title"] for _s, _w, d in scored[:3]]}
        return {"mode": "query", "query": query, "ok": True, "total": len(scored),
                "note": "", "near": [],
                "hits": [_hit(sc, why, d, self.titles) for sc, why, d in hits]}

    def _triage(self, raw, args):
        """Сырой вывод: каждый значимый сигнал разбирается отдельно.

        Повтор одного и того же разбора по разным сигналам не печатается второй раз —
        это один и тот же дефект, увиденный с двух сторон, и дублировать его значит
        сделать вид, что проблем две.
        """
        found = engine.extract_signals(raw, limit=max(args.signals, 1) + 2)
        if not found:
            return {"mode": "triage", "query": "", "ok": False, "signals": [],
                    "note": ("В этом выводе не нашлось строк, похожих на ошибку. "
                             "Похоже, вывод чистый — или ошибка в форме, которую разбор "
                             "не знает. Тогда передайте саму строку запросом."),
                    "lines": len(raw.splitlines()), "signals_total": 0,
                    "answered": 0, "unanswered": 0, "rest": []}

        out, shown = [], {}
        answered = unanswered = 0
        for i, (sig, _w, n) in enumerate(found[: args.signals], 1):
            scored = engine.search(sig, self.docs, args)
            terms = engine.terms_of(sig)
            stats = engine.query_stats(sig, terms, self.docs)
            answers = [x for x in scored if x[2]["type"] in engine.ANSWER_TYPES]
            grounded = [x for x in (answers or scored)
                        if engine.anchored(x[2], terms, stats)]
            hits = engine.confident(grounded, min(args.top, 2), floor=engine.TRIAGE_FLOOR)
            item = {"n": i, "signal": sig, "count": n, "hits": [], "note": "", "same_as": None}
            if not hits:
                unanswered += 1
                top = scored[0] if scored else None
                engine.log_gap(sig, "triage", top[0] if top else 0,
                               top[2]["title"] if top else "")
                item["note"] = ("В базе разбора на этот сигнал нет. Это дыра в покрытии, "
                                "а не отсутствие ответа.")
                out.append(item)
                continue
            answered += 1
            fresh = [h for h in hits if h[2]["id"] not in shown]
            if not fresh:
                first = hits[0][2]
                item["same_as"] = shown[first["id"]]
                item["note"] = (f"Тот же разбор, что и по сигналу {item['same_as']}: "
                                f"«{first['title']}» — сигналы про одну проблему.")
                out.append(item)
                continue
            for sc, why, d in fresh:
                shown[d["id"]] = i
                item["hits"].append(_hit(sc, why, d, self.titles))
            out.append(item)

        rest = [{"signal": s, "count": n} for s, _w, n in found[args.signals:]]
        return {"mode": "triage", "query": "", "ok": answered > 0, "signals": out,
                "note": "", "lines": len(raw.splitlines()),
                "signals_total": len(found), "answered": answered,
                "unanswered": unanswered, "rest": rest}


def render_text(res, full=False):
    """Плоский текст ответа — для бота и для всего, где нет разметки."""
    L = []
    if res["mode"] == "triage":
        if not res.get("signals"):
            return res["note"]
        L.append(f"Строк вывода: {res['lines']}. Значимых сигналов: {res['signals_total']}.")
        for it in res["signals"]:
            rep = f" ×{it['count']}" if it["count"] > 1 else ""
            L.append("")
            L.append(f"── СИГНАЛ {it['n']}{rep}: {it['signal'][:200]}")
            if it["note"]:
                L.append(f"   {it['note']}")
            for h in it["hits"]:
                L.extend(_hit_lines(h, full))
        if res["rest"]:
            L.append("")
            L.append(f"Ещё сигналов в выводе: {len(res['rest'])} (не разбирались)")
        L.append("")
        L.append(f"Итог: разобрано — {res['answered']}, без ответа в базе — {res['unanswered']}.")
        return "\n".join(L)

    if not res["ok"]:
        L.append(res["note"])
        if res.get("near"):
            L.append("")
            L.append("Ближайшее по смыслу:")
            L.extend(f"  · {t}" for t in res["near"])
        return "\n".join(L)

    L.append(f"Запрос: {res['query']}")
    L.append(f"Найдено разборов: {len(res['hits'])} (из {res['total']} совпадений)")
    for h in res["hits"]:
        L.extend(_hit_lines(h, full))
    return "\n".join(L)


def _hit_lines(h, full):
    L = ["", f"▸ {h['title']}",
         f"  {h['envelope']} · достоверность: {h['confidence']}"]
    cause = h["cause_full"] if full else h["cause"]
    if cause:
        L.append("")
        L.append("  ПРИЧИНА / СУТЬ")
        L.extend("    " + ln for ln in cause.splitlines())
    fix = h["fix_full"].splitlines() if full else ["• " + b for b in h["fix"]]
    if any(x.strip() for x in fix):
        L.append("")
        L.append("  ЧТО ДЕЛАТЬ")
        L.extend("    " + ln for ln in fix)
    return L
