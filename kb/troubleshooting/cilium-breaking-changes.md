---
id: TROUBLE-CILIUM_BREAKING_CHANGES
type: troubleshooting
title: "cilium: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.10.0 <=9.0.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium breaking changes
  - cilium upgrade broke
  - cilium action required upgrade
  - what breaks upgrading cilium
tags:
  - upgrade
  - breaking-change
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes — entries marked breaking / action required
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium: declared breaking changes by release

## Summary

**192 behaviour changes** the project itself marked as breaking or action-required, across
29 releases from 0.10.0 to 9.0.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.10.0

- Update based on `azcore` refactor [#15383](https://github.com/Azure/azure-sdk-for-go/pull/15383)

### 0.11.0

- Unexported `AzureCLICredentialOptions.TokenProvider` and its type, `AzureCLITokenProvider`

### 0.12.0

- Removed `NewAuthenticationPolicy()` from credentials. Clients should instead use azcore's `runtime.NewBearerTokenPolicy()` to construct a bearer token authorization policy
- The `AuthorityHost` field in credential options structs is now a custom type, `AuthorityHost`, with underlying type `string`
- `NewChainedTokenCredential` has a new signature to accommodate a placeholder options struct: ```go // before cred, err := NewChainedTokenCredential(credA, credB)
- Removed `ExcludeAzureCLICredential`, `ExcludeEnvironmentCredential`, and `ExcludeMSICredential` from `DefaultAzureCredentialOptions`
- `NewClientCertificateCredential` requires a `[]*x509.Certificate` and `crypto.PrivateKey` instead of a path to a certificate file. Added `ParseCertificates` to simplify getting these in common cases: ```go // before cred, err := NewClientCertificateCredential("tenant", "client-id", "/cert.pem", nil)
- Removed `InteractiveBrowserCredentialOptions.ClientSecret` and `.Port`
- Removed `id` parameter of `NewManagedIdentityCredential()`. User assigned identities are now specified by `ManagedIdentityCredentialOptions.ID`: ```go // before cred, err := NewManagedIdentityCredential("client-id", nil) // or, for a resource ID opts := &ManagedIdentityCredentialOptions{ID: ResourceID} cred, err := NewManagedIdentityCredential("/subscriptions/...", opts)
- `DeviceCodeCredentialOptions.UserPrompt` has a new type: `func(context.Context, DeviceCodeMessage) error`
- Credential options structs now embed `azcore.ClientOptions`. In addition to changing literal initialization syntax, this change renames `HTTPClient` fields to `Transport`
- `AzureCLICredential` no longer reads the environment variable `AZURE_CLI_PATH`
- `NewManagedIdentityCredential` no longer reads environment variables `AZURE_CLIENT_ID` and `AZURE_RESOURCE_ID`. Use `ManagedIdentityCredentialOptions.ID` instead
- Unexported `AuthenticationFailedError` and `CredentialUnavailableError` structs. In their place are two interfaces having the same names

### 0.13.0

- Replaced `AuthenticationFailedError.RawResponse()` with a field having the same name
- Instances of `ChainedTokenCredential` will now skip looping through the list of source credentials and re-use the first successful credential on subsequent calls to `GetToken`. If `ChainedTokenCredentialOptions.RetrySources` is true, `ChainedTokenCredential` will continue to try all of the originally provided credentials each time the `GetToken` method is called. `ChainedTokenCredential.successfulCredential` will contain a reference to the last successful credential. `DefaultAzureCredenial` will also re-use the first successful credential on subsequent calls to `GetToken`. `DefaultAzureCredential.chain.successfulCredential` will also contain a reference to the last successful credential

### 0.14.0

- Removed `AuthorityHost`. Credentials are now configured for sovereign or private clouds with the API in `azcore/cloud`, for example: ```go // before opts := azidentity.ClientSecretCredentialOptions{AuthorityHost: azidentity.AzureGovernment} cred, err := azidentity.NewClientSecretCredential(tenantID, clientID, secret, &opts)

### 0.15.0

- remove `Response.UnmarshalError` as it's no longer required

### 0.17.0

- Rename `AnonymousCredential` to `NewAnonymousCredential` (https://github.com/Azure/azure-sdk-for-go/pull/15104)
- rename `AuthenticationPolicyOptions` to `AuthenticationOptions` (https://github.com/Azure/azure-sdk-for-go/pull/15103)
- Make Header constants private (https://github.com/Azure/azure-sdk-for-go/pull/15038)

### 0.19.0

- Split content out of `azcore` into various packages. The intent is to separate content based on its usage (common, uncommon, SDK authors). `azcore` has all core functionality. `log` contains facilities for configuring in-box logging. `policy` is used for configuring pipeline options and creating custom pipeline policies. `runtime` contains various helpers used by SDK authors and generated content. `streaming` has helpers for streaming IO operations
- `NewTelemetryPolicy()` now requires module and version parameters and the `Value` option has been removed. As a result, the `Request.Telemetry()` method has been removed
- The telemetry policy now includes the SDK prefix `azsdk-go-` so callers no longer need to provide it
- The `*http.Request` in `runtime.Request` is no longer anonymously embedded. Use the `Raw()` method to access it
- The `UserAgent` and `Version` constants have been made internal, `Module` and `Version` respectively

### 0.20.0

- Removed `azcore.Credential` and `.NewAnonymousCredential()` `NewRPRegistrationPolicy` now requires an `azcore.TokenCredential`
- `runtime.NewPipeline` has a new signature that simplifies implementing custom authentication
- `arm/runtime.RegistrationOptions` embeds `policy.ClientOptions`
- Contents in the `log` package have been slightly renamed
- Removed `AuthenticationOptions` in favor of `policy.BearerTokenOptions`
- Changed parameters for `NewBearerTokenPolicy()`
- Moved policy config options out of `arm/runtime` and into `arm/policy`

### 0.21.0

- Moved `[]policy.Policy` parameters of `arm/runtime.NewPipeline` and `runtime.NewPipeline` into a new struct, `runtime.PipelineOptions`
- Renamed `arm/ClientOptions.Host` to `.Endpoint`
- Moved `Request.SkipBodyDownload` method to function `runtime.SkipBodyDownload`
- `arm.NewPoller()` and `runtime.NewPoller()` no longer require an `eu` parameter
- `runtime.NewResponseError()` no longer requires an `error` parameter

### 0.22.0

- Moved `WithHTTPHeader` and `WithRetryOptions` from the `policy` package to the `runtime` package

### 0.23.0

- Removed the `Poller` type-alias to the internal poller implementation
- Added `Ptr[T any]` and `SliceOfPtrs[T any]` in the `to` package and removed all non-generic implementations
- `NullValue` and `IsNullValue` now take a generic type parameter instead of an interface func parameter
- Replaced `arm.Endpoint` with `cloud` API Removed the `endpoint` parameter from `NewRPRegistrationPolicy()` `arm/runtime.NewPipeline()` and `.NewRPRegistrationPolicy()` now return an `error`
- Refactored `NewPoller` and `NewPollerFromResumeToken` funcs in `arm/runtime` and `runtime` packages. Removed the `pollerID` parameter as it's no longer required. Created optional parameter structs and moved optional parameters into them
- Changed `FinalStateVia` field to a `const` type

### 1.0.0

- Renamed `cloud.Configuration.LoginEndpoint` to `.ActiveDirectoryAuthorityHost`
- Renamed `cloud.AzurePublicCloud` to `cloud.AzurePublic`
- Removed `AuxiliaryTenants` field from `arm/ClientOptions` and `arm/policy/BearerTokenOptions`
- `Poller[T].PollUntilDone()` now takes an `options *PollUntilDoneOptions` param instead of `freq time.Duration`
- Removed `arm/runtime.Poller[T]`, `arm/runtime.NewPoller[T]()` and `arm/runtime.NewPollerFromResumeToken[T]()`
- Removed `arm/runtime.FinalStateVia` and related `const` values
- Renamed `runtime.PageProcessor` to `runtime.PagingHandler`
- The `arm/runtime.ProviderRepsonse` and `arm/runtime.Provider` types are no longer exported
- Renamed `NewRequestIdPolicy()` to `NewRequestIDPolicy()`
- `TokenCredential.GetToken` now returns `AccessToken` by value
- Removed `AuthorizationCodeCredential`. Use `InteractiveBrowserCredential` instead to authenticate a user with the authorization code flow
- Instances of `AuthenticationFailedError` are now returned by pointer
- `GetToken()` returns `azcore.AccessToken` by value

### 1.3.0

- Renamed `NewOnBehalfOfCredentialFromCertificate` to `NewOnBehalfOfCredentialWithCertificate`
- Renamed `NewOnBehalfOfCredentialFromSecret` to `NewOnBehalfOfCredentialWithSecret`

### 1.5.0

- Removed `TokenRequestOptions.Claims` and `.TenantID`
- Removed ARM client support for CAE and cross-tenant auth
- Removed persistent token caching. It will return in v1.6.0-beta.1

### 1.6.0

- Removed `AzurePipelinesCredential` and the persistent token caching API. They will return in v1.7.0-beta.1

### 1.7.0

- The beta features for CAE, tracing, and fakes have been omitted for this release
- Removed the persistent token caching API. It will return in v1.8.0-beta.1

### 1.8.0

- The beta features for tracing and fakes have been omitted for this release

### 1.9.0

- The function `NewTokenCredential` has been removed from the `fake` package. Use a literal `&fake.TokenCredential{}` instead
- The field `TracingNamespace` in `runtime.PipelineOptions` has been replaced by `TracingOptions`

### 1.13.0

- Removed the `WorkloadIdentityCredential` support for identity binding mode added in v1.13.0-beta.1. It will return in v1.14.0-beta.1

### 1.14.0

- Removed `WorkloadIdentityCredentialOptions.EnableAzureProxy`. It will return in v1.15.0-beta.1

### 2.0.0

- Type of `GalleryProperties.ProvisioningState` has been changed from `*GalleryPropertiesProvisioningState` to `*GalleryProvisioningState`
- Type of `GalleryImageVersionProperties.ProvisioningState` has been changed from `*GalleryImageVersionPropertiesProvisioningState` to `*GalleryProvisioningState`
- Type of `GalleryImageProperties.ProvisioningState` has been changed from `*GalleryImagePropertiesProvisioningState` to `*GalleryProvisioningState`
- Type of `GalleryApplicationVersionProperties.ProvisioningState` has been changed from `*GalleryApplicationVersionPropertiesProvisioningState` to `*GalleryProvisioningState`
- Type of `VirtualMachineScaleSetIdentity.UserAssignedIdentities` has been changed from `map[string]*VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue` to `map[string]*UserAssignedIdentitiesValue`
- Const `GalleryImagePropertiesProvisioningStateFailed` has been removed
- Const `GalleryImagePropertiesProvisioningStateMigrating` has been removed
- Const `GalleryImageVersionPropertiesProvisioningStateCreating` has been removed
- Const `GalleryImageVersionPropertiesProvisioningStateMigrating` has been removed
- Const `GalleryApplicationVersionPropertiesProvisioningStateFailed` has been removed
- Const `GalleryPropertiesProvisioningStateMigrating` has been removed
- Const `GalleryApplicationVersionPropertiesProvisioningStateDeleting` has been removed
- Const `GalleryPropertiesProvisioningStateDeleting` has been removed
- Const `GalleryApplicationVersionPropertiesProvisioningStateCreating` has been removed
- Const `GalleryImageVersionPropertiesProvisioningStateSucceeded` has been removed
- Const `GalleryImagePropertiesProvisioningStateCreating` has been removed
- Const `GalleryImagePropertiesProvisioningStateUpdating` has been removed
- Const `GalleryImageVersionPropertiesProvisioningStateDeleting` has been removed
- Const `GalleryPropertiesProvisioningStateFailed` has been removed
- Const `SharingProfileGroupTypesCommunity` has been removed
- Const `GalleryApplicationVersionPropertiesProvisioningStateSucceeded` has been removed
- Const `GalleryApplicationVersionPropertiesProvisioningStateMigrating` has been removed
- Const `GalleryPropertiesProvisioningStateUpdating` has been removed
- Const `GalleryImageVersionPropertiesProvisioningStateFailed` has been removed
- Const `GalleryImagePropertiesProvisioningStateDeleting` has been removed
- Const `GalleryImageVersionPropertiesProvisioningStateUpdating` has been removed
- Const `GalleryPropertiesProvisioningStateCreating` has been removed
- Const `GalleryApplicationVersionPropertiesProvisioningStateUpdating` has been removed
- Const `GalleryImagePropertiesProvisioningStateSucceeded` has been removed
- Const `GalleryPropertiesProvisioningStateSucceeded` has been removed
- Function `PossibleGalleryPropertiesProvisioningStateValues` has been removed
- Function `PossibleGalleryImageVersionPropertiesProvisioningStateValues` has been removed
- Function `PossibleGalleryImagePropertiesProvisioningStateValues` has been removed
- Function `PossibleGalleryApplicationVersionPropertiesProvisioningStateValues` has been removed
- Struct `VirtualMachineScaleSetIdentityUserAssignedIdentitiesValue` has been removed
- Const `DdosCustomPolicyProtocolSyn` has been removed
- Const `DdosCustomPolicyTriggerSensitivityOverrideHigh` has been removed
- Const `DdosSettingsProtectionCoverageBasic` has been removed
- Const `DdosCustomPolicyProtocolUDP` has been removed
- Const `DdosCustomPolicyProtocolTCP` has been removed
- Const `DdosCustomPolicyTriggerSensitivityOverrideLow` has been removed
- Const `DdosCustomPolicyTriggerSensitivityOverrideDefault` has been removed
- Const `DdosSettingsProtectionCoverageStandard` has been removed
- Const `DdosCustomPolicyTriggerSensitivityOverrideRelaxed` has been removed
- Type alias `DdosSettingsProtectionCoverage` has been removed
- Type alias `DdosCustomPolicyTriggerSensitivityOverride` has been removed
- Type alias `DdosCustomPolicyProtocol` has been removed
- Function `PossibleDdosCustomPolicyProtocolValues` has been removed
- Function `PossibleDdosSettingsProtectionCoverageValues` has been removed
- Function `PossibleDdosCustomPolicyTriggerSensitivityOverrideValues` has been removed
- Struct `ProtocolCustomSettingsFormat` has been removed
- Field `PublicIPAddresses` of struct `DdosCustomPolicyPropertiesFormat` has been removed
- Field `ProtocolCustomSettings` of struct `DdosCustomPolicyPropertiesFormat` has been removed
- Field `DdosCustomPolicy` of struct `DdosSettings` has been removed
- Field `ProtectedIP` of struct `DdosSettings` has been removed
- Field `ProtectionCoverage` of struct `DdosSettings` has been removed

### 3.0.0

- Function `*CloudServicesClient.BeginCreateOrUpdate` parameter(s) have been changed from `(context.Context, string, string, *CloudServicesClientBeginCreateOrUpdateOptions)` to `(context.Context, string, string, CloudService, *CloudServicesClientBeginCreateOrUpdateOptions)`
- Function `*CloudServicesClient.BeginUpdate` parameter(s) have been changed from `(context.Context, string, string, *CloudServicesClientBeginUpdateOptions)` to `(context.Context, string, string, CloudServiceUpdate, *CloudServicesClientBeginUpdateOptions)`
- Function `*CloudServicesUpdateDomainClient.BeginWalkUpdateDomain` parameter(s) have been changed from `(context.Context, string, string, int32, *CloudServicesUpdateDomainClientBeginWalkUpdateDomainOptions)` to `(context.Context, string, string, int32, UpdateDomain, *CloudServicesUpdateDomainClientBeginWalkUpdateDomainOptions)`
- Type of `CloudServiceExtensionProperties.Settings` has been changed from `*string` to `interface{}`
- Type of `CloudServiceExtensionProperties.ProtectedSettings` has been changed from `*string` to `interface{}`
- Field `Parameters` of struct `CloudServicesClientBeginUpdateOptions` has been removed
- Field `Parameters` of struct `CloudServicesClientBeginCreateOrUpdateOptions` has been removed
- Field `Parameters` of struct `CloudServicesUpdateDomainClientBeginWalkUpdateDomainOptions` has been removed
- Type of `EffectiveRouteMapRoute.Prefix` has been changed from `[]*string` to `*string`
- `LoadBalancerBackendAddressAdminStateDrain` from enum `LoadBalancerBackendAddressAdminState` has been removed
- Field `PeerRouteList` of struct `VirtualHubBgpConnectionsClientListAdvertisedRoutesResponse` has been removed
- Field `PeerRouteList` of struct `VirtualHubBgpConnectionsClientListLearnedRoutesResponse` has been removed

### 4.0.0

- Type of `GalleryImageVersionStorageProfile.Source` has been changed from `*GalleryArtifactVersionSource` to `*GalleryArtifactVersionFullSource`
- Type of `SharingProfile.CommunityGalleryInfo` has been changed from `interface{}` to `*CommunityGalleryInfo`
- Type of `VirtualMachineExtensionUpdateProperties.ProtectedSettingsFromKeyVault` has been changed from `interface{}` to `*KeyVaultSecretReference`
- Type of `GalleryOSDiskImage.Source` has been changed from `*GalleryArtifactVersionSource` to `*GalleryDiskImageSource`
- Type of `GalleryDiskImage.Source` has been changed from `*GalleryArtifactVersionSource` to `*GalleryDiskImageSource`
- Type of `GalleryDataDiskImage.Source` has been changed from `*GalleryArtifactVersionSource` to `*GalleryDiskImageSource`
- Type of `VirtualMachineScaleSetExtensionProperties.ProtectedSettingsFromKeyVault` has been changed from `interface{}` to `*KeyVaultSecretReference`
- Type of `VirtualMachineExtensionProperties.ProtectedSettingsFromKeyVault` has been changed from `interface{}` to `*KeyVaultSecretReference`
- Field `URI` of struct `GalleryArtifactVersionSource` has been removed
- `ApplicationGatewayCustomErrorStatusCodeHTTPStatus499` from enum `ApplicationGatewayCustomErrorStatusCode` has been removed

### 5.0.0

- Type of `CommunityGalleryImageProperties.Identifier` has been changed from `*GalleryImageIdentifier` to `*CommunityGalleryImageIdentifier`
- Type of `GalleryTargetExtendedLocation.StorageAccountType` has been changed from `*StorageAccountType` to `*EdgeZoneStorageAccountType`
- Type of `RestorePointSourceVMDataDisk.DiskRestorePoint` has been changed from `*APIEntityReference` to `*DiskRestorePointAttributes`
- Type of `RestorePointSourceVMOSDisk.DiskRestorePoint` has been changed from `*APIEntityReference` to `*DiskRestorePointAttributes`
- `StorageAccountTypeStandardSSDLRS` from enum `StorageAccountType` has been removed
- Field `ID` of struct `VirtualMachineScaleSetIPConfiguration` has been removed
- Field `ID` of struct `VirtualMachineScaleSetNetworkConfiguration` has been removed
- Field `ID` of struct `VirtualMachineScaleSetUpdateIPConfiguration` has been removed
- Field `ID` of struct `VirtualMachineScaleSetUpdateNetworkConfiguration` has been removed
- Type of `VirtualApplianceConnectionProperties.RoutingConfiguration` has been changed from `*RoutingConfigurationNfv` to `*RoutingConfiguration`
- Struct `PropagatedRouteTableNfv` has been removed
- Struct `RoutingConfigurationNfv` has been removed
- Struct `RoutingConfigurationNfvSubResource` has been removed

### 6.0.0

- Type of `SecurityPostureReference.ExcludeExtensions` has been changed from `[]*VirtualMachineExtension` to `[]*string`
- Struct `FirewallPacketCaptureParametersFormat` has been removed
- Field `ID`, `Properties` of struct `FirewallPacketCaptureParameters` has been removed

### 7.0.0

- Type of `OperationValue.Display` has been changed from `*OperationValueDisplay` to `*OperationDisplay`
- Type of `OperationValue.Origin` has been changed from `*string` to `*Origin`
- Enum `AvailabilitySetSKUTypes` has been removed
- Operation `*VirtualMachineImagesClient.NewListWithPropertiesPager` does not support pagination anymore, use `*VirtualMachineImagesClient.ListWithProperties` instead
- Struct `DiskImageEncryption` has been removed
- Struct `GalleryArtifactPublishingProfileBase` has been removed
- Struct `GalleryArtifactSafetyProfileBase` has been removed
- Struct `GalleryArtifactSource` has been removed
- Struct `GalleryArtifactVersionSource` has been removed
- Struct `GalleryResourceProfilePropertiesBase` has been removed
- Struct `GalleryResourceProfileVersionPropertiesBase` has been removed
- Struct `LatestGalleryImageVersion` has been removed
- Struct `LogAnalyticsInputBase` has been removed
- Struct `OperationValueDisplay` has been removed
- Struct `PirCommunityGalleryResource` has been removed
- Struct `PirSharedGalleryResource` has been removed
- Struct `ResourceWithOptionalLocation` has been removed
- Struct `SharedGalleryDiskImage` has been removed
- Struct `UpdateResourceDefinition` has been removed
- Struct `VirtualMachineImagesWithPropertiesListResult` has been removed
- Type of `LoadBalancerHealthPerRulePerBackendAddress.NetworkInterfaceIPConfigurationID` has been changed from `*InterfaceIPConfiguration` to `*string`
- Function `*ConnectionMonitorsClient.BeginQuery` has been removed
- Function `*ConnectionMonitorsClient.BeginStart` has been removed

### 8.0.0

- All Cloud Services (classic) related types, clients, and functions have been removed due to the [Azure Cloud Services (classic) retirement](https://azure.microsoft.com/updates?id=486344)
- `ApplicationGatewayWafRuleSensitivityTypesNone` from enum `ApplicationGatewayWafRuleSensitivityTypes` has been removed
- `SensitivityTypeNone` from enum `SensitivityType` has been removed

### 9.0.0

- `FirewallPolicyIntrusionDetectionProfileTypeAdvanced`, `FirewallPolicyIntrusionDetectionProfileTypeBasic`, `FirewallPolicyIntrusionDetectionProfileTypeStandard` from enum `FirewallPolicyIntrusionDetectionProfileType` has been removed


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

- Upstream releases of `cilium/cilium`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cilium.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
