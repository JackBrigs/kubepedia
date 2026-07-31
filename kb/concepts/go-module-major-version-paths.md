---
id: CONCEPT-GO_MODULE_MAJOR_PATH
type: concept
title: "Go module major-version paths when querying vulnerability data"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - go module vN path
  - osv query returns too few cves
  - containerd v2 module path
  - why does the cve matrix under-report
tags:
  - security
  - cve
  - tooling
sources:
  - type: docs
    path: osv.dev API queried for github.com/containerd/containerd vs .../v2
    url: https://osv.dev/list?q=github.com/containerd/containerd/v2
    note: "the unsuffixed path answers only for the 1.x line; querying it for a 2.x version returns a subset without any error"
relations:
  - type: see_also
    target: TROUBLE-CONTAINERD_KNOWN_CVES
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Go module major-version paths when querying vulnerability data

## Summary

From major version 2 onwards, a Go module's import path carries the major version as a suffix:
`github.com/containerd/containerd` is the 1.x line, `github.com/containerd/containerd/v2` is the 2.x
line. To a vulnerability database these are **two different packages**.

Query the wrong one and nothing fails. You get a well-formed answer about a different code line —
which is how a security matrix can quietly under-report.

## Context

**This has already cost this knowledge base once.** The containerd matrix recorded 3 CVEs for
Kubespray v2.28.0–v2.31.0 where the correct number is 6–8: the sweep queried the unsuffixed path for
2.x versions and received the 1.x answer. The error is silent by construction — a subset is
indistinguishable from a smaller true count.

**Not every project adds the suffix.** Some stay on v1 forever, some (Calico among them) publish
without a `/vN` path at all. Deriving the suffix mechanically from the version number is therefore
also wrong: it invents paths for projects that do not use them and produces empty answers, which
read as "no known vulnerabilities".

**The rule that holds:** the module path is a declared fact, not a derived one. It belongs in the
matrix's own `sources` block, one entry per line of the component, and the tooling queries exactly
what is declared — `scripts/cve_sweep.py` works this way deliberately.

## Known Issues

**An empty or unchanging result is a signal, not a reassurance.** If a component reports zero
vulnerabilities, or reports the identical set for every shipped version, suspect the query before
concluding the component is clean. Both are the classic shapes of a wrong package path or an
incomplete record — see [[CONCEPT-OSV_RECORD_PITFALLS]].

**Ecosystem matters as much as the path.** The same project may be indexed as a Go module, as a
distribution package and as a GitHub advisory, with different completeness in each. A component
absent from one ecosystem is not absent from the others.

## References

- Verified against osv.dev for containerd 1.x and 2.x, 2026-07-31; the resulting correction is in
  [[TROUBLE-CONTAINERD_KNOWN_CVES]].
- Tracking: [[CONCEPT-SECURITY_ADVISORIES]].
