from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import JSONB
import uuid

class PetHealthRecordBase(SQLModel):
    pdoc_id: str
    structured_data: dict = Field(sa_column=Column(JSONB))

class PetHealthRecord(PetHealthRecordBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)

class PetHealthRecordCreate(PetHealthRecordBase):
    pass

