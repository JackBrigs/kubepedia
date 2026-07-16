---
id: PRACTICE-REGISTRY
type: best_practice
title: Private Docker registry addon in a Kubespray/Kubernetes cluster
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - Private registry
tags:
  - registry
  - docker
sources:
  - type: docs
    path: docs/advanced/registry.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/registry.md
    note: "Optional in-cluster private Docker registry addon with per-node localhost proxy"
relations: []
---

# Private Docker registry addon in a Kubespray/Kubernetes cluster

## Summary
Describes an optional in-cluster private Docker registry for storing truly private images. The registry runs as a Pod; because it has no SSL or authentication (triggering Docker's "insecure registry" logic), a per-node proxy daemonset exposes it via `hostPort` on `localhost:5000`, which Docker treats as secure. Pods then reference images as `localhost:5000/user/container`.

## Context
Applies when you want a private image store inside the cluster. Components: a PersistentVolume/PersistentVolumeClaim for storage, a ReplicationController running `registry:2`, a Service exposing port 5000, and a DaemonSet (`kube-registry-proxy`) mapping node `localhost:5000` to the registry Service. Storage must be provisioned independently (Kubernetes does not create the underlying disk). For multiple replicas the CSI driver must support `ReadWriteMany`; for throwaway/no-storage use, swap the PVC for an `emptyDir` volume.

## Implementation
### Storage
- Create a `PersistentVolume` (e.g. gcePersistentDisk, or NFS by swapping the volume block) sized to your registry disk; the underlying storage must exist beforehand.
- Bind it with a `PersistentVolumeClaim` named `kube-registry-pvc` in namespace `kube-system` (`ReadWriteOnce`).

### Registry pod
- Run a `ReplicationController` `kube-registry-v0` (namespace `kube-system`, label `k8s-app: registry`) using image `registry:2`.
- Env: `REGISTRY_HTTP_ADDR=:5000`, `REGISTRY_STORAGE_FILESYSTEM_ROOTDIRECTORY=/var/lib/registry`; mount the PVC at `/var/lib/registry`; container port 5000.

### Service
- Expose a `Service` `kube-registry` (namespace `kube-system`, selector `k8s-app: registry`) on port 5000/TCP.

### Per-node proxy
- Deploy a `DaemonSet` `kube-registry-proxy` using `gcr.io/google_containers/kube-registry-proxy:0.4`.
- Env: `REGISTRY_HOST=kube-registry.kube-system.svc.cluster.local`, `REGISTRY_PORT="5000"`; containerPort 80 mapped to `hostPort: 5000`.
- This directs `localhost:5000` on each node to the registry Service.
- Caveat: keep identifiers unique across the rc/svc pair and the daemonset; non-unique identifiers cause the localhost proxy daemonsets to register with the upstream service and try to proxy themselves, which fails.
- Verify with `curl localhost:5000` — a `404 page not found` indicates it is running.

### Using the registry
- Reference images as `image: localhost:5000/user/container`.
- To push images: build/push directly on a node as `localhost:5000/...`, or from a local machine set up `kubectl port-forward --namespace kube-system $POD 5000:5000` (find a Running registry pod via label `k8s-app=registry`) and push to `localhost:5000/yourname/container`.

### Caveats
- No SSL and no authentication — treated as an insecure registry, worked around only via the localhost proxy.
- Some cluster installs (e.g. GCE) can enable it at cluster birth via `ENABLE_CLUSTER_REGISTRY` / `KUBE_ENABLE_CLUSTER_REGISTRY=true`; otherwise apply the manifests above.

## References
- docs/advanced/registry.md (tag v2.31.0 1c9add4)
