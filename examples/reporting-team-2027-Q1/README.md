# Example: reporting team, 2027-Q1 (real agent run)

Claude Code ran the installed commands headless. A PM persona answered from a fixed fact sheet. Company OKRs came from the mock MCP server (`tools/mock-okr-mcp`), and team OKRs lived in the repo.

| Step | Command | What to look at |
|------|---------|-----------------|
| 1 | `/speckit-okr-set` (pasted team OKRs) | Faithful import, then the ladder check: KR-3 (new deals) does not move C-KR-3 (NRR). A proposal was sent to the company through MCP: [`mock-okr-tool-calls.log`](mock-okr-tool-calls.log) |
| 2 | `/speckit-okr-frame` "export reports to PDF" | The PDF becomes a candidate idea (CI-1). The bet is about stakeholders receiving the report, with a refutation criterion and anti-gaming and cannibalization guardrails: [bet](okr/teams/reporting/bets/H-1-stakeholder-report-sharing.md) |
| 3 | `/speckit-specify … okr:reporting/H-1` (with the `okr-bet` preset) | P1 is email sharing, because a PDF download cannot refute the hypothesis. The PDF is a gated scale story: [spec](specs/001-stakeholder-report-sharing/spec.md) |
| 4 | `/speckit-okr-align` | Feasibility finding: a pilot cannot move the global KR to 30% within the quarter |
| 5 | `/speckit-okr-review` (new session, hypothetical data) | Refused to record a verdict until the data was declared a rehearsal. Used the control group to attribute a latency regression: [review](specs/001-stakeholder-report-sharing/okr-reviews/2027-03-31.md) |
| 6 | `/speckit-okr-checkin close` | Proposal accepted upstream → C-KR-4 appears. Statuses at close: [team set](okr/teams/reporting/2027-Q1.md) |
| 7 | `/speckit-okr-status` | The tree, plus findings: the KR without a bet, the ladder opportunity, and rehearsal data in real files |

Transcripts: [`transcripts/`](transcripts/). Post-launch values are hypothetical and marked SIMULATED. This run predates the `dry-run` flag, which was added because of it.

In a real project, `okr/` lives at `.specify/okr/`, and `plan.md`, `tasks.md`, and `measurement-plan.md` were skipped in this run.
