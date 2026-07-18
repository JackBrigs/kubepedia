---
id: TROUBLE-K8S_SPDY_WEBSOCKETS
type: troubleshooting
title: "kubectl exec/port-forward/cp fails through a proxy — SPDY→WebSockets transition (on-by-default 1.31)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubectl exec fails through proxy
  - port-forward websocket
  - PortForwardWebsockets
  - SPDY proxy broken exec
  - kubectl cp hangs proxy
tags:
  - kubernetes
  - troubleshooting
  - apiserver
  - kubectl
sources:
  - type: code
    path: keps/sig-api-machinery/4006-transition-spdy-to-websockets
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/4006-transition-spdy-to-websockets
    note: "kep.yaml: PortForwardWebsockets/TranslateStreamCloseWebsocketRequests alpha 1.29, beta/on-by-default 1.31"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# kubectl exec/port-forward/cp fails through a proxy — SPDY→WebSockets transition (on-by-default 1.31)

## Summary

`kubectl exec`, `port-forward`, `cp`, and `attach` historically streamed over **SPDY**. Kubernetes is
moving these to **WebSockets** (`PortForwardWebsockets` and related gates **on by default from 1.31**).
If a **reverse proxy / load balancer / API gateway** in front of the API server only handles SPDY (or
mishandles WebSocket `Upgrade`/`Connection` headers), these commands start **failing or hanging** after
the cluster reaches 1.31 (Kubespray v2.29.0+). The cluster is fine — the middlebox is the problem.

## Problem

- `kubectl exec`/`attach` returns an error or hangs; `port-forward` won't establish; `kubectl cp`
  stalls — specifically **through a proxy**, while direct-to-apiserver works.
- Errors mentioning WebSocket `Upgrade`, `101 Switching Protocols` not completing, or connection reset
  on the streamed channel.

## Context

- Milestone (`keps/sig-api-machinery/4006-...` kep.yaml): alpha **1.29**, beta/on-by-default **1.31**.
  `kubectl` prefers WebSockets and **falls back** to SPDY only against **old servers** — but once the
  server is ≥1.31 the WebSocket path is used, exposing proxies that don't support it.
- Common culprits: an L7 proxy/WAF, an ingress in front of the apiserver, or an old
  `kubectl`-proxy/bastion that terminates and re-originates the stream without WebSocket support.

## Diagnostics

- Bypass the proxy: run the same command with a kubeconfig pointing **directly** at the apiserver /
  the API VIP — if it works direct but fails via the proxy, the proxy is the cause.
- Check the proxy supports **WebSocket upgrade** (passes `Upgrade: websocket` / `Connection: Upgrade`,
  allows `101 Switching Protocols`, no idle-timeout killing the long-lived stream).
- Confirm server version ≥1.31 (`kubectl version`).

## Known Issues

- **Fix (correct):** configure the proxy/LB to support **WebSocket** upgrades for the apiserver path
  (enable Upgrade header passthrough; raise idle timeouts for long-lived streams). This is the durable
  fix — SPDY is going away.
- **Temporary:** newer `kubectl` still negotiates; keeping the server path WebSocket-capable is
  required. Do not rely on SPDY-only middleboxes long-term.
- **Pre-upgrade check:** before moving to K8s 1.31, verify any proxy in front of the apiserver handles
  WebSockets ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-api-machinery/4006-transition-spdy-to-websockets` (kep.yaml on-by-default 1.31). Silent
  changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; version support [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
