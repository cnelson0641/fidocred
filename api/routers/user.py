from fastapi import APIRouter
from typing import List
from models.resources import User, UserCreate
from dependencies.db import users
import uuid

router = APIRouter(prefix="/users", tags=["users"])

# Get all users
@router.get("/", response_model=List[User])
def list_users():
    return users

# Get a user
@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    user = next((u for u in users if u.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create a new user
@router.post("/", response_model=User)
def create_user(user_in: UserCreate):
    user = User(
        id = str(uuid.uuid4()),
        name = user_in.name,
        email = user_in.email,
    )
    users.append(user)
    return user

# Update a user
@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, updated_user: UserCreate):
    for i, user in enumerate(users):
        if user.id == user_id:
            updated_user_with_id = updated_user.model_copy(update={"id": user_id})
            users[i] = updated_user_with_id
            return updated_user_with_id
    raise HTTPException(status_code=404, detail="User not found")

# Delete a user
@router.delete("/{user_id}")
def delete_user(user_id: str):
    for i, user in enumerate(users):
        if user.id == user_id:
            users.pop(i)
            return {"detail": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")
