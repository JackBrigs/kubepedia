---
id: TROUBLE-TBOT
type: troubleshooting
title: "tbot (Teleport Machine ID): certs not issued/renewed — join token, proxy address, role/output config"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "18.7.4"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - tbot not renewing certs
  - teleport machine id join failed
  - tbot proxy address
  - tbot output config
tags:
  - troubleshooting
  - security
  - teleport
  - certificates
sources:
  - type: external
    path: tbot
    url: https://goteleport.com/docs/machine-id/
    note: "tbot joins Teleport with a token and writes short-lived certs; failures are join token, proxy address, or role/output"
relations:
  - type: see_also
    target: CONCEPT-ADDON_TBOT
---

# tbot (Teleport Machine ID): certs not issued/renewed — join token, proxy address, role/output config

## Summary

`tbot` is Teleport's **Machine ID** agent: it joins Teleport and continuously writes **short-lived certificates** for workloads. When certs stop appearing/renewing it's a **join token** problem, a wrong **proxy/auth address**, or an **output/role** misconfig. App tracks Teleport `18.x`.

## Problem

- Workloads get auth failures because tbot isn't producing/renewing certs; tbot logs join or renewal errors.

## Context

- tbot `18.x` ([[CONCEPT-ADDON_TBOT]]); verify the exact running image (some inventory-pinned tags may not exist).
- **Join token:** tbot authenticates to Teleport with a join method/token; expired/wrong token → it can't start the identity.
- **Proxy/auth address:** the `--proxy-server`/auth address must be correct and reachable with valid TLS.
- **Output/role:** the bot's role must permit the requested certs, and the output destination (dir/secret) must be writable.

## Diagnostics

```bash
kubectl -n <ns> logs deploy/tbot | tail        # join / renewal errors
kubectl -n <ns> get secret | grep -i tbot       # output secret present/updating?
```

## Known Issues

- **Join — fix:** issue a valid join token / configure the join method; restart tbot to re-establish identity.
- **Address — fix:** set the correct Teleport proxy/auth address with a trusted cert and network reachability.
- **Role/output — fix:** grant the bot role the needed cert permissions and ensure the output destination is writable.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_TBOT]].
