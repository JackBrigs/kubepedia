---
id: PRACTICE-DEBUG_EPHEMERAL_CONTAINERS
type: best_practice
title: "Debugging distroless workloads with ephemeral containers"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-08-04"
confidence: verified
aliases:
  - kubectl debug ephemeral container
  - cannot patch pods/ephemeralcontainers
  - debug distroless container no shell
  - kubectl debug target container
  - kubectl cp fails distroless
  - ephemeral container cannot see processes
tags:
  - troubleshooting
  - rbac
  - debugging
sources:
  - type: docs
    path: kubectl 1.33 — `kubectl debug --help` (flag semantics verified locally)
    note: "--profile values; --keep-labels defaults to false; --share-processes only applies with --copy-to"
  - type: docs
    path: Kubernetes docs — Ephemeral Containers
    url: https://kubernetes.io/docs/concepts/workloads/pods/ephemeral-containers/
    note: "the container joined via --target is the *target container*; field is targetContainerName"
relations:
  - type: see_also
    target: TROUBLE-RBAC_FORBIDDEN
  - type: see_also
    target: PRACTICE-RBAC_LEAST_PRIVILEGE
---

# Debugging distroless workloads with ephemeral containers

## Summary

A distroless image has no shell and no tools, so the usual `kubectl exec` is useless on it. The
supported answer is an **ephemeral container**: a throwaway container injected into a running Pod,
carrying the tooling the workload deliberately lacks.

Four things about it are learned the hard way, and each looks like a broken image or a broken
cluster when it happens:

1. the permission it needs is in **no default role**;
2. without `--target` you see none of the workload's processes;
3. `kubectl cp` cannot read from a distroless container;
4. the debug image is a privilege path, not just a convenience.

## Context

**The permission is the first wall.** `kubectl debug --target` issues a `PATCH` on the
`pods/ephemeralcontainers` subresource. The built-in `admin` and `edit` ClusterRoles do **not**
include it — verified against a live cluster: only `cluster-admin` has it, and only through its
wildcard. So a user who is full admin of a namespace still gets:

```
cannot patch resource "pods/ephemeralcontainers"
```

This is deliberate upstream design, not a misconfiguration: joining another container's namespaces
exposes its processes and memory.

Check before blaming anything else:

```bash
kubectl auth can-i patch pods/ephemeralcontainers -n <ns>
# for someone else:
kubectl auth can-i patch pods/ephemeralcontainers --as=<user> -n <ns>
```

**What is actually shared.** Network, IPC and hostname belong to the **Pod** — every container has
them, `--target` or not. What `--target` adds is the **process namespace of that one container**,
and with it `/proc/1/root` — the target's filesystem seen through its own PID 1.

Forgetting `--target` therefore produces an empty `ps` and an unreadable `/proc/1/root`, which reads
as "the debug image is broken". It is not; the flag is missing.

**Ephemeral containers cannot declare ports or resources**, and are never restarted after they exit.
`--share-processes` does **not** apply to them — that flag only works together with `--copy-to`.

## Implementation

**Find the target container first**, since a Pod usually has several:

```bash
kubectl get pod -n <ns> <pod> -o jsonpath='{.spec.containers[*].name}{"\n"}'
```

**Attach:**

```bash
kubectl debug -it -n <ns> <pod> --target=<container> \
  --image=<team debug image> --image-pull-policy=Always -- bash
```

Then the target is reachable through its PID 1:

```bash
ls /proc/1/root/          # its filesystem
ps afux                   # its processes
curl localhost            # its network — shared at Pod level
```

**Extra capabilities** (for `strace` and friends) come from a partial container spec passed to
`--custom`, on top of a named profile:

```yaml
# ptrace-profile.yaml
securityContext:
  capabilities:
    add: [SYS_PTRACE]
```

```bash
kubectl debug ... --profile=general --custom=./ptrace-profile.yaml -- bash
```

`--profile` accepts `legacy` (the default), `general`, `baseline`, `netadmin`, `restricted`,
`sysadmin`.

### Getting artefacts out — the trap

`kubectl cp` runs `tar` **inside the container it copies from**. A distroless container has no
`tar`, so copying from the workload container fails, and the failure is easy to misread as a path
problem.

Copy from the **debug container** instead — it has the tooling:

```bash
# the ephemeral container's generated name
kubectl get pod -n <ns> <pod> -o jsonpath='{.spec.ephemeralContainers[*].name}{"\n"}'

kubectl cp -n <ns> --container=<debug-container> \
  <pod>:/proc/1/root/tmp/artifact.tar.gz ./artifact.tar.gz
```

Write artefacts into the target's filesystem (`/proc/1/root/tmp`) rather than the ephemeral
container's own, so they survive the debug session and stay reachable. When a tool insists on a
writable temp directory, point it there:

```bash
export TMPDIR=/proc/1/root/tmp TEMP=/proc/1/root/tmp TMP=/proc/1/root/tmp
```

### Debugging a copy instead

`kubectl debug --copy-to=<name>` clones the Pod as an ordinary standalone Pod. Useful when touching
the live Pod is unacceptable.

Two facts worth knowing, both verified against `kubectl debug --help`:

- **labels are dropped by default** (`--keep-labels=false`), so the clone does *not* join Services
  and receives no traffic. Adding `--keep-labels` is what would make it dangerous;
- the clone has **no owner reference** — it is invisible to the Deployment or StatefulSet that
  produced the original, and does not affect their replica accounting.

The real limitation is different: a copy is a *new* process. A hung thread, a leaked allocation or a
stuck connection in the original will not be there. For live symptoms, only `--target` helps.

## Known Issues

**Granting the permission is granting access to secrets.** Through `--target` the debug container
sees the workload's processes, memory and filesystem — including anything it read from a Secret at
startup. A debug image that additionally bypasses admission policy restricting root, or ships a
known root password, turns that into a straightforward privilege path.

Prefer a namespaced `Role` for the teams that need it over aggregating the permission into `edit`
cluster-wide:

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ephemeral-containers-debug
  namespace: <ns>
rules:
  - apiGroups: [""]
    resources: ["pods/ephemeralcontainers"]
    verbs: ["patch", "update"]
```

**Terminology.** The container joined with `--target` is the **target container** upstream — the API
field is `targetContainerName`. Local names such as "patient container" do not appear in any
documentation or error message, which makes searching harder for whoever reads the error next.

## References

- `kubectl debug --help` (client 1.33) — flag semantics quoted above, verified 2026-08-04.
- Kubernetes documentation, Ephemeral Containers.
- Related: [[TROUBLE-RBAC_FORBIDDEN]], [[PRACTICE-RBAC_LEAST_PRIVILEGE]].
- Built-in role contents checked against a live cluster: `admin` and `edit` carry no
  `pods/ephemeralcontainers` rule.
