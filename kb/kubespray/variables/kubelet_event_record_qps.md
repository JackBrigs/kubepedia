---
id: VARIABLE-KUBELET_EVENT_RECORD_QPS
type: variable
title: kubelet_event_record_qps
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_event_record_qps
tags:
  - kubelet
  - events
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kubelet eventRecordQPS; default 50"
relations: []
---

# kubelet_event_record_qps

## Summary
Sets the kubelet `eventRecordQPS`, the maximum QPS at which the kubelet creates events. Default is `50`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_event_record_qps: 50
```

The default (`50`) is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 748 in v2.29.0/v2.29.1, 751 in v2.30.0, 770 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Maps to the kubelet configuration field `eventRecordQPS`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
