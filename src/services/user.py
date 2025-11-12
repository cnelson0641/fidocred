from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlmodel import select as sql_select
from models import User, UserCreate

#################
# User Service
#################

async def get_users(db: AsyncSession) -> list[User]:
    result = await db.execute(sql_select(User))
    return result.scalars().all()


async def get_user(db: AsyncSession, user_id: str) -> User | None:
    result = await db.execute(sql_select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def update_user(db: AsyncSession, user_id: str, updated_user: UserCreate) -> User | None:
    user = await get_user(db, user_id)
    if not user:
        return None

    for field, value in updated_user.dict().items():
        setattr(user, field, value)

    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user_id: str) -> bool:
    user = await get_user(db, user_id)
    if not user:
        return False

    await db.delete(user)
    await db.commit()
    return True

