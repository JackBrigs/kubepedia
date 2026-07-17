---
id: TROUBLE-APISERVER_MEMORY_LISTS
type: troubleshooting
title: "kube-apiserver: OOM / memory growth from LISTs & relists"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - apiserver oom large list
  - apiserver memory not released
  - informer relist thundering herd
  - too old resource version relist storm
  - watchlist streaming list
tags:
  - troubleshooting
  - apiserver
  - memory
  - scale
sources:
  - type: docs
    path: kube-apiserver API streaming (WatchList)
    url: https://kubernetes.io/blog/2024/12/17/kube-apiserver-api-streaming/
    note: "streaming list cuts memory O(watchers×~2MB)"
  - type: docs
    path: apiserver OOM on large LIST issue
    url: https://github.com/kubernetes/kubernetes/issues/114276
    note: "full LIST assembled in memory, not released"
relations:
  - type: see_also
    target: TROUBLE-APISERVER_APF_429
  - type: see_also
    target: TROUBLE-APISERVER_ETCD_LATENCY
---

# kube-apiserver: OOM / memory growth from LISTs & relists

## Summary

The apiserver RSS spikes (and often doesn't fall back) when it serves large **LIST** responses
or many informers **relist** at once — up to OOM. The structural fix is **WatchList /
streaming-list**; the tactical fix is pagination + APF.

## Problem

- apiserver memory jumps after a few large LISTs and stays high; concurrent large LISTs OOM-kill
  it (e.g. a 20 MB CRD dataset: 10 LISTs → ~8 GB, 20 → ~12 GB; 100 watches → only ~3 GB).
- Memory rises as objects are created and **stays high after deletion** (CRD parsing/conversion
  cache; ~10k objects of a 5-version CRD ≈ 2 GB retained).
- After a CRD spec change / apiserver restart, watchers get `too old resource version` and **all
  relist simultaneously** → memory spike / OOM.

## Context

- Applies to Kubernetes **1.29–1.35** (larger clusters / big CRD datasets). Companion to APF
  ([[TROUBLE-APISERVER_APF_429]]).

## Diagnostics

- **Why:** the apiserver assembles the **entire LIST in memory** (etcd fetch → deserialize →
  convert → serialize) before the first byte, and doesn't promptly return memory to the OS;
  footprint ≈ O(watchers × page-size × object-size). Watches instead stream from the watch cache
  (issues #114276 / #125580).
- **Enable WatchList / streaming-list** (KEP-3157, `WatchListClient`; beta in 1.32): the initial
  informer LIST becomes a streaming watch from cache — upstream scale tests cut apiserver memory
  ~20 GB → ~2 GB.
- **Paginate** LISTs (`limit`/continue); avoid full cross-namespace dumps; **cap blast radius
  with APF** ([[TROUBLE-APISERVER_APF_429]]).
- **Bound object growth:** ResourceQuota **object counts** + TTL cleanup; reduce **served/stored
  CRD versions** (multiple versions multiply the parsing-cache cost, issue #133846).
- **Relist storm:** add informer jitter/backoff; the restart-time storm is mitigated by
  PR #86430, but the CRD-cacher-recreation variant (#123074, closed not-planned) needs
  streaming + APF + memory headroom.

## Known Issues

- These are **design/behaviour** issues, not CVEs — no upstream "fix" for the LIST-memory
  retention itself; a restart reclaims memory.

## References

- API-streaming blog + issues #114276/#125580/#133846/#123074, PR #86430 (above). Related:
  [[TROUBLE-APISERVER_APF_429]], [[TROUBLE-APISERVER_ETCD_LATENCY]].
