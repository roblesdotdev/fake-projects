from fastapi import APIRouter

router = APIRouter(prefix="/api")


@router.get("/")
def hello():
    return {"message": "Welcome to my api"}
