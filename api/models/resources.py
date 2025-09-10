from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

#################
# Main Models
#################
class User(BaseModel):
    id: str
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str

class Pet(BaseModel):
    id: str
    name: str
    species: str
    breed: Optional[str] = None
    owner_ids: List[str] = Field(default_factory=list)

class PetCreate(BaseModel):
    name: str
    species: str
    breed: Optional[str] = None
    owner_ids: List[str] = Field(default_factory=list)

class PetDocument(BaseModel):
    id: str
    pet_id: str
    filename: str
    filedata: str

class PetDocumentCreate(BaseModel):
    pet_id: str
    filename: str
    filedata: str

class PetHealthRecord(BaseModel):
    id: str
    pdoc_id: str
    structured_data: dict

class PetReport(BaseModel):
    id: str
    phr_id: str

class PetReportCreate(BaseModel):
    phr_id: str

class PetTimeline(BaseModel):
    id: str
    summary: str
    report_ids: List[str] = Field(default_factory=list)

class PetTimelineCreate(BaseModel):
    summary: str
    report_ids: List[str] = Field(default_factory=list)
