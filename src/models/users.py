from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class UserRole(str, Enum):
    PO  = "PetOwner"
    SPV = "ServiceProviderVet"
    SPB = "ServiceProviderBoarder"
    A   = "Admin"

class User(BaseModel):
    id: str
    name: str
    email: str
    role: List[UserRole] = Field(default_factory=list)
    pets: Optional[List[str]] = Field(default_factory=list)
