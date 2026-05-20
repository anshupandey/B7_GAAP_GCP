# Assignment 3 — Dataset Package

## Agentic Enterprise Data Assistant: Multi-Agent RAG + NLQ→SQL Engine

### Contents

```
data/
├── bigquery/
│   ├── orders.csv              (500 rows — order transactions)
│   ├── suppliers.csv           (20 rows — supplier profiles)
│   └── inventory_snapshots.csv (1,200 rows — daily inventory levels)
├── knowledge_base/
│   ├── 01_supplier_onboarding_policy.md
│   ├── 02_fda_compliance_guidelines.md
│   ├── 03_emergency_procurement_sop.md
│   ├── 04_inventory_reorder_policy.md
│   ├── 05_product_recall_procedure.md
│   ├── 06_supplier_performance_review.md
│   ├── 07_data_privacy_phi_handling.md
│   └── 08_cold_chain_temperature_sop.md
├── load_bigquery.sh            (Helper script to load CSVs into BigQuery)
└── README.md                   (This file)
```

### Quick Start

#### 1. Load CSVs into BigQuery

```bash
# Set your project ID
export PROJECT_ID=your-gcp-project-id

# Run the loader script
chmod +x load_bigquery.sh
./load_bigquery.sh
```

Or manually:
```bash
bq mk --dataset ${PROJECT_ID}:medsupply_ops

bq load --source_format=CSV --autodetect \
  medsupply_ops.suppliers bigquery/suppliers.csv

bq load --source_format=CSV --autodetect \
  medsupply_ops.orders bigquery/orders.csv

bq load --source_format=CSV --autodetect \
  medsupply_ops.inventory_snapshots bigquery/inventory_snapshots.csv
```

#### 2. Load Knowledge Base into Vector Store

Chunk the 8 Markdown files from `knowledge_base/`, embed with Vertex AI `text-embedding-005`, and load into your chosen vector store (AlloyDB AI / ChromaDB).

Recommended chunking: 300–500 tokens per chunk with 50-token overlap. Preserve document name and section headers as metadata.

### Data Highlights

These patterns are intentionally seeded to make the test queries interesting:

| Pattern | Details |
|---------|---------|
| High defect suppliers | SUP-002 (MedTech Global, 6.8%), SUP-009 (MediFlow, 7.2%), SUP-016 (AsiaHealth, 8.1%), SUP-020 (EmergencyMed, 11.5%) |
| Expiring contracts | SUP-016 expires May 2026, SUP-003 and SUP-002 expire June 2026 |
| Cancel-heavy suppliers | SUP-020 (9 cancellations), SUP-016 (8), SUP-002 and SUP-011 (6 each) |
| Low inventory | N95 Masks in US-West trending toward stockout; Insulin in US-East near reorder point |
| Policy thresholds | Defect rate >5% triggers escalation (doc 06); >1000 units recall gets special handling (doc 05) |

These patterns enable rich HYBRID queries that cross-reference data with policy.
