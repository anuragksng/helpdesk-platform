from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_health_check():
    return {"status": "ok"}