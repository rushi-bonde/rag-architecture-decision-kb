#!/usr/bin/env python3
"""
CLI Query Interface for Enterprise Architecture Decision Knowledge Base
"""
import sys
from engine import ArchitectureRAGEngine

def main():
    query_str = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hub and Spoke firewall"
    engine = ArchitectureRAGEngine()
    results = engine.query(query_str)
    
    print(f"\n🔍 Query: '{query_str}'")
    print(f"📊 Found {len(results)} matching Architecture Decision Records:\n")
    for r in results:
        print(f"  📄 [{r['document']}] (Relevance: {r['relevance_score'] * 100:.1f}%)")
        print(f"     {r['snippet']}\n")

if __name__ == "__main__":
    main()