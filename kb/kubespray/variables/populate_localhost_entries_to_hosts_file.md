---
id: VARIABLE-POPULATE_LOCALHOST_ENTRIES_TO_HOSTS_FILE
type: variable
title: populate_localhost_entries_to_hosts_file
status: active
kubespray_version: ">=v2.27.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - populate_localhost_entries_to_hosts_file
tags:
  - kubernetes
  - preinstall
  - variable
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/kubernetes/preinstall/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# populate_localhost_entries_to_hosts_file

## Summary

Kubespray variable `populate_localhost_entries_to_hosts_file` — default `true`. Defined in `roles/kubernetes/preinstall/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.28.1` of the indexed range. **Removed after `v2.28.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/preinstall/defaults/main.yml` (Kubespray `v2.28.1`):

```yaml
populate_localhost_entries_to_hosts_file: true
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.28.1`. **Removed after `v2.28.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/preinstall/defaults/main.yml` (Kubespray `v2.28.1`).
