# Changelog

All notable changes to this extension are documented here. This project follows [Semantic Versioning](https://semver.org/).

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
