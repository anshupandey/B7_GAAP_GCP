# Inventory Reorder Policy

**Document ID:** POL-INV-004  
**Effective Date:** January 15, 2025  
**Review Cycle:** Quarterly  
**Owner:** Warehouse Operations & Planning

## 1. Purpose

This policy establishes the rules for inventory replenishment across all MedSupply Corp warehouses. It defines reorder points, safety stock calculations, and regional allocation strategies to prevent stockouts while minimizing carrying costs.

## 2. Reorder Point Calculation

The reorder point (ROP) for each product-region combination is calculated as:

**ROP = (Average Daily Demand × Lead Time in Days) + Safety Stock**

Where:
- Average Daily Demand = trailing 90-day average consumption
- Lead Time = supplier's avg_lead_time_days + 3 days (internal processing buffer)
- Safety Stock = see Section 3

Reorder points are recalculated weekly by the automated planning system.

## 3. Safety Stock Formulas

### Standard Products (PPE, Consumables)
Safety Stock = 1.65 × Standard Deviation of Daily Demand × √(Lead Time)

This provides approximately 95% service level (probability of not stocking out during lead time).

### Critical Products (Pharma, Life-Safety Equipment)
Safety Stock = 2.33 × Standard Deviation of Daily Demand × √(Lead Time)

This provides approximately 99% service level. Products classified as critical:
- All pharmaceutical products (insulin, epinephrine, controlled substances)
- N95 respirator masks (per pandemic preparedness directive)
- Pulse oximeters and blood pressure monitors

### Seasonal Adjustment
During flu season (October–March), safety stock for PPE and pharmaceutical categories is increased by 25%. This adjustment is applied automatically by the planning system.

## 4. Reorder Triggers

### Automatic Reorder
When quantity_on_hand drops below the reorder_point, the system automatically:
1. Generates a purchase requisition
2. Routes to the assigned primary supplier
3. Creates a PO draft for Procurement Specialist approval (SLA: 4 hours)
4. If primary supplier cannot fulfill: escalates to secondary supplier within 8 hours

### Manual Override
Warehouse Managers may manually trigger reorders when:
- Anticipated demand spike (e.g., confirmed large customer order)
- Supplier early warning of production issues
- Quality hold on existing inventory reduces available stock

### Critical Alert
When days_of_supply drops below 7 days for any product-region combination:
- Red alert generated to Warehouse Manager + Procurement Manager
- If below 3 days: escalates to VP Operations and triggers Emergency Procurement SOP consideration

## 5. Regional Allocation Rules

When total available inventory is insufficient to fill all regional requirements:

1. **Patient-critical products** (Pharma, life-safety): Allocated proportionally based on each region's trailing 30-day consumption, with a minimum allocation of 70% of each region's reorder point
2. **Standard products** (PPE, Consumables): Allocated based on open customer order volume, prioritizing orders with confirmed delivery dates
3. **Inter-regional transfers:** Permitted when donor region has > 150% of its own reorder point. Transfer cost charged to receiving region's budget.

## 6. Excess Inventory Management

Products exceeding 120 days of supply are flagged for review:
- Demand forecast reassessment
- Promotional allocation to customers
- Inter-regional transfer if another region has higher demand
- Products approaching 80% of shelf life: marked for priority distribution or donation
