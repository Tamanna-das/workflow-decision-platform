from app.storage.in_memory_db import DB

class IdempotencyManager:
    def exists(self, key):
        return key in DB["idempotency"]

    def get(self, key):
        return DB["idempotency"][key]

    def save(self, key, value):
        DB["idempotency"][key] = value
