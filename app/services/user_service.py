from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.logging import logger
from app.core.security import get_password_hash, verify_password
from app.crud.user import (create_user, delete_user, get_all_users,
                           get_user_by_email, get_user_by_id, update_user)
from app.schemas.user import UserCreate, UserUpdate


async def register_user(db: AsyncSession, user_in: UserCreate):
    logger.info("User Registration started")
    existing_user = await get_user_by_email(db, user_in.email)
    if existing_user:
        logger.error("Email already registered")
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user_in.password)
    new_user = await create_user(db, user_in, hashed_password)
    logger.info("User Created")
    return new_user


async def list_all_users(db: AsyncSession):
    return await get_all_users(db)


async def retrieve_user(db: AsyncSession, user_id: int):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def update_user_data(db: AsyncSession, user_id: int, user_in: UserUpdate):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = await update_user(db, user, user_in)
    return updated_user


async def delete_user_data(db: AsyncSession, user_id: int):
    user = await get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(db, user)
    return
