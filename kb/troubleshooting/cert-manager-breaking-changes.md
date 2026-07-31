---
id: TROUBLE-CERT_MANAGER_BREAKING_CHANGES
type: troubleshooting
title: "cert-manager: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.2.0 <=1.21.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cert-manager breaking changes
  - cert-manager upgrade broke
  - cert-manager action required upgrade
tags:
  - upgrade
  - breaking-change
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes — "breaking changes" / "action required" entries
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py, short and duplicate lines filtered out"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager: declared breaking changes by release

## Summary

**23 behaviour changes** the project itself marked as breaking or action-required, across
11 releases from 0.2.0 to 1.21.0. Read this before planning
an upgrade that crosses any of these versions: unlike defects, these are changes that work as
designed and still break a working configuration.

## Problem

An upgrade across a breaking change usually succeeds — the failure appears afterwards, in behaviour:
a setting silently ignored, a default flipped, an API version withdrawn.

## Context

### 0.2.0

- Move to 'jetstack' organisation. Action required: this will require updating your existing deployments to point to the new image repository, as new tags will not be pushed to the old 'jetstackexperimental/cert-manager-controller` repository. A `helm upgrade` should take care of this. (#145, @munnerz)
- Set the Kubernetes secret type to TLS. Action required: this will cause renewals of existing certificates to fail. You **must** delete certificates that have been previously produced by cert-manager else cert-manager may enter a renewal loop when saving the new certificates. Alternatively, you may specify a new secret to store your certificate in and manually update your ingress resource/applications to reference the new secret. (#172, @munnerz)

### 0.3.0

- Supporting resources for ClusterIssuer's (e.g. signing CA certificates, or ACME account private keys) will now be stored in the same namespace as cert-manager, instead of kube-system in previous versions (#329, @munnerz):
- Use ConfigMaps for leader election (#327, @mikebryant):
- Remove support for ACMEv1 in favour of ACMEv2 (#309, @munnerz):
- Remove ingress-shim and link it into cert-manager itself (#502, @munnerz)
- Add `certmanager.k8s.io/acme-http01-edit-in-place` annotation and change ingress-shim to set 'ingressClass' on ACME Certificate resources by default. (#493, @munnerz)

### 0.4.0

- Check the acme issuer has the 'HTTP01' challenge type configured if in use. (#629, @groner)

### 0.6.0

- ACTION REQUIRED: Fix ACME issues relating to wildcard CNAME records and add a 'cnameStrategy' field to the ACME Issuer DNS01 provider config. (#1136, @munnerz)

### 0.11.0

- Rename `certmanager.k8s.io` API group to `cert-manager.io` ([#2096](https://github.com/jetstack/cert-manager/pull/2096), [@munnerz](https://github.com/munnerz))
- Move Order and Challenge resources to the acme.cert-manager.io API group ([#2093](https://github.com/jetstack/cert-manager/pull/2093), [@munnerz](https://github.com/munnerz))
- Move v1alpha1 API to v1alpha2 ([#2087](https://github.com/jetstack/cert-manager/pull/2087), [@munnerz](https://github.com/munnerz))
- Allow controlling whether temporary certificates are issued using a new annotation "certmanager.k8s.io/issue-temporary-certificate"

### 1.2.0

- **⚠️ BREAKING CHANGE ⚠️ The minimum supported Kubernetes version is now v1.16.0** as of cert-manager `v1.2.0`. Users still running Kubernetes `v1.15` or below should upgrade to a supported version before installing cert-manager or use cert-manager `v1.1`.

### 1.7.0

- Breaking change: pprof now runs by default on localhost:6060 for webhook and controller, but only if explicitly enabled. Pprof can now be enabled also for cainjector. All three components have `--enable-profiling`, `--profiler-address` CLI flags to configure profiling. Thanks to @bitscuit for help with this! (#4550, @irbekrm)
- Breaking change: removes the deprecated `dns01-self-check-nameservers` flag. Use `--dns01-recursive-nameservers` instead. (#4551, @irbekrm)

### 1.8.0

- ACTION REQUIRED: The field `spec.privateKey.rotationPolicy` on Certificate resources is now validated. Valid options are Never and Always. If you are using a GitOps flow and one of your YAML manifests contains a Certificate with an invalid value, you will need to update it with a valid value to prevent your GitOps tool from failing on the new validation. ([#4913](https://github.com/cert-manager/cert-manager/pull/4913), [@jahrlin](https://github.com/jahrlin))
- ACTION REQUIRED: Server-Side Apply: the feature gate `ServerSideApply=true` now configures the `ingress-shim` and `gateway-shim` controllers to use Kubernetes Server-Side Apply on Certificate resources. When upgrading to cert-manger 1.8 with `ServerSideApply=true`, do make sure there are no Challenge resources currently in the cluster. If there are some, you will need to manually delete them once they are in 'valid' state as cert-manager post-1.8 with the Server-Side Apply feature is not able to clean up Challenge resources created pre-1.8. ([#4811](https://github.com/cert-manager/cert-manager/pull/4811), [@JoshVanL](https://github.com/JoshVanL))
- ACTION REQUIRED: The import path for cert-manager has been updated to `github.com/cert-manager/cert-manager`. If you import cert-manager as a go module (which isn't currently recommended), you'll need to update the module import path in your code to import cert-manager 1.8 or later. ([#4587](https://github.com/cert-manager/cert-manager/pull/4587), [@SgtCoDFish](https://github.com/SgtCoDFish))
- ACTION REQUIRED: The field `additionalOutputFormats`, which is available as an alpha feature on Certificate resources, is now correctly validated. Previously, it would only get validated when the `privateKey` field was set on the Certificate. If you are using the `additionalOutputFormats` field, you will want to add the feature gate `AdditionalCertificateOutputFormats` to both the webhook and the controller. Previously, you only needed to set `AdditionalCertificateOutputFormats` on the controller. If the feature gate is missing on either the controller or the webhook, you won't be able to use the `additionalOutputFormat` field. ([#4814](https://github.com/cert-manager/cert-manager/pull/4814), [@JoshVanL](https://github.com/JoshVanL))

### 1.11.0

- Breaking: updates the gateway API integration to use the more stable v1beta1 API version. Any users of the cert-manager `ExperimentalGatewayAPISupport` alpha feature must ensure that `v1beta` of Gateway API is installed in cluster. (#5583, @lvyanru8200)

### 1.15.0

- Breaking Change: Fixed unintended certificate chain is used if `preferredChain` is configured. (#6755, @import-shiburin)

### 1.21.0

- **BREAKING**: The Helm chart no longer ships a default `Role` and `RoleBinding` granting the cert-manager controller ServiceAccount permission to create tokens for itself (`serviceaccounts/token: create`). This RBAC was added in v1.16 (#7213) but no documented workflow requires it, and the motivating Route53 docs section was removed in Oct 2024. If you rely on `serviceAccountRef.name` pointing at the controller ServiceAccount (an undocumented pattern), you must now create your own `Role` and `RoleBinding` granting `serviceaccounts/token: create` on that ServiceAccount, or migrate to one of the documented patterns (IRSA ambient, or a dedicated ServiceAccount with its own RBAC). (#8931, @wallrj-cyberark)

## Diagnostics

Compare the version in use against the list above:

```bash
kubectl get nodes -o wide          # runtime versions, for node components
helm list -A                       # chart-deployed components
```

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than 45
characters and duplicates were dropped, because section headings and list fragments come through the
extractor as if they were entries. If a release you care about looks empty here, read its notes
upstream before concluding nothing changed.

## References

- Upstream releases of `cert-manager/cert-manager`, read 2026-07-31 via `scripts/upstream_issues.py`;
  raw extraction in `reports/upstream/cert-manager.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
