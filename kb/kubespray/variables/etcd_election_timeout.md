---
id: VARIABLE-ETCD_ELECTION_TIMEOUT
type: variable
title: etcd_election_timeout
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_election_timeout
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines etcd_election_timeout, default \"5000\" (milliseconds)"
relations: []
---

# etcd_election_timeout

## Summary
Sets the etcd election timeout in milliseconds (the `--election-timeout` flag).
Default is `"5000"`. Controls how long a follower waits without a leader
heartbeat before starting a new leader election.

## Implementation
Defined as `etcd_election_timeout: "5000"` in
`roles/etcd_defaults/defaults/main.yml`. The same default is also declared in
`roles/kubespray_defaults/defaults/main/main.yml` and
`roles/kubernetes/control-plane/defaults/main/etcd.yml`, all with value `"5000"`.
The value is unchanged across v2.29.0–v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Paired with `etcd_heartbeat_interval`
(default `"250"`); etcd requires the election timeout to be several times the
heartbeat interval.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- roles/kubernetes/control-plane/defaults/main/etcd.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
