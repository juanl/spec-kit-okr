"""Static checks for the okr extension and the okr-bet preset."""

import re
from pathlib import Path

import pytest
import yaml
from specify_cli.extensions import ExtensionManifest
from specify_cli.presets import PresetManifest

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ExtensionManifest(ROOT / "extension.yml")
COMMANDS = [ROOT / c["file"] for c in MANIFEST.commands]
TOKEN = re.compile(r"__SPECKIT_COMMAND_([A-Z0-9_-]+)__")
CORE = {"SPECIFY", "CLARIFY", "PLAN", "TASKS", "IMPLEMENT", "ANALYZE", "CHECKLIST"}
SHARED_DOCS = re.compile(r"\.specify/extensions/okr/(docs/[a-z0-9-]+\.md)")


def test_manifest_identity():
    assert MANIFEST.id == "okr"
    assert {c["name"].split(".")[-1] for c in MANIFEST.commands} == {
        "set", "frame", "align", "measure", "review", "checkin", "status",
    }


@pytest.mark.parametrize("path", COMMANDS, ids=lambda p: p.name)
def test_command_has_frontmatter_description(path):
    text = path.read_text()
    assert text.startswith("---\n")
    front = yaml.safe_load(text.split("---\n")[1])
    assert front["description"]


@pytest.mark.parametrize("path", COMMANDS, ids=lambda p: p.name)
def test_command_references_are_tokens(path):
    text = path.read_text()
    # Literal "/speckit.x" invocations break on non-slash agents.
    assert not re.search(r"`/speckit[.-]", text), "use __SPECKIT_COMMAND_*__ tokens"
    own = {c["name"].removeprefix("speckit.").replace(".", "_").upper() for c in MANIFEST.commands}
    for name in TOKEN.findall(text):
        assert name in own | CORE, f"unknown command token {name}"


@pytest.mark.parametrize("path", COMMANDS, ids=lambda p: p.name)
def test_commands_read_shared_rules(path):
    text = path.read_text()
    docs = SHARED_DOCS.findall(text)
    assert "docs/okr-sources.md" in docs, "every command must load the shared source rules"
    for doc in docs:
        assert (ROOT / doc).is_file(), doc


def test_hooks_point_to_provided_commands():
    names = {c["name"] for c in MANIFEST.commands}
    for event, hook in MANIFEST.data["hooks"].items():
        assert hook["command"] in names, event


def test_templates_exist():
    for t in MANIFEST.data["provides"]["templates"]:
        assert (ROOT / t["file"]).is_file()


# Headings the commands read from or write into each artifact.
SECTIONS = {
    "templates/team-okrs-template.md": [
        "## Objectives", "## Key Results", "## Team Guardrails", "## Hypotheses",
        "## Check-in History", "## Company Impact Notes", "## Change Log", "## Period Close",
    ],
    "templates/company-okrs-template.md": ["## Objectives", "## Key Results", "## Import Notes"],
    "templates/bet-template.md": [
        "## Hypothesis", "## Validation", "## Guardrails", "## Candidate Ideas", "## Boundaries",
        "## Verification Contract", "## Decision Rules", "## Stories", "## Quality Gate",
        "## Open Questions", "## Framing Decisions", "## Reviews",
    ],
    "templates/measurement-plan-template.md": [
        "## Capture", "## Dependencies", "## Initiative Signals", "## Baseline Capture",
    ],
}


@pytest.mark.parametrize("template", SECTIONS, ids=lambda p: Path(p).stem)
def test_template_sections(template):
    text = (ROOT / template).read_text()
    for heading in SECTIONS[template]:
        assert f"\n{heading}\n" in text, heading


@pytest.mark.parametrize("header", ["Source", "Synced at", "Last check-in", "Status"])
def test_team_set_has_living_headers(header):
    assert f"- **{header}**:" in (ROOT / "templates" / "team-okrs-template.md").read_text(), header


@pytest.mark.parametrize("header", ["Source", "Synced at", "Status"])
def test_company_copy_has_sync_headers(header):
    assert f"- **{header}**:" in (ROOT / "templates" / "company-okrs-template.md").read_text(), header


def test_company_level_is_read_only():
    # Company OKRs are context: no write policy, no write tools, no company check-in.
    config = yaml.safe_load((ROOT / "okr-config.template.yml").read_text())
    company = config["levels"]["company"]
    assert "agent_writes" not in company
    assert set(company["mcp"]["tools"]) == {"read"}
    assert "level=team|company" not in (ROOT / "commands/speckit.okr.checkin.md").read_text()
    for path in ROOT.glob("commands/*.md"):
        assert "Proposals to company" not in path.read_text(), path.name


def test_preset_manifest_and_files():
    preset = PresetManifest(ROOT / "preset" / "preset.yml")
    assert preset.id == "okr-bet"
    for t in preset.data["provides"]["templates"]:
        assert t["strategy"] == "append"
        assert (ROOT / "preset" / t["file"]).is_file()


def test_bet_token_is_consistent():
    # frame writes it, the preset and align read it.
    for path in ("commands/speckit.okr.frame.md", "commands/speckit.okr.align.md", "preset/commands/speckit.specify.okr.md"):
        assert "okr:<team>/H-n" in (ROOT / path).read_text(), path


def test_verification_contract_is_the_shared_definition():
    # frame writes the contract; the preset, align, measure and review read it.
    for path in (
        "commands/speckit.okr.frame.md", "commands/speckit.okr.align.md",
        "commands/speckit.okr.measure.md", "commands/speckit.okr.review.md",
        "preset/commands/speckit.specify.okr.md", "templates/bet-template.md",
    ):
        assert "Verification Contract" in (ROOT / path).read_text(), path
    bet = (ROOT / "templates/bet-template.md").read_text()
    for column in ("Source (owner)", "Baseline", "Validated if", "Refuted if", "Measurable today?"):
        assert column in bet, column
    assert "BLOCKED" in (ROOT / "commands/speckit.okr.frame.md").read_text()


def test_versions_match():
    preset = PresetManifest(ROOT / "preset" / "preset.yml")
    assert MANIFEST.version == preset.version
