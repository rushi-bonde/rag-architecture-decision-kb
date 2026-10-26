# ADR-004: Model Context Protocol (MCP) Integration for Autonomous SRE

* **Status:** Accepted
* **Deciders:** Rushikesh Bonde
* **Date:** 2026-08-18

## Decision
Implement custom Model Context Protocol (MCP) servers to allow AI reasoning models to autonomously query live Kubernetes cluster state, inspect Terraform drift, and recommend validated remediation pull requests.