# app/crud/user.py
from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
    """Получить пользователя по его ID."""
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    """Получить пользователя по email."""
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def get_all_users(db: AsyncSession) -> List[User]:
    """Получить список всех пользователей."""
    stmt = select(User)
    result = await db.execute(stmt)
    return result.scalars().all()


async def create_user(
    db: AsyncSession, user_in: UserCreate, hashed_password: str
) -> User:
    """Создать нового пользователя. Пароль здесь уже должен быть захэширован до вызова функции."""
    new_user = User(
        username=user_in.username, email=user_in.email, hashed_password=hashed_password
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def update_user(db: AsyncSession, db_user: User, user_in: UserUpdate) -> User:
    """
    Обновить данные пользователя.
    Используем схему UserUpdate, где все поля опциональны (partial update).
    """
    if user_in.username is not None:
        db_user.username = user_in.username
    if user_in.email is not None:
        db_user.email = user_in.email
    # при необходимости — обновление других полей

    await db.commit()
    await db.refresh(db_user)
    return db_user


async def delete_user(db: AsyncSession, db_user: User) -> None:
    """Удалить пользователя из базы."""
    await db.delete(db_user)
    await db.commit()
