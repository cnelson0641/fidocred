from fastapi import APIRouter, HTTPException
from typing import List
from models.resources import PetDocument, PetDocumentCreate
from dependencies.db import petdocs
import uuid

router = APIRouter(prefix="/pdocs", tags=["pet_documents"])

# Get all pet documents
@router.get("/", response_model=List[PetDocument])
def get_pet_documents():
    return petdocs

# Get a single pet document by ID
@router.get("/{pdoc_id}", response_model=PetDocument)
def get_pet_document(pdoc_id: str):
    pdoc = next((d for d in petdocs if d.id == pdoc_id), None)
    if not pdoc:
        raise HTTPException(status_code=404, detail="PetDocument not found")
    return pdoc

# Create a new pet document
@router.post("/", response_model=PetDocument)
def create_pet_document(pdoc_in: PetDocumentCreate):
    # Validate pet_id exists
    if not any(p.id == pdoc_in.pet_id for p in petdocs):
        raise HTTPException(status_code=400, detail="Pet not found")
    pdoc = PetDocument(
        id=str(uuid.uuid4()),
        pet_id=pdoc_in.pet_id,
        filename=pdoc_in.filename,
        filedata=pdoc_in.filedata,
    )
    petdocs.append(pdoc)
    return pdoc

# Update a pet document
@router.put("/{pdoc_id}", response_model=PetDocument)
def update_pet_document(pdoc_id: str, updated_pdoc: PetDocumentCreate):
    for i, pdoc in enumerate(petdocs):
        if pdoc.id == pdoc_id:
            updated_pdoc_with_id = updated_pdoc.model_copy(update={"id": pdoc_id})
            petdocs[i] = updated_pdoc_with_id
            return updated_pdoc_with_id
    raise HTTPException(status_code=404, detail="PetDocument not found")

# Delete a pet document
@router.delete("/{pdoc_id}")
def delete_pet_document(pdoc_id: str):
    for i, pdoc in enumerate(petdocs):
        if pdoc.id == pdoc_id:
            petdocs.pop(i)
            return {"detail": "PetDocument deleted"}
    raise HTTPException(status_code=404, detail="PetDocument not found")
