from pydantic import BaseModel
from typing import List, Optional
from models.resources import Pet, PetDocument, PetHealthRecord, PetReport, PetTimeline

class PetCreate(Pet):
    class Config:
        fields = {
            'id': {'exclude': True},
        }

class PetDocumentCreate(PetDocument):
    class Config:
        fields = {
            'id': {'exclude': True},
        }

class PetHealthRecordCreate(PetHealthRecord):
    class Config:
        fields = {
            'id': {'exclude': True},
        }

class PetReportCreate(PetReport):
    class Config:
        fields = {
            'id': {'exclude': True},
            'exports': {'exclude': True},
        }

class PetTimelineCreate(PetTimeline):
    class Config:
        fields = {
            'pet_id': {'exclude': False},  # still required
            'exports': {'exclude': True},
        }

