#!/usr/bin/env bash
# Build the release archives and print the catalog entry fields.
# Usage: tools/release.sh <version>   (run from a clean checkout of the tag)
set -euo pipefail
v=${1:?version}
grep -q "version: \"$v\"" extension.yml || { echo "extension.yml is not at $v" >&2; exit 1; }
mkdir -p dist
git archive --format=zip -o "dist/spec-kit-okr-$v.zip" HEAD -- . ':!tests' ':!.github' ':!examples' ':!tools' ':!preset'
(cd preset && git archive --format=zip -o "../dist/spec-kit-okr-bet-preset-$v.zip" HEAD -- .)
for f in dist/*-"$v".zip; do printf '%s  sha256=%s\n' "$f" "$(shasum -a 256 "$f" | cut -d' ' -f1)"; done
