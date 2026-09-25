from fastapi import FastAPI

from app import health

app = FastAPI()
app.include_router(health.router, prefix="/health", tags=["Health"])
