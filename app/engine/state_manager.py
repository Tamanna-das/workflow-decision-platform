from app.storage.in_memory_db import DB

class StateManager:
    def create(self, request_id):
        DB["state"][request_id] = ["RECEIVED"]

    def update(self, request_id, state):
        DB["state"][request_id].append(state)
