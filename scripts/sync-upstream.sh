#!/usr/bin/env bash
set -euo pipefail

UPSTREAM_URL="https://github.com/VoltAgent/awesome-clawdbot-skills.git"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

# ── Add upstream remote if missing ────────────────────────────────────────────
if ! git remote get-url upstream &>/dev/null; then
    echo "Adding upstream remote: $UPSTREAM_URL"
    git remote add upstream "$UPSTREAM_URL"
fi

# ── Check for clean working tree ─────────────────────────────────────────────
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "Error: Working tree is not clean. Please commit or stash your changes first."
    exit 1
fi

# ── Fetch & merge upstream ────────────────────────────────────────────────────
echo "Fetching upstream..."
git fetch upstream

echo "Merging upstream/main..."
if ! git merge upstream/main --no-edit; then
    echo ""
    echo "Error: Merge conflict detected!"
    echo "Resolve conflicts manually, then run:"
    echo "  python3 scripts/generate-zh-readme.py --patch-readme"
    echo "  python3 scripts/generate-zh-readme.py"
    echo "  git add -A && git commit"
    git merge --abort
    exit 1
fi

# ── Regenerate Chinese README ─────────────────────────────────────────────────
echo "Patching README.md with language switcher..."
python3 "$SCRIPT_DIR/generate-zh-readme.py" --patch-readme

echo "Generating README_zh.md..."
python3 "$SCRIPT_DIR/generate-zh-readme.py"

# ── Stage changes and show summary ────────────────────────────────────────────
git add README.md README_zh.md

if git diff --cached --quiet; then
    echo ""
    echo "No changes to commit — already up to date."
else
    echo ""
    echo "=== Changes staged ==="
    git diff --cached --stat
    echo ""
    echo "Review the changes above, then commit manually:"
    echo '  git commit -m "sync: merge upstream + update README_zh.md"'
fi
