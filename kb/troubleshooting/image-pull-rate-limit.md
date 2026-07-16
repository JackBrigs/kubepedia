---
id: TROUBLE-IMAGE_PULL_RATE_LIMIT
type: troubleshooting
title: "ImagePullBackOff: 429 Too Many Requests (registry rate limit)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - image-pull-rate-limit
tags:
  - troubleshooting
  - operations
  - containerd
sources:
  - type: docs
    url: https://kubernetes.io/docs/concepts/containers/images/
    note: "Kubernetes images / registries"
relations:
  - type: see_also
    target: PRACTICE-CONTAINERD_DIAGNOSTICS
---

# ImagePullBackOff: 429 Too Many Requests (registry rate limit)

## Summary

Pods fail with `ImagePullBackOff` and `429 Too Many Requests` (or 'toomanyrequests') when pulling from a public registry (e.g. Docker Hub anonymous limits).

## Problem

Public registries rate-limit anonymous/low-tier pulls. Large clusters pulling the same public image on many nodes hit the limit.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
kubectl describe pod <p> | grep -iE "429|toomanyrequests|pull"
crictl pull <image>          # reproduce on a node
```

## Known Issues

Use an authenticated pull (image pull secret / registry auth), mirror images into an internal registry (PRACTICE-OFFLINE_ENVIRONMENT), or use `download_run_once` so images are fetched once and distributed. Avoid `imagePullPolicy: Always` for public images at scale.

## References

- https://kubernetes.io/docs/concepts/containers/images/ — Kubernetes images / registries (verified behavior, 2026-07-16).
