---
id: PRACTICE-ANSIBLE
type: best_practice
title: Running Kubespray with Ansible — install, vars, and tags
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - ansible usage
tags:
  - ansible
  - tags
  - install
sources:
  - type: docs
    path: docs/ansible/ansible.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/ansible/ansible.md
    note: "Ansible install/venv, Python compatibility, variable customization layers, playbook tags reference, and example filtered runs"
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "serial: 1 for the control plane and serial: 20% for nodes — unlike cluster.yml, whose control-plane play has no serial"
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
  - type: see_also
    target: CONCEPT-DESTRUCTIVE_ACTIONS
---

# Running Kubespray with Ansible — install, vars, and tags

## Summary
Covers installing the correct Ansible version for Kubespray, the variable customization layers and their precedence, the catalog of playbook tags for filtering runs, and example filtered commands. Key takeaway: pin Ansible via the shipped `requirements.txt` in a Python venv, customize through inventory `group_vars`, and use `--tags`/`--skip-tags` only when you fully understand the affected roles.

## Context
Applies to preparing the Ansible control host and invoking Kubespray playbooks (e.g. `cluster.yml`). Prerequisites: a compatible Python version and the inventory (see the inventory guide). Variable customization involves inventory `group_vars`/`host_vars`, extra vars, and internal `roles/vars/`.

## Implementation
Installation — deploy the Kubespray-supported Ansible into a Python virtualenv using the shipped requirements:

```ShellSession
VENVDIR=kubespray-venv
KUBESPRAYDIR=kubespray
python3 -m venv $VENVDIR
source $VENVDIR/bin/activate
cd $KUBESPRAYDIR
pip install -r requirements.txt
```

Python/Ansible compatibility: if pip cannot satisfy the pinned Ansible version, your Python is too old. For this tag, Ansible `>=2.18.0,<2.19.0` requires Python 3.11–3.13.

Customize Ansible vars — use these sources, in increasing precedence:

- inventory vars: **inventory group_vars** (most used) and inventory host_vars (per-host overrides).
- **extra vars** always win precedence: override with `ansible-playbook -e @foo.yml`.

Caveat: extra vars are best used to override Kubespray internal variables (e.g. `roles/vars/`). Those internals are not part of the Kubespray user interface and may change, disappear, or break unexpectedly.

Playbook tags — a large set of tags let you scope a run to specific roles/components. Examples from the reference: `bootstrap_os`, `preinstall`, `facts`, `download`, `upload`, `upgrade`, `etcd`, `etcd-secrets`, `control-plane`, `kube-apiserver`, `kubelet`, `kube-proxy`, `network`, `cni`, plus per-CNI (`calico`, `cilium`, `flannel`, `kube-ovn`, `kube-router`, `macvlan`, `multus`), per-runtime (`containerd`, `crio`, `docker`, `crun`, `gvisor`, `youki`, `kata-containers`), CSI/cloud-provider, `coredns`/`nodelocaldns`/`resolvconf`, and reset-related tags (`reset`, `iptables`, `mounts`, `services`, `files`). Consult the full table in the doc for exact meanings.

Example filtered commands:

```ShellSession
# apply only DNS/preinstall config, skip download and OS bootstrap
ansible-playbook -i inventory/sample/hosts.ini cluster.yml --tags preinstall,facts --skip-tags=download,bootstrap_os

# remove the cluster DNS resolver IP from hosts' /etc/resolv.conf
ansible-playbook -i inventory/sample/hosts.ini -e dns_mode='none' cluster.yml --tags resolvconf

# prepare all images locally on the runner, no upload/upgrade
ansible-playbook -i inventory/sample/hosts.ini cluster.yml \
    -e download_run_once=true -e download_localhost=true \
    --tags download --skip-tags upload,upgrade
```

Note: use `--tags`/`--skip-tags` only if you are certain what they do.

Troubleshooting: wrong Ansible/collection/Python versions cause failures. Kubespray ships custom modules; point Ansible at them via `export ANSIBLE_LIBRARY=<kubespray_dir>/library`. To guarantee correct versions, use the pre-built Quay image and bind-mount the inventory and SSH key:

```ShellSession
docker pull quay.io/kubespray/kubespray:v2.31.0
docker run --rm -it --mount type=bind,source="$(pwd)"/inventory/sample,dst=/inventory \
  --mount type=bind,source="${HOME}"/.ssh/id_rsa,dst=/root/.ssh/id_rsa \
  quay.io/kubespray/kubespray:v2.31.0 bash
```

## Known Issues

**`group_vars` must sit next to the inventory file, or the whole layer is silently ignored.**
Ansible loads group variables from a `group_vars/` directory adjacent to the inventory
(`inventory/<cluster>/group_vars/all/…`, `…/group_vars/k8s_cluster/…`). Directories named
`all/` or `k8s_cluster/` placed **directly** in the inventory root are not group_vars — they
are just directories, and every variable in them is unused. Nothing warns: the run is green,
the cluster is simply built from defaults. The symptom reaches you later and disguised — a
component behaving as if its setting was never set, an inventory pin that "does not work".
Cheap check: `ansible -i <inventory> <host> -m debug -a 'var=<your_var>'` before blaming the
role.

**Dictionaries are replaced, not merged.** Ansible's default `hash_behaviour` is `replace`,
so when the same dict variable is defined in two places (a shared defaults layer and a
per-cluster file), the winner **replaces the whole dict** — it does not merge keys. Redefining
`cilium_extra_values` to add one key silently drops every key the other definition had. Always
restate the full dict, and verify the rendered artefact rather than the inventory.

**Rendered artefacts on the node show the *last run*, not the inventory.** Files such as
`{{ kube_config_dir }}/cilium-extra-values.yaml` are written during a run. Reading one is an
excellent way to see what actually reached a component — but it is evidence about the moment
of the last run, so always pair it with "when did this cluster last converge".

## Service impact

Installing Ansible and editing `group_vars` is free; **running a playbook against a live
cluster never is**, and tag filtering changes the blast radius rather than removing it.

- **Control-host work is non-disruptive:** creating the venv, `pip install -r
  requirements.txt`, pulling the Quay image, editing inventory — nothing touches the
  cluster.
- **Any `cluster.yml` run is a converge, not a no-op.** Every template task whose output
  differs notifies a restart handler — apiserver sandbox removal, `Node | restart kubelet`,
  `Restart containerd`. A run made "just to check" can restart the control plane if
  someone's inventory drifted from what is deployed. Use `--check --diff` to see the
  difference without applying it, and `--limit` to bound it to one node.
- **Tags narrow the work but not the risk.** `--tags resolvconf` rewrites `/etc/resolv.conf`
  on every host; `--tags network`/`--tags cilium` re-apply the CNI; `--tags containerd`
  restarts the runtime. Conversely `--skip-tags` can leave the cluster half-converged: skipping
  `preinstall`/`facts` means later roles run against stale facts. Run a tag only when you know
  which handlers it can fire.
- **Extra vars win over everything**, including values you keep in `group_vars`. Overriding
  Kubespray internals (`roles/*/vars/`) with `-e` is unsupported and can silently change
  behaviour between tags.
- **The control-plane play has no `serial`** in `cluster.yml`, so restarts there are parallel
  by default; `upgrade_cluster.yml` uses `serial: 1` (control plane) and `serial: 20%`
  (nodes). If you need staged behaviour, use the upgrade playbook or `--limit`, not
  `cluster.yml`.

## References
- docs/ansible/ansible.md (tag v2.31.0 1c9add4); `playbooks/cluster.yml` /
  `playbooks/upgrade_cluster.yml` (serial settings) at tag v2.31.0.
