---
id: PRACTICE-AWX
type: best_practice
title: Running Kubespray from AWX / AAP — job templates, limits, tags, and the prompts that hang
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-27"
confidence: verified
aliases:
  - awx
  - aap
  - ansible automation platform
  - job template
  - job tags
  - tower
tags:
  - ansible
  - awx
  - tags
  - operations
sources:
  - type: code
    path: playbooks/reset.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/reset.yml
    note: "interactive pause prompt; skipping it requires reset_confirmation, not skip_confirmation alone"
  - type: code
    path: playbooks/remove_node.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/remove_node.yml
    note: "asserts `node` is defined; pause prompt suppressed by skip_confirmation"
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "serial: 1 (control plane) / serial: '{{ serial | default(20%) }}' (nodes) — serial is an extra var, not a tag"
  - type: code
    path: ansible.cfg
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/ansible.cfg
    note: "sets pipelining and host_key_checking; does NOT set become — privilege escalation must be enabled on the job template"
  - type: code
    path: playbooks/facts.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/facts.yml
    note: "the fact-refresh playbook lives under playbooks/ — there is no root facts.yml in v2.27.0–v2.31.0"
relations:
  - type: see_also
    target: PRACTICE-ANSIBLE
  - type: see_also
    target: CONCEPT-RUNBOOKS_INDEX
  - type: see_also
    target: PLAYBOOK-RESET
  - type: see_also
    target: PLAYBOOK-REMOVE_NODE
---

# Running Kubespray from AWX / AAP — job templates, limits, tags, and the prompts that hang

## Summary

Kubespray documentation is written for `ansible-playbook` on a control host. Under AWX / Ansible
Automation Platform there is no terminal, no `-b` flag and no working directory: every CLI flag
becomes a **job template field**. The translation is mostly mechanical, but three details are not,
and each one costs a failed or hung job: **privilege escalation is off unless you enable it**
(`ansible.cfg` does not set `become`), **two playbooks pause for an interactive answer** that never
arrives in AWX, and **`facts.yml` is not at the repo root**.

## Context

Applies to driving Kubespray from AWX/AAP against Kubespray tags v2.27.0–v2.31.0. The project
points at a Kubespray checkout; the job template selects a playbook from it; the inventory is the
same `hosts.yaml` structure as on the CLI ([[CONCEPT-SAMPLE_INVENTORY_LAYOUT]]).

**Playbook paths.** Every root playbook is a one-line wrapper that imports its real body from
`playbooks/`: `cluster.yml` imports `playbooks/cluster.yml`. Either path works in the job template's
**Playbook** field. The exception matters: **`facts.yml` exists only as `playbooks/facts.yml`** —
there is no root wrapper for it in any tag of the envelope. A job template pointed at `facts.yml`
will not find the playbook.

## Implementation

**Flag → job template field:**

| CLI | AWX / AAP |
|---|---|
| `-i inventory/<cluster>/hosts.yaml` | **Inventory** (the job template's inventory) |
| the playbook argument | **Playbook** (`cluster.yml` or `playbooks/cluster.yml`) |
| `-b` / `--become` | **Privilege Escalation** checkbox — **required**, `ansible.cfg` does not set `become` |
| `--limit=<host-or-group>` | **Limit** field |
| `--tags a,b` | **Job Tags** (comma-separated, no `--tags`) |
| `--skip-tags a` | **Skip Tags** |
| `-e key=value` | **Extra Variables** (YAML: `key: value`) |
| `-vv` | **Verbosity** |
| the Kubespray tag you checked out | **Project** revision / branch — pin the tag there, not in the template |

Enable *prompt on launch* for **Limit**, **Job Tags** and **Extra Variables** on the templates you
use for scoped work — otherwise every scoped run needs a template edit.

**The confirmation prompts — verified against the tagged source.** Two playbooks call
`ansible.builtin.pause` with a prompt. In AWX the job simply blocks until it is cancelled or times
out; there is no stdin to type `yes` into.

- **`reset.yml`** — pass **`reset_confirmation: true`** in Extra Variables. `skip_confirmation: true`
  alone is **not enough**: it suppresses the prompt, but the following check fails the play unless
  `reset_confirmation` is truthy (`playbooks/reset.yml`, the *Check confirmation* task).
- **`remove-node.yml`** — pass **`skip_confirmation: true`**, and **`node: <NAME>`** is mandatory:
  from **v2.28.0** the first play asserts `node is defined` and aborts with *"No nodes specified for
  removal"*. **At v2.27.0 that assert does not exist** and the play falls back to
  `hosts: "{{ node | default('etcd:k8s_cluster:calico_rr') }}"` — an empty `node` on that tag targets
  the **entire cluster**. On v2.27.0 never expose `node` as an optional prompt-on-launch field.
- **`upgrade_node_confirm: true`** is a CLI-only convenience — it pauses before **every** node. Do
  not set it in AWX; pace the roll with `serial` instead.

**Pacing is an extra var, not a tag.** `playbooks/upgrade_cluster.yml` runs the control plane at
`serial: 1` and nodes at `serial: "{{ serial | default('20%') }}"`. To go one node at a time, put
`serial: 1` in Extra Variables. `cluster.yml` has **no `serial`** on its control-plane play — you
cannot pace `cluster.yml` this way ([[PRACTICE-ANSIBLE]]).

**Limit and the fact cache.** A limited run only gathers facts for the hosts in the Limit, and other
roles then render against stale or missing facts for the rest. Before a limited `scale.yml`, run
`playbooks/facts.yml` **with an empty Limit** to refresh the cache for all nodes
([[PLAYBOOK-SCALE]]).

## Known Issues

- **The job hangs with no output near the start of `reset.yml` / `remove-node.yml`.** That is the
  pause prompt. Cancel, add the confirmation variable above, relaunch. It is not a connectivity
  problem.
- **`reset.yml` fails immediately with "Reset confirmation failed"** after you added
  `skip_confirmation: true`. Expected — add `reset_confirmation: true` as well.
- **Everything fails with permission errors on the first task.** Privilege Escalation is unchecked
  on the job template. Kubespray's `ansible.cfg` sets only `pipelining` and `host_key_checking`.
- **"playbook not found: facts.yml".** Use `playbooks/facts.yml`.
- **`remove-node.yml` with an empty `node` on v2.27.0 targets the whole cluster** — see above.
  This is the single most destructive AWX-specific trap in the envelope.
- **A Limit left over from a previous scoped launch.** With prompt-on-launch enabled, AWX
  pre-fills the last value; a `cluster.yml` converge that silently ran against one node leaves the
  cluster half-converged. Confirm the Limit field is empty before a full run.
- **Tags do not reduce risk, only scope.** `network`/`cilium` re-applies the CNI, `containerd`
  restarts the runtime, `resolvconf` rewrites `/etc/resolv.conf` on every host. The blast radius of
  a tag is the handlers it can fire ([[PRACTICE-ANSIBLE]]).

## Service impact

- Creating or editing a job template is free; **launching one against a live cluster is a converge**
  with the same disruption profile as the equivalent CLI run — AWX changes the interface, not the
  behaviour.
- The confirmation prompts exist to make `reset.yml` and `remove-node.yml` hard to run by accident.
  Passing the confirmation variables removes that guard permanently for that template: restrict who
  can launch it, and prefer prompt-on-launch over a hardcoded `node:` value.
- A hung job holds its inventory slot and can block scheduled runs behind it; cancel a prompt-hung
  job rather than waiting it out.

## References

- `playbooks/reset.yml`, `playbooks/remove_node.yml`, `playbooks/upgrade_cluster.yml`,
  `playbooks/facts.yml`, `ansible.cfg` — read at tag **v2.31.0**; the playbook layout and the
  confirmation-prompt behaviour were re-read at v2.27.0 and v2.29.0 and are identical. The one
  difference in the envelope: the `node is defined` assert in `remove_node.yml` exists from
  **v2.28.0** only.
- CLI-side detail: [[PRACTICE-ANSIBLE]]; per-operation procedures: [[CONCEPT-RUNBOOKS_INDEX]].
