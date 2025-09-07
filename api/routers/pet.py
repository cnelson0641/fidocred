from fastapi import APIRouter

router = APIRouter(prefix="/pets", tags=["pets"])

@router.get("/")
def list_pets():
    return [{"id": 1, "name": "Fido Doggerson"}]
