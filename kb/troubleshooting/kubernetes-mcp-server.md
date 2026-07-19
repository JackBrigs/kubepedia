---
id: TROUBLE-KUBERNETES_MCP
type: troubleshooting
title: "kubernetes-mcp-server: LLM can't act / over-broad access — MCP auth, RBAC scope, open-webui link"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.0.56"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - kubernetes mcp server
  - mcp llm cluster access
  - open-webui mcp
  - mcp rbac scope
tags:
  - troubleshooting
  - ai
  - mcp
  - security
sources:
  - type: external
    path: kubernetes_mcp
    url: https://github.com/manusa/kubernetes-mcp-server
    note: "mcp-server exposes cluster ops to LLMs over MCP; its ServiceAccount RBAC bounds what the LLM can do"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KUBERNETES_MCP
  - type: see_also
    target: CONCEPT-SECURITY_INDEX
---

# kubernetes-mcp-server: LLM can't act / over-broad access — MCP auth, RBAC scope, open-webui link

## Summary

`kubernetes-mcp-server` (app `0.0.56`, pre-1.0) lets an LLM drive the cluster over MCP, paired with open-webui. Two failure directions: the LLM **can't do anything** (MCP not connected / RBAC too tight), or — more dangerous — it has **over-broad access** because the server's ServiceAccount is cluster-admin. Treat its RBAC as a security boundary ([[CONCEPT-SECURITY_INDEX]]).

## Problem

- open-webui/LLM can't run cluster actions (tools error), or conversely the MCP SA is far more privileged than intended.

## Context

- kubernetes-mcp-server `0.0.56` ([[CONCEPT-ADDON_KUBERNETES_MCP]]); **pre-1.0**, expect churn.
- **RBAC = capability:** the server acts as its **ServiceAccount**; whatever RBAC that SA has is what the LLM can do. Cluster-admin here means the LLM is cluster-admin.
- **MCP link:** open-webui must be pointed at the mcp-server endpoint with valid auth or tools won't register.

## Diagnostics

```bash
kubectl -n <ns> logs deploy/kubernetes-mcp-server | tail
kubectl -n <ns> get sa,clusterrolebinding | grep -i mcp   # how privileged is it?
kubectl auth can-i --list --as=system:serviceaccount:<ns>:<mcp-sa>
```

## Known Issues

- **Can't act — fix:** connect open-webui to the MCP endpoint; grant the SA the **minimum** RBAC for the intended actions.
- **Over-broad — fix:** scope the SA down from cluster-admin to only what's needed; this is a real security exposure ([[CONCEPT-SECURITY_INDEX]]).

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_KUBERNETES_MCP]].
