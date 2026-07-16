---
id: CONFIG-APISERVER_AUTHENTICATION_CONFIG
type: configuration
title: "API server structured authentication config (new in Kubespray v2.31.0)"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - AuthenticationConfiguration
  - structured authentication configuration
  - kube_apiserver_use_authentication_config_file
  - apiserver jwt oidc config file
  - kube_apiserver_authentication_config_jwt
  - anonymous authentication config
tags:
  - kubernetes
  - apiserver
  - authentication
  - configuration
  - oidc
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "530-537"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_use_authentication_config_file + _api_version/_anonymous/_jwt (added in v2.31.0)"
  - type: code
    path: roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    note: "renders the AuthenticationConfiguration wiring (tag v2.31.0)"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-K8S_1_34_CHANGES
---

# API server structured authentication config (new in Kubespray v2.31.0)

## Summary

Kubespray `v2.31.0` **adds** support for the Kubernetes **structured
AuthenticationConfiguration** file — configuring JWT/OIDC issuers and anonymous access
through a config object instead of the legacy `--oidc-*` / `--anonymous-auth` apiserver
flags. It is **off by default** (`kube_apiserver_use_authentication_config_file: false`);
turning it on lets you declare **multiple** JWT authenticators and fine-grained anonymous
rules. This capability did not exist in `v2.29.0`–`v2.30.0`.

## Configuration

Variables (defaults from `roles/kubespray_defaults/defaults/main/main.yml`, tag
`v2.31.0`):

| Variable | Default | Purpose |
|----------|---------|---------|
| `kube_apiserver_use_authentication_config_file` | `false` | master switch — emit and use an AuthenticationConfiguration file |
| `kube_apiserver_authentication_config_api_version` | `v1beta1` if `kube_version < 1.34`, else `v1` | API version of the config object (version-aware) |
| `kube_apiserver_authentication_config_anonymous` | *(unset)* | structured anonymous-authentication config (conditions/paths) |
| `kube_apiserver_authentication_config_jwt` | `[]` | list of JWT/OIDC authenticators (issuer, audiences, claim mappings/validations) |

- Enabling it makes Kubespray render an `AuthenticationConfiguration` and point the
  apiserver at it (wired through the kubeadm config template).
- **`kube_apiserver_authentication_config_jwt`** is a list — you can define **several**
  issuers (a key advantage over the single-issuer `--oidc-*` flags): each entry has
  `issuer` (url, audiences), `claimMappings` (username/groups), and optional
  `claimValidationRules`.
- **`kube_apiserver_authentication_config_anonymous`** expresses anonymous access as
  structured config (e.g. allow only specific endpoints), replacing the blunt
  `--anonymous-auth` toggle.

## Compatibility

- **New in Kubespray `v2.31.0`** — not present in `v2.29.0`–`v2.30.0`. On those older
  tags use the apiserver `--oidc-*` flags via `kube_apiserver_extra_args` instead.
- **Config API version is version-aware:** `v1beta1` for Kubernetes `< 1.34`, `v1` for
  `>= 1.34` (the field graduated to `v1` in 1.34). Kubespray picks the right one from
  `kube_version`, so don't hard-code it.
- Structured auth config and the legacy `--oidc-*` flags are mutually exclusive on the
  apiserver — pick one. Migrating from flags to the config file is the upstream-preferred
  direction.
- Because it changes apiserver auth, roll it out carefully (a bad JWT config can lock out
  clients) and keep a working admin kubeconfig outside the affected issuer.

## References

- `main.yml:530-537` (auth-config variables) and the kubeadm config template at tag
  `v2.31.0`. kubeadm config API: [[CONFIG-KUBEADM_CONFIG_API_VERSION]]; version window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
