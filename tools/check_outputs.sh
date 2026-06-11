\
#!/usr/bin/env bash
set -euo pipefail

missing=0

check_file() {
  local path="$1"
  if [[ -f "$path" ]]; then
    echo "OK      $path"
  else
    echo "MISSING $path"
    missing=1
  fi
}

check_dir() {
  local path="$1"
  if [[ -d "$path" ]]; then
    echo "OK      $path/"
  else
    echo "MISSING $path/"
    missing=1
  fi
}

echo "Checking base workflow files..."
check_file ".github/copilot-instructions.md"
check_dir ".github/prompts"
check_file "README.md"
check_file "RUNBOOK.md"
check_file "tools/extract_docx.py"

echo
echo "Checking extraction outputs..."
check_file "working/extracted/document_text.md"
check_file "working/extracted/tables.md"
check_file "working/extracted/image_inventory_raw.md"
check_dir "working/extracted/images"

echo
echo "Checking common pipeline outputs when available..."
for file in \
  output/10_extraction_summary.md \
  output/11_translation_policy.md \
  output/12_normalized_evidence.md \
  output/13_translation_review_report.md \
  output/20_image_analysis.md \
  output/21_domain_glossary.md \
  output/30_requirement_inventory.md \
  output/31_business_rule_catalog.md \
  output/32_open_questions.md \
  output/40_FD_DRAFT.md \
  output/41_FD_INTERNAL_TRACEABILITY.md \
  output/42_FD_REVIEW_REPORT.md
do
  if [[ -f "$file" ]]; then
    echo "OK      $file"
  else
    echo "OPTIONAL_NOT_FOUND $file"
  fi
done

echo
if [[ "$missing" -eq 0 ]]; then
  echo "Base check passed."
else
  echo "Base check failed. Create or restore missing required files."
fi

exit "$missing"
