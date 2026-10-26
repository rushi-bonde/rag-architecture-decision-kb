# 🧠 Enterprise Cloud Architecture RAG Knowledge Engine

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Architecture: ADR](https://img.shields.io/badge/Architecture-ADR_Framework-FF6B6B?style=for-the-badge)](adrs/)
[![Protocol: RAG](https://img.shields.io/badge/AI-Retrieval_Augmented_Generation-7928CA?style=for-the-badge)](engine.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

**An enterprise Retrieval-Augmented Generation (RAG) knowledge engine indexing Architecture Decision Records (ADRs), cloud governance policies, and compliance benchmarks for instant technical query responses.**

[Decision Records](adrs/) · [RAG Engine](engine.py) · [CLI Tool](cli.py)

</div>

---

## ⚡ Features

* **Contextual Retrieval:** Indexes enterprise ADRs including Hub-Spoke networking, CMK encryption, and Model Context Protocol integrations.
* **Instant Compliance Audit:** Engineers can query compliance rationale (e.g. *"Why is forced tunneling required on our database subnets?"*) via CLI or automated CI bots.

---

## 🚀 Quickstart

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run test suite
pytest tests/

# 3. Query the knowledge base
python cli.py "Hub and Spoke firewall"
python cli.py "Customer Managed Keys encryption"
```

---

## 🤝 Maintained by
**Rushikesh Bonde** · Licensed under MIT.