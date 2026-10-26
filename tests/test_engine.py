from engine import ArchitectureRAGEngine

def test_rag_indexing():
    engine = ArchitectureRAGEngine()
    assert len(engine.documents) >= 4

def test_rag_query():
    engine = ArchitectureRAGEngine()
    results = engine.query("firewall hub spoke")
    assert len(results) > 0
    assert results[0]["document"] == "ADR-001-hub-and-spoke.md"