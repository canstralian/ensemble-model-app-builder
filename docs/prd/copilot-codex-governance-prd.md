# PRD: Copilot + Codex Governance for Trading Bot Swarm

## Product Summary
Create a unified governance framework for AI-assisted development using GitHub Copilot and Codex so teams can move faster without compromising safety, quality, or compliance.

## Problem Statement
Teams receive inconsistent AI-generated output, leading to style drift, missing tests, and elevated operational risk in trading-critical services.

## Objectives
- Standardize assistant behavior and coding expectations.
- Enforce automated quality gates for code changes.
- Reduce security and operational regressions from generated code.

## Non-Goals
- Fully autonomous coding/deployment with no human review.
- Replacing existing SDLC ownership or incident response processes.

## Personas
- **Quant/Strategy Engineer**: needs safe, fast iteration on strategy code.
- **Platform Engineer**: needs enforceable CI/CD and dependency hygiene.
- **Reviewer/Approver**: needs predictable PRs with strong validation signals.

## Functional Requirements
1. Define custom instructions for Copilot and Codex with shared behavior model.
2. Require test/lint execution for non-doc code changes.
3. Provide GitHub Actions templates for quality gates, release, and scanning.
4. Document contributor process and validation criteria.
5. Publish a runbook for troubleshooting CI failures and optimization.

## Success Metrics
- 95%+ PRs pass quality-gate on first or second run.
- 100% of merged non-doc PRs include automated lint/test evidence.
- 30% reduction in post-merge defects tied to style/test gaps.
- 100% of repos use standardized assistant instruction baseline.

## Risks and Mitigations
- **Risk**: Overly strict rules slow delivery.  
  **Mitigation**: periodic tuning + documented exception process.
- **Risk**: Teams bypass templates.  
  **Mitigation**: branch protection and required checks.
- **Risk**: AI suggestions introduce hidden security flaws.  
  **Mitigation**: security scans + mandatory human review for critical domains.

## Rollout Plan
1. Pilot in one strategy repo + one platform repo.
2. Gather metrics for 2–4 weeks.
3. Adjust policies and publish v1.0 baseline.
4. Expand to all Trading Bot Swarm repositories.

## Acceptance Criteria
- PR template + instruction docs merged and discoverable.
- CI workflows active and required on `main`.
- Runbook available with troubleshooting and optimization guidance.
- Quarterly owner assigned for governance updates.
