---
id: TAG-DOWNLOAD
type: ansible_tag
title: download (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - download
  - --tags download
tags:
  - ansible-tag
  - download
sources:
  - type: code
    path: playbooks/cluster.yml
    lines: "17"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role: download tagged download; when: not skip_downloads; hosts k8s_cluster:etcd"
  - type: code
    path: roles/download/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/download/tasks
    note: "download_container.yml, download_file.yml, extract_file.yml, prep_download.yml"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: COMPONENT-ETCD
---

# download (Ansible run-tag)

## Summary

`download` runs the `download` role, which fetches all binaries, archives, and
container images the cluster needs (kubelet/kubeadm/kubectl, etcd, containerd,
runc, CNI, CoreDNS images, etc.) and extracts/caches them. It is the tag used to
pre-stage or refresh artifacts, and is commonly skipped with `--skip-tags
download` on repeat runs.

## Context

- **Playbook:** `cluster.yml` (in the "Prepare for etcd install" play).
- **Hosts:** `k8s_cluster:etcd`.
- **Condition:** runs only when `not skip_downloads`.
- Central to offline/air-gapped installs (download once, cache, distribute).

## Implementation

`playbooks/cluster.yml`:

```yaml
- { role: download, tags: download, when: "not skip_downloads" }
```

The `download` role (`roles/download/tasks/`) decides what to pull
(`check_pull_required.yml`), downloads container images
(`download_container.yml`) and files (`download_file.yml`), and extracts archives
(`extract_file.yml`). Versions of the fetched artifacts are the component
versions documented under `kb/components/` (e.g. [[COMPONENT-ETCD]],
[[COMPONENT-CONTAINERD]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `download` tags the `download` role in
  `cluster.yml`, gated on `not skip_downloads`.
- **Standalone-run safety: safe.** Running only `--tags download` fetches/caches
  artifacts without configuring services; it is the recommended pre-stage step.
  Other tags depend on it having run (or on a populated cache).

## References

- `playbooks/cluster.yml:17` — `download` tag and `skip_downloads` gate.
- `roles/download/tasks/` — pull/extract logic.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
