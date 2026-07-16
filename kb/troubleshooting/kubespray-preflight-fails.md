---
id: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
type: troubleshooting
title: Kubespray preflight assertion fails ("Stop if …")
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - preflight failed
  - assertion failed kubespray
  - Stop if
  - verify-settings failed
tags:
  - troubleshooting
  - preflight
  - preinstall
  - inventory
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/0040-verify-settings.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0040-verify-settings.yml
    note: "preinstall assertions (tag v2.31.0)"
  - type: code
    path: roles/validate_inventory/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/validate_inventory/tasks/main.yml
    note: "inventory validation assertions (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
  - type: see_also
    target: TROUBLE-NODE_MEMORY_TOO_SMALL
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# Kubespray preflight assertion fails ("Stop if …")

## Summary

Before touching a node, Kubespray runs **assertion tasks** (named `Stop if …`) in the
`validate_inventory` and `kubernetes/preinstall` roles. A failed assertion aborts the
run with a `fail_msg`/`msg`. These are guardrails, not bugs — each points at a concrete
inventory or host precondition you must fix. This document maps every in-range preflight
assertion to its cause and fix.

## Problem

The playbook fails early (during `validate_inventory` or `preinstall`) with a task
called `Stop if <something>` and an `assertion failed` / custom message, before any
cluster changes are made.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Two assertion stages run: **`validate_inventory`** (inventory-level, `run_once`) and
  **`kubernetes/preinstall` `0040-verify-settings.yml`** (per-host).
- Most per-host checks are guarded by `when: not ignore_assert_errors`. Setting
  `ignore_assert_errors: true` **bypasses** them — an emergency escape hatch, not a fix;
  you then own the consequences (e.g. an under-provisioned or unsupported node).

## Diagnostics

**Inventory-level (`validate_inventory`):**

| Assertion | Cause | Fix |
|-----------|-------|-----|
| `Group 'kube_control_plane' … empty` | no hosts in `kube_control_plane` | add ≥1 host to that inventory group |
| `Group 'etcd' cannot be empty in external etcd mode` | `etcd` group empty and not `etcd_deployment_type: kubeadm` | populate `etcd` group or use kubeadm-managed etcd |
| `Removed variables present: …` | inventory uses variables removed in this release | rename/drop the listed variables |
| `only support newer version of Kubernetes than <min>` | `kube_version` below `kube_version_min_required` | raise `kube_version` (see [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]) |

**Per-host (`preinstall/0040-verify-settings.yml`):**

| Assertion | Condition that must hold | Fix |
|-----------|--------------------------|-----|
| non-systemd OS | `ansible_service_mgr == systemd` | use a systemd-based OS |
| unsupported OS | distro ∈ supported list (RedHat/CentOS/Fedora/Ubuntu/Debian/Flatcar/Suse/openSUSE/ClearLinux/OracleLinux/AlmaLinux/Rocky/Amazon/Kylin/UnionTech/openEuler) | use a supported distro or set `allow_unsupported_distribution_setup: true` |
| control-plane RAM too small | `memtotal_mb >= 1500` (`minimal_master_memory_mb`) | give control-plane nodes ≥1500 MB (see [[TROUBLE-NODE_MEMORY_TOO_SMALL]]) |
| node RAM too small | `memtotal_mb >= 1024` (`minimal_node_memory_mb`) | give worker nodes ≥1024 MB |
| cgroups not enabled | `stat -fc %T /sys/fs/cgroup/` succeeds | enable cgroups (kernel/boot) |
| `ip` does not match local IPs | `ip ∈ host's IPv4/IPv6` | set `ip`/`access_ip` to an address the host actually holds |
| `access_ip` not pingable | `ping -c1 main_access_ip` (only if `ping_access_ip`) | fix routing/firewall or set `ping_access_ip: false` |
| kernel too low for cilium | kernel `>= 4.9.17` (cilium) | upgrade kernel; some cilium features need `>= 5.6.0` |
| kernel too low for nftables | kernel `>= 5.13` when `kube_proxy_mode: nftables` | upgrade kernel or use `ipvs`/`iptables` (see [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]) |
| bad hostname | lowercase alphanumeric, `.`/`-`, alnum ends | rename host to a DNS-1123-style name |
| empty resolv.conf nameservers | `/etc/resolv.conf` has ≥1 nameserver (coredns modes) | add a nameserver, set `upstream_dns_servers`, or `disable_host_nameservers` |
| `--limit` without facts cache | excluded hosts have cached facts | run `facts.yml` first without `--limit` |
| `download_run_once` on Flatcar | not Flatcar when `download_run_once`/`download_force_cache` | disable `download_run_once` on Flatcar |

To see which assertion failed, read the failing task name (`Stop if …`) and its
`msg` in the Ansible output; match it to the table above.

## Known Issues

- `ignore_assert_errors: true` silences per-host checks globally — convenient for labs,
  dangerous in production (you can deploy onto an unsupported/undersized host that later
  fails in subtle ways). Prefer fixing the precondition.
- The `--limit` facts-cache check is easy to hit in CI: always run the `facts.yml`
  playbook first, or don't use `--limit` on the first run.
- CNI-specific asserts (cilium/calico/flannel) live in each plugin's `check.yml` and add
  further preconditions (e.g. `cilium_identity_allocation_mode` must be `crd`/`kvstore`;
  `cilium_ipsec_key` required for ipsec encryption).

## References

- `0040-verify-settings.yml` and `validate_inventory/tasks/main.yml` at tag `v2.31.0`.
- Where to set inventory values: [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]].
