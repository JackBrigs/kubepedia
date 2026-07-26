#!/usr/bin/env python3
"""Поиск по симптому: по тексту ошибки — готовый разбор из базы.

    kubepedia ask "cannot create regular file '/hostbin/cilium-mount': Permission denied"
    kubepedia ask "node NotReady cni plugin not initialized" --tag cilium
    kubepedia ask "Source /tmp/releases/cilium not found" --full

Ищет по алиасам (там лежат реальные строки ошибок), заголовкам, телу и тегам.
Печатает СУТЬ и ФИКС, а не только путь к файлу: причина + что делать.
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kdslib  # noqa: E402

REPO = os.path.dirname(HERE)
KB = os.path.join(REPO, "kb")

# разборы проблем и раннбуки — обычно то, что ищут по симптому
TYPE_BOOST = {"troubleshooting": 10, "runbook": 6, "best_practice": 3, "upgrade": 3}
# секции, где лежит «что делать»
FIX_SECTIONS = ("Known Issues", "Resolution", "Fix", "Remediation", "Procedure", "Steps")
CAUSE_SECTIONS = ("Summary", "Problem")
STOP = {
    "the", "and", "for", "not", "with", "that", "this", "from", "was", "are", "has",
    "при", "для", "как", "что", "это", "все", "или", "нет", "the", "los",
    "error", "err", "failed", "failure",  # слишком общие в логах
}


def norm(s):
    return re.sub(r"\s+", " ", (s or "")).strip()


def terms_of(query):
    """Токены запроса: слова/пути/идентификаторы длиной >=3, без стоп-слов."""
    raw = re.split(r"[^\w./-]+", query.lower(), flags=re.UNICODE)
    out = []
    for t in raw:
        t = t.strip("./-_")
        if len(t) >= 3 and t not in STOP:
            out.append(t)
    return out


def section_text(body, names):
    """Текст первой найденной секции из names."""
    for name in names:
        m = re.search(
            r"^##[ \t]+" + re.escape(name) + r"[ \t]*$(.*?)(?=^##[ \t]|\Z)",
            body, re.S | re.M)
        if m:
            return m.group(1).strip()
    return ""


def bullets(text, limit):
    """Первые `limit` маркеров списка (или абзацев), схлопнутые в одну строку каждый."""
    items = re.findall(r"^[-*][ \t]+(.+?)(?=^[-*][ \t]|\Z)", text, re.S | re.M)
    if not items:
        items = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    return [norm(re.sub(r"\s+", " ", i))[:400] for i in items[:limit]]


def load_docs():
    docs = []
    for path in kdslib.iter_doc_paths(KB):
        try:
            fm, _sections, body = kdslib.parse_doc(path)
        except Exception:
            continue
        if not isinstance(fm, dict) or not fm.get("id"):
            continue
        docs.append({
            "id": fm["id"],
            "title": fm.get("title") or "",
            "type": fm.get("type") or "",
            "tags": [str(t) for t in (fm.get("tags") or [])],
            "aliases": [str(a) for a in (fm.get("aliases") or [])],
            "ksp": fm.get("kubespray_version"),
            "k8s": fm.get("kubernetes_version"),
            "confidence": fm.get("confidence") or "",
            "path": os.path.relpath(path, REPO),
            "body": body,
            "lbody": body.lower(),
        })
    return docs


def score(doc, query, terms):
    """Счёт релевантности + причины совпадения."""
    q = query.lower().strip()
    s = 0
    why = []

    al = [a.lower() for a in doc["aliases"]]
    ttl = doc["title"].lower()

    # фраза целиком — самый сильный сигнал
    for a in al:
        if q and (q in a or a in q) and len(a) >= 6:
            s += 120
            why.append(f"алиас «{a}»")
            break
    if q and len(q) >= 8:
        if q in ttl:
            s += 70
            why.append("фраза в заголовке")
        elif q in doc["lbody"]:
            s += 45
            why.append("фраза в тексте")

    # по токенам
    hit_alias = hit_title = 0
    body_hits = 0
    for t in terms:
        if any(t in a for a in al):
            s += 14
            hit_alias += 1
        if t in ttl:
            s += 9
            hit_title += 1
        if t in [x.lower() for x in doc["tags"]]:
            s += 6
        c = doc["lbody"].count(t)
        if c:
            body_hits += 1
            s += min(c, 4) * 2

    if terms:
        # доля покрытия запроса телом — защищает от случайных совпадений
        s += int(20 * body_hits / len(terms))
    if hit_alias:
        why.append(f"совпало слов в алиасах: {hit_alias}")
    if hit_title:
        why.append(f"в заголовке: {hit_title}")

    s += TYPE_BOOST.get(doc["type"], 0)
    if doc["confidence"] in ("verified", "confirmed"):
        s += 4
    return s, why


def deref(text, titles):
    """Ссылки [[ID]] -> «Заголовок документа». Внутренние ID наружу не показываем."""
    def sub(m):
        rid = m.group(1).strip()
        t = titles.get(rid)
        return f"«{t}»" if t else "(см. смежный разбор)"
    text = re.sub(r"\[\[([^\]]+)\]\]", sub, text)
    # подстраховка: голый ID, если он просочился без скобок
    def sub_bare(m):
        t = titles.get(m.group(0))
        return f"«{t}»" if t else "(смежный разбор)"
    return re.sub(r"\b(?:TROUBLE|CONCEPT|PRACTICE|VARIABLE|COMPONENT|TAG|RELEASE|"
                  r"UPGRADE|RUNBOOK|API|MIGRATION|COMMAND|ADDON|OS)-[A-Z0-9_]+", sub_bare, text)


def envelope(doc):
    parts = []
    if doc["ksp"]:
        parts.append(f"Kubespray {doc['ksp']}")
    if doc["k8s"]:
        parts.append(f"k8s {doc['k8s']}")
    return "; ".join(parts) or "версия не ограничена"


def main():
    ap = argparse.ArgumentParser(
        description="Поиск по симптому: текст ошибки -> разбор из базы")
    ap.add_argument("query", nargs="+", help="текст ошибки или симптом")
    ap.add_argument("-n", "--top", type=int, default=3, help="сколько разборов показать")
    ap.add_argument("--tag", action="append", default=[],
                    help="сузить по тегу (можно несколько раз)")
    ap.add_argument("--type", dest="dtype", help="сузить по типу документа")
    ap.add_argument("--full", action="store_true",
                    help="показать полностью причину и все шаги фикса")
    ap.add_argument("--paths", action="store_true", help="только пути к файлам")
    args = ap.parse_args()

    query = " ".join(args.query)
    terms = terms_of(query)
    if not terms:
        print("нужен более содержательный запрос", file=sys.stderr)
        return 2

    docs = load_docs()
    titles = {d["id"]: d["title"] for d in docs}
    if args.tag:
        want = {t.lower() for t in args.tag}
        docs = [d for d in docs if want & {x.lower() for x in d["tags"]}]
    if args.dtype:
        docs = [d for d in docs if d["type"] == args.dtype]

    scored = []
    for d in docs:
        s, why = score(d, query, terms)
        if s > 0:
            scored.append((s, why, d))
    scored.sort(key=lambda x: (-x[0], x[2]["title"]))

    # отсечь шум: заметно слабее лидера — не показывать
    if not scored:
        print(f"По запросу «{query}» в базе ничего не найдено.")
        print("Знания в базе на английском: попробуйте слова прямо из текста ошибки")
        print("(например «NotReady cni», «Permission denied») или сузьте: --tag cilium")
        return 1
    best = scored[0][0]
    hits = [x for x in scored[: args.top] if x[0] >= max(25, best * 0.35)]
    if not hits:
        print(f"По запросу «{query}» уверенных совпадений нет "
              f"(лучший счёт {best} — слишком слабо).")
        print("Знания в базе на английском: попробуйте слова прямо из текста ошибки")
        print("(например «NotReady cni», «Permission denied») или сузьте: --tag cilium")
        print("\nБлижайшее по смыслу:")
        for _s, _w, d in scored[:3]:
            print(f"  · {d['title']}")
        return 1

    if args.paths:
        for _s, _w, d in hits:
            print(d["path"])
        return 0

    print(f"Запрос: {query}")
    print(f"Найдено разборов: {len(hits)} (из {len(scored)} совпадений)\n")

    for rank, (s, why, d) in enumerate(hits, 1):
        print("=" * 78)
        print(f"[{rank}] {d['title']}")
        print(f"    {envelope(d)} · достоверность: {d['confidence'] or 'н/д'} · {d['path']}")
        if why:
            print(f"    почему найдено: {', '.join(why[:3])} (счёт {s})")
        cause = section_text(d["body"], CAUSE_SECTIONS)
        if cause:
            print("\n  ПРИЧИНА / СУТЬ")
            if args.full:
                for line in deref(cause, titles).splitlines():
                    print("    " + line)
            else:
                txt = norm(deref(cause, titles))
                print("    " + txt[:600] + ("…" if len(txt) > 600 else ""))
        fix = section_text(d["body"], FIX_SECTIONS)
        if fix:
            print("\n  ЧТО ДЕЛАТЬ")
            if args.full:
                for line in deref(fix, titles).splitlines():
                    print("    " + line)
            else:
                for b in bullets(deref(fix, titles), 3):
                    print("    • " + b)
        print()
    if not args.full:
        print("Подробнее (полная причина и все шаги):  kubepedia ask \"…\" --full")
    return 0


if __name__ == "__main__":
    sys.exit(main())
