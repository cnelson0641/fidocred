from typing import List
from sqlmodel import SQLModel, Field, Relationship
import uuid

from models.links import TimelineReportsLink

class PetTimelineBase(SQLModel):
    summary: str

class PetTimeline(PetTimelineBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    reports: List["PetReport"] = Relationship(back_populates="timelines", link_model=TimelineReportsLink)

class PetTimelineCreate(PetTimelineBase):
    pass

