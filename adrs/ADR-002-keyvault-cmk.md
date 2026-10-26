# ADR-002: Customer Managed Keys (CMK) for Enterprise Key Vault

* **Status:** Accepted
* **Deciders:** Rushikesh Bonde
* **Date:** 2026-04-02

## Decision
All sensitive data at rest (VM disks, Azure SQL, Blob storage) must be encrypted using Customer-Managed Keys (CMK) provisioned within Azure Key Vault Premium with Soft-Delete and Purge Protection enforced.