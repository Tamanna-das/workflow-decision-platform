# workflow-decision-platform

# Configurable Workflow Decision Platform

A resilient, configurable workflow decision system designed for real-world business workflows.

## Features
- Config-driven workflows & rules
- Multi-step decision evaluation
- Full lifecycle state tracking
- Explainable audit logs
- Idempotency support
- Retry & failure handling
- External dependency simulation

## Tech Stack
- Python 3.10+
- FastAPI
- Pydantic
- Pytest

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API available at:
http://localhost:8000/docs

## Example Workflow
- Application approval
- Claim processing
- Vendor onboarding

## Key Endpoints
POST `/workflow/{workflow_name}/execute`

## Configuration
All workflows and rules are defined in `/configs/*.json`

## Testing
```bash
pytest tests/
```
