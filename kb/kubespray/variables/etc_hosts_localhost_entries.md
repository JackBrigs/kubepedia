---
id: VARIABLE-ETC_HOSTS_LOCALHOST_ENTRIES
type: variable
title: etc_hosts_localhost_entries
status: active
kubespray_version: ">=v2.27.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - etc_hosts_localhost_entries
tags:
  - kubernetes
  - preinstall
  - variable
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/kubernetes/preinstall/defaults/main.yml
    note: "default: (structured / block value — see source)"
relations: []
---
<!-- generated: variable-stub -->

# etc_hosts_localhost_entries

## Summary

Kubespray variable `etc_hosts_localhost_entries` — default `(structured / block value — see source)`. Defined in `roles/kubernetes/preinstall/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.28.1` of the indexed range. **Removed after `v2.28.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/preinstall/defaults/main.yml` (Kubespray `v2.28.1`):

```yaml
etc_hosts_localhost_entries: (structured / block value — see source)
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.28.1`. **Removed after `v2.28.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/preinstall/defaults/main.yml` (Kubespray `v2.28.1`).
