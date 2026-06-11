\
#!/usr/bin/env bash
set -euo pipefail

echo "Resetting generated working/output/design files..."
rm -rf working/extracted
mkdir -p working/extracted/images

rm -rf output
mkdir -p output
touch output/.gitkeep

rm -f design/fd/*.yaml 2>/dev/null || true
rm -f design/dd/*.yaml 2>/dev/null || true
rm -rf design/coding/copilot_tasks
mkdir -p design/coding/copilot_tasks

echo "Done. Input files were not removed."
