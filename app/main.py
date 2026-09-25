from fastapi import FastAPI

from app import health
from tests import test_health

app = FastAPI()
app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(test_health.router, prefix="/test_health", tags=["Test Health"])
