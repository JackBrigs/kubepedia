---
id: PRACTICE-ANSIBLE
type: best_practice
title: Running Kubespray with Ansible — install, vars, and tags
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
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
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
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

## References
- docs/ansible/ansible.md (tag v2.31.0 1c9add4)
