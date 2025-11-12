from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
import uuid


#################
# Timeline-Reports Link
#################
class TimelineReportsLink(SQLModel, table=True):
    timeline_id: str = Field(foreign_key="pettimeline.id", primary_key=True)
    report_id: str = Field(foreign_key="petreport.id", primary_key=True)

#################
# Pet-Users Link (for owners of pets)
#################
class PetUserLink(SQLModel, table=True):
    pet_id: str = Field(foreign_key="pet.id", primary_key=True)
    user_id: str = Field(foreign_key="user.id", primary_key=True)

#################
# User
#################
class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)

class UserCreate(UserBase):
    pass

#################
# Pet
#################
class PetBase(SQLModel):
    name: str
    species: str
    breed: Optional[str] = None

class Pet(PetBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    owners: List["User"] = Relationship(back_populates="pets", link_model=PetUserLink)

class PetCreate(PetBase):
    pass

#################
# Pet Doc
#################
class PetDocumentBase(SQLModel):
    filename: str
    filedata: str

class PetDocument(PetDocumentBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)

class PetDocumentCreate(SQLModel):
    pass

#################
# Pet Health Record
#################
class PetHealthRecord(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    pdoc_id: str
    structured_data: dict = Field(sa_column=Column(JSONB))

#################
# Pet Report
#################
class PetReportBase(SQLModel):
    phr_id: str

class PetReport(PetReportBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)

class PetReportCreate(SQLModel):
    pass

#################
# Pet Timeline
#################
class PetTimelineBase(SQLModel):
    summary: str

class PetTimeline(SQLModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    report_ids: List["PetReport"] = Relationship(back_populates="petreports", link_model=TimelineReportsLink)

class PetTimelineCreate(SQLModel):
    pass
