---
id: TROUBLE-IMAGEPULLBACKOFF
type: troubleshooting
title: "ImagePullBackOff / ErrImagePull (triage)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - ImagePullBackOff
  - ErrImagePull
  - failed to pull image
  - manifest unknown
  - pull access denied
  - unauthorized image pull
  - image not found
tags:
  - troubleshooting
  - images
  - registry
  - pods
sources:
  - type: docs
    path: Kubernetes images / debug
    url: https://kubernetes.io/docs/concepts/containers/images/
    note: "ImagePullBackOff = kubelet cannot pull the image; describe event names the reason"
relations:
  - type: see_also
    target: TROUBLE-CONTAINERD_REGISTRY_CONFIG
  - type: see_also
    target: TROUBLE-IMAGE_PULL_RATE_LIMIT
  - type: see_also
    target: TROUBLE-POD_CONTAINERCREATING
---

# ImagePullBackOff / ErrImagePull (triage)

## Summary

`ErrImagePull` (then `ImagePullBackOff` as the kubelet backs off) means the container
image can't be pulled. It's a *state* — the `describe` event names the real reason:
**image not found**, **auth required**, **rate-limited**, or **registry unreachable**.
This triage routes each to its fix.

## Problem

`kubectl get pod` shows `ErrImagePull`/`ImagePullBackOff`; `kubectl describe pod` →
`Failed to pull image "…": … <reason>`. The pod stays `ContainerCreating` meanwhile.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (`container_manager: containerd` — same triage
  for CRI-O/Docker with runtime-specific config).
- The kubelet asks the CRI to pull; registry resolution/auth/TLS use the runtime's config
  ([[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]).

## Diagnostics

- **`kubectl describe pod <pod>`** — the `Failed to pull image` event carries the exact
  error string; match it below.
- **Reproduce on the node:** `crictl pull <image>` — clearer error than the kubelet event,
  and confirms it's node-side not scheduler-side.

## Known Issues

Match the `describe`/`crictl` error to its fix:

- **`manifest unknown` / `not found` / `repository does not exist`** — wrong image name,
  tag, or registry host; the tag/digest doesn't exist. Fix the reference. (A private image
  can also masquerade as "not found" when auth is missing — check auth too.)
- **`unauthorized` / `pull access denied` / `401`/`403`** — the registry needs
  credentials. Add an `imagePullSecret` to the pod's ServiceAccount, or configure
  runtime-level auth (`containerd_registry_auth` —
  [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]).
- **`429 Too Many Requests`** — Docker Hub (or other) rate limit; use a pull-through
  mirror / authenticated pulls ([[TROUBLE-IMAGE_PULL_RATE_LIMIT]]).
- **`x509` / `tls: failed to verify` / `http: server gave HTTP response to HTTPS`** — TLS
  to a private/insecure registry; configure the CA or `skip_verify` via `hosts.toml`
  ([[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]).
- **`connection refused` / `no route to host` / timeout** — registry unreachable:
  network/proxy/firewall or a mirror that's down ([[CONFIG-PROXY]],
  [[TROUBLE-DOWNLOAD_FAILS]]).
- **`no matching manifest for <arch>` / `exec format error` (later)** — wrong CPU
  architecture image.

**Gotchas:**

- `ImagePullBackOff` keeps the pod in `ContainerCreating` — it's a sub-case of that state
  ([[TROUBLE-POD_CONTAINERCREATING]]).
- **`imagePullPolicy: Always`** re-pulls every start — a flaky registry then flaps the pod;
  `IfNotPresent` avoids re-pull when the image is cached.
- Private image "not found" is often really an **auth** failure — the registry hides
  existence from unauthenticated clients; verify credentials before assuming a typo.
- Kubespray's own control-plane/add-on images pull from `kube_image_repo`
  (`registry.k8s.io`) — a pull failure there during deploy is a registry/mirror/offline
  issue ([[TROUBLE-DOWNLOAD_FAILS]]).

## References

- Kubernetes images concept. Registry config: [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]; rate
  limits: [[TROUBLE-IMAGE_PULL_RATE_LIMIT]]; parent state: [[TROUBLE-POD_CONTAINERCREATING]].
