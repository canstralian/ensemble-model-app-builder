# Runbook: Operating Copilot + Codex Standards in Trading Bot Swarm

## Purpose
Operational playbook for maintaining AI-assistant quality standards, resolving CI issues, and keeping governance docs up to date.

## Change Workflow
1. Create branch `policy/<topic>` or `chore/<topic>`.
2. Update instruction/config/workflow files.
3. Run local lint/tests if change affects executable code.
4. Open PR with:
   - intent and risk summary
   - impacted repos/services
   - rollback plan
5. Merge only after required checks pass.

## Quality Gate Checklist
- Lint clean (`ruff`, `black --check`, `isort --check-only`).
- Type checks pass (`mypy`).
- Unit tests pass (`pytest`).
- Docs-only changes may skip code checks if workflow `paths-ignore` applies.

## Troubleshooting

### 1) Lint failures after AI-generated code
- Re-run formatter and lint tools in fix mode.
- Prefer existing project utility functions over newly generated duplicates.
- Add missing imports/types and remove dead code.

### 2) Flaky tests in CI
- Identify nondeterministic dependencies (clock, network, randomness).
- Add deterministic test fixtures and explicit timeouts.
- Quarantine flaky tests only with ticket + owner + expiry date.

### 3) Async deadlocks/timeouts
- Verify no blocking sync I/O in async code paths.
- Ensure all awaits are bounded with timeouts.
- Add cancellation handling and structured concurrency.

### 4) Security scan regressions
- Review vulnerable package tree (`pip-audit` output).
- Patch or pin safe versions.
- For temporary exceptions, document risk and expiry in a tracked issue.

## Optimization Tips
- Cache dependency installs in Actions.
- Run test matrix only on impacted modules when feasible.
- Use path filters so docs-only PRs avoid heavy jobs.
- Keep AI instruction files concise and versioned.

## Review and Validation Process
- Reviewer checks policy adherence, risk notes, and evidence of validation.
- Required checks must be green before merge.
- For trading-critical logic, require domain-owner approval.

## Maintenance Schedule
- **Weekly**: inspect failing workflow trends.
- **Monthly**: refresh scanner/tool versions.
- **Quarterly**: audit AI instructions against current architecture and controls.
- **After incidents**: update runbook with lessons learned and preventive checks.

## Escalation
If a policy change blocks emergency production fixes:
1. Create emergency exception PR with explicit expiry.
2. Obtain approver sign-off from platform + strategy owner.
3. Schedule follow-up hardening PR within next sprint.

## End State
Consistent AI-assisted engineering standards that improve reliability, performance, and safety across the trading ecosystem.
