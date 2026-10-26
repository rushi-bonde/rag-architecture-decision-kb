# ADR-001: Adoption of Azure Hub-and-Spoke Topology

* **Status:** Accepted
* **Deciders:** Rushikesh Bonde (Lead Cloud Architect)
* **Date:** 2026-03-15

## Context & Problem Statement
Our enterprise workloads need strict isolation between environments (Dev, UAT, Prod) while enforcing centralized internet egress inspection and secure on-premises ExpressRoute connectivity.

## Decision
Adopt Microsoft Cloud Adoption Framework (CAF) Hub-and-Spoke architecture:
1. Centralized HUB VNet hosts Azure Firewall Premium (TLS inspection) and GatewaySubnet.
2. Spoke VNets peer with Hub; User Defined Routes (UDR) force `0.0.0.0/0` traffic through the firewall.
3. PaaS services use Private Endpoints with centralized Private DNS Resolver.