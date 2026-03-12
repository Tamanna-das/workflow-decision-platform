## Architecture Overview

The system follows a layered architecture:

API Layer
↓
Workflow Engine
↓
Rule Engine + State Manager
↓
Audit Logger + Storage

### Design Principles
- Separation of concerns
- Config-first design
- Idempotent execution
- Deterministic decisions
- Failure isolation

### Trade-offs
- In-memory DB for simplicity
- JSON configs over DSL
- Sync execution over async

### Scaling Considerations
- Replace in-memory DB with PostgreSQL
- Use message queues for async workflows
- Cache rule evaluations
- Distributed idempotency keys
