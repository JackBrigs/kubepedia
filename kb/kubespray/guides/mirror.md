---
id: PRACTICE-MIRROR
type: best_practice
title: Using a public download mirror in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - download mirror
tags:
  - mirror
  - offline
sources:
  - type: docs
    path: docs/operations/mirror.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/mirror.md
    note: "configuring image and file download mirrors"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "kube_image_repo (L92) feeds kubeadm_image_repo, kube_proxy_image_repo, pod_infra_image_repo (pause), coredns/nodelocaldns image repos — the blast radius of changing a mirror"
relations:
  - type: see_also
    target: PRACTICE-OFFLINE_ENVIRONMENT
  - type: see_also
    target: CONFIG-PROXY
---

# Using a public download mirror in Kubespray

## Summary
Public mirrors speed up downloading of public images and files in regions with slow access to upstream registries (e.g. China). Kubespray is pointed at a mirror by overriding the image-repo and files-repo variables, reusing the same download-configuration mechanism as offline deployments. Only use mirrors from providers you trust.

## Context
Applies when upstream registries (gcr, k8s, docker, quay, ghcr) and file downloads are slow or blocked. Configuration follows the offline-environment approach and is set in `<your_inventory>/group_vars/k8s_cluster.yml`. Involves the image-repo override variables and `files_repo`.

## Implementation
Override the download endpoints in `<your_inventory>/group_vars/k8s_cluster.yml`. Example using the DaoCloud mirror (China):
```yaml
gcr_image_repo: "gcr.m.daocloud.io"
kube_image_repo: "k8s.m.daocloud.io"
docker_image_repo: "docker.m.daocloud.io"
quay_image_repo: "quay.m.daocloud.io"
github_image_repo: "ghcr.m.daocloud.io"

files_repo: "https://files.m.daocloud.io"
```
Replace `m.daocloud.io` with any mirror site you prefer. See the offline-environment doc for the full image/file download configuration.

Caveats:
- Use mirror sites only if you trust the provider; the Kubespray team cannot verify their reliability or security.

Community-run mirror sites (DaoCloud, China): public-image-mirror and public-binary-files-mirror on GitHub.

## Service impact

Setting a mirror is not a download-only knob — on an **existing** cluster it rewrites image
references and therefore restarts things.

- **On a fresh install: no impact.** The variables only change where artefacts are fetched
  from before anything runs.
- **On a running cluster the blast radius is wide.** `kube_image_repo` feeds
  `kubeadm_image_repo`, `kube_proxy_image_repo`, `coredns_image_repo`,
  `nodelocaldns_image_repo` **and `pod_infra_image_repo`** (the pause/sandbox image) —
  `roles/kubespray_defaults/defaults/main/download.yml`. A `cluster.yml` run after the
  change re-renders the kubeadm config, the control-plane static-pod manifests, the
  kube-proxy/CoreDNS manifests and containerd's `config.toml`, so the apiserver and the
  container runtime restart, and every image is pulled again from the new registry.
- **A wrong or unreachable mirror fails closed:** image pulls fail, the run aborts
  mid-flight, and any component already re-templated to the new reference is stuck in
  `ImagePullBackOff`. Verify the mirror serves every needed image/tag **before** the run.
- **Changing the pause image reference restarts pod sandboxes** as they are recreated — do
  it in a maintenance window and node by node (`--limit`), not cluster-wide at once.
- **Trust is part of the impact.** A mirror serves the binaries and images your cluster
  runs; a compromised or stale mirror is a supply-chain problem, not a performance one.
  Prefer a mirror you control ([[PRACTICE-OFFLINE_ENVIRONMENT]]) and keep checksums
  enabled.

## References
- docs/operations/mirror.md (tag v2.31.0 1c9add4)
