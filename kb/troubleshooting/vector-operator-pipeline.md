---
id: TROUBLE-VECTOR_OPERATOR
type: troubleshooting
title: "vector-operator: logs not flowing — invalid pipeline CRD -> bad Vector config, image, sink auth"
status: active
kubespray_version: null
kubernetes_version: ">=1.28 <=1.31"
component_version: ">=0.3.3"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - vector pipeline not working
  - vectorpipeline crd invalid
  - vector pod crashloop config
  - vector sink auth failed
  - kaasops vector operator
tags: [troubleshooting, observability, vector, logging]
sources:
  - type: external
    path: kaasops vector-operator
    url: https://github.com/kaasops/vector-operator
    note: "operator aggregates VectorPipeline/ClusterVectorPipeline CRs into Vector config; Vector image user-supplied"
relations:
  - type: see_also
    target: CONCEPT-ADDON_VECTOR_OPERATOR
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# vector-operator: logs not flowing — invalid pipeline CRD -> bad Vector config, image, sink auth

## Summary

The kaasops vector-operator compiles `VectorPipeline`/`ClusterVectorPipeline` CRs into a **Vector
config** and runs Vector as a DaemonSet/aggregator. When logs stop flowing it's usually an **invalid
pipeline** producing a config Vector rejects (crashloop), a **user-supplied Vector image** that's wrong,
or a **sink** the pipeline can't authenticate to. Operator app `v0.3.3`.

## Problem

- No logs reach the sink; the Vector pod is `CrashLoopBackOff` ("configuration error"), or a pipeline CR
  shows a not-valid status.

## Context

- vector-operator `0.3.3` ([[CONCEPT-ADDON_VECTOR_OPERATOR]]); K8s window **1.28–1.31** (older — check
  compatibility on newer clusters). The managed **Vector image is user-supplied via the CRD**, not pinned
  by the chart.
- **Bad pipeline → bad config:** the operator merges all pipelines; one invalid source/transform/sink
  makes the whole generated config fail validation, so Vector won't start (all pipelines down, not just
  the broken one).
- **Sink auth:** an Elasticsearch/Loki/S3 sink with wrong endpoint/creds fails at runtime — Vector runs
  but drops/errors on delivery.

## Diagnostics

```bash
kubectl -n vector get vectorpipeline,clustervectorpipeline -o wide      # valid?
kubectl -n vector logs deploy/vector-operator | tail
kubectl -n vector get secret,cm | grep -i vector                        # generated config
kubectl -n vector logs ds/vector | tail                                 # config/sink errors
```

## Known Issues

- **Invalid pipeline — fix:** `describe` the pipeline CR for the validation error; fix the offending
  source/transform/sink — one bad CR blocks the merged config.
- **Image — fix:** set a valid Vector image/tag in the CRD (the operator doesn't pin one).
- **Sink auth — fix:** correct the sink endpoint and credentials secret; watch the Vector pod logs for
  delivery errors ([[CONCEPT-OBSERVABILITY_STACK]]).

## References

- kaasops vector-operator. Addon [[CONCEPT-ADDON_VECTOR_OPERATOR]]; stack [[CONCEPT-OBSERVABILITY_STACK]].
