---
id: PRACTICE-DOCKER
type: best_practice
title: Docker container runtime in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - Docker CRI
tags:
  - cri
  - docker
  - container-runtime
sources:
  - type: docs
    path: docs/CRI/docker.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CRI/docker.md
    note: "Configuring Docker as the container manager and its daemon tunables"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_MANAGER
---

# Docker container runtime in Kubespray

## Summary
Kubespray supports Docker as a container manager. Because the in-tree `dockershim` is deprecated (removed in Kubernetes 1.24+), Kubespray uses Mirantis' `cri-dockerd` project to bridge Docker to the CRI; `cri-dockerd` replaced `dockershim` across supported Kubernetes versions in Kubespray 2.20. This guide covers selecting Docker and tuning its daemon (storage, cgroup driver, DNS, logging, registries).

## Context
Applies when you deploy with `container_manager: docker`. The variables below configure the Docker daemon on cluster nodes and are typically set in group_vars. Choices such as cgroup driver and storage driver must be consistent with the node OS and kernel.

## Implementation
Select Docker:

```yaml
container_manager: docker
```

Key daemon tunables:

- `docker_storage_options: -s overlay2` — enable the overlay2 graph driver.
- `docker_cgroup_driver: systemd` — cgroup driver; valid options `systemd` or `cgroupfs`, default `systemd`.
- `docker_dns_servers_strict: false` — if more than 3 nameservers exist, Kubespray uses only the first 3 and otherwise fails; set false to avoid deployment failure.
- `docker_daemon_graph: "/var/lib/docker"` — path where Docker stores data.
- `docker_iptables_enabled: "false"` — toggle Docker daemon iptables support.
- `docker_log_opts: "--log-opt max-size=50m --log-opt max-file=5"` — log rotation (example: rotate at 50m, keep last 5).
- `docker_bin_dir: "/usr/bin"` — Docker bin dir; do not change unless using a custom Docker package.
- `docker_rpm_keepcache: 1` — keep docker packages after install to speed up repeated provisioning runs (Kubespray otherwise deletes the package each run).
- `docker_mount_flags:` — override system MountFlags; takes a mount propagation flag `shared`, `slave`, or `private`. Leave empty for the system default.
- `docker_options: ""` — extra options passed to the docker daemon exactly as written.
- `docker_repo_key_keyring: /etc/apt/trusted.gpg.d/docker.gpg` — for Debian-based distros, path to store the GPG key instead of the `apt_key` module default.

Registries:

```yaml
docker_insecure_registries:
  - mirror.registry.io
  - 172.19.16.11

docker_registry_mirrors:
  - https://registry.docker-cn.com
  - https://mirror.aliyuncs.com
```

`docker_insecure_registries` allows access to self-hosted registries by IP address or domain name; `docker_registry_mirrors` adds registry mirrors (e.g., a China mirror).

Caveat: the `docker_dns_servers_strict` 3-nameserver limit can silently drop nameservers or fail deployment if not handled.

## References
- docs/CRI/docker.md (tag v2.31.0 1c9add4)
