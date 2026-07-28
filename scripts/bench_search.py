#!/usr/bin/env python3
"""Замер качества поиска по базе — до и после любой правки ранжирования.

Четыре класса запросов, по каждому доля попаданий в первую позицию и в тройку:

  alias    — строка ошибки из алиасов документа (доминирующий реальный запрос)
  title    — заголовок целиком
  partial  — заголовок без первого значимого термина (лёгкий перефраз)
  prose    — предложение из тела документа (запрос «своими словами»)

Ground truth — документ, из которого взят запрос. У класса prose эта разметка
несовершенна по своей природе: тема часто покрыта несколькими документами, и
«промах» может означать корректный ответ другим доком. Поэтому есть --misses:
он печатает промахи, чтобы отделить настоящие ошибки от артефактов разметки.

    python3 scripts/bench_search.py
    python3 scripts/bench_search.py --n 200 --misses prose
"""
import argparse
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ask  # noqa: E402

ANSWER_TYPES = ("troubleshooting", "concept", "best_practice", "runbook", "upgrade")


class Args:
    """Заглушка под сигнатуру ask.search()."""
    tag = []
    dtype = None
    top = 3


def body_sentence(doc):
    """Предложение из середины тела — как оператор описал бы проблему словами."""
    body = re.sub(r"```.*?```", " ", doc["body"], flags=re.S)
    body = re.sub(r"\[\[[^\]]+\]\]", " ", body)
    body = re.sub(r"[|#*`>-]", " ", body)
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body)
             if 60 < len(s.strip()) < 220]
    return sents[len(sents) // 2] if sents else None


def drop_first_term(title):
    words = [w for w in re.split(r"\W+", title) if len(w) > 3]
    return " ".join(words[1:]) if len(words) > 2 else title


def build_sets(pool, n, seed):
    random.seed(seed)
    aliases = [(a, d["id"]) for d in pool for a in d["aliases"] if len(a) >= 12]
    sets = {
        "alias": random.sample(aliases, min(n, len(aliases))),
        "title": [(d["title"], d["id"]) for d in random.sample(pool, min(n, len(pool)))],
        "partial": [(drop_first_term(d["title"]), d["id"])
                    for d in random.sample(pool, min(n, len(pool)))],
    }
    prose = []
    for d in random.sample(pool, min(n, len(pool))):
        q = body_sentence(d)
        if q:
            prose.append((q, d["id"]))
    sets["prose"] = prose
    return sets


def run(name, pairs, docs, show_misses):
    hit1 = hit3 = miss = 0
    misses = []
    for q, want in pairs:
        ranked = ask.search(q, docs, Args)[:3]
        ids = [x[2]["id"] for x in ranked]
        if ids[:1] == [want]:
            hit1 += 1
        elif want in ids:
            hit3 += 1
        else:
            miss += 1
            misses.append((q, want, ranked[0][2] if ranked else None))
    n = max(hit1 + hit3 + miss, 1)
    print(f"{name:8} n={n:3}  top-1 {100 * hit1 / n:5.1f}%   "
          f"top-3 {100 * (hit1 + hit3) / n:5.1f}%   промах {100 * miss / n:5.1f}%")
    if show_misses:
        titles = {d["id"]: d["title"] for d in docs}
        for q, want, got in misses:
            print(f"    ЗАПРОС : {q[:110]}")
            print(f"    ЖДАЛИ  : {titles.get(want, want)}")
            print(f"    ПОЛУЧИЛИ: {got['title'] if got else '—'}\n")
    return hit1, hit3, miss


def main():
    ap = argparse.ArgumentParser(description="Замер качества поиска по базе")
    ap.add_argument("--n", type=int, default=120, help="запросов на класс")
    ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--misses", help="печатать промахи класса (alias|title|partial|prose|all)")
    ap.add_argument("--only", help="считать только этот класс")
    args = ap.parse_args()

    docs = ask.load_docs()
    pool = [d for d in docs if d["type"] in ANSWER_TYPES]
    print(f"документов: {len(docs)}, отвечающий слой: {len(pool)}\n")

    sets = build_sets(pool, args.n, args.seed)
    for name, pairs in sets.items():
        if args.only and name != args.only:
            continue
        run(name, pairs, docs, args.misses in (name, "all"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
