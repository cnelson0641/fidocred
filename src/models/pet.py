from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
import uuid

from models.links import PetUserLink

class PetBase(SQLModel):
    name: str
    species: str
    breed: Optional[str] = None

class Pet(PetBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    owners: List["User"] = Relationship(back_populates="pets", link_model=PetUserLink)

class PetCreate(PetBase):
    pass

