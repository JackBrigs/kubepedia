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
  - what breaks upgrading cert-manager
tags:
  - upgrade
  - breaking-change
  - cert-manager
sources:
  - type: docs
    path: cert-manager/cert-manager release notes — entries marked breaking / action required
    url: https://github.com/cert-manager/cert-manager/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cert-manager: declared breaking changes by release

## Summary

**28 behaviour changes** the project itself marked as breaking or action-required, across
12 releases from 0.2.0 to 1.21.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.2.0

- this will require updating your existing deployments to point to the new image repository, as new tags will not be pushed to the old 'jetstackexperimental/cert-manager-controller` repository. A `helm upgrade` should take care of this. (#145, @munnerz)
- this will cause renewals of existing certificates to fail. You **must** delete certificates that have been previously produced by cert-manager else cert-manager may enter a renewal loop when saving the new certificates. Alternatively, you may specify a new secret to store your certificate in and manually update your ingress resource/applications to reference the new secret. (#172, @munnerz)

### 0.3.0

- Supporting resources for ClusterIssuer's (e.g. signing CA certificates, or ACME account private keys) will now be stored in the same namespace as cert-manager, instead of kube-system in previous versions (#329, @munnerz): *
- **: you will need to ensure to properly manually migrate these referenced resources across into the deployment namespace of cert-manager, else cert-manager may not be able to find account private keys or signing CA certificates
- Use ConfigMaps for leader election (#327, @mikebryant): *
- **: Before upgrading, scale the cert-manager Deployment to 0, to avoid two controllers attempting to operate on the same resources
- Remove support for ACMEv1 in favour of ACMEv2 (#309, @munnerz): *
- **: As this release drops support for ACMEv1, all Issuer resources that use ACMEv1 endpoints (e.g. existing Let's Encrypt Issuers) will need updating to use equivalent ACMEv2 endpoints. (TODO: link to docs guide)
- Remove ingress-shim and link it into cert-manager itself (#502, @munnerz) *
- **: You must change your 'helm install' command to use the new --ingressShim.defaultIssuerName, --ingressShim.defaultIssuerKind options when upgrading as --ingressShim.extraArgs has been removed
- Add `certmanager.k8s.io/acme-http01-edit-in-place` annotation and change ingress-shim to set 'ingressClass' on ACME Certificate resources by default. (#493, @munnerz) *
- **: This is a potentially breaking change for users of ingress controllers that map a single IP address to a single Ingress resource, such as the GCE ingress controller. These users will need to add the following annotation to their ingress: `certmanager.k8s.io/acme-http01-edit-in-place: "true"`

### 0.4.0

- Check the acme issuer has the 'HTTP01' challenge type configured if in use. (#629, @groner)

### 0.6.0

- Fix ACME issues relating to wildcard CNAME records and add a 'cnameStrategy' field to the ACME Issuer DNS01 provider config. (#1136, @munnerz)

### 0.11.0

- Rename `certmanager.k8s.io` API group to `cert-manager.io` ([#2096](https://github.com/jetstack/cert-manager/pull/2096), [@munnerz](https://github.com/munnerz))
- Move Order and Challenge resources to the acme.cert-manager.io API group ([#2093](https://github.com/jetstack/cert-manager/pull/2093), [@munnerz](https://github.com/munnerz))
- Move v1alpha1 API to v1alpha2 ([#2087](https://github.com/jetstack/cert-manager/pull/2087), [@munnerz](https://github.com/munnerz))
- Allow controlling whether temporary certificates are issued using a new annotation "certmanager.k8s.io/issue-temporary-certificate" on Certificate resources. Previously, when an ACME certificate was requested, a temporary certificate would be issued in order to improve compatibility with ingress-gce. ingress-shim has been updated to automatically set this annotation on managed Certificate resources when using the 'edit-in-place' annotation, but users that have manually created their Certificate resources will need to manually add the new annotation to their Certificate resources. ([#2089](https://github.com/jetstack/cert-manager/pull/2089), [@munnerz](https://github.com/munnerz))

### 0.12.0

- Users who have previously set the Kubernetes Auth Mount Path will need to update their manifests to include the entire mount path. The `/login` endpoint is added for you

### 1.2.0

- **⚠️ BREAKING CHANGE ⚠️ The minimum supported Kubernetes version is now v1.16.0** as of cert-manager `v1.2.0`. Users still running Kubernetes `v1.15` or below should upgrade to a supported version before installing cert-manager or use cert-manager `v1.1`

### 1.7.0

- Breaking change: pprof now runs by default on localhost:6060 for webhook and controller, but only if explicitly enabled. Pprof can now be enabled also for cainjector. All three components have `--enable-profiling`, `--profiler-address` CLI flags to configure profiling. Thanks to @bitscuit for help with this! (#4550, @irbekrm)
- Breaking change: removes the deprecated `dns01-self-check-nameservers` flag. Use `--dns01-recursive-nameservers` instead. (#4551, @irbekrm)

### 1.8.0

- The field `spec.privateKey.rotationPolicy` on Certificate resources is now validated. Valid options are Never and Always. If you are using a GitOps flow and one of your YAML manifests contains a Certificate with an invalid value, you will need to update it with a valid value to prevent your GitOps tool from failing on the new validation. ([#4913](https://github.com/cert-manager/cert-manager/pull/4913), [@jahrlin](https://github.com/jahrlin))
- Server-Side Apply: the feature gate `ServerSideApply=true` now configures the `ingress-shim` and `gateway-shim` controllers to use Kubernetes Server-Side Apply on Certificate resources. When upgrading to cert-manger 1.8 with `ServerSideApply=true`, do make sure there are no Challenge resources currently in the cluster. If there are some, you will need to manually delete them once they are in 'valid' state as cert-manager post-1.8 with the Server-Side Apply feature is not able to clean up Challenge resources created pre-1.8. ([#4811](https://github.com/cert-manager/cert-manager/pull/4811), [@JoshVanL](https://github.com/JoshVanL))
- The field `additionalOutputFormats`, which is available as an alpha feature on Certificate resources, is now correctly validated. Previously, it would only get validated when the `privateKey` field was set on the Certificate. If you are using the `additionalOutputFormats` field, you will want to add the feature gate `AdditionalCertificateOutputFormats` to both the webhook and the controller. Previously, you only needed to set `AdditionalCertificateOutputFormats` on the controller. If the feature gate is missing on either the controller or the webhook, you won't be able to use the `additionalOutputFormat` field. ([#4814](https://github.com/cert-manager/cert-manager/pull/4814), [@JoshVanL](https://github.com/JoshVanL))

### 1.11.0

- Breaking: updates the gateway API integration to use the more stable v1beta1 API version. Any users of the cert-manager `ExperimentalGatewayAPISupport` alpha feature must ensure that `v1beta` of Gateway API is installed in cluster. (#5583, @lvyanru8200)

### 1.15.0

- Breaking Change: Fixed unintended certificate chain is used if `preferredChain` is configured. (#6755, @import-shiburin)

### 1.21.0

- **BREAKING**: The Helm chart no longer ships a default `Role` and `RoleBinding` granting the cert-manager controller ServiceAccount permission to create tokens for itself (`serviceaccounts/token: create`). This RBAC was added in v1.16 (#7213) but no documented workflow requires it, and the motivating Route53 docs section was removed in Oct 2024. If you rely on `serviceAccountRef.name` pointing at the controller ServiceAccount (an undocumented pattern), you must now create your own `Role` and `RoleBinding` granting `serviceaccounts/token: create` on that ServiceAccount, or migrate to one of the documented patterns (IRSA ambient, or a dedicated ServiceAccount with its own RBAC). (#8931, @wallrj-cyberark)


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `cert-manager/cert-manager`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cert-manager.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
