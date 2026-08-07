"""
Shared helpers for Kubepedia KDS tooling (validator + index generator).

Single source of the type/section/version tables so the two scripts never drift.
Tables mirror standards/kds.md; keep them in sync when KDS changes.
"""
import os
import re
import glob
import datetime
import hashlib
import pickle

import yaml

# type -> ID prefix (KDS "ID-type table")
TYPE_PREFIX = {
    "component": "COMPONENT",
    "variable": "VARIABLE",
    "role": "ROLE",
    "playbook": "PLAYBOOK",
    "task": "TASK",
    "api": "API",
    "feature_gate": "FEATUREGATE",
    "configuration": "CONFIG",
    "release": "RELEASE",
    "issue": "ISSUE",
    "pull_request": "PR",
    "troubleshooting": "TROUBLE",
    "best_practice": "PRACTICE",
    "migration": "MIGRATION",
    "upgrade": "UPGRADE",
    "command": "COMMAND",
    "concept": "CONCEPT",
    "ansible_tag": "TAG",
}

# additional required sections per type (KDS "Section Profiles"); every type
# also requires Summary (first) and References (last).
PROFILE = {
    "component": ["Context", "Implementation", "Configuration", "Compatibility"],
    "variable": ["Implementation", "Compatibility"],
    "role": ["Implementation", "Configuration", "Compatibility"],
    "playbook": ["Implementation", "Compatibility"],
    "task": ["Implementation"],
    "api": ["Implementation", "Compatibility", "Upgrade Notes"],
    "feature_gate": ["Implementation", "Compatibility"],
    "configuration": ["Configuration", "Compatibility"],
    "release": ["Implementation", "Upgrade Notes", "Compatibility"],
    "issue": ["Problem", "Context", "Known Issues"],
    "pull_request": ["Implementation"],
    "troubleshooting": ["Problem", "Context", "Diagnostics", "Known Issues"],
    "best_practice": ["Context", "Implementation"],
    "migration": ["Problem", "Implementation", "Upgrade Notes", "Compatibility"],
    "upgrade": ["Implementation", "Upgrade Notes", "Compatibility"],
    "command": ["Diagnostics"],
    "concept": ["Context"],
    "ansible_tag": ["Context", "Implementation", "Compatibility"],
}

# which non-null version dimension a type requires (KDS "Version Fields")
# kubespray | kubernetes | component | any
VERSION_RULE = {
    "variable": "kubespray",
    "role": "kubespray",
    "playbook": "kubespray",
    "task": "kubespray",
    "release": "kubespray",
    "migration": "kubespray",
    "upgrade": "kubespray",
    "ansible_tag": "kubespray",
    "api": "kubernetes",
    "feature_gate": "kubernetes",
    "component": "component",
    "issue": "any",
    "pull_request": "any",
    "troubleshooting": "any",
    "best_practice": "any",
    "command": "any",
    "configuration": "any",
    "concept": "any",
}

ID_RE = re.compile(r"^[A-Z]+-[A-Z0-9]+(_[A-Z0-9]+)*(__[A-Z0-9]+(_[A-Z0-9]+)*)?$")

VERSION_KEYS = ("kubespray_version", "kubernetes_version", "component_version")


def required_sections(doc_type):
    return ["Summary"] + PROFILE.get(doc_type, []) + ["References"]


def iter_doc_paths(kb_root):
    return sorted(
        glob.glob(os.path.join(kb_root, "**", "*.md"), recursive=True)
    )


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_doc(path):
    """Return (frontmatter dict, section-title list, body). Raises on bad YAML."""
    text = read(path)
    fm, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if m:
        fm = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)
        # YAML parses unquoted ISO dates as date objects; KDS stores them as ISO
        # strings. Normalize top-level date/datetime scalars so schema validation
        # and JSON index serialization see strings.
        if isinstance(fm, dict):
            for k, v in list(fm.items()):
                if isinstance(v, (datetime.date, datetime.datetime)):
                    fm[k] = v.isoformat()
    sections = re.findall(r"^##[ \t]+(.+?)[ \t]*$", body, re.M)
    return fm, sections, body


# Разбор всей базы стоит ~1.6 с на 2700 документов, и почти всё это — yaml.safe_load
# фронтматтера. Для ночного прогона это неважно, но поиск по симптому платит ту же
# секунду на каждый запрос, а его дёргают из диалога по несколько раз подряд. Поэтому
# разобранный корпус кладётся в pickle рядом с базой.
#
# Инвалидация — по подписи из (путь, mtime_ns, размер) всех файлов: обход и stat 2700
# файлов стоят 11 мс, то есть проверка актуальности дешевле разбора в полтораста раз.
# Содержимое не хэшируется намеренно: любая правка меняет mtime и размер, а совпадение
# обоих при изменённом тексте потребовало бы подгонки байт в байт.
#
# Кэш — производное от kb/, а не знание: он вне git, его безопасно удалить в любой
# момент, и при первом же запросе он соберётся заново.
CORPUS_CACHE_VERSION = 1


def corpus_cache_path(kb_root):
    return os.path.join(os.path.dirname(os.path.abspath(kb_root)), ".cache", "corpus.pkl")


def _corpus_signature(paths):
    h = hashlib.sha1()
    h.update(f"v{CORPUS_CACHE_VERSION}\n".encode())
    for p in paths:
        st = os.stat(p)
        h.update(f"{p}\0{st.st_mtime_ns}\0{st.st_size}\n".encode())
    return h.hexdigest()


def load_corpus(kb_root):
    """Вернуть [(path, frontmatter, sections, body)] по всей базе, разобрав её один раз.

    Документы с битым YAML пропускаются: это путь для чтения, а не для проверки —
    о нарушениях сообщает validate_kds.py, который разбирает базу сам и видит ошибку.
    """
    paths = iter_doc_paths(kb_root)
    sig = _corpus_signature(paths)
    cache = corpus_cache_path(kb_root)
    try:
        with open(cache, "rb") as f:
            blob = pickle.load(f)
        if blob.get("sig") == sig:
            return blob["docs"]
    except Exception:
        pass  # нет кэша, старый формат, битый файл — всё лечится пересборкой

    docs = []
    for path in paths:
        try:
            fm, sections, body = parse_doc(path)
        except Exception:
            continue
        docs.append((path, fm, sections, body))

    # Запись через временный файл и rename: два параллельных запроса не должны
    # оставить наполовину записанный кэш, который следующий запуск примет за целый.
    try:
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        tmp = f"{cache}.{os.getpid()}.tmp"
        with open(tmp, "wb") as f:
            pickle.dump({"sig": sig, "docs": docs}, f, protocol=pickle.HIGHEST_PROTOCOL)
        os.replace(tmp, cache)
    except Exception:
        pass  # кэш — ускорение, а не условие работы

    return docs


def build_index(kb_root, repo_root):
    """Build the derived index from documents. Returns (documents, relations, ids)
    as deterministically ordered lists of plain dicts / strings."""
    documents, relations, ids = [], [], []
    for path in iter_doc_paths(kb_root):
        fm, _sections, _body = parse_doc(path)
        did = fm.get("id")
        if not did:
            continue
        ids.append(did)
        documents.append({
            "id": did,
            "type": fm.get("type"),
            "title": fm.get("title"),
            "status": fm.get("status"),
            "kubespray_version": fm.get("kubespray_version"),
            "kubernetes_version": fm.get("kubernetes_version"),
            "component_version": fm.get("component_version"),
            "aliases": fm.get("aliases") or [],
            "tags": fm.get("tags") or [],
            "path": os.path.relpath(path, repo_root),
        })
        for rel in fm.get("relations") or []:
            if isinstance(rel, dict) and rel.get("type") and rel.get("target"):
                relations.append({
                    "source": did,
                    "type": rel["type"],
                    "target": rel["target"],
                })
    documents.sort(key=lambda d: d["id"])
    relations.sort(key=lambda r: (r["source"], r["type"], r["target"]))
    ids.sort()
    return documents, relations, ids


def build_facets(kb_root, repo_root):
    """Inverted retrieval facets: tag -> ids and alias -> ids.

    These let a simple (LLM-free) client answer "which docs are tagged X?" or
    resolve an alias to document IDs directly from index/, without scanning kb/ or
    walking the graph — the AI-first retrieval contract for leaf docs (variables,
    ansible tags) that are intentionally reached by facet, not by graph edge."""
    tags, aliases = {}, {}
    for path in iter_doc_paths(kb_root):
        fm, _sections, _body = parse_doc(path)
        did = fm.get("id")
        if not did:
            continue
        for t in fm.get("tags") or []:
            tags.setdefault(t, set()).add(did)
        for a in fm.get("aliases") or []:
            aliases.setdefault(a, set()).add(did)
    tag_rows = [{"ids": sorted(v), "tag": t} for t, v in sorted(tags.items())]
    alias_rows = [{"alias": a, "ids": sorted(v)} for a, v in sorted(aliases.items())]
    return tag_rows, alias_rows
