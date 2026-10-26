# ADR-003: Trunk-Based Development with Mandatory DevSecOps Shift-Left Gates

* **Status:** Accepted
* **Deciders:** Rushikesh Bonde
* **Date:** 2026-05-10

## Decision
Transition engineering teams from GitFlow to Trunk-Based Development with short-lived feature branches (`feature/*`, `fix/*`). Main branch is protected by mandatory PR reviews (min 2 senior approvals), GitLeaks secret scanning, and Checkov IaC evaluation.