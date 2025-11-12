from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select as sql_select
from models import Pet, PetCreate

#################
# Pet Service
#################

async def get_pets(db: AsyncSession) -> list[Pet]:
    result = await db.execute(sql_select(Pet))
    return result.scalars().all()


async def get_pet(db: AsyncSession, pet_id: str) -> Pet | None:
    result = await db.execute(sql_select(Pet).where(Pet.id == pet_id))
    return result.scalar_one_or_none()


async def create_pet(db: AsyncSession, pet_in: PetCreate) -> Pet:
    pet = Pet(**pet_in.dict())
    db.add(pet)
    await db.commit()
    await db.refresh(pet)
    return pet


async def update_pet(db: AsyncSession, pet_id: str, updated_pet: PetCreate) -> Pet | None:
    pet = await get_pet(db, pet_id)
    if not pet:
        return None

    for field, value in updated_pet.dict().items():
        setattr(pet, field, value)

    db.add(pet)
    await db.commit()
    await db.refresh(pet)
    return pet


async def delete_pet(db: AsyncSession, pet_id: str) -> bool:
    pet = await get_pet(db, pet_id)
    if not pet:
        return False

    await db.delete(pet)
    await db.commit()
    return True

