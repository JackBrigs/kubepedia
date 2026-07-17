---
id: PRACTICE-INTEGRATION
type: best_practice
title: Integrating Kubespray into Your Own Ansible Repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubespray submodule
tags:
  - integration
  - ansible
  - git
sources:
  - type: docs
    path: docs/operations/integration.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/integration.md
    note: "How to embed Kubespray as a git submodule in an existing Ansible repo and contribute changes upstream"
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# Integrating Kubespray into Your Own Ansible Repo

## Summary
Kubespray can be embedded into an existing Ansible repository as a git submodule of your own fork, letting you import its playbooks/roles while keeping your changes isolated on a work branch. The doc also describes the upstream contribution flow (sign CLA, cherry-pick, squash, PR from your fork). Never commit sensitive data to public forks and never commit on the master branch of your fork.

## Context
Applies when you already maintain an Ansible repo and want to reuse Kubespray rather than run it standalone. Involves git submodules, `.gitmodules`, `ansible.cfg` (`library`, `roles_path`), Kubespray `group_vars`, and inventory group mapping to Kubespray's group names (`kube_node`, `etcd`, `kube_control_plane`).

## Implementation
Embedding as a submodule:
1. Fork the Kubespray repo (forks of public repos are public — never commit secrets).
2. Add your fork as a submodule, e.g. `git submodule add https://github.com/YOUR_GITHUB/kubespray.git kubespray` (creates `.gitmodules`).
3. Show submodule status: `git config --global status.submoduleSummary true`.
4. Add the original repo as upstream: `git remote add upstream https://github.com/kubernetes-sigs/kubespray.git`.
5. Sync master with upstream (`git fetch upstream` / `git merge upstream/master` / `git push origin master`).
6. Create a `work` branch for your changes — never commit on master of your fork.
7. In `ansible.cfg`, extend paths (role names must be unique), e.g. `library = ./library/:3d/kubespray/library/` and `roles_path = ./roles/:3d/kubespray/roles/`.
8. Copy/modify configs from Kubespray `group_vars` into your project (you may rename `all.yml`, e.g. to `kubespray.yml`, and create a matching inventory group).
9. Map your existing inventory groups to Kubespray names using `:children` groups (`kube_node`, `etcd`, `kube_control_plane`).
10. Include Kubespray in your playbooks: `import_playbook: 3d/kubespray/cluster.yml` (or copy individual tasks).
11. Commit submodule pointer changes to your Ansible repo when you update the work branch. Teammates use `git submodule sync` and `git submodule update --init` to fetch submodule code.

Contributing changes upstream:
1. Sign the CNCF CLA.
2. Work inside the submodule dir (e.g. `3d/kubespray`); set `user.name`/`user.email` (submodule `foreach` can help).
3. Sync with upstream master (`git fetch upstream` / `git merge upstream/master` / `git push origin master`).
4. Create a descriptive fix branch (include date/index).
5. `git cherry-pick <COMMIT_HASH>` your relevant commit from the work branch.
6. Squash temporary commits with `git rebase -i HEAD~N` and drop commits you do not want to contribute.
7. Re-check upstream before pushing: `git status`, then `git pull --rebase upstream master`.
8. Push to your fork (`git push`, or `git push --set-upstream origin <branch>`), then open the PR from GitHub, review the diff, add a clear description, and confirm. A bad branch can be deleted locally and remotely to restart.

## References
- docs/operations/integration.md (tag v2.31.0 1c9add4)
