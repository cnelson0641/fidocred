from models.resources import Pet, User, PetDocument
from datetime import datetime

# Dummy data to be replaced by a db
petdocs_data = [
    {
        "id": "1",
        "pet_id": "1",
        "filename": "vaccine_record.pdf",
        "filedata": "Sample data 1",
    },
    {
        "id": "2",
        "pet_id": "2",
        "filename": "vet_visit_2023_10_01.pdf",
        "filedata": "Sample data 2",
    },
]
# Convert them all to PetDocument objects
petdocs = [PetDocument(**pd) for pd in petdocs_data]

# Dummy data to be replaced by a db
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
# Convert them all to Pet objects
users = [User(**u) for u in users_data]

# Dummy data to be replaced by a db
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
# Convert them all to Pet objects
pets = [Pet(**p) for p in pets_data]

