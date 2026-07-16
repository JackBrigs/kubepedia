---
id: VARIABLE-CONTAINERD_GRPC_MAX_SEND_MESSAGE_SIZE
type: variable
title: containerd_grpc_max_send_message_size
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd_grpc_max_send_message_size
tags:
  - containerd
  - grpc
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "Max gRPC send message size for containerd; default 16777216 (16 MiB)"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
---

# containerd_grpc_max_send_message_size

## Summary
Sets the maximum gRPC send message size (in bytes) for the containerd gRPC server. Default is `16777216` (16 MiB).

## Implementation
Defined in `roles/container-engine/containerd/defaults/main.yml`:

```yaml
containerd_grpc_max_send_message_size: 16777216
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related: `containerd_grpc_max_recv_message_size`.

## References
- roles/container-engine/containerd/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
