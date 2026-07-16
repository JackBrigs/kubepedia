---
id: PRACTICE-MIRROR
type: best_practice
title: Using a public download mirror in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
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
relations: []
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

## References
- docs/operations/mirror.md (tag v2.31.0 1c9add4)
