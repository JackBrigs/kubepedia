# KEDB · storage

_20 известных ошибок. Сгенерировано; не править руками._

### KEDB-038 · ceph-csi-cephfs: PVC Pending / mount fails — clusterID mismatch, secret, MDS, subvolumegroup
- **Симптом:** A CephFS PVC stays `Pending` (no volume provisioned), or the pod fails to mount with `MountVolume.MountDevice failed`, `no mds server is up` / `clusterID <x> not found`, or `subvolumegroup ... does not exist`
- **Затронутые CIs:** storage, ceph, csi  ·  _>=1.29 <=1.32 / >=3.13.0 <=3.14.2_
- **Root cause:** ceph-csi-cephfs `3.13.0`/`3.14.2` ; requires Ceph Pacific (≥16.2.0) with a healthy MDS. It's a CSI external provisioner · **clusterID** in the StorageClass must match the `clusterID` → `monitors` entry in the ceph-csi **ConfigMap** (`ceph-csi-config`). A copy-pasted SC with the wrong/blank clusterID is the #1 cause · The provisioner/node plugins authenticate with the **csi-cephfs-secret** (`adminID`/`adminKey`, or `u…
- **Workaround / fix:** **clusterID mismatch — fix:** align the StorageClass `clusterID` with the `ceph-csi-config` ConfigMap entry; the value is the Ceph **fsid** (`ceph fsid`), not an arbitrary name · **auth — fix:** recreate `csi-cephfs-secret` with a valid `adminID`/`adminKey` (a cephx user with the right caps on the fs/pool); rotated keys must be updated in the secret · **subvolumegroup — fix:** create it (`ceph fs subvolumegroup creat…
- **Источник:** `kb/troubleshooting/ceph-csi-cephfs-mount.md`

### KEDB-039 · Consul server Raft quorum lost (leave_on_terminate, scale-down, PVC loss) — etcd-class outage
- **Симптом:** `No cluster leader` in server logs; all `<release>-server-*` pods `NotReady`; the `-server` Service has no endpoints · Manually scaling the server StatefulSet down (e.g. 5→3) unexpectedly reduces fault tolerance / loses data · After deleting server PVCs: Consul comes up empty (Raft data gone) → forces ACL re-bootstrap
- **Затронутые CIs:** consul, raft, storage  ·  _>=1.29 <=1.35 / >=1.22.7 <=2.0.2_
- **Root cause:** Applies to consul-k8s **1.9.x–2.0.x** · **`leave_on_terminate: true` (hardcoded, `server-config-configmap.yaml`@v2.0.2 L69):** a server that stops gracefully *leaves* the pool. So scaling down N→M shrinks quorum to match M — "before this change the quorum would have remained at 3" (changelog). Losing more nodes than the new quorum tolerates = data loss · **Autopilot guards:** the chart sets `autopilot.min_quorum` (fr…
- **Workaround / fix:** **Fix (fault tolerance):** run **3 or 5** server replicas (never 1 in prod); keep the PDB enabled and set `autopilotMinQuorum` appropriately · **Fix (safe scale/rollout):** understand `leave_on_terminate` — do not scale the StatefulSet down casually; use `server.updatePartition` to gate rollouts. Recover a lost-quorum cluster like etcd: from a snapshot / `consul operator raft` peer recovery · **Fix (storage):** size …
- **Источник:** `kb/components/consul/consul-server-quorum.md`

### KEDB-040 · containerd: overlayfs snapshotter fails to mount
- **Симптом:** Startup/error: `failed to mount overlay: operation not permitted` / `invalid argument`; images won't unpack; pods stuck
- **Затронутые CIs:** containerd, storage, snapshotter  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to containerd on Kubernetes **1.29–1.35** ; also common on K3s/nested/WSL2 setups
- **Workaround / fix:** `native` snapshotter uses far more disk/IO (full copy per layer) — a fallback, not a default
- **Источник:** `kb/troubleshooting/containerd-overlayfs.md`

### KEDB-041 · Draining/removing a node with node-local PVCs (local-path) strands the workload and loses data
- **Симптом:** After `kubectl drain <node>` (or a node-maintenance / remove-node run), a pod (often a DB / stateful single-replica) is stuck `Pending` with `node(s) had volume node affinity conflict` / `waiting for a volume to be created` · The service stays down as long as the node is cordoned, and never recovers if the node is removed · After removing the node, the PVC's data is gone (it lived on that node's disk)
- **Затронутые CIs:** storage, local-path, node  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across the Kubespray range (**v2.27.0–v2.31.0**); local-path-provisioner is a managed addon ; local-volume-provisioner is the same class · **Why it strands:** local-path uses `volumeBindingMode: WaitForFirstConsumer` and creates the PV on the node where the first consumer landed; the PV's `nodeAffinity` then binds the pod to that node forever. Draining removes the pod but the scheduler can't place it elsewher…
- **Workaround / fix:** **Fix (migrate first):** for each node-local PVC on the target node, **migrate the data before draining** — back up the volume, recreate the workload's PVC on a **different node / a networked (CSI) storage class**, restore the data, and only then drain/remove the node. For a StatefulSet, move/reschedule the replica onto surviving storage first · **Fix (accept the trade-off):** if the data is disposable (cache, scratc…
- **Источник:** `kb/troubleshooting/node-local-pvc-drain.md`

### KEDB-042 · external-snapshotter 7→8: one class per driver, webhook removed
- **Симптом:** Snapshots fail or are ambiguous after upgrade because there are multiple default VolumeSnapshotClasses for one driver · Objects that previously passed now fail CRD validation · The snapshot validation webhook stops mattering / is gone
- **Затронутые CIs:** storage, csi, snapshots, upgrade  ·  _>=8.0.0 <=8.6.0_
- **Root cause:** Applies to external-snapshotter **8.0.0–8.6.0** (base: 7.0.2 / addon 6.3.0 — , )
- **Workaround / fix:** Coordinate with backup tools that depend on snapshots (Velero, VolSync) — validate their VolumeSnapshotClass references after the upgrade
- **Источник:** `kb/troubleshooting/snapshot-controller-7-to-8.md`

### KEDB-043 · gitRepo volume no longer works — driver disabled by default (K8s 1.33)
- **Симптом:** After upgrading to Kubespray v2.31.0 (K8s 1.33+), pods with a `spec.volumes[].gitRepo` **fail to start** / the volume is rejected · Legacy manifests or charts that used `gitRepo` to seed content no longer work
- **Затронутые CIs:** kubernetes, storage, security  ·  _>=v2.31.0 <=v2.31.0 / >=1.33 <=1.35_
- **Root cause:** Milestone (`keps/sig-storage/5040-...` kep.yaml): `GitRepoVolumeDriver` gate **off by default 1.33** (removal path). It was deprecated long ago; the driver could execute Git hooks with the kubelet's privileges — a real attack surface · Applies at **K8s 1.33+** → Kubespray **v2.31.0**; earlier tags (≤1.32) still allow it
- **Workaround / fix:** **Fix (correct):** replace the `gitRepo` volume with an **init container** that runs `git clone` into an `emptyDir` shared with the main container — this is the documented, safe replacement · **Temporary bridge:** the `GitRepoVolumeDriver` feature gate can be re-enabled to buy migration time , but it is on the removal track — do not treat re-enabling as a durable fix · **Pre-upgrade audit:** grep for `gitRepo` volume…
- **Источник:** `kb/troubleshooting/gitrepo-volume-removed.md`

### KEDB-044 · Kubespray registry addon (2.8.1): image loss, no auth/TLS, can't scale
- **Симптом:** Pushed images **disappear** after the registry pod restarts/reschedules · Anyone can push/pull (no credentials); or pushes fail because the client expects TLS · Scaling `registry_replica_count > 1` leaves replicas `ContainerCreating` (Multi-Attach)
- **Затронутые CIs:** registry, storage, kubespray  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35 / 2.8.1_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** (mechanism identical back to v2.27.0). Registry version **2.8.1** — constant across all tags. This is the **Kubespray-managed addon**, not a registry you upgrade to v3 ( is that separate case)
- **Workaround / fix:** This addon is a **simple single-node registry**, not production-grade/HA — for real workloads use an external registry (Harbor, cloud registry, or distribution 2.8.1 with S3/GCS storage via `registry_config.storage`) · With `emptyDir`, even a node drain / rolling update loses all cached images — always set a storage class in any environment where the registry holds anything you can't re-push
- **Источник:** `kb/troubleshooting/registry-addon.md`

### KEDB-045 · Multi-Attach error / RWO volume stuck attached after node loss
- **Симптом:** `Warning FailedAttachVolume Multi-Attach error for volume "pvc-…": Volume is already exclusively attached to one node and can't be attached to another` · Pod stuck `ContainerCreating` for minutes after a node loss
- **Затронутые CIs:** controller-manager, storage, csi  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (the remedy is GA since 1.28). Companion:
- **Workaround / fix:** Pair this with node deletion / eviction handling ; a half-recovered node can re-attach. Genuine CSI attach limits are a different Pending cause
- **Источник:** `kb/troubleshooting/kcm-volume-multiattach.md`

### KEDB-046 · Node drain gotchas — PDB hangs it, emptyDir data lost, bare pods force-deleted
- **Симптом:** `kubectl drain` (or the Kubespray upgrade) **stalls**: `Cannot evict pod as it would violate the pod's disruption budget` / `error when evicting pods ... still waiting` · A pod's **emptyDir** data (cache, scratch, a mis-configured DB) is **gone** after drain · **Bare pods** (created without a Deployment/StatefulSet/DaemonSet) **vanish** after `--force` and never come back · A single-replica service is **down** during…
- **Затронутые CIs:** node, drain, storage  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0** and any `kubectl drain`. Kubespray's graceful upgrade drains via the eviction API with `drain_grace_period`, `drain_timeout` (default `360s`), `drain_retries` · **PDB hang:** eviction respects **PodDisruptionBudgets**. A PDB with `maxUnavailable: 0`, or `minAvailable` equal to the replica count, or a **single-replica** workload with any PDB, means the API server **refuses every evic…
- **Workaround / fix:** **PDB hang — fix:** ensure enough replicas/headroom so one can move, or **temporarily relax** the PDB (raise `maxUnavailable` / lower `minAvailable`) for the maintenance window; don't `--force` blindly (that bypasses the PDB and can violate real availability guarantees) · **emptyDir — fix:** confirm the emptyDir data is disposable before `--delete-emptydir-data`; if it isn't, it shouldn't be on emptyDir — back it up …
- **Источник:** `kb/troubleshooting/node-drain-gotchas.md`

### KEDB-047 · Pod can't mount volume (FailedMount — ConfigMap/Secret/PVC)
- **Симптом:** Pod is stuck `ContainerCreating`; `kubectl describe pod` shows `FailedMount` / `Unable to attach or mount volumes` / `MountVolume.SetUp failed for volume …` with a specific reason
- **Затронутые CIs:** storage, volumes, pods  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · A volume source must exist **in the pod's own namespace** (ConfigMaps/Secrets are namespaced); PVC-backed volumes additionally need a bound PV and a working CSI attach/mount
- **Workaround / fix:** **`configmap/secret "X" not found`** — create it, fix the name, or move the pod/object to the same namespace. A pod referencing a not-yet-created ConfigMap waits indefinitely · **Missing key / subPath** — the ConfigMap/Secret exists but lacks the `key` the volume mounts (`items`/`subPath`); add the key · **PVC not bound** — no provisioner/StorageClass or the pool is exhausted · **`volume node affinity conflict`** — t…
- **Источник:** `kb/troubleshooting/failed-mount.md`

### KEDB-048 · PVC stuck Pending — no provisioner / no default StorageClass
- **Симптом:** `kubectl get pvc` shows `Pending`; the Pod using it stays `Pending` (`pod has unbound immediate PersistentVolumeClaims`). `kubectl describe pvc` shows `no persistent volumes available for this claim and no storage class is set`, or a provisioning error
- **Затронутые CIs:** storage, csi, pvc  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. All storage add-ons are **off by default**: `local_path_provisioner_enabled: false`, `local_volume_provisioner_enabled: false`, and every `*_csi_enabled` flag false · A PVC with **no `storageClassName`** binds only if a **default** StorageClass exists; a PVC naming a class binds only if that class + its provisioner exist
- **Workaround / fix:** **Simplest on bare metal — local-path-provisioner:** set `local_path_provisioner_enabled: true`. It creates the `local-path` StorageClass and, with `local_path_provisioner_is_default_storageclass: "true"` (the default), marks it **default** — so class-less PVCs start binding. Storage is node-local hostPath under `local_path_provisioner_claim_root` (`/opt/local-path-provisioner/`) · **Real cloud/SAN storage — a CSI dr…
- **Источник:** `kb/troubleshooting/pvc-pending-no-storageclass.md`

### KEDB-049 · PVC stuck Pending: no provisioner / no matching PV
- **Симптом:** `kubectl get pvc` shows `Pending`; the pod is `Pending`/`ContainerCreating` · Events: `no persistent volumes available for this claim and no storage class is set`, or `waiting for a volume to be created`
- **Затронутые CIs:** storage, csi, pvc  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to any CSI/storage backend (Rook-Ceph , lvm-localpv , cloud CSI). Diagnosis is generic
- **Workaround / fix:** Snapshot-restore PVCs additionally need a working snapshot-controller + `VolumeSnapshotClass`
- **Источник:** `kb/troubleshooting/pvc-pending-no-provisioner.md`

### KEDB-050 · PVC volume expansion doesn't take effect — allowVolumeExpansion, FileSystemResizePending, can't shrink
- **Симптом:** Editing the PVC size is **rejected**: `persistentvolumeclaims "x" is forbidden: only dynamically provisioned pvc ... field can be expanded` / `...forbidden ... allowVolumeExpansion` · The PVC `capacity` updated but the **app/`df` still shows the old size** — the filesystem wasn't grown · Trying to **lower** the size is rejected outright
- **Затронутые CIs:** storage, pvc, expansion  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0** and any CSI/in-tree class that supports expansion · **`allowVolumeExpansion`:** a per-StorageClass boolean, **default false**. If it isn't `true`, the API server refuses to increase the PVC request. Not every driver/class supports it · **Two-phase resize:** expansion is (1) grow the backing volume/device, then (2) grow the filesystem. Many CSI drivers do (1) online but **defer (2) t…
- **Workaround / fix:** **Rejected edit — fix:** ensure the StorageClass has `allowVolumeExpansion: true` (edit the class or move the PVC to one that supports it); it can't be enabled retroactively on a class that doesn't support the operation in the driver · **New space not visible — fix:** if the PVC shows `FileSystemResizePending`, **restart / recreate the consuming pod** (for a StatefulSet, delete the pod so it's recreated) to complete …
- **Источник:** `kb/troubleshooting/pvc-volume-expansion.md`

### KEDB-051 · PVC/PV deletion gotchas — stuck Terminating (finalizers), reclaim-policy data loss / orphaned Released PV
- **Симптом:** `kubectl delete pvc/pv` hangs in **`Terminating`** and never completes · After deleting a PVC, the **data is gone** (reclaimPolicy `Delete`) · A `Retain` PV sits in **`Released`** and a new (even identical) PVC **stays `Pending`** — it won't bind to the released PV
- **Затронутые CIs:** storage, pvc, lifecycle  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0** and any CSI/storage class · **Finalizers (stuck Terminating):** `kubernetes.io/pvc-protection` keeps a PVC from deleting **while a pod still references it**; `kubernetes.io/pv-protection` keeps a PV while a PVC is bound. The object shows `Terminating` until the consumer is removed. Force-removing the finalizer deletes the API object but can **leave the backing volume + data orphaned…
- **Workaround / fix:** **Stuck Terminating — fix:** delete/evict the **consuming pod** (or the workload) first; the finalizer clears and the PVC/PV deletes cleanly. **Do not** blindly `kubectl patch ... finalizers=null` — that deletes the object while leaving the real volume/data orphaned in the backend · **`Delete` data loss — prevent:** for data you must keep, use a StorageClass with **`reclaimPolicy: Retain`** (and/or a `Retain` Statefu…
- **Источник:** `kb/troubleshooting/pvc-pv-deletion-gotchas.md`

### KEDB-052 · rook-ceph-cluster helm upgrade fails: StorageClass is immutable
- **Симптом:** `helm upgrade` errors: cannot patch StorageClass — field is immutable · After upgrade, RBD/CephFS provisioning breaks with CSI-operator conversion errors · `CephCluster` creation rejected on a bad CRUSH/topology hierarchy
- **Затронутые CIs:** rook, ceph, storage, upgrade  ·  _>=1.18.0 <=1.20.2_
- **Root cause:** Applies to Rook **1.18.0–1.20.2** (owner runs 1.18.9 — ). v1.18 raised the K8s minimum to **1.29**
- **Workaround / fix:** **Ceph v20.2.0 (Tentacle) has a data-corruption bug when "read affinity" is enabled** — wait for v20.2.1. Cluster is also exposed to **Ceph CVE-2025-52555** if running an affected Ceph patch (18.2.1–18.2.4 / 19.0.0–19.2.2; fixed 18.2.5 / 19.2.3)
- **Источник:** `kb/troubleshooting/rook-ceph-upgrade-sc-immutable.md`

### KEDB-053 · Rook-Ceph: HEALTH_WARN / OSD down / PGs degraded
- **Симптом:** `CephCluster` shows a non-`HEALTH_OK` phase; volumes slow or read-only · An OSD pod is `CrashLoopBackOff` or the OSD is `down`/`out` · PGs stuck `degraded`, `undersized`, or `inactive`
- **Затронутые CIs:** rook, ceph, storage  ·  _>=1.18.0 <=1.20.2_
- **Root cause:** Applies to Rook **1.18–1.20** (owner runs 1.18.9 — )
- **Workaround / fix:** **Ceph v20.2.0 (Tentacle)** has a data-corruption bug with "read affinity" enabled — wait for v20.2.1. Ceph CVE-2025-52555 affects some 18.2.x/19.x patches · StorageClass immutability breaks `helm upgrade` of the cluster chart
- **Источник:** `kb/troubleshooting/rook-ceph-health-warn-osd.md`

### KEDB-054 · snapshot-controller: VolumeSnapshotClass still on a pre-v1 API
- **Симптом:** Kubespray's VolumeSnapshotClass manifest was updated to `v1`; the older version could be rejected by the API server on current Kubernetes
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0` · Confirmed via the merged PR #12775 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12775 (in `roles/kubernetes-apps`). Workaround before upgrading: apply your VolumeSnapshotClass as `snapshot.storage.k8s.io/v1`, or upgrade to v2.31.0. The durable fix is to upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/volumesnapshotclass-v1.md`

### KEDB-055 · Snapshots misbehave: more than one snapshot-controller in the cluster
- **Симптом:** `VolumeSnapshot`/`VolumeSnapshotContent` stuck `readyToUse: false` or churning · CRD apply conflicts / two controller Deployments reconciling the same objects · Backup tools report VolumeSnapshotClass or CRD-version errors
- **Затронутые CIs:** cross-component, storage, snapshots  ·  _>=1.29 <=1.35_
- **Root cause:** Applies wherever more than one component ships the snapshot-controller/CRDs. In this platform that's Kubespray + the `snapshotter` addon (6.3.0) + potentially Velero/VolSync/Rook
- **Workaround / fix:** external-snapshotter v8 enforces **one default VolumeSnapshotClass per driver** and removed the validation webhook — align CRDs to the single owner
- **Источник:** `kb/troubleshooting/multiple-snapshot-controllers.md`

### KEDB-056 · Velero backup/restore PartiallyFailed or Failed
- **Симптом:** `velero backup get` / `velero restore get` shows `PartiallyFailed` or `Failed`; the app's PV data is missing after restore, or the backup completed with warnings/errors
- **Затронутые CIs:** backup, velero, storage  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters running Velero · Two moving parts fail independently: **object storage** (backup metadata + file-level PV data) and **volume snapshots** (CSI/`VolumeSnapshot`)
- **Workaround / fix:** **BackupStorageLocation `Unavailable`** — fix the object-store credentials/endpoint/ region/bucket; without it nothing is stored. The most common first failure · **No PV data / snapshots not created** — the CSI snapshot path needs the **snapshot-controller enabled** + a `VolumeSnapshotClass` labelled for Velero (`velero.io/csi-volumesnapshot-class`) + a snapshot-capable driver . Otherwise use **file-level** (kopia/re…
- **Источник:** `kb/ecosystem/velero-backup-restore-fails.md`

### KEDB-057 · VolSync: mover retries on lock, AZ affinity, SCC/xattr, cache full
- **Симптом:** Restic mover job retries forever when the repo is locked · Mover/cache pod `Pending`: `node(s) had volume node affinity conflict` · Rsync mover fails `@ERROR: setgid failed` (exit 5) · Restore fails writing xattrs on OpenShift restricted SCC · Cache PVC hits `ENOSPC` with no warning
- **Затронутые CIs:** volsync, storage, backup  ·  _>=1.29 <=1.35 / >=0.15.0 <=0.16.0_
- **Root cause:** Applies to VolSync **0.15–0.16** (owner runs 0.15.0 — ). Depends on CSI snapshots — see
- **Workaround / fix:** **0.15.0 removed the `kube-rbac-proxy` sidecar** — ServiceMonitor/metrics-auth setups may need adjustment
- **Источник:** `kb/troubleshooting/volsync-mover-issues.md`

