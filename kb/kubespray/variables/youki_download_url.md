---
id: VARIABLE-YOUKI_DOWNLOAD_URL
type: variable
title: youki_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - youki_download_url
tags:
  - youki
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for the youki release archive."
relations: []
---

# youki_download_url

## Summary
The URL from which the youki runtime release archive is downloaded. It is a computed default built from `github_url`, `youki_version`, and the node's `ansible_architecture`, pointing at the youki-dev GitHub release asset (a gnu tar.gz archive).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`youki_download_url: "{{ github_url }}/youki-dev/youki/releases/download/v{{ youki_version }}/youki-{{ youki_version }}-{{ ansible_architecture }}-gnu.tar.gz"`

The expression is unchanged across v2.29.0-v2.31.0 (line 167 in v2.29.0; line 169 in v2.29.1/v2.30.0/v2.31.0). The concrete URL varies only through the resolved `youki_version` and per-host architecture.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `github_url`, `youki_version`, `youki_archive_checksum`, `youki_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
