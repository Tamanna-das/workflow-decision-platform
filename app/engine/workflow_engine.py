import json
from app.engine.rule_engine import RuleEngine
from app.engine.state_manager import StateManager
from app.engine.audit_logger import AuditLogger
from app.engine.idempotency import IdempotencyManager

class WorkflowEngine:
    def __init__(self):
        self.state = StateManager()
        self.audit = AuditLogger()
        self.idempotency = IdempotencyManager()

    def execute(self, workflow_name, payload):
        request_id = payload.get("request_id")
        if self.idempotency.exists(request_id):
            return self.idempotency.get(request_id)

        config = json.load(open(f"configs/{workflow_name}.json"))
        rules = RuleEngine(config["rules"])

        self.state.create(request_id)
        decision, trace = rules.evaluate(payload)

        self.state.update(request_id, decision)
        self.audit.log(request_id, trace)

        response = {
            "request_id": request_id,
            "decision": decision,
            "audit_trace": trace
        }

        self.idempotency.save(request_id, response)
        return response
