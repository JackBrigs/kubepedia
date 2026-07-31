---
id: CONCEPT-OSV_RECORD_PITFALLS
type: concept
title: "Reading osv.dev records: when 'affected' does not mean affected"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - osv introduced 0 no fixed
  - every version shows the same cves
  - osv git range not version filterable
  - cve matrix says fixed version is affected
tags:
  - security
  - cve
  - tooling
sources:
  - type: docs
    path: osv.dev API records for k8s.io/ingress-nginx (GO-2025-3565, GO-2025-3567)
    url: https://osv.dev/list?q=k8s.io/ingress-nginx
    note: "ranges are SEMVER with a single event {introduced: 0} and no fixed event; the paired GHSA record carries the fix versions"
relations:
  - type: see_also
    target: CONCEPT-GO_MODULE_MAJOR_PATH
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
---

# Reading osv.dev records: when 'affected' does not mean affected

## Summary

osv.dev answers "is this version affected" better than any changelog — when the record is complete.
Three shapes of incomplete record make it answer "yes" for versions where the problem was fixed long
ago, and each one has been hit while building the matrices in this knowledge base.

## Context

**Unbounded range: `introduced: 0`, no `fixed` event.** Formally this claims every version ever
released is affected. Sometimes that is true — a genuinely unfixed vulnerability looks exactly like
this. Often it just means the record's authors did not fill in the fix. Observed on
`k8s.io/ingress-nginx`: version 1.13.3 matched ten CVEs, including ones the project fixed in 1.12.1.

**Paired records with different completeness.** The same CVE arrives as two records — one from the
Go vulnerability database, one from GitHub advisories — and the fix versions may exist in only one
of them. Reading a single record decides affectedness on partial data; the fix versions have to be
merged across every record sharing the CVE id.

**GIT-only ranges.** When the affected range is expressed as commit hashes and nothing else, no
version comparison is possible at all. Such a record matches whatever version is asked about.

**Branch-specific fixes.** A fix list like `1.11.5, 1.12.1` means two maintenance branches were
patched. Comparing a 1.11.6 install against the highest entry (1.12.1) would wrongly call it
affected: the comparison must prefer the fix on the same line, falling back to the highest only when
that line has none.

## Known Issues

**Identical counts across versions are the tell.** A matrix where every shipped version carries the
same CVE list is almost never true — components do get fixed. Treat it as a defect in the query or
the data, and verify one entry by hand against the project's own release notes before publishing.

**Empty results deserve the same suspicion**, for the mirror-image reason: a wrong package path
returns nothing and reads as safety. See [[CONCEPT-GO_MODULE_MAJOR_PATH]].

**Publishing an unverified matrix is worse than having none.** It converts an unknown into a
confident false statement, and downstream planning — pins, upgrade windows, risk acceptance — is
built on it.

## References

- Records inspected directly on 2026-07-31 for `k8s.io/ingress-nginx`; the fix-merging logic that
  resulted lives in `scripts/gen_cve_matrix.py`.
- Module paths: [[CONCEPT-GO_MODULE_MAJOR_PATH]]; tracking: [[CONCEPT-SECURITY_ADVISORIES]].
