# Data Privacy & PHI Handling in Supply Chain Systems

**Document ID:** POL-PRI-007  
**Effective Date:** May 1, 2025  
**Review Cycle:** Annual  
**Owner:** Information Security & Compliance

## 1. Purpose

This policy governs the handling of Protected Health Information (PHI) and personally identifiable information (PII) within MedSupply Corp's supply chain systems. While MedSupply Corp is primarily a B2B distributor, certain data touchpoints may involve PHI, particularly in pharmaceutical distribution and direct-to-facility shipments.

## 2. HIPAA Applicability

MedSupply Corp operates as a **Business Associate** under HIPAA when:
- Handling patient-specific pharmaceutical orders (e.g., specialty pharmacy distribution)
- Managing inventory for healthcare facilities that share patient consumption data
- Processing returns or recalls that reference patient identifiers

**Business Associate Agreements (BAAs)** are required with all healthcare facility customers before receiving any PHI.

## 3. Data Classification

### PHI (Protected Health Information)
- Patient names, dates of birth, medical record numbers
- Prescription details linked to identifiable patients
- Facility-specific consumption data that could identify patients (facilities with < 50 beds)

### PII (Personally Identifiable Information)
- Employee names, SSNs, contact information
- Supplier contact persons' personal details
- Customer facility staff contact information

### Business Confidential
- Pricing agreements, contract terms
- Supplier performance data, defect rates
- Internal inventory levels and demand forecasts

### Public
- General product catalogs, published pricing, regulatory filings

## 4. Handling Requirements

### PHI in Supply Chain Systems
1. **Minimization:** Only collect PHI when operationally necessary. Default to de-identified data.
2. **Encryption:** PHI must be encrypted at rest (AES-256) and in transit (TLS 1.2+)
3. **Access Control:** Role-based access; only Pharmacy Operations and designated Compliance staff
4. **Logging:** All PHI access logged with user ID, timestamp, and justification. Logs retained 6 years.
5. **De-identification:** When sharing supply chain reports with external auditors or partners, all PHI must be de-identified using Safe Harbor method (removal of 18 HIPAA identifiers) or Expert Determination.

### PII in Reports & Analytics
1. Employee SSNs: Never included in supply chain reports. Use employee ID only.
2. Contact information: Permitted in internal reports; redacted in external-facing reports.
3. Supplier contact names: Permitted in procurement reports; anonymized in performance benchmarks shared externally.

### Data in AI/ML Systems
1. No PHI may be used as training data for AI models without explicit BAA coverage and de-identification
2. AI system prompts and logs must not contain PHI; use reference IDs only
3. AI-generated reports must be reviewed for inadvertent PHI disclosure before distribution
4. Vector databases used for document retrieval must not index documents containing raw PHI

## 5. Incident Response

### PHI Breach
1. Immediate containment (within 1 hour of discovery)
2. Privacy Officer notified within 4 hours
3. Breach risk assessment within 24 hours
4. If breach affects 500+ individuals: HHS notification within 60 days, media notification
5. If breach affects < 500 individuals: HHS annual log submission
6. Affected individuals notified within 60 days with description, mitigation steps, contact information

### PII Incident
1. IT Security team notified within 4 hours
2. Scope assessment within 24 hours
3. State breach notification laws followed (varies by jurisdiction; some require notification within 30 days)

## 6. Third-Party Data Sharing

Before sharing any data with third parties (auditors, consultants, technology vendors):
1. Data classification review
2. Appropriate agreement in place (NDA for Business Confidential; BAA for PHI)
3. Data minimization: share only what is necessary for the stated purpose
4. De-identification or aggregation applied where feasible
5. Approval from Data Privacy Officer for any PHI sharing
