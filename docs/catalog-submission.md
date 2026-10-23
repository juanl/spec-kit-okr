# Catalog submission (draft)

File it with the [Extension Submission](https://github.com/github/spec-kit/issues/new?template=extension_submission.yml) issue template after the release exists. Fill `sha256` from `tools/release.sh 0.1.0`.

```json
{
  "name": "OKR Bets",
  "id": "okr",
  "description": "Treat every spec as a bet on a team Key Result: living company and team OKRs (repo or MCP), a hypothesis with a refutation criterion before specify, measurement in the plan, and a post-launch verdict that gates scaling.",
  "author": "juanl (@juanl)",
  "version": "0.1.0",
  "download_url": "https://github.com/juanl/spec-kit-okr/releases/download/v0.1.0/spec-kit-okr-0.1.0.zip",
  "sha256": "<from tools/release.sh>",
  "repository": "https://github.com/juanl/spec-kit-okr",
  "documentation": "https://github.com/juanl/spec-kit-okr/blob/main/README.md",
  "changelog": "https://github.com/juanl/spec-kit-okr/blob/main/CHANGELOG.md",
  "license": "MIT",
  "category": "process",
  "effect": "read-write",
  "requires": { "speckit_version": ">=0.9.0" },
  "provides": { "commands": 7, "hooks": 3 },
  "tags": ["okr", "product", "metrics", "impact", "hypothesis", "experimentation", "workflow"]
}
```

The `okr-bet` preset can be submitted separately to the preset catalog (`presets/catalog.community.json` process), with download URL `…/spec-kit-okr-bet-preset-0.1.0.zip`.
