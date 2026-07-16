"""
Shared helpers for Kubepedia KDS tooling (validator + index generator).

Single source of the type/section/version tables so the two scripts never drift.
Tables mirror standards/kds.md; keep them in sync when KDS changes.
"""
import os
import re
import glob
import datetime

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
