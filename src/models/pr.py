from sqlmodel import SQLModel, Field, Relationship
import uuid
from typing import List

from models.links import TimelineReportsLink

class PetReportBase(SQLModel):
    phr_id: str

class PetReport(PetReportBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    timelines: List["PetTimeline"] = Relationship(back_populates="reports", link_model=TimelineReportsLink)

class PetReportCreate(PetReportBase):
    pass

