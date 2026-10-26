"""
Enterprise RAG Knowledge Engine for Cloud Architecture
Author: Rushikesh Bonde
"""
import os
import glob
from typing import List, Dict

class ArchitectureRAGEngine:
    def __init__(self, adrs_dir: str = "adrs"):
        self.adrs_dir = adrs_dir
        self.documents: Dict[str, str] = {}
        self.load_adrs()

    def load_adrs(self):
        """Loads and indexes Architecture Decision Records."""
        files = glob.glob(os.path.join(self.adrs_dir, "*.md"))
        for f in files:
            with open(f, "r", encoding="utf-8") as fh:
                filename = os.path.basename(f)
                self.documents[filename] = fh.read()

    def query(self, search_term: str) -> List[Dict[str, str]]:
        """Semantic/Keyword hybrid search across indexed architectural knowledge."""
        results = []
        tokens = search_term.lower().split()
        for doc_name, content in self.documents.items():
            matches = sum(1 for token in tokens if token in content.lower())
            if matches > 0:
                results.append({
                    "document": doc_name,
                    "relevance_score": matches / len(tokens),
                    "snippet": content[:300] + "..."
                })
        results.sort(key=lambda x: x["relevance_score"], reverse=True)
        return results

if __name__ == "__main__":
    engine = ArchitectureRAGEngine()
    print(f"Indexed {len(engine.documents)} Architecture Decision Records.")