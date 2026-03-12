from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Workflow Decision Platform")
app.include_router(router)
