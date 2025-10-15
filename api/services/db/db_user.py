from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from models.resources import User, UserCreate
from dependencies.db import UserORM
import uuid

async def get_users(db: AsyncSession) -> List[User]:
    result = await db.execute(select(UserORM))
    users = result.scalars().all()
    return [User(id=u.id, name=u.name, email=u.email) for u in users]

async def get_user(db: AsyncSession, user_id: str) -> Optional[User]:
    result = await db.execute(select(UserORM).where(UserORM.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return None
    return User(id=user.id, name=user.name, email=user.email)

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user_id = str(uuid.uuid4())
    db_user = UserORM(id=user_id, name=user_in.name, email=user_in.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return User(id=db_user.id, name=db_user.name, email=db_user.email)

async def update_user(db: AsyncSession, user_id: str, user_in: UserCreate) -> Optional[User]:
    result = await db.execute(select(UserORM).where(UserORM.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return None
    user.name = user_in.name
    user.email = user_in.email
    await db.commit()
    await db.refresh(user)
    return User(id=user.id, name=user.name, email=user.email)

async def delete_user(db: AsyncSession, user_id: str) -> bool:
    result = await db.execute(select(UserORM).where(UserORM.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        return False
    await db.delete(user)
    await db.commit()
    return True
