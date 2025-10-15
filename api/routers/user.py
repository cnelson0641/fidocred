from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from models.resources import User, UserCreate
from dependencies.db import get_db
from services.db.db_user import get_users, get_user, create_user, update_user, delete_user

router = APIRouter(prefix="/users", tags=["users"])

# Get all users
@router.get("/", response_model=List[User])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

# Get a user
@router.get("/{user_id}", response_model=User)
async def get_user_route(user_id: str, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Create a new user
@router.post("/", response_model=User)
async def create_user_route(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user_in)

# Update a user
@router.put("/{user_id}", response_model=User)
async def update_user_route(user_id: str, updated_user: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await update_user(db, user_id, updated_user)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Delete a user
@router.delete("/{user_id}")
async def delete_user_route(user_id: str, db: AsyncSession = Depends(get_db)):
    success = await delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted"}