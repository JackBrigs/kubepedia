#!/usr/bin/env python3
"""Общая логика «затронута ли версия» для всех инструментов, читающих osv.dev.

Появилась не от любви к абстракциям, а после того как ночной прогон начал
ежедневно поднимать ложную тревогу: матрицы строит `gen_cve_matrix.py`, а сверяет
их `cve_sweep.py` — и каждый отвечал на вопрос «затронута ли эта версия» по-своему.

Три расхождения, из-за которых они спорили:

1. **Запись без версии исправления.** Диапазон вида `introduced: 0` без события
   `fixed` формально объявляет затронутыми все версии подряд. Иногда это правда
   (уязвимость не закрыта), но часто — просто неполная запись. Проверено на
   ingress-nginx: версия 1.13.3 получала CVE, закрытые в 1.12.1.

2. **Парные записи одного CVE.** Один и тот же CVE приходит и из базы Go, и из
   GitHub Advisory, а сведения об исправлении есть не в обеих. Смотреть надо
   объединение по всем записям с этим идентификатором.

3. **Разные идентификаторы одного и того же.** `GO-2026-5354` и `CVE-2026-32254`
   могут быть одной уязвимостью. Считать их порознь — завышать счёт.

Правило сравнения версий: если фикс есть на той же линии поддержки — сравниваем с
ним; иначе с самым старшим. Иначе 1.11.6 при фиксах `1.11.5, 1.12.1` был бы объявлен
затронутым по старшему значению.
"""
import re


def vt(text):
    """Версия как кортеж чисел; хвосты вроде -rc1 отбрасываются."""
    return tuple(int(n) for n in re.findall(r"\d+", str(text))[:3])


def canonical_id(vuln):
    """Идентификатор, под которым уязвимость известна человеку: CVE, если он есть."""
    for alias in vuln.get("aliases", []):
        if alias.startswith("CVE-"):
            return alias
    return vuln.get("id")


def version_resolvable(vuln):
    """Умеет ли запись отвечать на вопрос о конкретной версии.

    Запись, где затронутый диапазон описан только коммитами (тип GIT), совпадает
    с любой версией — по ней нельзя сказать ничего.
    """
    for affected in vuln.get("affected", []):
        for rng in affected.get("ranges", []):
            if rng.get("type") in ("SEMVER", "ECOSYSTEM"):
                return True
    return False


def fixed_versions(vuln):
    """Все версии, в которых эта запись объявляет проблему исправленной."""
    out = set()
    for affected in vuln.get("affected", []):
        for rng in affected.get("ranges", []):
            for event in rng.get("events", []):
                if event.get("fixed"):
                    out.add(event["fixed"])
    return out


def merge_fixes(vulns):
    """Идентификатор -> версии исправления, собранные по всем записям этого CVE."""
    merged = {}
    for v in vulns:
        merged.setdefault(canonical_id(v), set()).update(fixed_versions(v))
    return merged


def still_affected(cid, version, fixes_by_id):
    """Затронута ли `version` уязвимостью `cid` с учётом объединённых фиксов.

    Нет ни одной версии исправления — уязвимость открыта, версия затронута.
    Есть — сравниваем с фиксом на той же линии поддержки, а при его отсутствии
    с самым старшим.
    """
    fixes = fixes_by_id.get(cid) or set()
    if not fixes:
        return True
    same_line = [f for f in fixes if vt(f)[:2] == vt(version)[:2]]
    threshold = max(same_line or fixes, key=vt)
    return vt(version) < vt(threshold)


def affected_ids(vulns, version):
    """Идентификаторы уязвимостей, реально затрагивающих версию.

    Единственная точка, где принимается это решение. И матрица, и её сверка
    обязаны звать именно её — иначе они снова начнут спорить.
    """
    usable = [v for v in vulns if version_resolvable(v)]
    fixes = merge_fixes(usable)
    return sorted({canonical_id(v) for v in usable
                   if still_affected(canonical_id(v), version, fixes)})
