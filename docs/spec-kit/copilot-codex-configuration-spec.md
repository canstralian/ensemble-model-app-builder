# Spec Kit: GitHub Copilot + Codex Configuration for Trading Bot Swarm

## 1) Purpose and Scope
This spec standardizes how AI assistants (GitHub Copilot and Codex) are configured and used across the Trading Bot Swarm ecosystem.

**Goals**
- Keep generated code production-safe, testable, and reviewable.
- Enforce consistency in style, async behavior, observability, and release readiness.
- Reduce risk from insecure defaults and unverified code suggestions.

**Copilot role definition**
Copilot is a **pair programmer**, not an autonomous deployer. It must:
- Suggest code that follows repository standards.
- Never bypass tests, lint checks, or security controls.
- Prefer explicit, deterministic, and auditable patterns.

## 2) Configuration Overview

### 2.1 Quality Controls
- **Tests**: all code changes must run impacted unit/integration tests.
- **Linting/format**: enforce `ruff`, `black`, `isort`, `mypy` (or stack equivalent).
- **Code style**: typed signatures, small functions, no hidden side effects.
- **PR checks**: required status checks gate merge.

### 2.2 Async/Concurrency Patterns
- Use structured async (`asyncio.TaskGroup` or equivalent) for fan-out jobs.
- Define cancellation, timeout, and retry behavior explicitly.
- Prevent blocking calls in event loops; use async clients for I/O.

### 2.3 Security Defaults
- Never hardcode secrets; use env/secret stores.
- Validate and sanitize external inputs (market data, webhook payloads).
- Use least-privilege tokens and scoped credentials.
- Pin critical dependencies and enforce vulnerability scanning.

### 2.4 Logging and Observability
- Structured JSON logs with correlation IDs.
- Emit key metrics: order latency, model inference latency, error rates.
- Add traces around strategy execution and broker API calls.
- Redact sensitive payloads and credentials.

### 2.5 CI/CD and Version Control
- Protect `main` with required reviews and passing checks.
- Short-lived branches; conventional commits for change intent.
- Signed tags/releases; semantic versioning with changelog automation.

## 3) Custom Instruction Behavior for Codex and Copilot

### 3.1 Example Rules
- Generate code only in approved directories.
- Prefer existing utilities over new abstractions.
- Add/adjust tests for behavior changes.
- Skip test execution only when files are docs-only.
- Flag risky operations (fund transfer/order execution) for human review.

### 3.2 Conceptual YAML (shared instruction model)
```yaml
assistant_policy:
  scope: trading-bot-swarm
  behavior:
    role: pair_programmer
    require_human_review_for:
      - order_execution_logic
      - auth_or_secret_handling
      - risk_limits
  coding_standards:
    languages: [python]
    style:
      formatter: black
      lint: ruff
      typing: mypy_strict
    async:
      avoid_blocking_io_in_event_loop: true
      require_timeouts: true
      require_cancellation_paths: true
  quality_gates:
    tests:
      required_for: [code_changes, config_changes]
      ignored_for: [docs_changes]
    lint:
      required_for: [code_changes]
  security:
    secret_handling:
      allow_plaintext_secrets: false
      required_sources: [github_actions_secrets, vault]
    dependency_policy:
      pin_versions: true
      run_vulnerability_scan: true
  observability:
    structured_logging: true
    required_fields: [service, env, trace_id, strategy_id]
    redact_fields: [api_key, secret, token]
```

## 4) GitHub Workflow Example: Lint + Test Automation
```yaml
name: quality-gate

on:
  pull_request:
    branches: [main]
    paths-ignore:
      - "**/*.md"
      - "docs/**"
  push:
    branches: [main]

jobs:
  quality-gate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Lint
        run: ruff check . && black --check . && isort --check-only .
      - name: Type check
        run: mypy .
      - name: Unit tests
        run: pytest -q
```

## 5) Best-Practice Workflow: Semantic Release + Version Tagging
```yaml
name: release
on:
  push:
    branches: [main]

jobs:
  semantic-release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Release
        run: npx semantic-release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## 6) Best-Practice Workflow: Security + Dependency Scanning
```yaml
name: security-scan
on:
  schedule:
    - cron: "0 4 * * 1"
  pull_request:
    branches: [main]

jobs:
  scans:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install scanners
        run: pip install pip-audit bandit
      - name: Dependency audit
        run: pip-audit
      - name: SAST
        run: bandit -r . -x tests
```

## 7) Contributor Guidelines
- Open a proposal issue for significant policy/process updates.
- Use small PRs with clear risk notes for trading logic changes.
- Include before/after behavior and rollback instructions.
- Review criteria: correctness, risk controls, observability, test coverage.
- Validation: quality-gate must pass before merge.

## 8) Maintenance Cadence
- **Monthly**: review tooling versions, workflow runtime, flaky checks.
- **Quarterly**: validate AI instruction set against architecture and compliance.
- **Per incident**: postmortem-driven updates to rules and runbooks.

## 9) Closing Note
This standard is designed to **normalize engineering excellence** and strengthen the Trading Bot Swarm’s reliability, performance, and safety.
