from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

#################
# Helper Classes
#################
class ExportEvent(BaseModel):
    exported_by: str  # User.id
    exported_at: datetime = Field(default_factory=datetime.utcnow)

#################
# Main Models
#################
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
    uploaded_by: str  # User.id
    filename: str
    file_type: str = "pdf"

class PetDocumentCreate(BaseModel):
    pet_id: str
    uploaded_by: str  # User.id
    filename: str
    file_type: str = "pdf"

class PetHealthRecord(BaseModel):
    id: str
    pdoc_id: str  # 1:1 mapping to PetDocument
    structured_data: dict

class PetHealthRecordCreate(BaseModel):
    structured_data: dict

class PetReport(BaseModel):
    id: str
    phr_id: str  # reference to PetHealthRecord
    summary: str
    notes: Optional[str] = None
    exports: List[ExportEvent] = Field(default_factory=list)

class PetReportCreate(BaseModel):
    summary: str
    notes: Optional[str] = None

class PetTimeline(BaseModel):
    pet_id: str
    summary: str
    reports: List[PetReport] = Field(default_factory=list)
    exports: List[ExportEvent] = Field(default_factory=list)

class PetTimelineCreate(BaseModel):
    summary: str
    reports: List[PetReport] = Field(default_factory=list)

