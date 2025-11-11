from typing import List, Optional
from sqlmodel import SQLModel, Field
import uuid

#################
# Main Models
#################
class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)

class UserCreate(UserBase):
    pass

#TODO create base class
class Pet(SQLModel):
    id: str
    name: str
    species: str
    breed: Optional[str] = None
    owner_ids: List[str] = Field(default_factory=list)

class PetCreate(SQLModel):
    name: str
    species: str
    breed: Optional[str] = None
    owner_ids: List[str] = Field(default_factory=list)

class PetDocument(SQLModel):
    id: str
    pet_id: str
    filename: str
    filedata: str

class PetDocumentCreate(SQLModel):
    pet_id: str
    filename: str
    filedata: str

class PetHealthRecord(SQLModel):
    id: str
    pdoc_id: str
    structured_data: dict

class PetReport(SQLModel):
    id: str
    phr_id: str

class PetReportCreate(SQLModel):
    phr_id: str

class PetTimeline(SQLModel):
    id: str
    summary: str
    report_ids: List[str] = Field(default_factory=list)

class PetTimelineCreate(SQLModel):
    summary: str
    report_ids: List[str] = Field(default_factory=list)
