from models.resources import Pet, User, PetDocument, PetHealthRecord, PetReport, PetTimeline
from datetime import datetime

#TODO refactor into a DB

# Exportable lists, one for each resource
pets = None
users = None
petdocs = None
phrs = None
prs = None
pts = None

####################
# Fill in Data
####################
# Declare data
pets_data = [
    {
        "id": "1",
        "name": "Fido",
        "species": "Dog",
        "breed": "Golden Retriever",
        "owner_ids": ["1","2"],
    },
    {
        "id": "2",
        "name": "Buddy",
        "species": "Dog",
        "breed": "Great Pyrenees",
        "owner_ids": ["1"],
    },
    {
        "id": "3",
        "name": "Gus",
        "species": "Cat",
        "breed": "Mixed",
        "owner_ids": ["2"],
    },
]
users_data = [
    {
        "id": "1",
        "name": "Chris Nelson",
        "email": "lol@lol.com",
    },
    {
        "id": "2",
        "name": "John Smith",
        "email": "rofl@lol.com",
    }
]
petdocs_data = [
    {
        "id": "1",
        "pet_id": "1",
        "filename": "vaccine_record.pdf",
        "filedata": "Vaccinations present, teeth brushed",
    },
    {
        "id": "2",
        "pet_id": "2",
        "filename": "vet_visit_2023_10_01.pdf",
        "filedata": "Vaccinations present",
    },
]
phrs_data = [
    {
        "id": "1",
        "pdoc_id": "1",
        "structured_data": {"data": petdocs_data[0]["filedata"]},
    },
    {
        "id": "2",
        "pdoc_id": "2",
        "structured_data": {"data": petdocs_data[1]["filedata"]},
    },
]
prs_data = [
    {
        "id": "1",
        "phr_id": "1",
    },
    {
        "id": "2",
        "phr_id": "2",
    },
]
pts_data = [
    {
        "id": "1",
        "summary": "Only 1 PHR",
        "report_ids": ["1"],
    },
    {
        "id": "2",
        "summary": "Two PHR in this",
        "report_ids": ["1", "2"],
    },
]

# Create objects from the data above
pets = [Pet(**p) for p in pets_data]
users = [User(**u) for u in users_data]
petdocs = [PetDocument(**pd) for pd in petdocs_data]
phrs = [PetHealthRecord(**phr) for phr in phrs_data]
prs = [PetReport(**pr) for pr in prs_data]
pts = [PetTimeline(**pt) for pt in pts_data]
