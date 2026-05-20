#!/bin/bash
# ─────────────────────────────────────────────────────────
# Assignment 3 — Load CSVs into BigQuery
# Usage: export PROJECT_ID=your-project && ./load_bigquery.sh
# ─────────────────────────────────────────────────────────

set -euo pipefail

if [ -z "${PROJECT_ID:-}" ]; then
  echo "ERROR: Set PROJECT_ID first → export PROJECT_ID=your-gcp-project-id"
  exit 1
fi

DATASET="medsupply_ops"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BQ_DIR="${SCRIPT_DIR}/bigquery"

echo "=== Loading Assignment 3 data into ${PROJECT_ID}:${DATASET} ==="

# Create dataset (ignore if exists)
bq mk --project_id="${PROJECT_ID}" --dataset "${DATASET}" 2>/dev/null || true
echo "✓ Dataset ${DATASET} ready"

# Load suppliers
bq load --project_id="${PROJECT_ID}" \
  --source_format=CSV --autodetect --replace \
  "${DATASET}.suppliers" "${BQ_DIR}/suppliers.csv"
echo "✓ suppliers loaded (20 rows)"

# Load orders
bq load --project_id="${PROJECT_ID}" \
  --source_format=CSV --autodetect --replace \
  "${DATASET}.orders" "${BQ_DIR}/orders.csv"
echo "✓ orders loaded (500 rows)"

# Load inventory snapshots
bq load --project_id="${PROJECT_ID}" \
  --source_format=CSV --autodetect --replace \
  "${DATASET}.inventory_snapshots" "${BQ_DIR}/inventory_snapshots.csv"
echo "✓ inventory_snapshots loaded (1,200 rows)"

echo ""
echo "=== All tables loaded successfully ==="
echo "Verify: bq ls ${DATASET}"
echo "Query:  bq query 'SELECT COUNT(*) FROM ${DATASET}.orders'"
