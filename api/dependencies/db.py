from models.resources import Pet
from datetime import datetime

# Fake in-memory "table"
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

