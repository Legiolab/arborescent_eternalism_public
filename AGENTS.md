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

## LEGIOlab — AI contribution provenance (mandatory)

GitHub branch names, commit author/email and PR author do **not** prove which
AI system performed the work. A connected assistant may use the owner's GitHub
identity; never present that identity as proof of human authorship.

### Commit and PR identification
- Prefix AI-authored commit subjects with the **actual** executing agent:
  `[ChatGPT] ...`, `[Claude] ...`, `[Codex] ...`, or
  `[Agent: <verified name>] ...`. Never guess an agent/model/version.
- In every AI-authored PR, include a **Contribution provenance** section:
  - Executing agent/provider and model/version, if reliably known; otherwise
    state `unknown`.
  - Authenticated GitHub account used, if known, and whether it is shared
    with the repository owner.
  - Exact PR head SHA and changed-file scope.
  - Reviewer/auditor agent and audited SHA, or `not yet audited`.
  - Audit verdict (`ACCEPTABLE`, `CORRECTIONS REQUIRED`, `BLOCKED`)
    when an audit was actually completed, plus test evidence/limitations.
  - Human decision: `pending owner decision` until explicitly made.
- A second-pass audit must re-read the diff at the exact current SHA. If the
  head changes, mark the previous audit stale. An agent reviewing its own
  changes must state `same-agent second pass; not independent`.
- Do not claim that a GitHub PR approval, a green CI run, a commit signature,
  a label, or a provenance declaration establishes human approval.
- Never overwrite Git author identity or email to impersonate a different
  person. Where the connector forces the owner's identity, disclose that
  explicitly in the PR; do not attempt to rewrite history to conceal it.
- Only the owner may authorize a merge. An audit verdict is advice, never
  merge authorization.

### Security boundary
This is **declarative provenance**, not cryptographic attribution or
enforceable separation of identities. Real attribution requires distinct,
least-privilege agent credentials and effective branch protection.
