#!/usr/bin/env python3
"""Generate an ITIL 4 Known Error Database (KEDB) export from the troubleshooting layer.

Renders each `type: troubleshooting` KDS doc under kb/ into a Known Error record
(symptom / affected CIs / root cause / workaround-fix), grouped by domain, into
templates/itil/kedb/. This is an OUTPUT layer — the KDS base is untouched, and the
export carries NO internal KDS IDs (user-facing deliverable): KEDB-NNN + title + path.

Usage:  .venv/bin/python scripts/gen_kedb.py
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "templates", "itil", "kedb")

# domain buckets by first keyword match over (tags + id), priority-ordered
DOMAINS = [
    ("etcd & control-plane", ["etcd", "control-plane", "apiserver", "kube-controller", "scheduler", "leader"]),
    ("storage", ["storage", "pvc", "csi", "volume", "snapshot", "ceph", "rook", "local-path"]),
    ("dns", ["dns", "coredns", "nodelocaldns"]),
    ("networking & CNI", ["network", "cni", "cilium", "calico", "metallb", "proxy", "bgp", "ingress", "loadbal", "conntrack", "arp", "kube-router"]),
    ("security & admission", ["security", "rbac", "admission", "pod-security", "webhook", "cve", "cert-manager", "vault", "kyverno"]),
    ("node & runtime", ["node", "kubelet", "runtime", "containerd", "crio", "drain", "cgroup", "kernel", "inotify"]),
    ("scaling", ["scale", "hpa", "autoscal", "keda"]),
    ("upgrade & join", ["upgrade", "kubeadm", "skew", "join", "add-node"]),
    ("addons", ["addon", "argocd", "rabbitmq", "dragonfly", "gitlab", "velero", "k8up", "volsync",
                "postgres", "eck", "gpu", "otel", "prometheus", "vmagent", "capsule", "registry", "consul"]),
]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    fm, body = m.group(1), m.group(2)
    d = {}
    for key in ("id", "title", "kubespray_version", "kubernetes_version", "component_version"):
        km = re.search(rf"^{key}:\s*(.+)$", fm, re.M)
        if km:
            d[key] = km.group(1).strip().strip('"')
    tags = re.search(r"^tags:\s*\n((?:\s*-\s*.+\n)+)", fm, re.M)
    d["tags"] = re.findall(r"-\s*(.+)", tags.group(1)) if tags else []
    return d, body


def clean(s):
    s = re.sub(r"\(\[\[[^\]]+\]\]\)", "", s)          # ([[ID]]) cross-refs
    s = re.sub(r"\[\[[^\]]+\]\]", "", s)               # [[ID]]
    s = re.sub(r"\s+", " ", s).strip(" .;—-")
    return s


def section(body, name, limit=420):
    m = re.search(rf"^##\s+{re.escape(name)}\s*\n(.*?)(?=^##\s|\Z)", body, re.S | re.M)
    if not m:
        return ""
    bullets = re.findall(r"^\s*[-*]\s+(.+?)(?=\n\s*[-*]\s|\n\n|\Z)", m.group(1), re.S | re.M)
    text = " · ".join(clean(b) for b in bullets if clean(b)) if bullets else clean(m.group(1))
    return (text[:limit] + "…") if len(text) > limit else text


def domain_of(tags, _id):
    hay = " ".join(tags).lower() + " " + _id.lower()
    for name, kws in DOMAINS:
        if any(k in hay for k in kws):
            return name
    return "other"


def main():
    entries = {}
    for f in glob.glob(os.path.join(ROOT, "kb", "**", "*.md"), recursive=True):
        text = open(f).read()
        if not re.search(r"^type:\s*troubleshooting", text, re.M):
            continue
        d, body = frontmatter(text)
        if not d.get("id"):
            continue
        rel = os.path.relpath(f, ROOT)
        cis = ", ".join(t for t in d["tags"] if t != "troubleshooting") or "—"
        ver = " / ".join(v for v in (d.get("kubespray_version"), d.get("kubernetes_version"),
                                     d.get("component_version")) if v and v != "null")
        dom = domain_of(d["tags"], d["id"])
        entries.setdefault(dom, []).append({
            "title": clean(d.get("title", d["id"])),
            "symptom": section(body, "Problem") or section(body, "Summary"),
            "cause": section(body, "Context"),
            "fix": section(body, "Known Issues") or section(body, "Diagnostics"),
            "cis": cis, "ver": ver, "src": rel,
        })

    os.makedirs(OUT, exist_ok=True)
    order = [n for n, _ in DOMAINS] + ["other"]
    n = 0
    index = ["# KEDB — Known Error Database (сгенерировано из troubleshooting-слоя базы)\n",
             "ITIL 4 Known Error records, отрендеренные из базы знаний. **Не редактировать руками** —",
             "перегенерируется `scripts/gen_kedb.py`. Формат: симптом / затронутые CIs / root cause /",
             "workaround-fix / источник. Внутренних KDS-ID нет (пользовательский деливерабл).\n",
             "## Домены\n"]
    total = sum(len(v) for v in entries.values())
    for dom in order:
        items = sorted(entries.get(dom, []), key=lambda e: e["title"].lower())
        if not items:
            continue
        slug = re.sub(r"[^a-z0-9]+", "-", dom.lower()).strip("-")
        fn = f"{slug}.md"
        index.append(f"- [{dom}]({fn}) — {len(items)} записей")
        lines = [f"# KEDB · {dom}\n", f"_{len(items)} известных ошибок. Сгенерировано; не править руками._\n"]
        for e in items:
            n += 1
            lines.append(f"### KEDB-{n:03d} · {e['title']}")
            lines.append(f"- **Симптом:** {e['symptom'] or '—'}")
            lines.append(f"- **Затронутые CIs:** {e['cis']}" + (f"  ·  _{e['ver']}_" if e['ver'] else ""))
            lines.append(f"- **Root cause:** {e['cause'] or '—'}")
            lines.append(f"- **Workaround / fix:** {e['fix'] or '—'}")
            lines.append(f"- **Источник:** `{e['src']}`\n")
        open(os.path.join(OUT, fn), "w").write("\n".join(lines) + "\n")
    index.insert(4, f"\n**Всего: {total} Known Error записей.**\n")
    open(os.path.join(OUT, "README.md"), "w").write("\n".join(index) + "\n")
    print(f"KEDB: {total} записей в {len([d for d in order if entries.get(d)])} доменах -> {OUT}")


if __name__ == "__main__":
    main()
