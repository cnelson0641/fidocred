from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from models import Pet, PetCreate
from db.db import get_db
import services.pet as pet_service

router = APIRouter(prefix="/pets", tags=["pets"])

# Get all pets
@router.get("/", response_model=List[Pet])
async def list_pets(db: AsyncSession = Depends(get_db)):
    return await pet_service.get_pets(db)

# Get a pet
@router.get("/{pet_id}", response_model=Pet)
async def get_pet_route(pet_id: str, db: AsyncSession = Depends(get_db)):
    pet = await pet_service.get_pet(db, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

# Create pet
@router.post("/", response_model=Pet)
async def create_pet_route(pet_in: PetCreate, db: AsyncSession = Depends(get_db)):
    return await pet_service.create_pet(db, pet_in)

# Update pet
@router.put("/{pet_id}", response_model=Pet)
async def update_pet_route(pet_id: str,updated_pet: PetCreate,db: AsyncSession = Depends(get_db)):
    pet = await pet_service.update_pet(db, pet_id, updated_pet)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

# Delete pet
@router.delete("/{pet_id}")
async def delete_pet_route(pet_id: str, db: AsyncSession = Depends(get_db)):
    success = await pet_service.delete_pet(db, pet_id)
    if not success:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"detail": "Pet deleted"}

