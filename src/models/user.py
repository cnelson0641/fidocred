from typing import List
from sqlmodel import SQLModel, Field, Relationship
import uuid

from models.links import PetUserLink

class UserBase(SQLModel):
    name: str
    email: str

class User(UserBase, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    pets: List["Pet"] = Relationship(back_populates="owners", link_model=PetUserLink)

class UserCreate(UserBase):
    pass

