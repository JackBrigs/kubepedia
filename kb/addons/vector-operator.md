---
id: CONCEPT-ADDON_VECTOR_OPERATOR
type: concept
title: "Add-on: vector-operator (kaasops) — log pipelines as cluster resources"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.0.29 <=0.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - vector operator
  - clustervectorpipeline
  - cvp resource kubernetes
  - vectorpipeline configCheckResult false
  - LastAppliedPipelineHash
tags:
  - addon
  - observability
  - logging
sources:
  - type: code
    path: kaasops/vector-operator api/v1alpha1/vectorpipeline_types.go
    url: https://github.com/kaasops/vector-operator
    note: "status fields and the int64 rationale quoted from the type definition at origin/main"
  - type: code
    path: kaasops/vector-operator config/crd/bases/observability.kaasops.io_*.yaml
    note: "five CRDs: Vector, VectorPipeline, ClusterVectorPipeline, VectorAggregator, ClusterVectorAggregator"
relations:
  - type: see_also
    target: CONCEPT-COMPONENT_INTERACTION_FAILURES
---

# Add-on: vector-operator (kaasops) — log pipelines as cluster resources

## Summary

Not part of Kubespray. The operator runs a **Vector agent DaemonSet on every node** to collect
container and node logs, and turns pipeline configuration into Kubernetes objects instead of files:
sources, transforms and sinks are declared as CRs and merged by the operator into the Vector config.

Five CRDs, in two pairs plus one: `Vector` (the agent deployment itself), `VectorPipeline` /
`ClusterVectorPipeline` (namespaced and cluster-scoped pipelines, short names `vp` and `cvp`), and
`VectorAggregator` / `ClusterVectorAggregator` for the aggregator role.

## Context

**The reconcile loop is hash-driven.** Each pipeline's status carries three fields that explain
everything an operator needs day to day:

| Status field | Meaning |
|---|---|
| `role` | `agent` or `aggregator` — which side of the pipeline this object configures |
| `configCheckResult` | did the rendered Vector config pass validation (`VALID` column in `kubectl get vp`) |
| `LastAppliedPipelineHash` | CRC32 of the last **successfully applied** config |

On every reconcile the operator hashes the desired pipeline and compares it with
`LastAppliedPipelineHash`. Equal means "already applied, nothing to do". This is why a pipeline can
sit unchanged for months with no work being done — and why clearing that field is the accepted way
to force a full re-render:

```bash
kubectl patch cvp <name> --subresource=status --type=merge \
  -p '{"status":{"LastAppliedPipelineHash":null}}'
```

`--type=merge` makes `null` **delete** the key rather than zero it, and `--subresource=status`
edits observed state, not the spec. The operator then sees "nothing applied yet" and rebuilds.

**The field is `int64` for a reason, and the reason is a real defect.** Quoting the type definition:

> It is stored as an int64 because a uint32 can exceed the int32 upper bound (2147483647); an int32
> field would reject roughly half of all hash values and leave the pipeline stuck with
> `configCheckResult=false`.

So a pipeline stuck at `VALID=false` on an older operator may be nothing to do with the pipeline: a
hash above the int32 boundary was rejected by the API server. Upgrading the operator (or clearing
the hash) is the remedy, not rewriting the pipeline.

**Config validation runs in a separate pod.** The operator renders the merged config and validates
it before applying, so a broken pipeline is normally caught with `configCheckResult=false` and a
`reason`, rather than by a crash-looping agent.

## Known Issues

**A `VALID=false` pipeline does not stop the others**, but it does not participate either: its
sources are absent from the merged config, so those logs are simply not collected. Nothing alerts on
this by default — the object sits in the list with `false` and everything else keeps working.

**Forcing a re-render restarts log shipping on the agents.** Vector reloads with the new config;
whatever it had not yet flushed depends on the sink's buffering and on whether checkpointing is
enabled. For audit logs this is the difference between a gap and a delay.

**Clearing the hash is diagnosis, not repair.** It makes the reconcile loop run again; if the
pipeline drifts repeatedly, the cause is elsewhere and the patch will be needed every time.

## References

- `api/v1alpha1/vectorpipeline_types.go` and `config/crd/bases/observability.kaasops.io_*.yaml`
  at `origin/main`, read 2026-07-31; upstream issue #232 is cited in the type definition itself.
- Interaction failures between add-ons: [[CONCEPT-COMPONENT_INTERACTION_FAILURES]].
