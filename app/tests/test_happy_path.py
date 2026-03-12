from app.engine.workflow_engine import WorkflowEngine

def test_approved():
    engine = WorkflowEngine()
    result = engine.execute("application_approval", {
        "request_id": "1",
        "age": 30,
        "credit_score": 720
    })
    assert result["decision"] == "APPROVED"
