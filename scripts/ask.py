#!/usr/bin/env python3
"""Поиск по симптому: по тексту ошибки — готовый разбор из базы.

    kubepedia ask "cannot create regular file '/hostbin/cilium-mount': Permission denied"
    kubepedia ask "node NotReady cni plugin not initialized" --tag cilium
    kubepedia ask "Source /tmp/releases/cilium not found" --full

Принимает и **сырой вывод** — не нужно вытаскивать строку ошибки руками:

    kubectl -n kube-system describe pod cilium-abcde | kubepedia ask -
    kubectl -n kube-system logs ds/cilium --tail=200 | kubepedia ask -
    journalctl -u kubelet -n 300 --no-pager | kubepedia ask -

В этом режиме из вывода выделяются значимые сигналы (Warning-события, Reason,
строки уровня error/fatal/panic, отказы systemd), шум вроде таймстампов, IP и
хешей вычищается, близкие строки схлопываются — и каждый сигнал разбирается
отдельно. Сигналы, на которые в базе ответа нет, показываются явно: это дыры,
а не «ничего не найдено».

Ищет по алиасам (там лежат реальные строки ошибок), заголовкам, телу и тегам.
Печатает СУТЬ и ФИКС, а не только путь к файлу: причина + что делать.
"""
import argparse
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kdslib  # noqa: E402

REPO = os.path.dirname(HERE)
KB = os.path.join(REPO, "kb")

# разборы проблем и раннбуки — обычно то, что ищут по симптому
# бонус типа намеренно мал: по симптому ищут разбор проблемы, но перевешивать
# содержательное совпадение он не должен — замер показал, что при большом весе
# он начинает тасовать доки внутри отвечающего слоя и портит выдачу
TYPE_BOOST = {"troubleshooting": 10, "runbook": 6, "best_practice": 3, "upgrade": 3}
# секции, где лежит «что делать»
FIX_SECTIONS = ("Known Issues", "Resolution", "Fix", "Remediation", "Procedure", "Steps")
CAUSE_SECTIONS = ("Summary", "Problem")
# типы, которые отвечают на вопрос «что случилось и что делать»
ANSWER_TYPES = {"troubleshooting", "runbook", "best_practice", "upgrade", "concept"}
# порог уверенности для строк лога (см. confident): ниже — честное «нет ответа»
# пороги калиброваны по замеру: мусорный запрос набирает 17-26, самый слабый
# реальный сигнал из лога — 65, точное совпадение строки ошибки — сотни
TRIAGE_FLOOR = 60
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


# --- разбор сырого вывода (kubectl describe / logs / journalctl) ---

# строки, которые стоит разбирать, и их вес: чем конкретнее сигнал, тем выше
# Порядок весов важнее самих чисел: конкретная ошибка должна обгонять состояние.
# `Reason: CrashLoopBackOff` описывает СИМПТОМ, а `Permission denied ...` — причину;
# если состояние весит больше, разбор уходит в общий док про CrashLoopBackOff и
# настоящая строка отказа теряется в хвосте.
SIGNAL_PATTERNS = [
    # конкретный отказ — то, ради чего вывод и вставляют
    (re.compile(r"\b(?:Permission denied|no such file or directory|connection refused|"
                r"context deadline exceeded|i/o timeout|no route to host|"
                r"certificate has expired|certificate is not valid|x509|"
                r"exec format error|address already in use|too many open files|"
                r"read-only file system|invalid capacity|quorum|"
                r"unauthorized|forbidden)\b", re.I), 36),
    (re.compile(r"panic:\s*(.+)$"), 34),
    (re.compile(r"\blevel=(?:error|fatal)\b(.*)$"), 26),
    (re.compile(r"^[EF]\d{4}\s+[\d:.]+\s+\d+\s+\S+\]\s*(.+)$"), 26),   # klog E0727 …
    (re.compile(r"\b(?:Failed to|failed to|Unable to|unable to|cannot|Cannot|"
                r"Error:|error:)\s(.{6,})$"), 24),
    (re.compile(r"^\s*Warning\s+(\S+)\s+.*?\s(.+)$"), 22),        # события describe
    # состояние — контекст, а не причина: намеренно ниже конкретных строк
    (re.compile(r"\b(CrashLoopBackOff|ImagePullBackOff|ErrImagePull|CreateContainerConfigError|"
                r"CreateContainerError|RunContainerError|FailedScheduling|FailedMount|"
                r"FailedAttachVolume|NetworkNotReady|ContainerStatusUnknown|OOMKilled|Evicted|"
                r"NodeNotReady|InvalidImageName|ErrImageNeverPull)\b"), 16),
]

# шум, который мешает схлопывать одинаковые по смыслу строки
NOISE = [
    # journalctl: «Jul 27 05:58:14 worker-03 kubelet[1842]:» целиком
    (re.compile(r"^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+\S+\s+[\w.-]+\[\d+\]:\s*"), ""),
    (re.compile(r"\b\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?Z?\b"), " "),
    (re.compile(r"\b\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\b"), " "),      # journalctl без юнита
    # klog: «E0727 05:58:14.100221    1842 remote_runtime.go:222]» где бы ни стоял
    (re.compile(r"[IWEF]\d{4}\s+[\d:.]+\s+\d+\s+[\w.-]+:\d+\]\s*"), ""),
    (re.compile(r"^[IWEF]\d{4}\s+[\d:.]+\s+\d+\s+\S+?\]"), " "),          # klog, иные формы
    (re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}(?::\d+)?\b"), "<ip>"),
    (re.compile(r"\b[0-9a-f]{7,}\b"), "<hash>"),
    (re.compile(r"\b\d+m?s\b"), "<dur>"),
    (re.compile(r"\b\d{3,}\b"), "<n>"),
    (re.compile(r"\s+"), " "),
]


def looks_raw(text):
    """Похоже ли на вставленный вывод команды, а не на короткий запрос."""
    return text.count("\n") >= 2 or len(text) > 400


def denoise(line):
    out = line.strip()
    for rx, rep in NOISE:
        out = rx.sub(rep, out)
    return out.strip(" |·-")


def extract_signals(text, limit=4):
    """Значимые строки из сырого вывода -> [(строка_для_поиска, вес, сколько_раз)].

    Одинаковые по смыслу строки схлопываются после вычистки шума: повтор в логе
    усиливает сигнал, но не должен занимать все места в выдаче.
    """
    found = {}
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or len(line.strip()) < 12:
            continue
        weight = 0
        for rx, w in SIGNAL_PATTERNS:
            if rx.search(line):
                weight = max(weight, w)
        if not weight:
            continue
        key = denoise(line).lower()
        if len(key) < 12:
            continue
        if key in found:
            found[key]["n"] += 1
            found[key]["w"] = max(found[key]["w"], weight)
        else:
            found[key] = {"text": denoise(line), "w": weight, "n": 1}
    ranked = sorted(found.values(), key=lambda x: (-(x["w"] + min(x["n"], 5) * 2), x["text"]))
    return [(x["text"], x["w"], x["n"]) for x in ranked[:limit]]


GAP_LOG = os.path.join(REPO, "reports", "gaps.jsonl")


def log_gap(query, mode, best_score=0, best_title=""):
    """Записать запрос, на который база не ответила.

    Это единственный сигнал, которого не хватало петле самоулучшения: learn.py
    видит, О ЧЁМ спрашивают (темы), но не видел, на чём база промолчала. Файл
    локальный и не коммитится — в строку ошибки попадают имена хостов и адреса;
    наружу идёт только агрегат, который собирает learn.py.
    """
    if os.environ.get("KUBEPEDIA_NO_GAP_LOG"):
        return
    rec = {
        "ts": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "query": norm(query)[:300],
        "mode": mode,
        "best_score": int(best_score),
        "best_title": best_title[:120],
    }
    try:
        os.makedirs(os.path.dirname(GAP_LOG), exist_ok=True)
        with open(GAP_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except OSError:
        pass          # журнал не должен ломать ответ


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
            "ltitle": (fm.get("title") or "").lower(),
            "laliases": " ".join(str(a).lower() for a in (fm.get("aliases") or [])),
            "ltags": " ".join(str(t).lower() for t in (fm.get("tags") or [])),
            "dl": max(len(body), 1),
        })
    return docs


def query_stats(query, terms, pool):
    """Веса терминов и средняя длина документа — считаются один раз на запрос.

    Без IDF длинный запрос прозой тонет в общих словах: `node`, `version`,
    `kubespray` встречаются в сотнях документов и дают столько же очков, сколько
    `nf_conntrack`. Редкость термина — главный сигнал, а не факт совпадения.
    """
    n = max(len(pool), 1)
    idf = {}
    for t in set(terms):
        df = 0
        for d in pool:
            if t in d["lbody"] or t in d["ltitle"] or t in d["laliases"]:
                df += 1
        # BM25-овский idf: термин, встречающийся почти везде, весит около нуля
        idf[t] = math.log(1 + (n - df + 0.5) / (df + 0.5))
    avgdl = sum(d["dl"] for d in pool) / n
    return {"idf": idf, "avgdl": avgdl, "mass": sum(idf.values()) or 1.0}


K1 = 1.2      # насыщение по частоте: третье вхождение термина почти не добавляет
B = 0.75      # нормировка по длине документа
W_BODY = 1.0
W_TITLE = 2.5
W_ALIAS = 3.0
W_TAG = 0.8
# бонусы за совпадение фразой: после нормировки базовый счёт живёт в сотнях,
# поэтому точное совпадение алиаса должно весить сопоставимо, иначе строка
# ошибки проигрывает документу, где просто много общих слов
PHRASE_ALIAS = 400
PHRASE_TITLE = 200
PHRASE_BODY = 120


def score(doc, query, terms, stats):
    """Счёт релевантности + причины совпадения.

    Итог нормируется на суммарный вес терминов запроса, чтобы пороги
    (`confident`, `TRIAGE_FLOOR`) означали одно и то же для короткой строки
    ошибки и для длинного предложения прозой.
    """
    q = query.lower().strip()
    idf, avgdl = stats["idf"], stats["avgdl"]
    s = 0.0
    why = []
    al, ttl = doc["laliases"], doc["ltitle"]
    ltags = doc["ltags"]

    hit_alias = hit_title = covered = 0
    for t in set(terms):
        w = idf.get(t, 0.0)
        if w <= 0:
            continue
        found = False
        tf = doc["lbody"].count(t)
        if tf:
            norm = tf * (K1 + 1) / (tf + K1 * (1 - B + B * doc["dl"] / avgdl))
            s += w * norm * W_BODY
            found = True
        if t in ttl:
            s += w * W_TITLE
            hit_title += 1
            found = True
        if t in al:
            s += w * W_ALIAS
            hit_alias += 1
            found = True
        if t in ltags:
            s += w * W_TAG
            found = True
        covered += 1 if found else 0

    # доля покрытия запроса: документ, где нашлась половина слов, не равен тому,
    # где нашлись все — даже если суммарные частоты близки
    if terms:
        frac = covered / len(set(terms))
        s *= 0.25 + 0.75 * frac * frac

    s = 100.0 * s / stats["mass"]

    # фраза целиком — сигнал сильнее любой поштучной суммы, но с оглядкой на
    # покрытие: короткий общий алиас внутри длинного запроса не равен строке
    # ошибки, совпавшей целиком
    for a in doc["aliases"]:
        a = a.lower()
        if not q or len(a) < 6:
            continue
        if q in a:
            s += PHRASE_ALIAS
            why.append(f"алиас «{a}»")
            break
        if a in q:
            # алиас внутри длинного запроса: до 30% покрытия это шум (общее слово
            # вроде «network» внутри предложения), дальше вес растёт до полного
            cover = len(a) / len(q)
            s += PHRASE_ALIAS * max(0.0, (cover - 0.3) / 0.7)
            if cover >= 0.3:
                why.append(f"алиас «{a}»")
            break
    if q and len(q) >= 8:
        if q in ttl:
            s += PHRASE_TITLE
            why.append("фраза в заголовке")
        elif q in doc["lbody"]:
            s += PHRASE_BODY
            why.append("фраза в тексте")

    # соседние слова запроса, стоящие рядом и в документе
    # соседние слова запроса, стоящие рядом и в документе. Вес — по редкости пары:
    # «warning failed» встречается в половине базы и не должен ничего значить,
    # а «cilium-cni failed» — сильный сигнал
    near = gain = 0
    for a, b in zip(terms, terms[1:]):
        if f"{a} {b}" in ttl or f"{a} {b}" in doc["lbody"]:
            near += 1
            gain += min(idf.get(a, 0.0), idf.get(b, 0.0))
    if gain:
        s += 25 * gain
        why.append(f"словосочетаний: {near}")

    if hit_alias:
        why.append(f"совпало слов в алиасах: {hit_alias}")
    if hit_title:
        why.append(f"в заголовке: {hit_title}")

    s += TYPE_BOOST.get(doc["type"], 0)
    if doc["confidence"] in ("verified", "confirmed"):
        s += 4
    return int(s), why


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


def search(query, docs, args):
    """[(счёт, причины, док)] по убыванию — отфильтровано по тегу/типу и порогу."""
    terms = terms_of(query)
    if not terms:
        return []
    pool = docs
    if args.tag:
        want = {t.lower() for t in args.tag}
        pool = [d for d in pool if want & {x.lower() for x in d["tags"]}]
    if args.dtype:
        pool = [d for d in pool if d["type"] == args.dtype]
    stats = query_stats(query, terms, pool)
    scored = []
    for d in pool:
        sc, why = score(d, query, terms, stats)
        if sc > 0:
            scored.append((sc, why, d))
    scored.sort(key=lambda x: (-x[0], x[2]["title"]))
    return scored


IDF_SPECIFIC = 4.0     # термин примерно из <1.5% документов базы


def anchored(doc, terms, stats):
    """Опирается ли совпадение хоть на один специфичный термин запроса.

    Строка лога всегда содержит общие слова (`warning`, `failed`, `kubelet`), и
    по ним найдётся «похожий» документ для чего угодно. Ответ засчитывается,
    только если он держится на редком термине — имени параметра, компонента,
    вызова. Иначе честнее сказать, что разбора нет.
    """
    idf = stats["idf"]
    return any(
        idf.get(t, 0.0) >= IDF_SPECIFIC
        and (t in doc["lbody"] or t in doc["ltitle"] or t in doc["laliases"])
        for t in set(terms)
    )


def confident(scored, top, floor=40):
    """Совпадения, которые не стыдно показать: не сильно слабее лидера и выше порога.

    В триаже порог выше: там запрос — строка лога целиком, и почти любой док
    наберёт очки на общих словах вроде `failed`, `node`, `container`. Без
    абсолютного пола незнакомая ошибка получает уверенный, но случайный разбор —
    хуже, чем честное «в базе этого нет».
    """
    if not scored:
        return []
    best = scored[0][0]
    return [x for x in scored[:top] if x[0] >= max(floor, best * 0.35)]


def print_hit(rank, sc, why, d, titles, full):
    print("=" * 78)
    print(f"[{rank}] {d['title']}")
    print(f"    {envelope(d)} · достоверность: {d['confidence'] or 'н/д'} · {d['path']}")
    if why:
        print(f"    почему найдено: {', '.join(why[:3])} (счёт {sc})")
    cause = section_text(d["body"], CAUSE_SECTIONS)
    if cause:
        print("\n  ПРИЧИНА / СУТЬ")
        if full:
            for line in deref(cause, titles).splitlines():
                print("    " + line)
        else:
            txt = norm(deref(cause, titles))
            print("    " + txt[:600] + ("…" if len(txt) > 600 else ""))
    fix = section_text(d["body"], FIX_SECTIONS)
    if fix:
        print("\n  ЧТО ДЕЛАТЬ")
        if full:
            for line in deref(fix, titles).splitlines():
                print("    " + line)
        else:
            for b in bullets(deref(fix, titles), 3):
                print("    • " + b)
    print()


def triage(raw, docs, args):
    """Разбор сырого вывода: выделить сигналы и разобрать каждый отдельно."""
    signals = extract_signals(raw, limit=max(args.signals, 1) + 2)
    titles = {d["id"]: d["title"] for d in docs}
    if not signals:
        print("В этом выводе не нашлось строк, похожих на ошибку.")
        print("Похоже, вывод чистый — или ошибка в форме, которую разбор не знает.")
        print("Тогда передайте саму строку:  kubepedia ask \"текст ошибки\"")
        return 1

    lines = len(raw.splitlines())
    print(f"Разобрано строк вывода: {lines}. Значимых сигналов: {len(signals)}.")
    print("Ниже — по одному разбору на сигнал, в порядке значимости.\n")

    answered = unanswered = 0
    shown = {}
    for i, (sig, _w, n) in enumerate(signals[: args.signals], 1):
        repeat = f" ×{n}" if n > 1 else ""
        print("─" * 78)
        print(f"СИГНАЛ {i}{repeat}: {sig[:200]}")
        print()
        scored = search(sig, docs, args)
        # в триаже нужен разбор проблемы, а не справочник: доки-справки
        # (теги ansible, переменные) отбрасываются, если есть хоть один разбор
        answers = [x for x in scored if x[2]["type"] in ANSWER_TYPES]
        stats = query_stats(sig, terms_of(sig), docs)
        grounded = [x for x in (answers or scored) if anchored(x[2], terms_of(sig), stats)]
        hits = confident(grounded, min(args.top, 2), floor=TRIAGE_FLOOR)
        if not hits:
            unanswered += 1
            top = scored[0] if scored else None
            log_gap(sig, "triage", top[0] if top else 0, top[2]["title"] if top else "")
            print("  В базе разбора на этот сигнал нет.")
            print("  Это дыра в покрытии, а не отсутствие ответа: если причина найдётся,")
            print("  её стоит внести отдельным разбором.\n")
            continue
        answered += 1
        fresh = [h for h in hits if h[2]["id"] not in shown]
        if not fresh:
            first = hits[0][2]
            print(f"  Тот же разбор, что и по сигналу {shown[first['id']]}: "
                  f"«{first['title']}» — сигналы описывают одну и ту же проблему.\n")
            continue
        for rank, (sc, why, d) in enumerate(fresh, 1):
            shown[d["id"]] = i
            print_hit(rank, sc, why, d, titles, args.full)

    rest = signals[args.signals:]
    if rest:
        print("─" * 78)
        print(f"Ещё сигналов в выводе: {len(rest)} (не разбирались, "
              f"поднимите порог: --signals {args.signals + len(rest)})")
        for sig, _w, n in rest:
            print(f"  · {sig[:150]}{' ×%d' % n if n > 1 else ''}")
    print()
    print(f"Итог: разобрано сигналов — {answered}, без ответа в базе — {unanswered}.")
    if not args.full:
        print("Подробнее (полная причина и все шаги):  … | kubepedia ask - --full")
    return 0 if answered else 1


def main():
    ap = argparse.ArgumentParser(
        description="Поиск по симптому: текст ошибки -> разбор из базы")
    ap.add_argument("query", nargs="*",
                    help="текст ошибки или симптом; «-» или пустой ввод — читать stdin")
    ap.add_argument("-n", "--top", type=int, default=3, help="сколько разборов показать")
    ap.add_argument("--tag", action="append", default=[],
                    help="сузить по тегу (можно несколько раз)")
    ap.add_argument("--type", dest="dtype", help="сузить по типу документа")
    ap.add_argument("--full", action="store_true",
                    help="показать полностью причину и все шаги фикса")
    ap.add_argument("--paths", action="store_true", help="только пути к файлам")
    ap.add_argument("--signals", type=int, default=3,
                    help="сколько сигналов разбирать из сырого вывода (по умолчанию 3)")
    args = ap.parse_args()

    query = " ".join(args.query)
    # «-», либо запуск без аргументов с данными на входе -> читаем сырой вывод
    if query.strip() == "-" or (not query and not sys.stdin.isatty()):
        query = sys.stdin.read()
    if not query.strip():
        ap.print_usage(sys.stderr)
        print("нужен текст ошибки, либо подайте вывод команды на stdin", file=sys.stderr)
        return 2

    docs = load_docs()
    if looks_raw(query):
        return triage(query, docs, args)

    titles = {d["id"]: d["title"] for d in docs}
    scored = search(query, docs, args)
    if not scored:
        log_gap(query, "query")
        print(f"По запросу «{query}» в базе ничего не найдено.")
        print("Знания в базе на английском: попробуйте слова прямо из текста ошибки")
        print("(например «NotReady cni», «Permission denied») или сузьте: --tag cilium")
        return 1
    hits = confident(scored, args.top)
    if not hits:
        log_gap(query, "query", scored[0][0], scored[0][2]["title"])
        print(f"По запросу «{query}» уверенных совпадений нет "
              f"(лучший счёт {scored[0][0]} — слишком слабо).")
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
    for rank, (sc, why, d) in enumerate(hits, 1):
        print_hit(rank, sc, why, d, titles, args.full)
    if not args.full:
        print("Подробнее (полная причина и все шаги):  kubepedia ask \"…\" --full")
    return 0


if __name__ == "__main__":
    sys.exit(main())
