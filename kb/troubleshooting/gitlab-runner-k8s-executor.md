---
id: TROUBLE-GITLAB_RUNNER_K8S_EXECUTOR
type: troubleshooting
title: "GitLab Runner (Kubernetes executor): job pods fail/pending/OOM"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=16.10.0 <=18.4.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - gitlab runner prepare environment context deadline exceeded
  - runner imagepullsecrets ignored
  - runner pods forbidden default serviceaccount
  - runner helper oomkilled cgroup v2
  - runner could not resolve host
tags:
  - troubleshooting
  - gitlab-runner
  - ci
sources:
  - type: docs
    path: GitLab Runner Kubernetes executor troubleshooting
    url: https://docs.gitlab.com/runner/executors/kubernetes/troubleshooting/
    note: "pod start, DNS, DIND, timeouts"
  - type: docs
    path: GitLab Runner Kubernetes install troubleshooting
    url: https://docs.gitlab.com/runner/install/kubernetes_troubleshooting/
    note: "RBAC, secrets"
relations:
  - type: see_also
    target: CONCEPT-ADDON_GITLAB_RUNNER
---

# GitLab Runner (Kubernetes executor): job pods fail/pending/OOM

## Summary

Community-sourced GitLab Runner K8s-executor failures: build pods **stuck Pending / timeout**,
**imagePullSecrets ignored**, **RBAC** errors (jobs run as `default` SA), **helper OOMKilled**
(incl. a cgroup-v2 hang), **orphaned pods**, **DNS** failures, and **DIND TLS/MTU** problems.

## Problem

- `prepare environment: context deadline exceeded` / `timed out waiting for pod to start`.
- `ErrImagePull`/`ImagePullBackOff` for job/service images despite secrets.
- `pods is forbidden: ... serviceaccount:<ns>:default cannot create pods`.
- Helper/build container `OOMKilled` (137); or OOM pod **hangs** until timeout.
- `Could not resolve host`; DIND `SSL_connect: SSL_ERROR_SYSCALL`.

## Context

- Applies to Runner **16.10–18.4** (owner runs 18.4.0 and 16.10.0 —
  [[CONCEPT-ADDON_GITLAB_RUNNER]]).

## Diagnostics

- **Pending/timeout:** cluster can't schedule before `poll_timeout`, or slow apiserver/admission
  webhooks / Docker Hub rate-limit. Raise `poll_timeout`/`prepare_timeout`, exclude the runner
  namespace from slow webhooks, add node capacity (issues #29580/#27367).
- **imagePullSecrets ignored:** reference the secret in
  `runners.kubernetes.image_pull_secrets`; secrets are read **at registration** so **restart
  the runner manager** after changing them; or use `DOCKER_AUTH_CONFIG` (issues #27664/#31066).
- **RBAC:** set `rbac.create: true` + an explicit `serviceAccount.name`; the Role needs `pods`
  (list/get/watch/create/delete), `pods/exec` (create), `pods/log` (get), plus
  secrets/configmaps (charts issue #353).
- **Helper OOM / cgroup v2:** set `helper_memory_limit`/`_request` (≥250 MiB); on **EKS/AL2023
  cgroup v2** the runner may not detect the OOMKill and the pod hangs — use
  **`FF_USE_POD_ACTIVE_DEADLINE_SECONDS`** (issue #38244).
- **Orphaned pods:** a runner-manager crash leaves job pods — `FF_USE_POD_ACTIVE_DEADLINE_SECONDS`
  (default on) / the Runner Pod Cleanup app (issue #37201).
- **DNS:** the default Alpine helper's musl resolver can fail — set
  `helper_image_flavor = "ubuntu"` (glibc).
- **DIND TLS/MTU:** set DIND `--mtu=1450` (overlay MTU), wait for DIND to start, and mount the
  GitLab CA (`tls-ca-file`).

## Known Issues

- Chart 0.81.0 bumped `ExternalSecret` to `v1` (external-secrets operator must support it).
- The **Ubuntu helper image ships a vulnerable git** (**CVE-2025-48384**, HIGH) — update the
  helper git (issue #39046). "runner" CVEs in GitLab server releases are a different product.

## References

- GitLab Runner K8s executor + install troubleshooting (above); issues
  #29580/#27664/#38244/#37201/#39046.
- Addon: [[CONCEPT-ADDON_GITLAB_RUNNER]].
