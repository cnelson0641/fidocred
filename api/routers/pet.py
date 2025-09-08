from fastapi import APIRouter, HTTPException
from typing import List
from models.resources import Pet, PetCreate
from dependencies.db import pets
import uuid

router = APIRouter(prefix="/pets", tags=["pets"])

# Create a new pet
@router.post("/", response_model=Pet)
def create_pet(pet_in: PetCreate):
    pet = Pet(
        id=str(uuid.uuid4()),  # server-generated
        name=pet_in.name,
        species=pet_in.species,
        breed=pet_in.breed,
        owner_ids=pet_in.owner_ids,
    )
    pets.append(pet)
    return pet

# Get all pets
@router.get("/", response_model=List[Pet])
def get_pets():
    return pets

# Get a single pet by ID
@router.get("/{pet_id}", response_model=Pet)
def get_pet(pet_id: str):
    pet = next((p for p in pets if p.id == pet_id), None)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet

# Update a pet
@router.put("/{pet_id}", response_model=Pet)
def update_pet(pet_id: str, updated_pet: PetCreate):
    for i, pet in enumerate(pets):
        if pet.id == pet_id:
            updated_pet_with_id = updated_pet.model_copy(update={"id": pet_id})
            pets[i] = updated_pet_with_id
            return updated_pet_with_id
    raise HTTPException(status_code=404, detail="Pet not found")

# Delete a pet
@router.delete("/{pet_id}")
def delete_pet(pet_id: str):
    for i, pet in enumerate(pets):
        if pet.id == pet_id:
            pets.pop(i)
            return {"detail": "Pet deleted"}
    raise HTTPException(status_code=404, detail="Pet not found")

