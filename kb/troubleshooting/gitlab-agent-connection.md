---
id: TROUBLE-GITLAB_AGENT
type: troubleshooting
title: "GitLab Agent (agentk): not connecting to KAS — token, KAS address/wss, egress/proxy, config project"
status: active
kubespray_version: null
kubernetes_version: ">=1.33 <=1.35"
component_version: ">=18.11.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - agentk not connecting
  - gitlab agent kas tunnel
  - gitlab agent token invalid
  - agentk websocket failed
  - gitlab agent config.yaml
tags: [troubleshooting, gitops, gitlab, agent]
sources:
  - type: external
    path: GitLab Agent troubleshooting
    url: https://docs.gitlab.com/ee/user/clusters/agent/troubleshooting.html
    note: "agentk dials KAS over wss with a registration token; config in .gitlab/agents/<name>/config.yaml"
relations:
  - type: see_also
    target: CONCEPT-ADDON_GITLAB_AGENT
  - type: see_also
    target: CONCEPT-GITOPS
---

# GitLab Agent (agentk): not connecting to KAS — token, KAS address/wss, egress/proxy, config project

## Summary

`agentk` dials the GitLab Agent Server (**KAS**) over a persistent **wss** tunnel using a registration
**token**. "Agent not connected" in the GitLab UI is almost always a **bad/revoked token**, the **wrong
KAS address**, **egress/proxy** blocking the WebSocket, or a **missing config** file in the agent's
project. agentk tracks GitLab `18.x`.

## Problem

- The agent shows **not connected** in GitLab; `agentk` logs repeat connection/handshake errors; GitOps
  syncs and CI cluster access don't work.

## Context

- GitLab Agent `agentk 18.11.0` ([[CONCEPT-ADDON_GITLAB_AGENT]]); pull-based GitOps + CI tunnel
  ([[CONCEPT-GITOPS]]).
- **Token:** agentk registers with a token from the agent's record; a revoked/rotated/wrong token →
  auth failure on connect.
- **KAS address:** the `--kas-address` (wss URL, e.g. `wss://kas.gitlab.example.com`) must be correct and
  TLS-valid; self-hosted GitLab must have KAS enabled and exposed.
- **Egress/proxy:** the tunnel is a long-lived **WebSocket**; a proxy/firewall that blocks wss or
  terminates idle connections kills it. Honor `http_proxy`/`no_proxy` for the agent.
- **Config project:** cluster-management/GitOps behavior comes from `.gitlab/agents/<name>/config.yaml`
  in the configured project; missing/misplaced config = agent connects but does nothing.

## Diagnostics

```bash
kubectl -n gitlab-agent logs deploy/<release>-agentk | tail       # handshake/tunnel errors
kubectl -n gitlab-agent get deploy,pods
# from a node: can it reach KAS?
kubectl -n gitlab-agent exec deploy/<release>-agentk -- /bin/sh -c 'wget -qO- https://<kas-host> || true'
```

## Known Issues

- **Token — fix:** re-create the agent token in GitLab and update the agent's secret; each agentk uses
  its own token.
- **KAS address — fix:** set the correct `wss://` KAS URL with a valid cert; confirm KAS is enabled on
  self-hosted GitLab.
- **Egress — fix:** allow wss egress to KAS; set proxy vars; ensure idle-timeouts don't cut the tunnel.
- **Config — fix:** add `.gitlab/agents/<name>/config.yaml` to the agent's project for GitOps/CI scope.

## References

- GitLab Agent troubleshooting. Addon [[CONCEPT-ADDON_GITLAB_AGENT]]; GitOps [[CONCEPT-GITOPS]].
