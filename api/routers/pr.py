from fastapi import APIRouter, HTTPException
from typing import List
from models.resources import PetReport, PetReportCreate
from dependencies.db import prs
import uuid

router = APIRouter(prefix="/prs", tags=["pet_reports"])

# Get all pet reports
@router.get("/", response_model=List[PetReport])
def get_pet_reports():
    return prs

# Get a pet report
@router.get("/{pr_id}", response_model=PetReport)
def get_pet_report(pr_id: str):
    pr = next((pr for pr in prs if pr.id == pr_id), None)
    if not pr:
        raise HTTPException(status_code=404, detail="PetReport not found")
    return pr

# Delete a pet report
@router.delete("/{pr_id}")
def delete_pet_report(pr_id: str):
    for i, pr in enumerate(prs):
        if pr.id == pr_id:
            prs.pop(i)
            return {"detail": "PetReport deleted"}
    raise HTTPException(status_code=404, detail="PetReport not found")
