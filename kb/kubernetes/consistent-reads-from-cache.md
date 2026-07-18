---
id: CONCEPT-K8S_CONSISTENT_READS_CACHE
type: concept
title: "Consistent reads from the watch cache — lower etcd load (on 1.31, GA 1.34)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ConsistentListFromCache
  - consistent reads from cache
  - reduce etcd load list
  - apiserver watch cache list
  - etcd read pressure kubernetes
tags:
  - kubernetes
  - apiserver
  - etcd
  - performance
sources:
  - type: code
    path: keps/sig-api-machinery/2340-Consistent-reads-from-cache
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/2340-Consistent-reads-from-cache
    note: "kep.yaml: alpha 1.28, beta/on-by-default 1.31, stable 1.34"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
---

# Consistent reads from the watch cache — lower etcd load (on 1.31, GA 1.34)

## Summary

The API server can now serve **consistent LIST** requests from its **in-memory watch cache** (using
etcd's progress-notify to guarantee freshness) instead of hitting etcd for every consistent read.
`ConsistentListFromCache` is **on by default from K8s 1.31** and **GA in 1.34**. The result is
**significantly lower etcd read load** on busy clusters — an automatic performance/scale win with no
config to set.

## Context

- Milestone (`keps/sig-api-machinery/2340-...` kep.yaml): alpha **1.28**, beta/on **1.31**, stable
  **1.34**.
- **What changes:** previously a "consistent" LIST (the default for `kubectl get`, controllers'
  relists) bypassed the cache and read from etcd; now the apiserver serves it from cache once the cache
  is provably up-to-date. Correctness is preserved (still linearizable).
- **Operator impact (positive):** less etcd CPU/IO and fewer large range reads — helps large clusters
  and reduces etcd as a bottleneck ([[COMPONENT-ETCD]]). No action; just expect **lower etcd read
  pressure** after 1.31, and don't be surprised that etcd request metrics drop. Pairs with WatchList
  (streaming informers) for the same "reduce apiserver↔etcd pressure" theme.

## References

- `keps/sig-api-machinery/2340-Consistent-reads-from-cache` (kep.yaml GA 1.34). etcd
  [[COMPONENT-ETCD]]; silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
