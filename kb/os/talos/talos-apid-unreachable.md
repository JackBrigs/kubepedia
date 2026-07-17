---
id: TROUBLE-TALOS_APID_UNREACHABLE
type: troubleshooting
title: "Talos: talosctl can't reach the node (apid / certs / endpoints)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talosctl connection refused
  - talosctl certificate error
  - talos maintenance mode insecure
  - talosctl timeout endpoints nodes
tags:
  - troubleshooting
  - talos
  - operations
sources:
  - type: docs
    path: Talos troubleshooting / control-plane
    url: https://www.talos.dev/latest/advanced/troubleshooting-control-plane/
    note: "apid, endpoints/nodes, certs, maintenance mode"
relations:
  - type: see_also
    target: CONCEPT-TALOS_TALOSCTL_WORKFLOW
  - type: see_also
    target: TROUBLE-TALOS_CP_BOOTSTRAP
---

# Talos: talosctl can't reach the node (apid / certs / endpoints)

## Summary

`talosctl` times out, is refused, or returns a certificate error. Since there's no SSH, this is
your only management path — the cause is almost always **endpoints/nodes** misconfig, a
**talosconfig cert** problem, the node being in **maintenance mode**, or the API port blocked.

## Problem

- `talosctl ...` → `connection refused` / `context deadline exceeded` / `certificate signed by
  unknown authority` / `x509`.
- Commands hang or hit the wrong node.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_TALOSCTL_WORKFLOW]]). apid listens on **TCP
  50000**, mTLS.

## Diagnostics

- **Endpoints vs nodes:** `--endpoints` must be a node actually running apid (a control-plane
  node); `--nodes` is the target proxied through it. Set them in `talosconfig`
  (`talosctl config endpoint/node`). Talking to a worker as an endpoint, or a wrong IP, causes
  timeouts.
- **Maintenance mode (no config yet):** a freshly-booted node has **no PKI**, so normal mTLS
  fails — use **`--insecure`** (and talk to the node directly) until `apply-config` installs the
  cluster PKI.
- **talosconfig cert:** an expired/mismatched client cert or the wrong cluster's `talosconfig`
  yields `x509`/`unknown authority`. Regenerate/obtain the correct `talosconfig` (from the
  secrets bundle) — see [[CONCEPT-TALOS_MACHINE_CONFIG]].
- **Port/firewall:** ensure **50000/tcp** is reachable to the endpoint node; a network policy or
  cloud SG can block it.
- **Node down / not booted:** if the node never came up (bad install disk, no network), there's
  nothing to talk to — check console/serial or the boot; a control-plane that never
  bootstrapped is [[TROUBLE-TALOS_CP_BOOTSTRAP]].

## Known Issues

- Large client↔node **version skew** can make some commands/resources unavailable — match
  `talosctl` to the node's Talos minor.

## References

- Talos control-plane troubleshooting (above); workflow: [[CONCEPT-TALOS_TALOSCTL_WORKFLOW]];
  bootstrap: [[TROUBLE-TALOS_CP_BOOTSTRAP]].
