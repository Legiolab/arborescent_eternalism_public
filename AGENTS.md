# Agent instructions

## LEGIOlab — Common Agent Governance Policy (mandatory)

Applies to ChatGPT, Claude, Codex, other AI assistants, automations and delegated subagents. This section supplements, and never replaces, repository-specific instructions. Where rules differ, follow the more restrictive rule and ask the owner.

### Permitted within an explicitly requested task
- Read and analyze repository content within authorized scope.
- Create a dedicated `ai/*` feature branch from the current default branch.
- Edit, commit, test and push changes only on that feature branch.
- Open or update a Pull Request with a summary, changed files, test results, uncertainties and risks.
- Stop at the PR: the owner alone decides whether and when to merge.

### Prohibited without separate, explicit human authorization
- Direct push to `main`, `master`, or any protected/default branch.
- Merge, approve, auto-merge, bypass branch protections, or change GitHub rules, permissions or repository settings.
- Force-push, rewrite shared history, delete remote branches, repositories or important files.
- Trigger deployments, releases, publications, external communications, financial transactions, or other consequential external actions.
- Change or expose credentials, secrets, tokens, access controls or CI/CD workflows.
- Run destructive commands, modify unrelated repositories, or broaden the requested scope.
- Treat task completion, prior general access, or silence as authorization for any prohibited action.

### Required workflow
1. Inspect existing instructions and preserve existing work and provenance.
2. Use a new `ai/*` branch; do not modify the default branch.
3. Make the smallest scoped changes; do not silently rewrite unrelated files.
4. Run safe tests when available and truthfully report what was and was not tested.
5. Push the feature branch and open a PR for owner review. Never merge it.
6. If a task requires a prohibited action, stop and request specific authorization.

### Security boundary
These are behavioral instructions, not enforceable access controls. The owner must separately configure GitHub rulesets, least-privilege agent identities, CI permissions and secret restrictions. A PR may trigger workflows; do not assume an unmerged PR is harmless.
