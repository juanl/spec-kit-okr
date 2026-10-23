"""Mock OKR tool exposed over MCP (stdio), backed by a JSON file.

For testing the okr extension's `source: mcp` path without a real OKR product.
Every call is appended to <data>.calls.log so tests can check what the agent did.

Run:  uv run --python 3.12 --with mcp==1.12.4 --with pydantic==2.11.7 server.py <data.json>
"""

import datetime as dt
import json
import sys
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DATA = Path(sys.argv[1]).resolve()
LOG = DATA.with_suffix(".calls.log")
mcp = FastMCP("okr-tool")


def _load():
    return json.loads(DATA.read_text())


def _save(data):
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def _log(tool, args):
    with LOG.open("a") as f:
        f.write(json.dumps({"at": dt.datetime.now().isoformat(timespec="seconds"), "tool": tool, "args": args}, ensure_ascii=False) + "\n")


def _set(data, level, period, team):
    key = f"{level}:{period}" if level == "company" else f"team:{team}:{period}"
    if key not in data["sets"]:
        raise ValueError(f"no OKR set {key}")
    return data["sets"][key]


@mcp.tool()
def get_okr_set(level: str, period: str, team: str = "") -> dict:
    """Read an OKR set. level: 'company' or 'team'. period like '2027-Q1'. team id for team sets."""
    _log("get_okr_set", {"level": level, "period": period, "team": team})
    return _set(_load(), level, period, team)


@mcp.tool()
def update_kr(level: str, period: str, kr_id: str, current: str = "", status: str = "", team: str = "") -> dict:
    """Update the current value and/or status of one Key Result."""
    _log("update_kr", {"level": level, "period": period, "kr_id": kr_id, "current": current, "status": status, "team": team})
    data = _load()
    kr = next(k for k in _set(data, level, period, team)["key_results"] if k["id"] == kr_id)
    if current:
        kr["current"] = current
    if status:
        kr["status"] = status
    _save(data)
    return kr


@mcp.tool()
def add_checkin(level: str, period: str, summary: str, team: str = "") -> dict:
    """Record a check-in note on an OKR set."""
    _log("add_checkin", {"level": level, "period": period, "summary": summary, "team": team})
    data = _load()
    s = _set(data, level, period, team)
    entry = {"date": dt.date.today().isoformat(), "summary": summary}
    s.setdefault("checkins", []).append(entry)
    s["last_checkin"] = entry["date"]
    _save(data)
    return entry


@mcp.tool()
def propose_change(level: str, period: str, proposal: str, reason: str, from_team: str = "") -> dict:
    """Propose a change to an OKR set for its owner to accept or reject. Does not change the set."""
    _log("propose_change", {"level": level, "period": period, "proposal": proposal, "reason": reason, "from_team": from_team})
    data = _load()
    s = _set(data, level, period, "")
    entry = {"date": dt.date.today().isoformat(), "from": from_team, "proposal": proposal, "reason": reason, "status": "open"}
    s.setdefault("proposals", []).append(entry)
    _save(data)
    return entry


if __name__ == "__main__":
    mcp.run()
