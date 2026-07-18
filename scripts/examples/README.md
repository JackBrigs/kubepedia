# Kubepedia tools

One CLI over everything — **`scripts/kubepedia.py`**:

```bash
kubepedia plan   --from v2.28.1 --to v2.31.0 --inventory scripts/examples/prod-cluster
kubepedia check  --version v2.31.0 --facts facts.json
kubepedia impact etcd
kubepedia verify        # KB integrity
kubepedia               # list commands
```

`plan` = pre-upgrade migration diff, `check` = post-upgrade verification, `impact` =
graph analysis, `report` = KB-narrative report, `verify`/`validate`/`index` = KB tooling.
Each subcommand proxies to its script, so `kubepedia <cmd> --help` shows that command's
own options. The sections below document the individual tools.

---

# Kubepedia handles — demo

Two consumer **handles** over the KB. Both take two Kubespray versions and (optionally)
your inventory, and default to **Russian** framing (`--lang en` for English).

## `upgrade_diff.py` — inventory migration diff (primary)

Action-oriented: **what to change in your inventory** to migrate.

```bash
# composite inventory (shared defaults folder + cluster folder), merged like Ansible
.venv/bin/python scripts/upgrade_diff.py --from v2.28.1 --to v2.31.0 \
    --inventory scripts/examples/shared-defaults \
    --inventory scripts/examples/prod-cluster

# generic diff, no inventory
.venv/bin/python scripts/upgrade_diff.py --from v2.30.0 --to v2.31.0
```

Emits: **component version diff**, **⚠ destructive actions & known issues** (inventory-value
rules like `kubelet_cpu_manager_policy: static` → delete `cpu_manager_state`; version-transition
rules like the Cilium DaemonSet rollout downtime or etcd 3.6's removed v2-store flags — every
warning is a **researched, concrete fact with its remediation**, never a "go read it yourself"),
**⚠ variables to REMOVE** (defaults gone in the target tag that your inventory still sets),
**all removed** (grouped) and **added** variables, and a **complete action checklist** that folds
in every remediation step. No `[[wikilink]]`/`[ID]` litter, no doc appendix.

**Data sources.** Versions: the curated `RELEASE-V*` KDS tables. Variables: a direct diff
of the Kubespray **role defaults** between the two tags in a local checkout (`--src`,
default `./kubespray-src`) — authoritative and per-tag. Inventory: resolved with
**`ansible-inventory`**, so multiple `--inventory` folders merge with real Ansible
precedence (a composite inventory works exactly as `ansible-playbook` would see it).

## `upgrade_report.py` — KB-narrative report (variant)

Pulls the prose upgrade notes from the `UPGRADE-*` KDS docs and personalizes/filters them.
Richer narrative, but it references KB docs inline. `--lang ru|en`.

```bash
.venv/bin/python scripts/upgrade_report.py --from v2.28.1 --to v2.31.0 \
    --inventory scripts/examples/prod-cluster
```

## Fixtures

- `shared-defaults/` — group_vars shared across many clusters (runtime, proxy, cert-manager…).
- `prod-cluster/` — a specific cluster: its `hosts.yaml`, CNI/kube_version, cloud, enabled
  add-ons (incl. `dashboard_enabled`/`ingress_nginx_enabled`/`deploy_netchecker`, which are
  **removed** in v2.31.0 — so the ⚠ section demonstrates the flag).

Pass **both** folders as separate `--inventory` args to see the composite merge.

## Notes

- **Language.** Framing is Russian by default; verbatim KDS excerpts (only in
  `upgrade_report.py`) stay English. For a fully human-Russian narrative, ask Claude to render
  it — the tools provide the facts.
- **Live clusters (future).** `upgrade_diff.py` reads inventory statically. Collecting facts
  from running nodes (ansible `-m setup` / `--check` dry-run) is a possible extension.

## `impact.py` — graph impact analysis

Query the KDS relation graph: "what depends on X", "what breaks if I change X".

```bash
.venv/bin/python scripts/impact.py etcd                 # what depends on etcd
.venv/bin/python scripts/impact.py COMPONENT-CILIUM --depth 2   # impact radius
.venv/bin/python scripts/impact.py --tag cni            # everything tagged cni
```

Resolves the target by ID, alias, tag, or title/ID substring; shows inbound edges
(who depends on / references it), outbound (its dependencies), and — with `--depth N`
— the transitive impact radius. `--json` for machine output; `--lang ru|en`.
