from app.storage.in_memory_db import DB

class AuditLogger:
    def log(self, request_id, trace):
        DB["audit"][request_id] = trace
