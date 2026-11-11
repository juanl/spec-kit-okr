# Changelog

All notable changes to this extension are documented here. This project follows [Semantic Versioning](https://semver.org/).

## [0.2.1] - 2026-11-11

### Fixed

- With `artifact_language: auto`, a command run with arguments only (e.g. `measure bet=H-1`, or from a hook) answered in English on a project written in another language. `auto` now falls back to the language of the bet file, the spec, or the team set, and English comes last. Edits keep the artifact's existing language.
- The README now shows how to install from the release zips, and how to upgrade with `add --force`. `specify extension remove` deletes `okr-config.yml`, so it is not part of an upgrade.

## [0.2.0] - 2026-11-09

Shaped by a real team's OKRs and a real bet framed by its PM.

### Added

- **Verification contract** in every bet: one row per number the verdict depends on (leading signals `S-n`, KRs, guardrails), each with a definition, source and owner, baseline, validated/refuted thresholds, and whether it can be measured today (`yes`, `instrument`, `blocked`, `unknown`). `frame` asks for it as one pre-filled card, before the spec.
- **BLOCKED** gate result in `frame`, for a verdict that cannot be computed yet. It names what unblocks it.
- **Readiness mode** in `measure` (`bet=H-n`, or no `plan.md`): sources, baselines, attribution, and blockers before any spec or plan exists.
- `measure` looks for numbers beyond product analytics: APM and tracing, logs, databases, BI, and third parties. Third-party rows become dependencies.

### Changed

- **Company OKRs are read-only context.** No company write policy, no company proposals, no company check-in. `set level=company` only imports a copy, and quality problems go to **Import Notes**. Weak ladders and the impact on company KRs go to the team set's new **Company Impact Notes**.
- The spec (via the `okr-bet` preset), `align`, `measure`, and `review` read definitions and thresholds from the contract and never redefine them. `review` never moves a threshold after seeing the data.
- A refutation criterion has to test the hypothesis, not just the change: "the signal didn't move" means iterate.
- The measurement plan template uses contract IDs, and adds Capture and Dependencies sections.

### Removed

- The bet's Measurement Readiness table, replaced by the verification contract.
- The company template's Team Contributions, Proposals, Check-in History, and Change Log sections.

### Fixed

- The measurement plan template pointed to `okr.md`, a file from an earlier design.

## [0.1.0] - 2026-10-23

First release.

### Added

- **Model**: company OKRs → team OKRs → hypotheses → specs. Each spec is the initiative that tests one hypothesis. Enabling work (compliance, tech debt) is supported without a hypothesis.
- **Living OKR sets** per level and period. Each set records its status, last check-in, change log, proposals, and period close.
- **Sources per level**: `file` (markdown in the repo) or `mcp` (an external OKR tool reached through an MCP server, with a local mirror that records `Synced at`).
- **Write policies** per level (`none`, `propose`, `confirm`). Company defaults to `propose`, so agents file proposals and never edit company OKRs.
- **Commands**:
  - `set`: create, update, or import OKR sets, with ladder checks.
  - `frame`: turn an idea into a bet (KR, hypothesis, refutation criterion, validation slice, guardrails, candidate ideas; `mode=lite`).
  - `align`: check that the spec can test its bet, or frame the bet post-hoc.
  - `measure`: definitions, signals, instrumentation, baselines, attribution, feasibility, deadline conflicts, and a check-in calendar, all fed into `plan.md`.
  - `review`: verdict on the hypothesis, which gates the scale stories.
  - `checkin`: team or company roll-up, propagation up and down, period close.
  - `status`: read-only tree with stale sets, orphans, and ladder gaps and opportunities.
- **`okr-bet` preset**: appends a Hypothesis & Bet section to the spec template, and teaches `/speckit.specify` to fill it from the `okr:<team>/H-n` token.
- **Shared rules** in `docs/`, read by every command: sources, write policy, freshness, down-propagation, IDs, interview rules, KR cards, coaching smells, ladder check, and how to state statistical claims.
- **`dry-run`** for `review` and `checkin`, so rehearsals never write simulated values into real OKR sets.
- **Mock OKR MCP server** (`tools/mock-okr-mcp`) for trying the MCP path.
- Optional hooks on `before_specify`, `after_specify`, and `after_plan`.

### Validated with a real agent

Headless Claude Code runs across four scenarios: OKR-first, spec-first (post-hoc), living OKRs with a company MCP source, and a review plus close check-in in a fresh session. The findings from those runs shaped this release. See `examples/reporting-team-2027-Q1`.
