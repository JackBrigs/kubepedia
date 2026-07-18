---
id: TROUBLE-KYVERNO_IMAGE_VERIFICATION_BLOCKS
type: troubleshooting
title: "Kyverno image verification blocks pods — Sigstore/TUF unreachable or keyless misconfig"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.18.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kyverno verifyImages fails
  - kyverno cosign rekor unreachable
  - kyverno ImageValidatingPolicy blocks
  - kyverno keyless tuf error
  - kyverno image signature blocks pod
tags:
  - kyverno
  - troubleshooting
  - image-verification
  - supply-chain
sources:
  - type: code
    path: config/crds/policies.kyverno.io/policies.kyverno.io_imagevalidatingpolicies.yaml
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/config/crds/policies.kyverno.io/policies.kyverno.io_imagevalidatingpolicies.yaml
    note: "attestors cosign/notary; ctlog/rekor public keys; insecureIgnoreTlog/insecureIgnoreSCT (L89-183)"
  - type: docs
    path: CHANGELOG.md
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/CHANGELOG.md
    note: "--tufRoot/--tufMirror configure custom Sigstore (v1.11 note)"
relations:
  - type: see_also
    target: CONCEPT-KYVERNO_CEL_POLICIES
  - type: see_also
    target: TROUBLE-KYVERNO_POLICY_NOT_APPLYING
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
---

# Kyverno image verification blocks pods — Sigstore/TUF unreachable or keyless misconfig

## Summary

Kyverno's image verification (`ImageValidatingPolicy` and legacy `verifyImages`) requires reachable
**Sigstore** infrastructure. When Rekor/Fulcio/the TUF mirror is unreachable, or a keyless
identity/cert-chain check fails, verification **errors** — and with an Enforce/Fail action that
**rejects pod creation cluster-wide**. This is different from "verifyImages not applying": here
verification *does* run, but fails due to signing-infra connectivity or keyless/TUF misconfig, and
takes pods down with it.

## Problem

- Pods rejected with image-verification errors (signature/attestation could not be verified) even
  though the image is legitimately signed.
- Intermittent failures correlated with Rekor/Fulcio/TUF availability (public Sigstore outages, egress
  blocked, air-gapped clusters).
- Keyless verification fails on identity/issuer or certificate-chain mismatch.

## Context

- Applies to Kyverno **1.18.x** ([[CONCEPT-ADDON_KYVERNO]], [[CONCEPT-KYVERNO_CEL_POLICIES]]).
- `attestors` demand **`cosign`** or **`notary`**, with `ctlog`/`rekor` public-key settings, TUF/Rekor
  URLs, and `insecureIgnoreTlog`/`insecureIgnoreSCT` toggles
  (`imagevalidatingpolicies.yaml`@v1.18.2 L89-183). Verification reaches out to Rekor (transparency
  log), Fulcio (keyless CA), and a TUF mirror.
- **Air-gapped / restricted egress** is the classic failure: the public Sigstore endpoints aren't
  reachable → every image check errors. `--tufRoot` / `--tufMirror` configure a **custom/self-hosted
  Sigstore** (CHANGELOG@v1.18.2, v1.11 note).
- Distinct from a policy simply not matching ([[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]]).

## Diagnostics

- Admission controller logs show the verification error (Rekor/Fulcio/TUF unreachable, signature
  mismatch, keyless identity failure).
- Test egress from the Kyverno pods to the Sigstore endpoints (Rekor, Fulcio, TUF mirror).
- Confirm the policy's `attestors` (key vs keyless), expected identities/issuer, and whether a private
  TUF/Rekor is configured.

## Known Issues

- **Fix (air-gapped / restricted):** stand up a **private Sigstore** (self-hosted Rekor/Fulcio + TUF
  mirror) and point Kyverno at it via `--tufRoot`/`--tufMirror`; or use **key-based** cosign attestors
  instead of keyless (no Fulcio/TUF dependency).
- **Fix (availability trade-off):** for non-critical enforcement, use `Audit`/`Warn` instead of a
  hard `Deny`/`Fail` so a Sigstore outage doesn't block scheduling; or `insecureIgnoreTlog`/
  `insecureIgnoreSCT` only if you accept the reduced guarantee.
- **Verify the signing chain:** for keyless, the `subject`/`issuer` (identity) and cert chain must match
  exactly — a mismatch fails even when infra is reachable.

## References

- Kyverno `config/crds/policies.kyverno.io/policies.kyverno.io_imagevalidatingpolicies.yaml`,
  `CHANGELOG.md` (@v1.18.2). CEL engine [[CONCEPT-KYVERNO_CEL_POLICIES]]; policy-not-matching
  [[TROUBLE-KYVERNO_POLICY_NOT_APPLYING]]; addon [[CONCEPT-ADDON_KYVERNO]].
