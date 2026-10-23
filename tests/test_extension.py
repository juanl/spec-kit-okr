"""Static checks for the okr extension: manifest validity and command conventions."""

import re
from pathlib import Path

import pytest
import yaml
from specify_cli.extensions import ExtensionManifest

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ExtensionManifest(ROOT / "extension.yml")
COMMANDS = [ROOT / c["file"] for c in MANIFEST.commands]
TOKEN = re.compile(r"__SPECKIT_COMMAND_([A-Z0-9_-]+)__")
CORE = {"SPECIFY", "CLARIFY", "PLAN", "TASKS", "IMPLEMENT", "ANALYZE", "CHECKLIST"}


def test_manifest_identity():
    assert MANIFEST.id == "okr"
    assert len(MANIFEST.commands) == 4


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


def test_hooks_point_to_provided_commands():
    names = {c["name"] for c in MANIFEST.commands}
    for event, hook in MANIFEST.data["hooks"].items():
        assert hook["command"] in names, event


def test_templates_exist():
    for t in MANIFEST.data["provides"]["templates"]:
        assert (ROOT / t["file"]).is_file()


# Headings that the commands read from or write into okr.md.
OKR_SECTIONS = [
    "## Objective", "## Key Results", "## Impact Hypothesis", "## Guardrails (Counter-metrics)",
    "## Boundaries", "## Candidate Initiatives", "## Measurement Readiness", "## Decision Rules",
    "## Initiatives", "## KR Coverage", "## Framing Decisions", "## Quality Gate", "## Open Questions", "## Check-in History",
]


def test_okr_template_has_parsed_sections():
    text = (ROOT / "templates/okr-template.md").read_text()
    for heading in OKR_SECTIONS:
        assert f"\n{heading}\n" in text, heading


@pytest.mark.parametrize("heading", ["Initiatives", "KR Coverage", "Candidate Initiatives", "Check-in History"])
def test_sections_referenced_by_commands_exist(heading):
    text = "\n".join(p.read_text() for p in COMMANDS)
    assert f"**{heading}**" in text or f"{heading} table" in text or f"**{heading}** table" in text
