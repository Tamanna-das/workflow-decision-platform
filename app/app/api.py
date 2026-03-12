from fastapi import APIRouter, HTTPException
from app.engine.workflow_engine import WorkflowEngine

router = APIRouter()
engine = WorkflowEngine()

@router.post("/workflow/{workflow_name}/execute")
def execute(workflow_name: str, payload: dict):
    try:
        return engine.execute(workflow_name, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
