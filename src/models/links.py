from sqlmodel import SQLModel, Field

class PetUserLink(SQLModel, table=True):
    pet_id: str = Field(foreign_key="pet.id", primary_key=True)
    user_id: str = Field(foreign_key="user.id", primary_key=True)

class TimelineReportsLink(SQLModel, table=True):
    timeline_id: str = Field(foreign_key="pettimeline.id", primary_key=True)
    report_id: str = Field(foreign_key="petreport.id", primary_key=True)

