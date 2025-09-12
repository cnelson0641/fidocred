from fastapi import APIRouter, HTTPException
from typing import List
from models.resources import PetTimeline, PetTimelineCreate
from dependencies.db import pts
import uuid

router = APIRouter(prefix="/pts", tags=["pet_timelines"])

# Get all pet timelines
@router.get("/", response_model=List[PetTimeline])
def get_pet_timelines():
    return pts

# Get a pet timeline
@router.get("/{pt_id}", response_model=PetTimeline)
def get_pet_timeline(pt_id: str):
    p = next((pt for pt in pts if pt.id == pt_id), None)
    if not p:
        raise HTTPException(status_code=404, detail="PetTimeline not found")
    return p

# Delete a pet timeline
@router.delete("/{pt_id}")
def delete_pet_timeline(pt_id: str):
    for i, pt in enumerate(pts):
        if pt.id == pt_id:
            pts.pop(i)
            return {"detail": "PetTimeline deleted"}
    raise HTTPException(status_code=404, detail="PetTimeline not found")

# Update a pet timeline
@router.put("/{pt_id}", response_model=PetTimeline)
def update_pet_timeline(pt_id: str, updated_pt: PetTimelineCreate):
    for i, pt in enumerate(pts):
        if pt.id == pt_id:
            updated_pt_with_id = updated_pt.model_copy(update={"id": pt_id})
            pts[i] = updated_pt_with_id
            return updated_pt_with_id
    raise HTTPException(status_code=404, detail="PetTimeline not found")
