# OKR Bets — a Spec Kit extension

**Every spec is a bet.** It tests a hypothesis the team holds about how to move one of its Key Results. Before `/speckit.specify`, this extension records the hypothesis and its **verification contract**: every number the verdict depends on, where it comes from, the threshold that validates or refutes the bet, and whether it can be read today. After launch, it gives the verdict that decides whether the bet gets scaled.

It is not an OKR management tool. The company OKRs are read-only context, used to see where the team's work impacts. The team OKRs are the team's own, and stay living while the work ships.

```text
Company   CO-n / C-KR-n            read-only: imported, or read from your OKR tool via MCP
└─ Team   O-n / KR-n               each KR says which company KR it moves
   └─ Hypothesis H-n               several bets per KR; each has a verification contract (S-n, KR-n, G-n)
      └─ Spec = the initiative     P1 validates the hypothesis; P2+ scale only if it holds
```

## What it adds to the workflow

```text
/speckit.okr.set      team OKRs for the period (living); imports a read-only copy of the company OKRs
        │
/speckit.okr.frame    idea → bet: which KR, the hypothesis, "refuted if…", verification contract, guardrails   (before_specify hook)
                      gate: READY | NEEDS WORK | BLOCKED (the verdict cannot be read yet)
        │
/speckit.specify      with the okr-bet preset: Hypothesis & Bet section with the contract, P1 = validation slice
        │
/speckit.okr.align    checks that the spec can test its bet; frames one post-hoc if missing   (after_specify hook)
        │
/speckit.plan → /speckit.okr.measure    contract → capture, baselines, attribution, calendar   (after_plan hook)
                      measure bet=H-n runs a readiness check before any spec or plan exists
        │
/speckit.tasks → /speckit.implement     measurement lands as tasks before the validation slice
        │
/speckit.okr.review   verdict on the hypothesis: validated / refuted / inconclusive → unlocks or stops P2+
        │
/speckit.okr.checkin  team check-in: KR statuses, roll-up of verdicts, impact on company KRs, period close
/speckit.okr.status   the whole tree, stale sets, orphaned work, ladder gaps (read-only)
```

All hooks are optional. Every command also runs on its own.

## Why

In a typical spec, the Success Criteria are acceptance thresholds ("users can export in under a minute"). They say nothing about whether the feature was worth building. In testing with a real agent, the extension caught issues like these:

- **A solution that could not move its own goal.** The request was "reminders for overdue tasks", but the goal was on-time completion, which a reminder sent after the due date cannot improve. The bet gained a pre-due reminder as its P1.
- **A requested solution that could not validate the hypothesis.** The request was "export to PDF", but a download does not show that the report reached anyone. The spec put email sharing at P1 and moved the PDF to a scale story.
- **KRs that ladder to nothing.** A team's KR on lost *new* enterprise deals was linked to the company's net revenue retention KR, which measures existing customers. The extension flagged the mismatch and sent a proposal to the company OKR owner through MCP. The owner accepted it, and the next status run surfaced the new company KR as a ladder opportunity.
- **Unreadable KRs.** It found events tracked per account while the KR counted users, a KR deadline that came before its observation period ended, and a pilot too small to move a global KR within the quarter.
- **A guardrail breach.** Report-page latency went up 14%. The review used the holdout to check whether the feature caused it, before deciding on a rollback.

## The verification contract

`frame` asks for it as one pre-filled card, inferring all it can from the team set, the code, configs, and dashboards. One row per number the verdict reads:

| ID | Role | Definition | Source (owner) | Baseline | Validated if | Refuted if | Measurable today? |
|----|------|------------|----------------|----------|--------------|------------|-------------------|
| S-1 | leading signal | P95 of payment service time per method, failures included, 7 days | APM (own team) | capture before the change | ≥ 25% lower | — | yes |
| KR-2 | key result | P95 end-to-end per payment journey, client side | vendor's client metrics (vendor) | unknown | drops ≥ half of S-1's gain | drops < half of S-1's gain after 4 weeks | blocked: vendor, no date |
| G-1 | guardrail | error rate per method, timeouts included | logs (own team) | 0.8% | — | > 1.2% | yes |

- **Refuted if** must be computable from the rows. "The signal didn't move" means iterate, not refuted: the hypothesis was never tested.
- A number can come from product analytics, APM or tracing, logs, a database, a survey, or a third party. Third-party rows become dependencies, not instrumentation tasks.
- If the verdict depends on a row that is `blocked` without an owner and a date, or whose source is `unknown`, the gate says **BLOCKED** and names what unblocks it. In that case the spec's P1 must include getting the number.
- The spec, `measure`, and `review` all read the contract. None of them redefines a number, and `review` never moves a threshold after seeing the data.

## Install

Requires Spec Kit `>= 0.9.0` (tested with 0.16.2).

From the release:

```bash
specify extension add okr --from https://github.com/juanl/spec-kit-okr/releases/download/v0.2.1/spec-kit-okr-0.2.1.zip
specify preset add --from https://github.com/juanl/spec-kit-okr/releases/download/v0.2.1/spec-kit-okr-bet-preset-0.2.1.zip   # recommended: Hypothesis & Bet section in specs
```

From a local checkout:

```bash
specify extension add --dev /path/to/spec-kit-okr
specify preset add --dev /path/to/spec-kit-okr/preset
```

**Upgrading**: run the same `add` command with `--force`. It keeps your `okr-config.yml` (and `okr-config.local.yml`). Don't run `specify extension remove okr` first: removing the extension deletes its config, and the next `add` scaffolds an empty one. Your OKR sets, bets, and specs live outside the extension folder and are never touched.

The **`okr-bet` preset** composes with your spec template (`append`) and with `/speckit.specify` (`append`), so it doesn't replace anything. Without it, `/speckit.okr.align` inserts the section afterwards.

## Configure

Copy `okr-config.template.yml` to `.specify/extensions/okr/okr-config.yml`:

```yaml
period: "2027-Q1"
team: "reporting"
levels:
  company:                      # always read-only
    source: mcp                 # or: file (an imported copy)
    mcp:
      server: okr-tool
      tools: { read: get_okr_set }
  team:
    source: file                # .specify/okr/teams/{team}/{period}.md
    agent_writes: confirm       # show the exact change, wait for a yes
```

| Key | Default | Meaning |
|-----|---------|---------|
| `levels.<level>.source` | `file` | `file`: the markdown set is the source of truth. `mcp`: an OKR tool behind an MCP server is the source of truth, and a local mirror records `Synced at` |
| `levels.team.agent_writes` | `confirm` | `none` / `propose` / `confirm`. The company level is always read-only |
| `levels.team.cadence_days` | 14 | Commands warn when the team set's last check-in is older than this |
| `levels.company.stale_days` | 30 | Commands warn when the imported company copy is older than this |
| `key_results.min` / `max` | 2 / 4 | KRs per objective |
| `scoring.thresholds` | 0.7 / 0.4 | Persevere / iterate thresholds |
| `interview.max_questions` | 8 | Primary questions (follow-ups don't count). `mode=lite` on `frame` uses 3 |
| `output.artifact_language` | `auto` | Body text language. `auto` follows your words, or the bet and spec when a command runs with arguments only. Headings, IDs and statuses stay in English |

> Removing and re-adding the extension deletes `.specify/extensions/okr/`, including your config. Keep a copy, or put your overrides in `okr-config.local.yml` and back it up.

### Trying the MCP path

`tools/mock-okr-mcp/` contains a small MCP server, backed by a JSON file, that implements the four operations the extension can use (`get_okr_set`, `update_kr`, `add_checkin`, `propose_change`). Only `read` is ever used for the company level; the write operations apply to a team set kept in an OKR tool. It logs every call, so you can check what the agent did:

```bash
uv run --python 3.12 --with mcp==1.12.4 --with pydantic==2.11.7 tools/mock-okr-mcp/server.py data.json
```

For a real OKR tool, map the operations to its MCP server's tools under `levels.<level>.mcp.tools`.

## Artifacts

```text
.specify/okr/
├── company/2027-Q1.md                      read-only copy of the company OKRs
└── teams/reporting/
    ├── 2027-Q1.md                          team set: KRs, hypotheses, check-ins, proposals, change log, period close
    └── bets/H-1-stakeholder-report-sharing.md   one bet: hypothesis, verification contract, guardrails, ideas, stories, reviews
specs/001-…/
├── spec.md                                 Input carries okr:reporting/H-1; Hypothesis & Bet section
├── measurement-plan.md
└── okr-reviews/2027-03-31.md
```

## Example

[`examples/reporting-team-2027-Q1`](examples/reporting-team-2027-Q1/) is a real run with Claude Code in headless mode, recorded with v0.1.0. It predates the verification contract, and back then company OKRs still accepted proposals. It goes through set → frame → specify (with the preset) → align → review → close check-in → status, with company OKRs served by the mock MCP server. The transcripts and every generated artifact are included, along with the MCP call log, which shows four reads, one proposal, and no edits to company OKRs. The post-launch numbers are hypothetical and marked SIMULATED.

## Limits

- **Validation so far.** v0.1.0 was tested with a PM persona answering from a fixed fact sheet. v0.2.0 was shaped by one real team's OKRs and a real bet framed by its PM, then re-run with a separate headless agent: it reached BLOCKED on its own, since the KR could only be read through a vendor with no date, and `measure` in readiness mode found that the vendor deliverable the team was counting on measured usage, not timings. The real-agent cost was about $1–2 for a set or a frame, about $1–3 for an align, and about $7 for a full feature cycle, most of it in the core `plan` and `tasks` commands.
- **Not worth it for small work.** Bugs, small changes, and tech debt don't need the full framing. Use `frame mode=lite`, or treat the work as an enabling initiative (`okr:<team>/enabling:<KR|guardrail>`).
- **Prompts, not code.** The extension is a set of agent instructions. How well it does depends on the agent following them. The rules that matter most are the write policies, the ban on invented numbers, and the dry-run mode, and they are stated in every command.
- **Agent memory.** Some agents keep their own memory across sessions, and may store facts from an OKR interview. That is outside this extension's control.

## Resumen en español

Extensión para Spec Kit que trata cada spec como una **apuesta**: una iniciativa que pone a prueba una hipótesis sobre cómo mover un Key Result del equipo. No gestiona OKRs. Los de compañía se leen, desde el repo o una herramienta vía MCP, para entender dónde impacta cada iniciativa. Los del equipo siguen vivos. El ciclo es:

- `frame`: antes del spec, define la apuesta (KR, hipótesis, "se refuta si…", guardrails) y su **contrato de verificación**. Ese contrato dice cada número del que depende el veredicto, de dónde sale, con qué umbral valida o refuta, y si hoy se puede medir. Si no se puede leer el veredicto, el gate da BLOCKED.
- El preset `okr-bet`: hace que el spec nazca con esa sección y con P1 como slice de validación.
- `measure`: convierte el contrato en captura, líneas base, atribución y calendario. Con `bet=H-n` corre antes del spec, como chequeo de factibilidad.
- `review`: da el veredicto sobre la hipótesis, que habilita o frena el escalado.
- `checkin` y `status`: mantienen vivos los OKRs del equipo, muestran el impacto en los KRs de compañía y detectan trabajo huérfano.

## License

MIT
