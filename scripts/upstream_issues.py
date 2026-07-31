#!/usr/bin/env python3
"""kubepedia issues — добыча «проблемного слоя» апстрима для компонентов и аддонов.

Отвечает на вопрос «что известно сломанного в той версии, что у нас стоит, и где это
починили» — по данным самого проекта, а не по памяти модели. Из заметок к релизам
вытаскиваются три среза:

  * **CVE** — что закрыто и в какой версии каждой линии поддержки;
  * **несовместимые изменения** — то, что ломает конфигурацию при апгрейде;
  * **исправления дефектов** — чтобы «а это уже чинили?» решалось чтением, а не воспроизведением.

Два источника, потому что апстримы ведут заметки по-разному:

  local  — клон в `src-cache/<имя>`: файлы `release-notes/*.yaml` (стиль Envoy Gateway)
           либо `CHANGELOG*.md` / `CHANGELOG/*.md`. Лимитов нет, работает офлайн.
  api    — GitHub Releases. Без токена это 60 запросов в час на всё про всё, поэтому
           режим включается только при заданном GITHUB_TOKEN (или `gh auth token`).

    kubepedia issues --list                 # что вообще умеем мыть и что уже клонировано
    kubepedia issues --component cilium     # один компонент
    kubepedia issues --all --local-only     # всё, что есть в src-cache
    kubepedia issues --all                  # плюс API там, где клона нет (нужен токен)

Результат — JSON на компонент в `reports/upstream/<имя>.json` и сводка в
`reports/UPSTREAM-ISSUES.md`. Документы KDS из этого пишутся руками: инструмент
собирает факты, но решает, что из них знание, человек.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "src-cache")
OUT = os.path.join(ROOT, "reports", "upstream")

# компонент -> апстрим-репозиторий. Ключ совпадает с именем каталога в src-cache,
# если клон уже есть. Список ведётся руками: угадывать репозиторий по имени компонента
# нельзя — ошибка тут тихо даёт чужие заметки к релизам.
REPOS = {
    # ядро кластера и рантаймы
    "etcd": "etcd-io/etcd",
    "containerd": "containerd/containerd",
    "runc": "opencontainers/runc",
    "cri-o": "cri-o/cri-o",
    "crun": "containers/crun",
    "youki": "youki-dev/youki",
    "nerdctl": "containerd/nerdctl",
    "skopeo": "containers/skopeo",
    # сеть
    "cilium": "cilium/cilium",
    "calico": "projectcalico/calico",
    "flannel": "flannel-io/flannel",
    "kube-ovn": "kubeovn/kube-ovn",
    "kube-router": "cloudnativelabs/kube-router",
    "multus": "k8snetworkplumbingwg/multus-cni",
    "cni-plugins": "containernetworking/plugins",
    "coredns": "coredns/coredns",
    "nodelocaldns": "kubernetes/dns",
    # вход и балансировка
    "ingress-nginx": "kubernetes/ingress-nginx",
    "metallb": "metallb/metallb",
    "kube-vip": "kube-vip/kube-vip",
    "envoy-gateway": "envoyproxy/gateway",
    # хранилище
    "local-path-provisioner": "rancher/local-path-provisioner",
    "snapshot-controller": "kubernetes-csi/external-snapshotter",
    "aws-ebs-csi": "kubernetes-sigs/aws-ebs-csi-driver",
    "azure-csi": "kubernetes-sigs/azuredisk-csi-driver",
    "cinder-csi": "kubernetes/cloud-provider-openstack",
    "gcp-pd-csi": "kubernetes-sigs/gcp-compute-persistent-disk-csi-driver",
    # платформа
    "argo-cd": "argoproj/argo-cd",
    "kyverno": "kyverno/kyverno",
    "cert-manager": "cert-manager/cert-manager",
    "metrics-server": "kubernetes-sigs/metrics-server",
    "node-feature-discovery": "kubernetes-sigs/node-feature-discovery",
    "scheduler-plugins": "kubernetes-sigs/scheduler-plugins",
    "helm": "helm/helm",
    "consul-k8s": "hashicorp/consul-k8s",
    "kata-containers": "kata-containers/kata-containers",
    # оркестратор и дистрибутив
    "kubernetes": "kubernetes/kubernetes",
    "kubespray": "kubernetes-sigs/kubespray",
    "talos": "siderolabs/talos",
}

SEC_RX = re.compile(r"CVE-\d{4}-\d{4,7}")
# Заголовки размечают не все проекты: containerd делит по подсистемам (CRI, Runtime),
# у kube-ovn и youki списки идут сплошняком. Поэтому строка классифицируется и сама по себе.
LINE_FIX_RX = re.compile(r"^\W*(fix|fixed|fixes|correct|resolve[sd]?|prevent|avoid)\b|\bfix(es|ed)?\b", re.I)
LINE_BREAK_RX = re.compile(r"^\W*(BREAKING|\[BREAKING\]|Action required)", re.I)


def classify(text, heading_sec):
    """Секция строки: явный заголовок сильнее, дальше — признаки самой строки."""
    if LINE_BREAK_RX.search(text):
        return "breaking changes"
    if SEC_RX.search(text):
        return "security updates"
    if heading_sec:
        return heading_sec
    if LINE_FIX_RX.search(text):
        return "bug fixes"
    return None
BREAK_RX = re.compile(r"breaking|action required|upgrade note|incompatib", re.I)
FIX_RX = re.compile(r"bug ?fix|fixes|fixed", re.I)
SECURITY_RX = re.compile(r"security|vulnerab|advisor", re.I)


def bullets(text):
    """Разбор списка в человеческих заметках: пункт может продолжаться на следующих строках.

    kubespray пишет «- Action required», а суть — строкой ниже с отступом; etcd вкладывает
    подпункты в основной. Пункт начинается только с нулевой колонки, всё, что с отступом,
    приклеивается к нему. Иначе в выдачу попадают обрывки: голое «Action required» или
    одинокие имена метрик.

    Возвращает пары (заголовок_раздела, текст_пункта).
    """
    out, sec, cur = [], None, None

    def flush():
        nonlocal cur
        if cur and len(cur[1].strip()) > 1:
            out.append((cur[0], re.sub(r"\s+", " ", cur[1]).strip()))
        cur = None

    for line in text.split("\n"):
        h = re.match(r"^#{2,4}\s+(.+?)\s*$", line)
        if h:
            flush()
            t = h.group(1)
            sec = ("breaking changes" if BREAK_RX.search(t) else
                   "security updates" if SECURITY_RX.search(t) else
                   "bug fixes" if FIX_RX.search(t) else None)
            continue
        top = re.match(r"^[-*]\s+(.*)$", line)
        if top:
            flush()
            cur = [sec, top.group(1)]
            continue
        if cur is not None and line.strip() and re.match(r"^\s+", line):
            cur[1] += " " + re.sub(r"^\s*[-*]\s*", "", line.strip())
            continue
        if not line.strip():
            flush()
    flush()
    return out


def sh(*args, cwd=None):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return p.stdout


def token():
    t = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if t:
        return t
    t = sh("gh", "auth", "token").strip()
    return t or None


# ---------------------------------------------------------------- источник: клон

def yaml_notes(path):
    """Заметки в стиле Envoy Gateway: release-notes/<version>.yaml с секциями."""
    files = sh("git", "ls-tree", "--name-only", "origin/main", "release-notes/", cwd=path).split()
    if not files:
        files = sh("git", "ls-tree", "--name-only", "HEAD", "release-notes/", cwd=path).split()
    out = {}
    for f in files:
        if not f.endswith(".yaml"):
            continue
        ver = os.path.basename(f)[:-5]
        if re.search(r"-(rc|alpha|beta)", ver, re.I):
            continue            # кандидаты дублируют финальный релиз — двойной счёт
        text = sh("git", "show", f"origin/main:{f}", cwd=path) or sh("git", "show", f"HEAD:{f}", cwd=path)
        secs = {}
        for name in ("breaking changes", "security updates", "bug fixes"):
            m = re.search(rf"^{name}: \|\n((?:  .*\n|\n)*)", text, re.M | re.I)
            items = [re.sub(r"\s+", " ", x).strip() for x in (m.group(1) if m else "").split("\n") if x.strip()]
            if items:
                secs[name] = items
        if secs:
            out[ver] = secs
    return out


def changelog_notes(path):
    """CHANGELOG.md: версии по заголовкам, строки-пункты классифицируются по подзаголовку."""
    names = [n for n in sh("git", "ls-tree", "--name-only", "-r", "HEAD", cwd=path).split("\n")
             if re.search(r"(^|/)CHANGELOG[^/]*\.md$", n, re.I)]
    out = {}
    for name in names[:12]:
        text = sh("git", "show", f"HEAD:{name}", cwd=path)
        for chunk in re.split(r"(?m)^(?=#{1,3}\s+\[?v?\d+\.\d+\.\d+)", text):
            h = re.match(r"^#{1,3}\s+\[?v?(\d+\.\d+\.\d+[^\]\s]*)", chunk)
            if not h:
                continue
            ver = h.group(1)
            if re.search(r"-(rc|alpha|beta)", ver, re.I):
                continue
            for sec, txt in bullets(chunk):
                key = classify(txt, sec)
                if key:
                    out.setdefault(ver, {}).setdefault(key, []).append(txt)
    return {v: s for v, s in out.items() if s}


def from_clone(name):
    path = os.path.join(CACHE, name)
    if not os.path.isdir(os.path.join(path, ".git")):
        return None, "клона нет"
    data = yaml_notes(path)
    if data:
        return data, "клон: release-notes/*.yaml"
    data = changelog_notes(path)
    if data:
        return data, "клон: CHANGELOG"
    return None, "клон есть, заметок к релизам не нашлось"


# ------------------------------------------------------------------ источник: API

def from_api(repo, tok, pages=3):
    if not tok:
        return None, "нет токена (GITHUB_TOKEN / gh auth login)"
    out = {}
    for page in range(1, pages + 1):
        url = f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}"
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json", "User-Agent": "kubepedia-issues",
            "Authorization": f"Bearer {tok}"})
        try:
            with urllib.request.urlopen(req, timeout=40) as r:
                batch = json.load(r)
        except Exception as exc:                       # noqa: BLE001 — сеть не должна ронять свип
            return (out or None), f"API: {exc}"
        if not batch:
            break
        for rel in batch:
            ver = (rel.get("tag_name") or "").lstrip("v")
            if rel.get("prerelease") or re.search(r"-(rc|alpha|beta)", ver, re.I):
                continue
            secs = {}
            for sec, txt in bullets(rel.get("body") or ""):
                key = classify(txt, sec)
                if key:
                    secs.setdefault(key, []).append(txt)
            if secs:
                out[ver] = secs
    return (out or None), "GitHub Releases API"


# ---------------------------------------------------------------------- сведение

def summarize(name, data, source):
    cves = sorted(set(SEC_RX.findall(json.dumps(data, ensure_ascii=False))))
    counts = {k: sum(len(v.get(k, [])) for v in data.values())
              for k in ("breaking changes", "security updates", "bug fixes")}
    return {"component": name, "repo": REPOS.get(name), "source": source,
            "releases": len(data), "cves": cves, "counts": counts}


def main():
    ap = argparse.ArgumentParser(description="Добыча проблемного слоя апстрима")
    ap.add_argument("--component", action="append", help="имя из карты репозиториев")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--local-only", action="store_true", help="не ходить в API")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list:
        for n, r in sorted(REPOS.items()):
            has = os.path.isdir(os.path.join(CACHE, n, ".git"))
            print(f"  {'клон' if has else '   —'}  {n:26} {r}")
        print(f"\nвсего {len(REPOS)}, клонировано {sum(os.path.isdir(os.path.join(CACHE,n,'.git')) for n in REPOS)}")
        return 0

    names = args.component or (sorted(REPOS) if args.all else [])
    if not names:
        ap.error("нужен --component, --all или --list")

    tok = None if args.local_only else token()
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for name in names:
        if name not in REPOS:
            print(f"[skip] {name}: нет в карте репозиториев", file=sys.stderr)
            continue
        data, source = from_clone(name)
        if not data and not args.local_only:
            data, source = from_api(REPOS[name], tok)
        if not data:
            rows.append({"component": name, "repo": REPOS[name], "source": source,
                         "releases": 0, "cves": [], "counts": {}})
            print(f"[--] {name:26} {source}")
            continue
        with open(os.path.join(OUT, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        row = summarize(name, data, source)
        rows.append(row)
        c = row["counts"]
        print(f"[ok] {name:26} релизов {row['releases']:4}  CVE {len(row['cves']):3}  "
              f"ломающих {c.get('breaking changes',0):3}  дефектов {c.get('bug fixes',0):4}  ({source})")

    lines = ["# Проблемный слой апстрима — сводка\n",
             "_Сгенерировано `kubepedia issues`. Числа — то, что объявил сам апстрим в заметках "
             "к релизам; это сырьё для документов базы, а не сами знания._\n",
             "| Компонент | Репозиторий | Релизов | CVE | Ломающих | Дефектов | Источник |",
             "|---|---|---:|---:|---:|---:|---|"]
    for r in sorted(rows, key=lambda x: -(x["counts"].get("bug fixes", 0))):
        c = r["counts"]
        lines.append(f"| {r['component']} | `{r['repo']}` | {r['releases']} | {len(r['cves'])} | "
                     f"{c.get('breaking changes',0)} | {c.get('bug fixes',0)} | {r['source']} |")
    allc = sorted({c for r in rows for c in r["cves"]})
    lines += ["", f"**Всего уникальных CVE по всем компонентам: {len(allc)}**", "",
              " ".join(f"`{c}`" for c in allc) if allc else "_(пусто)_"]
    with open(os.path.join(ROOT, "reports", "UPSTREAM-ISSUES.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nсводка: reports/UPSTREAM-ISSUES.md, детали: reports/upstream/*.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
