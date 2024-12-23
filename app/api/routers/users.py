from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import (delete_user_data, list_all_users,
                                       register_user, retrieve_user,
                                       update_user_data)

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await register_user(db, user_in)


@router.get("/", response_model=List[UserResponse])
async def get_all_users(db: AsyncSession = Depends(get_db)):
    return await list_all_users(db)


@router.get("/{user_id}", response_model=UserResponse)
async def get_one_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await retrieve_user(db, user_id)


@router.put("/{user_id}", response_model=UserResponse)
async def update_one_user(
    user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_db)
):
    return await update_user_data(db, user_id, user_in)


@router.delete("/{user_id}", status_code=204)
async def delete_one_user(user_id: int, db: AsyncSession = Depends(get_db)):
    await delete_user_data(db, user_id)
    return None
