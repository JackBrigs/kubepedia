---
id: TROUBLE-CILIUM_CLI_BINARY_NOT_DOWNLOADED
type: troubleshooting
title: "Cilium install fails — 'Source /tmp/releases/cilium not found' (cilium-cli binary missing, ran cilium tag without download)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-26"
confidence: verified
aliases:
  - Source /tmp/releases/cilium not found
  - cilium-cli binary missing
  - Cilium Copy Ciliumcli binary from download dir failed
  - could not find src /tmp/releases/cilium
  - --tags cilium without download
  - standalone cilium tag fails
  - local_release_dir cilium not found
tags:
  - troubleshooting
  - cilium
  - cni
  - download
  - ansible-tag
sources:
  - type: code
    path: roles/network_plugin/cilium/tasks/install.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/tasks/install.yml
    note: "task 'Cilium | Copy Ciliumcli binary from download dir': copy src={{ local_release_dir }}/cilium dest={{ bin_dir }}/cilium remote_src=true — errors 'Source ... not found' when the binary was never staged"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "download item 'ciliumcli': dest={{ local_release_dir }}/cilium-{{ cilium_cli_version }}-{{ image_arch }}.tar.gz, unarchive: true — the download role stages the 'cilium' binary into local_release_dir; enabled only when kube_network_plugin == 'cilium' or cilium_deploy_additionally"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "local_release_dir: /tmp/releases (default) — the staging dir the copy task reads from"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TAG-CILIUM
  - type: see_also
    target: TAG-DOWNLOAD
  - type: see_also
    target: VARIABLE-LOCAL_RELEASE_DIR
  - type: see_also
    target: VARIABLE-CILIUMCLI_DOWNLOAD_URL
  - type: see_also
    target: VARIABLE-BIN_DIR
---

# Cilium install fails — 'Source /tmp/releases/cilium not found' (cilium-cli binary missing, ran cilium tag without download)

## Summary

An Ansible run that touches the Cilium CNI fails at the task **`Cilium | Copy
Ciliumcli binary from download dir`** with `Source /tmp/releases/cilium not
found` (Ansible `copy` with `remote_src: true` cannot find `src`). Since
Kubespray `v2.29.0` Cilium is installed **via the `cilium-cli` binary** (`cilium
install/upgrade`), and that binary is staged into `local_release_dir`
(`/tmp/releases` by default) by the **`download` role** — the `ciliumcli`
download item fetches `cilium-<ver>-<arch>.tar.gz` and `unarchive: true` extracts
the `cilium` binary there. The install step then copies `{{ local_release_dir
}}/cilium` → `{{ bin_dir }}/cilium`. If the download step never ran — the usual
cause is a **tag-restricted run** (`--tags cilium` or `--tags network` **without
`download`**) — the tarball is never fetched/extracted, `/tmp/releases/cilium`
does not exist, and the copy errors. It is **not** a broken cluster: the CNI role
simply never had its prerequisite staged.

## Problem

- Playbook fails on `Cilium | Copy Ciliumcli binary from download dir` with
  `Source /tmp/releases/cilium not found` (or `could not find src=…/cilium`).
- Typically seen on a **narrow, tag-limited run** meant to only re-apply Cilium:
  `ansible-playbook cluster.yml --tags cilium` (or `--tags network`) with no
  `download` tag, so the `ciliumcli` download task was skipped.
- The failure is on `groups['kube_control_plane'][0]` (where `cilium
  install/upgrade` runs), or on any host in `k8s_cluster` if the copy runs
  cluster-wide.
- Distinguish from a **download that ran but could not fetch** — there the
  `download`/`ciliumcli` task itself fails earlier with an HTTP/checksum error
  (GitHub unreachable, offline/proxy, bad `ciliumcli_binary_checksum`), and
  `/tmp/releases` has no `cilium-*.tar.gz` at all. See "Known Issues".

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, where Cilium is deployed through
  `cilium-cli` rather than static manifests ([[TAG-CILIUM]], [[COMPONENT-CILIUM]]).
- The staging chain, all at tag `v2.31.0`:
  - `local_release_dir: /tmp/releases`
    (`roles/kubespray_defaults/defaults/main/main.yml`, [[VARIABLE-LOCAL_RELEASE_DIR]]).
  - download item **`ciliumcli`** (`.../download.yml`):
    `dest: {{ local_release_dir }}/cilium-{{ cilium_cli_version }}-{{ image_arch }}.tar.gz`,
    `url: {{ ciliumcli_download_url }}`, `unarchive: true`,
    `enabled: kube_network_plugin == 'cilium' or cilium_deploy_additionally` —
    this is what produces `{{ local_release_dir }}/cilium`
    ([[VARIABLE-CILIUMCLI_DOWNLOAD_URL]]).
  - install task `Cilium | Copy Ciliumcli binary from download dir`
    (`roles/network_plugin/cilium/tasks/install.yml`):
    `copy: src={{ local_release_dir }}/cilium dest={{ bin_dir }}/cilium
    remote_src=true` ([[VARIABLE-BIN_DIR]]).
- The `download` and `network_plugin` roles run in the **same play** on a full
  `cluster.yml`/`upgrade_cluster.yml`, so the binary is always present in a normal
  run. The gap only opens when an operator **restricts tags** to re-apply just the
  CNI and drops `download` — the standalone-run risk is called out on
  [[TAG-CILIUM]] ("izolated `--tags cilium` without `--tags download/network` is
  risky").
- The staged file is literally named `cilium` (the extracted CLI), **not**
  `cilium-mount` — do not confuse this with the `mount-cgroup` init-container
  `/hostbin/cilium-mount` copy failure, which is a running-node ownership problem
  ([[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]]).

## Diagnostics

- Read the failing task name and message: it is `Cilium | Copy Ciliumcli binary
  from download dir`, `Source /tmp/releases/cilium not found`.
- Confirm the binary is absent on the target host (usually the first
  control-plane): `ls -l /tmp/releases/cilium /tmp/releases/cilium-*.tar.gz`.
  - **Nothing at all** → the download step never ran (tag-restricted run) — the
    common case.
  - **Tarball present but no `cilium`** → unarchive failed (rare; permissions on
    `local_release_dir`).
- Check what tags the run used: if the command was `--tags cilium` / `--tags
  network` with no `download`, that is the cause.
- Rule out the "download ran but failed to fetch" variant: re-run with `download`
  and watch the `ciliumcli` task — an HTTP 403/404/timeout or checksum mismatch
  points at GitHub reachability / offline-registry / `ciliumcli_binary_checksum`,
  not at a skipped tag (see [[VARIABLE-CILIUMCLI_DOWNLOAD_URL]]).

## Known Issues

- **Fix (common case) — include the `download` tag.** Add `download` to the tag
  set so the `ciliumcli` item stages `/tmp/releases/cilium` before the copy:
  `ansible-playbook cluster.yml -b -i <inventory> --tags download,cilium`. In AWX,
  add `download` to the job's Job Tags (`download,cilium`), keep the same Limit.
  Or simply do not tag-restrict (run the CNI step from a full/normal play).
- **Do not narrow the Limit off the control plane.** The `cilium install/upgrade`
  runs on `groups['kube_control_plane'][0]`; that host must be in scope so the
  binary is staged and used there.
- **Offline / air-gapped or GitHub blocked.** If the `download`/`ciliumcli` task
  fails to fetch (not skipped), the `cilium-cli` tarball is unreachable. Confirm
  `ciliumcli_download_url` resolves from the control plane, fix the proxy, or
  pre-place the tarball / point `ciliumcli_download_url` (and the mirror) at your
  internal artifact store. Related offline pitfall for the Cilium images:
  [[TROUBLE-CILIUM_OPERATOR_GENERIC_OFFLINE_REGISTRY]].
- **Verify after the fix:** `ls -l /tmp/releases/cilium && /tmp/releases/cilium
  version` on the first control-plane, then re-run; the copy task and the
  subsequent `cilium install/upgrade` proceed.

## References

- `roles/network_plugin/cilium/tasks/install.yml` (copy task, `src:
  {{ local_release_dir }}/cilium`); `roles/kubespray_defaults/defaults/main/download.yml`
  (`ciliumcli` item, `unarchive: true`);
  `roles/kubespray_defaults/defaults/main/main.yml` (`local_release_dir:
  /tmp/releases`). Run-tag semantics: [[TAG-CILIUM]], [[TAG-DOWNLOAD]]. CNI:
  [[COMPONENT-CILIUM]]. Not to be confused with
  [[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]].
