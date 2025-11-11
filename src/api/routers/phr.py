from fastapi import APIRouter, HTTPException
from typing import List
from models.resources import PetHealthRecord
from dependencies.db import phrs
import uuid

router = APIRouter(prefix="/phrs", tags=["pet_healthrecords"])

# Get all pet health records
@router.get("/", response_model=List[PetHealthRecord])
def get_pet_healthrecords():
    return phrs

# Get a single pet health record by ID
@router.get("/{phr_id}", response_model=PetHealthRecord)
def get_pet_healthrecord(phr_id: str):
    phr = next((p for p in phrs if p.id == phr_id), None)
    if not phr:
        raise HTTPException(status_code=404, detail="PetHealthRecord not found")
    return phr

# Delete a pet health record
@router.delete("/{phr_id}")
def delete_pet_healthrecord(phr_id: str):
    for i, phr in enumerate(phrs):
        if phr.id == phr_id:
            phrs.pop(i)
            return {"detail": "PetHealthRecord deleted"}
    raise HTTPException(status_code=404, detail="PetHealthRecord not found")
