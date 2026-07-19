---
id: CONCEPT-AIRGAPPED_INSTALL
type: concept
title: "Air-gapped / offline Kubespray install — the two mirrors, the overrides, and the traps"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - air-gapped kubespray
  - offline environment install
  - files_repo images_repo
  - registry_host mirror
  - disconnected cluster install
  - offline.yml group_vars
  - no internet kubespray deploy
tags:
  - concept
  - offline
  - air-gap
  - install
  - index
sources:
  - type: docs
    path: docs/operations/offline-environment.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/offline-environment.md
    note: "files_repo + registry_host; per-source URL overrides; containerd_registries_mirrors; contrib/offline/generate_list.sh"
  - type: code
    path: inventory/sample/group_vars/all/offline.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/inventory/sample/group_vars/all/offline.yml
    note: "the override surface: kube_image_repo/gcr/docker/quay/github _image_repo, github_url, dl_k8s_io_url, storage_googleapis_url, get_helm_url"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_MANAGER
  - type: see_also
    target: CONCEPT-ADDON_SPEGEL
  - type: see_also
    target: CONFIG-PROXY
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
  - type: see_also
    target: TROUBLE-IMAGE_PULL_RATE_LIMIT
---

# Air-gapped / offline Kubespray install — the two mirrors, the overrides, and the traps

## Summary

Installing Kubespray with **no internet** is a first-class but under-documented non-default. It rests on
**two mirrors** you must stand up and point every download at: a **files_repo** (binaries, archives,
Helm charts) and a **container registry** (`registry_host`) for images. Kubespray doesn't discover them
— you override each upstream source explicitly. This spine gathers the override surface and the traps
(cred leakage, per-component specials like Cilium, containerd mirror config) into one place, from the
v2.31.0 `offline-environment.md`.

## Context

**The two mirrors.** Everything Kubespray fetches is either a **file** or an **image**:

- **files_repo** — HTTP(S) server holding binaries/charts. Tip: keep the **original domains as top
  directories** (`github.com/`, `dl.k8s.io/`, `storage.googleapis.com/`, `get.helm.sh/`) so the URL
  overrides line up. Authenticated form:
  `files_repo: "https://{{ files_repo_user }}:{{ files_repo_pass }}@{{ files_repo_host }}{{ files_repo_path }}"`.
- **registry_host** — a container registry mirroring all images.

**The override surface** (set in `group_vars/all/offline.yml`):

| What | Override to |
|---|---|
| container images | `kube_image_repo`, `gcr_image_repo`, `docker_image_repo`, `quay_image_repo`, `github_image_repo` → `{{ registry_host }}` |
| GitHub binaries | `github_url: "{{ files_repo }}/github.com"` |
| k8s binaries | `dl_k8s_io_url: "{{ files_repo }}/dl.k8s.io"` |
| Google storage | `storage_googleapis_url: "{{ files_repo }}/storage.googleapis.com"` |
| Helm | `get_helm_url: "{{ files_repo }}/get.helm.sh"` |
| containerd pulls | `containerd_registries_mirrors` (per-registry `host` + capabilities, for insecure/auth mirrors) |

**Build the artifact lists.** Use **`contrib/offline/generate_list.sh`** to produce the exact
files/images your target version needs, then seed both mirrors from a connected host. Other helpers live
under `contrib/offline/`.

**Per-component specials (don't miss these):**

- **Cilium** installs via Helm and needs the **chart** mirrored too: mirror `helm.cilium.io/index.yaml`
  and the `cilium-<ver>.tgz`, set `cilium_install_extra_flags: "--repository {{ files_repo }}/helm.cilium.io/"`,
  and override the operator/agent image repos to `registry_host`.
- `local_path_provisioner_helper_image_repo` (busybox helper) also needs pointing at the registry.
- OS package repos (Docker/containerd deps) must be mirrored per-distro if you install packages offline.

**Alternative to a central registry — Spegel.** [[CONCEPT-ADDON_SPEGEL]] is a peer-to-peer image mirror
across nodes; it reduces (not eliminates) the registry dependency and helps with pull scale
([[TROUBLE-IMAGE_PULL_RATE_LIMIT]]), but the initial images still have to reach the cluster.

**Semi-connected (proxy, not full air-gap):** if there's an egress proxy, use `http_proxy`/`https_proxy`
+ `no_proxy` ([[CONFIG-PROXY]]) instead of full mirroring — different mode, don't conflate the two.

### Traps

- **Credential leak:** `files_repo` with embedded `user:pass` is **printed** by the download role's
  "Show url of file to download" task when **`unsafe_show_logs: true`**. Keep `unsafe_show_logs` off, and
  vault-encrypt `files_repo_pass`.
- **Partial override = mystery timeout:** miss one source override and the run **hangs trying to reach
  the internet** for that single artifact. Symptom looks like a network fault; it's an un-mirrored URL.
  Cross-check the generated artifact list against what you seeded.
- **Version drift:** the artifact list is **per Kubespray/K8s version** — regenerate it for every
  upgrade or a new component will be missing from the mirror.
- **Addon catalog:** each enabled addon adds its own images/charts to mirror; enabling a new addon in an
  air-gapped cluster means re-seeding first.

## References

- `docs/operations/offline-environment.md`, `inventory/sample/group_vars/all/offline.yml`,
  `contrib/offline/` (tag `v2.31.0`). Runtime mirror config [[CONCEPT-CONTAINER_MANAGER]]; P2P mirror
  [[CONCEPT-ADDON_SPEGEL]]; proxy mode [[CONFIG-PROXY]]; inventory layout
  [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]].
